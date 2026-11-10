import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
reports=json.loads((root/'public/data/reports.json').read_text())
results=json.loads((root/'public/data/results.json').read_text())
tax=json.loads((root/'public/data/taxonomy.json').read_text())
assert len(reports)==44 and len(results)==44
assert {r['reportId'] for r in reports}=={x['reportId'] for x in results}
for x in results:
    assert x['verdict'] in tax['verdicts'], x['reportId']
    assert x['route'] in {'auto_apply','faculty_review','no_change'}, x['reportId']
    if x['repair']:
        assert x['repair'] in tax['repairs'], x['reportId']
        rule=tax['repairs'][x['repair']]
        if not rule['auto']:
            assert x['route']!='auto_apply', x['reportId']
        if x['route']=='auto_apply':
            assert x['edit'] and x['edit']['field'] in rule['fields'], x['reportId']
    if x['route']=='no_change':
        assert x['verdict']!='defect' or x['repair'] is None, x['reportId']
print('PASS: 44/44 reports covered; taxonomy keys and auto-apply guards valid.')
