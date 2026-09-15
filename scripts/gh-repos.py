import urllib.request
import json
import re

url = 'https://api.github.com/search/repositories?q=org:ARC-Minecraft&sort=stars&order=desc&per_page=30'
req = urllib.request.Request(url, headers={'User-Agent': 'arc-club-bot', 'Accept': 'application/vnd.github+json'})
data = json.loads(urllib.request.urlopen(req, timeout=20).read())
items = data.get('items', [])
print('total:', data.get('total_count'))
print()
for it in sorted(items, key=lambda x: (-x.get('stargazers_count', 0), -x.get('forks_count', 0), -x.get('pushed_at', '').count(''))):
    name = it.get('name')
    stars = it.get('stargazers_count', 0)
    forks = it.get('forks_count', 0)
    pushed = it.get('pushed_at', '')[:10]
    created = it.get('created_at', '')[:10]
    desc = (it.get('description') or '').replace('\r', ' ').replace('\n', ' ')[:140]
    lang = it.get('language') or '-'
    lic = (it.get('license') or {}).get('spdx_id') if it.get('license') else '-'
    print(f'  {stars:3d} star  {forks:2d} fork  {lang:8s} {lic:8s}  push {pushed}  create {created}')
    print(f'         {name}: {desc}')
