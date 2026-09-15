import os, re, posixpath, glob

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

stale = ['dont_starve.html', 'wind_quest.html', 'wind_island.html',
         'clash_royale.html', 'brawl_stars.html', 'servers.html']
bad_stale = []
broken = []
checked = 0
htmls = sorted(glob.glob('*.html') + glob.glob('*/*.html'))
for f in htmls:
    f = f.replace(os.sep, '/')
    d = posixpath.dirname(f)
    with open(f, encoding='utf-8') as fh:
        text = fh.read()
    for s in stale:
        if s in text:
            bad_stale.append((f, s))
    for r in re.findall(r'(?:href|src)="([^"]+)"', text):
        if r.startswith(('http:', 'https:', '//', '#', 'mailto:', 'data:', 'javascript:')):
            continue
        if "'" in r:  # JS concat artifact: src="' + src + '"
            continue
        target = posixpath.normpath(posixpath.join(d, r)) if d else posixpath.normpath(r)
        checked += 1
        if not os.path.exists(target):
            broken.append((f, r))

print('html files:', len(htmls))
print('local refs checked:', checked)
print('stale old names:', bad_stale if bad_stale else 'none')
if broken:
    print('BROKEN LINKS:')
    for f, r in broken:
        print('  %s -> %s' % (f, r))
else:
    print('broken links: none')
