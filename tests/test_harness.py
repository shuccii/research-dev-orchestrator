import copy, json, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'benchmarks'))
from cases import score
from harness import compare, digest, validate_adjudications


def row(case,version,pair,session='session-1',seconds=10.0):
    return {'benchmark_session_id':session,'run_id':f'{case}-{version}-{pair}','case_id':case,'version':version,'phase':'comparison','pair':pair,'status':'completed','active_wall_clock':seconds,'requested_model':'model','reasoning_effort':'high','pack_sha256':f'pack-{version}','case_sha256':f'case-{case}','grade':{'critical_pass':True,'noncritical_score':1}}


def config(cases):
    return {'benchmark_session_id':'session-1','model':'model','effort':'high','pack_sha256':{'v0.1.0':'pack-v0.1.0','working':'pack-working'},'case_sha256':{case:f'case-{case}' for case in cases}}


class HarnessTests(unittest.TestCase):
    def test_compare_pass_and_session_isolation(self):
        rows=[]
        for pair in range(3): rows += [row('format','v0.1.0',pair,seconds=10),row('format','working',pair,seconds=8)]
        rows.append(row('format','working',0,session='other',seconds=100))
        result=compare(rows,cases=['format'],config=config(['format']))
        self.assertEqual(result['decision'],'pass'); self.assertEqual(result['paired_ratio_median'],.8)

    def test_duplicate_and_frozen_mismatch_are_not_eligible(self):
        rows=[]
        for pair in range(3): rows += [row('format','v0.1.0',pair),row('format','working',pair)]
        rows.append(copy.deepcopy(rows[1])); rows[2]['case_sha256']='wrong'
        result=compare(rows,cases=['format'],config=config(['format']))
        self.assertEqual(result['decision'],'insufficient_measurement'); self.assertTrue(result['reasons'])

    def test_semantic_adjudication_is_bound_to_run(self):
        rows=[row('bugfix','v0.1.0',0),row('bugfix','working',0)]
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'adjudications.jsonl'
            decisions=[]
            for item in rows: decisions.append({'benchmark_session_id':'session-1','run_id':item['run_id'],'case_id':'bugfix','version':item['version'],'passed':True,'critical_failures':[],'reviewer_id':'reviewer-2','reviewed_at':'2026-09-02T00:00:00Z'})
            path.write_text('\n'.join(map(json.dumps,decisions))+'\n')
            self.assertEqual(len(validate_adjudications(rows,path)),2)
            decisions[0]['case_id']='format'; path.write_text(json.dumps(decisions[0])+'\n')
            with self.assertRaises(ValueError): validate_adjudications(rows,path)

    def test_failed_semantic_review_is_quality_failure(self):
        rows=[]; decisions={}
        for pair in range(3):
            for version in ('v0.1.0','working'):
                item=row('bugfix',version,pair,seconds=10 if version=='v0.1.0' else 8); rows.append(item)
                decisions[item['run_id']]={'passed':version=='v0.1.0'}
        result=compare(rows,cases=['bugfix'],config=config(['bugfix']),adjudications=decisions)
        self.assertEqual(result['decision'],'fail'); self.assertTrue(result['quality_failure'])

    def test_host_scorer_does_not_execute_generated_code(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); marker=root/'EXECUTED'
            (root/'average.py').write_text(f'from pathlib import Path\nPath({str(marker)!r}).write_text("bad")\ndef average(values): return 1\n')
            (root/'test_average.py').write_text('def test_placeholder(): pass\n')
            self.assertTrue(score('bugfix',root)['critical_pass']); self.assertFalse(marker.exists())

    def test_invalid_timeout_and_unobservable_budget_exit_nonzero(self):
        with tempfile.TemporaryDirectory() as directory:
            base=[sys.executable,str(ROOT/'benchmarks/harness.py'),'pilot','--output',directory]
            bad=subprocess.run(base+['--timeout','nan'],capture_output=True,text=True); self.assertNotEqual(bad.returncode,0)
            blocked=subprocess.run(base+['--max-llm-calls','1'],capture_output=True,text=True); self.assertNotEqual(blocked.returncode,0); self.assertTrue((Path(directory)/'preflight.json').exists())

    def test_holdout_gate_rejects_missing_primary(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory); root.joinpath('benchmark-session.json').write_text(json.dumps(config(['format']))); root.joinpath('metrics.jsonl').write_text('')
            process=subprocess.run([sys.executable,str(ROOT/'benchmarks/harness.py'),'holdout','--output',directory],capture_output=True,text=True)
            self.assertNotEqual(process.returncode,0)


if __name__=='__main__': unittest.main()
