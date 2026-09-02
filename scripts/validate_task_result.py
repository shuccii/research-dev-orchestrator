#!/usr/bin/env python3
"""Validate v0.2 results; legacy results are readable only with an explicit flag."""
import argparse, json, sys
from datetime import datetime
from pathlib import Path
from schema_subset import audit_schema, validate

ROOT=Path(__file__).resolve().parents[1]
def read(path):
    def reject(value): raise ValueError(f'non-finite number {value!r} is not valid')
    try: return json.loads(Path(path).read_text(),parse_constant=reject)
    except (OSError,json.JSONDecodeError,ValueError) as exc: raise ValueError(str(exc)) from exc

def valid_legacy(data):
    required={'status':str,'summary':str,'artifacts':list,'evidence':list,'risks':list,'next_actions':list,'verification':dict}
    if not all(key in data and isinstance(data[key],typ) for key,typ in required.items()): return False
    if data['status'] not in {'completed','needs_revision','blocked','awaiting_approval'}: return False
    if not all(isinstance(item,str) for key in ('artifacts','evidence','risks','next_actions') for item in data[key]): return False
    return all(isinstance(data['verification'].get(key),str) and data['verification'][key].strip() for key in ('execution','validity'))

def check_one(path,schema,manifest,legacy):
    try: data=read(path)
    except ValueError as exc: return {'path':str(path),'valid':False,'archive_readable':False,'completion_eligible':False,'errors':[str(exc)]}
    if not isinstance(data,dict): return {'path':str(path),'valid':False,'archive_readable':False,'completion_eligible':False,'errors':['$: expected object']}
    if 'schema_version' not in data:
        if legacy and valid_legacy(data): return {'path':str(path),'valid':True,'archive_readable':True,'completion_eligible':False,'legacy_version':'0.1','errors':[]}
        if legacy: return {'path':str(path),'valid':False,'archive_readable':False,'completion_eligible':False,'legacy_version':'0.1','errors':['$: does not satisfy the v0.1 archive shape']}
        return {'path':str(path),'valid':False,'archive_readable':False,'completion_eligible':False,'errors':['$: schema_version missing; --legacy-read-only is archive-only']}
    errors=validate(data,schema)
    if errors: return {'path':str(path),'valid':False,'archive_readable':False,'completion_eligible':False,'errors':errors}
    task=next((t for t in manifest['tasks'] if t['task_id']==data['task_id']),None) if manifest else None
    if manifest and task is None: errors.append('$.task_id: not found in manifest')
    if manifest and data['run_id']!=manifest['run_id']: errors.append('$.run_id: differs from manifest')
    if task and data['parent_task_id']!=task['parent_task_id']: errors.append('$.parent_task_id: differs from manifest')
    if datetime.fromisoformat(data['ended_at'][:-1]+'+00:00') < datetime.fromisoformat(data['started_at'][:-1]+'+00:00'): errors.append('$.ended_at: precedes started_at')
    if data['status']=='blocked' and 'blocked_reason' not in data: errors.append('$.blocked_reason: required for blocked')
    if data['status']!='blocked' and 'blocked_reason' in data: errors.append('$.blocked_reason: allowed only for blocked')
    verification=data['verification']; checks=verification['checks']; ids=[c['check_id'] for c in checks]
    if len(ids)!=len(set(ids)): errors.append('$.verification.checks: duplicate check_id')
    if len(verification['required_checks'])!=len(set(verification['required_checks'])): errors.append('$.verification.required_checks: duplicate check_id')
    evidence=set(data['evidence'])
    for check in checks:
        missing=set(check['evidence_refs'])-evidence
        if missing: errors.append(f'$.verification.checks.{check["check_id"]}: unknown evidence refs {sorted(missing)}')
        if check['type']=='command' and check['result']=='passed' and (not check.get('command') or check.get('exit_code')!=0): errors.append(f'$.verification.checks.{check["check_id"]}: passed command requires command and exit_code 0')
        if check['type']=='semantic_review' and check['observed_by']!='reviewer': errors.append(f'$.verification.checks.{check["check_id"]}: semantic review must be observed by reviewer')
    required=task['required_checks'] if task else verification['required_checks']
    if task and verification['required_checks']!=required: errors.append('$.verification.required_checks: differs from manifest')
    by_id={c['check_id']:c for c in checks}
    if task:
        policy=read(ROOT/'assets/verification-policy.json')['modes'][task['verification_mode']]
        for check_id in required:
            if check_id in by_id:
                check=by_id[check_id]
                if check['type'] not in policy['allowed_check_types'] or check['observed_by'] not in policy['allowed_observers']:
                    errors.append(f'$.verification.checks.{check_id}: check type/observer violates verification policy')
        approval=data['approval']; is_approval=task['operation_class']=='approval_required'
        if approval['required']!=is_approval: errors.append('$.approval.required: differs from operation_class')
        if not is_approval and approval != {'required':False,'status':'not_required','approved_by':None,'operation_succeeded':False}: errors.append('$.approval: non-approval task must use the not_required state')
        if not is_approval and data['status']=='awaiting_approval': errors.append('$.status: awaiting_approval requires approval_required operation_class')
        if is_approval:
            if approval['status'] not in {'pending','approved'}: errors.append('$.approval.status: approval task must be pending or approved')
            if approval['status']=='pending' and (approval['approved_by'] is not None or approval['operation_succeeded']): errors.append('$.approval: pending state cannot have approval or operation success')
            if approval['status']=='approved' and approval['approved_by']!='user': errors.append('$.approval: approved state requires approved_by user')
            if approval['operation_succeeded'] and approval['status']!='approved': errors.append('$.approval: operation success requires approved state')
            if data['status']=='awaiting_approval' and approval!={'required':True,'status':'pending','approved_by':None,'operation_succeeded':False}: errors.append('$.approval: awaiting_approval requires the pending state')
            operation=by_id.get('operation_success')
            special=read(ROOT/'assets/verification-policy.json')['approval_operation_success']
            if not operation or operation['type'] not in special['allowed_check_types'] or operation['observed_by'] not in special['allowed_observers']:
                errors.append('$.verification.checks.operation_success: violates approval success policy')
            elif approval['operation_succeeded'] != (operation['result']=='passed'):
                errors.append('$.approval.operation_succeeded: must agree with the operation_success check result')
    if data['status']=='completed':
        if not data['evidence']: errors.append('$.evidence: completed requires evidence')
        for check_id in required:
            if check_id not in by_id: errors.append(f'$.verification.checks: missing required check {check_id!r}')
            elif by_id[check_id]['result']!='passed': errors.append(f'$.verification.checks.{check_id}: required check did not pass')
        if task is None: errors.append('$: completed result requires --manifest for integration eligibility')
        elif task['verification_mode']=='semantic_review_required':
            review=verification['validity_review']
            if not data.get('worker_id'): errors.append('$.worker_id: required to establish independent semantic review')
            if not review['required'] or review['status']!='passed' or not review['reviewer_id']: errors.append('$.verification.validity_review: independent passed review required')
            if data.get('worker_id') and review['reviewer_id']==data['worker_id']: errors.append('$.verification.validity_review: reviewer equals worker')
            semantic=[by_id[check_id] for check_id in required if check_id in by_id and by_id[check_id]['type']=='semantic_review']
            if not semantic: errors.append('$.verification.required_checks: semantic mode requires a reviewer-observed semantic_review check')
            elif any(check.get('observer_id')!=review['reviewer_id'] for check in semantic): errors.append('$.verification.checks: semantic observer_id must match reviewer_id')
        elif verification['validity_review']['required'] and verification['validity_review']['status']!='passed': errors.append('$.verification.validity_review: required review did not pass')
        if task and task['operation_class']=='approval_required':
            if data['approval']!={'required':True,'status':'approved','approved_by':'user','operation_succeeded':True}: errors.append('$.approval: completed approval operation requires user approval and observed operation success')
        result_dir=Path(path).resolve().parent
        for artifact in data['artifacts']:
            rel=Path(artifact)
            candidate=result_dir/rel
            has_symlink=False; cursor=result_dir
            for part in rel.parts:
                cursor=cursor/part
                if cursor.is_symlink(): has_symlink=True
            try: contained=candidate.resolve().is_relative_to(result_dir)
            except (OSError,RuntimeError): contained=False
            if rel.is_absolute() or '..' in rel.parts or has_symlink or not contained or not candidate.exists(): errors.append(f'$.artifacts: missing or unsafe artifact {artifact!r}')
    return {'path':str(path),'valid':not errors,'archive_readable':not errors,'completion_eligible':not errors and data['status']=='completed' and task is not None,'errors':errors}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--json',action='store_true'); p.add_argument('--legacy-read-only',action='store_true'); p.add_argument('--manifest'); p.add_argument('results',nargs='+'); args=p.parse_args()
    try:
        schema=read(ROOT/'assets/task-result.schema.json'); audit_schema(schema); manifest=read(args.manifest) if args.manifest else None
        if manifest:
            from manifest_helper import validate_manifest
            errs=validate_manifest(manifest)
            if errs: raise ValueError('invalid manifest: '+'; '.join(errs))
        results=[check_one(path,schema,manifest,args.legacy_read_only) for path in args.results]
    except Exception as exc:
        print(json.dumps({'internal_error':str(exc)}) if args.json else f'Validation error: {exc}',file=sys.stderr); raise SystemExit(2)
    output={'valid':all(r['valid'] for r in results),'results':results}
    if args.json: print(json.dumps(output,indent=2))
    else:
        for r in results:
            print(('VALID' if r['valid'] else 'INVALID')+f': {r["path"]}')
            for error in r['errors']: print('  - '+error)
    raise SystemExit(0 if output['valid'] else 1)
if __name__=='__main__': main()
