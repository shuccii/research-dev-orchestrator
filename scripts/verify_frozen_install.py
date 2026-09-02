#!/usr/bin/env python3
"""Verify the immutable v0.1 tag and, when present, its installed cache."""
import hashlib, json, subprocess, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FREEZE=ROOT/'baseline/v0.1-freeze.json'
INSTALLED=Path.home()/'.codex/plugins/cache/personal/research-dev-orchestrator/0.1.0'

def sha(data): return hashlib.sha256(data).hexdigest()

def main():
    record=json.loads(FREEZE.read_text()); errors=[]; installed_checked=INSTALLED.is_dir()
    commit=subprocess.check_output(['git','rev-list','-n','1',record['tag']],cwd=ROOT,text=True).strip()
    if commit!=record['commit']: errors.append('tag commit differs from freeze record')
    for path,item in record['files'].items():
        tagged=subprocess.check_output(['git','show',f'{record["tag"]}:{path}'],cwd=ROOT)
        if sha(tagged)!=item['sha256']: errors.append(f'tag hash mismatch: {path}')
        if installed_checked:
            target=INSTALLED/path
            if not target.is_file() or sha(target.read_bytes())!=item['sha256']: errors.append(f'installed hash mismatch: {path}')
    print(json.dumps({'passed':not errors,'tag':record['tag'],'installed_checked':installed_checked,'errors':errors}))
    raise SystemExit(1 if errors else 0)

if __name__=='__main__': main()
