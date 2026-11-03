"""Create a SHA-256 catalogue for a GSCS profile repository; does not publish files."""
from pathlib import Path
import argparse, hashlib, json, re
parser=argparse.ArgumentParser();parser.add_argument('--directory',default='.');args=parser.parse_args()
root=Path(args.directory).resolve();profiles=[];ids=set()
for path in sorted((root/'templates').glob('*.json')):
    raw=path.read_bytes();template=json.loads(raw.decode('utf-8-sig'));identifier=template['id']
    if not re.fullmatch(r'[a-zA-Z0-9_-]{1,100}',identifier) or identifier in ids or path.stem!=identifier:raise ValueError('Invalid or duplicate profile identifier: '+path.name)
    ids.add(identifier)
    profiles.append(dict(id=identifier,name=template['name'],path='templates/'+path.name,sha256=hashlib.sha256(raw).hexdigest(),platforms=template.get('operatingSystems',[])))
if not profiles:raise ValueError('No profiles found under templates/')
(root/'catalog.json').write_text(json.dumps(dict(schemaVersion=1,profiles=profiles),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(profiles=len(profiles),catalog=str(root/'catalog.json'))))
