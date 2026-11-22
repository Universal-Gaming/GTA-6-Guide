#!/usr/bin/env python3
"""Cross-page content invariants for the static GTA VI guide."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
ROOT=Path(__file__).resolve().parent
errors=[]
class Parser(HTMLParser):
 def __init__(self):
  super().__init__();self.links=[];self.ids=set()
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='a':self.links.append(a.get('href',''))
pages={p.name:p.read_text(encoding='utf-8') for p in ROOT.glob('*.html')}
required=['index.html','map.html','missions.html','mission-detail.html','collectibles.html','progress-vault.html','encyclopedia.html','research.html','handbook.html']
for p in required:
 if p not in pages:errors.append('Missing required page: '+p)
if not errors:
 home=pages['index.html']
 for p in ['map.html','missions.html','collectibles.html','progress-vault.html','encyclopedia.html','research.html','handbook.html']:
  if p not in home:errors.append('Homepage lacks navigation to '+p)
 encyclopedia=pages['encyclopedia.html']
 ids=re.findall(r'(?:"id":"|id:\x27)(entry-\d+)',encyclopedia)
 if len(ids)!=len(set(ids)):errors.append('Duplicate encyclopedia IDs')
 if len(ids)<29:errors.append('Expected at least 29 encyclopedia records')
 for id in ['query','category','sort','results','count']:
  if 'id="'+id+'"' not in encyclopedia:errors.append('Encyclopedia missing UI element '+id)
 handbook=pages['handbook.html']
 for phrase in ['Manual saves and autosaves','Map, Index and waypoints','Paradise Taxi','RydeMe rideshare','Buses and trains']:
  if phrase not in handbook:errors.append('Handbook missing topic: '+phrase)
 missions=pages['missions.html']
 for phrase in ['33 of 95','SOURCED QUICK ROUTE','SOURCE REFERENCE ONLY','MISSION INDEX ONLY']:
  if phrase not in missions:errors.append('Mission coverage disclosure missing: '+phrase)
 vault=pages['progress-vault.html']
 for key in ['ugn-gta6-missions-v1','ugn-gta6-collectibles-v1','ugn-gta6-tracker-v1','ugn-gta6-saved-v1','ugn-gta6-personal-map-pins-v1','ugn-gta6-mission-notes-v1:']:
  if key not in vault:errors.append('Progress Vault omits '+key)
 for id in ['export','import','restore','reset','stats','status']:
  if 'id="'+id+'"' not in vault:errors.append('Progress Vault missing '+id)
 for page in ['map.html','collectibles.html']:
  if 'ugn-gta6-collectibles-v1' not in pages[page]:errors.append(page+' does not share collectible storage')
 for page in ['missions.html','mission-detail.html']:
  if 'ugn-gta6-missions-v1' not in pages[page]:errors.append(page+' does not share mission storage')
 for name,html in pages.items():
  parser=Parser();parser.feed(html)
  for url in parser.links:
   if url.startswith('javascript:'):errors.append(name+' contains javascript: URL')
print('Cross-page content validation:',len(pages),'pages,',len(errors),'errors')
for error in errors:print('ERROR:',error)
sys.exit(bool(errors))
