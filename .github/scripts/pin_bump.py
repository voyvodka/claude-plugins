"""Move catalog pins to each plugin's latest GitHub release.

Writes marketplace.json (ref, sha, version and the fields CI compares with plugin.json),
the README plugin table and a CHANGELOG line. Prints one `name old new` line per moved pin;
prints nothing when every pin is current.
"""
import json
import re
import subprocess
import sys
import urllib.request

MARKETPLACE = '.claude-plugin/marketplace.json'
SYNCED_FIELDS = ('description', 'license', 'keywords')


def run(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout.strip()


def repo_of(url):
    m = re.match(r'https://github\.com/([^/]+/[^/.]+)(\.git)?$', url)
    if not m:
        sys.exit(f'unsupported source url: {url}')
    return m.group(1)


def latest_tag(repo):
    return json.loads(run('gh', 'api', f'repos/{repo}/releases/latest'))['tag_name']


def tag_commit(url, tag):
    # An annotated tag lists its commit on the peeled `^{}` line; a lightweight tag has only the plain one.
    refs = dict(line.split('\t')[::-1] for line in run('git', 'ls-remote', url, f'refs/tags/{tag}*').splitlines())
    return refs.get(f'refs/tags/{tag}^{{}}') or refs[f'refs/tags/{tag}']


def manifest_at(repo, sha, path):
    raw = f'https://raw.githubusercontent.com/{repo}/{sha}/{path}/.claude-plugin/plugin.json'
    with urllib.request.urlopen(raw, timeout=30) as r:
        return json.load(r)


def version_key(tag):
    return tuple(int(x) for x in tag.lstrip('v').split('.'))


def add_changelog_lines(lines):
    text = open('CHANGELOG.md').read()
    start = text.index('## [Unreleased]')
    end = text.index('\n## [', start + 1)
    block = text[start:end]
    entry = '\n'.join(f'- {line}' for line in lines)
    if '### Changed\n' in block:
        head, rest = block.split('### Changed\n', 1)
        nxt = rest.find('\n### ')
        body, tail = (rest, '') if nxt == -1 else (rest[:nxt], rest[nxt:])
        block = f'{head}### Changed\n{body.rstrip()}\n{entry}\n{tail}'
    else:
        # Keep a Changelog order: Changed sits after Added and before the rest.
        after_added = re.search(r'### Added\n\n(?:- .*\n)+', block)
        at = after_added.end() if after_added else len('## [Unreleased]\n')
        block = f'{block[:at].rstrip()}\n\n### Changed\n\n{entry}\n{block[at:]}'
    open('CHANGELOG.md', 'w').write(text[:start] + block.rstrip() + '\n' + text[end:])


def main():
    catalog = json.load(open(MARKETPLACE))
    readme = open('README.md').read()
    moved, notes = [], []
    for entry in catalog['plugins']:
        src = entry['source']
        repo = repo_of(src['url'])
        tag = latest_tag(repo)
        if version_key(tag) <= version_key(src['ref']):
            continue
        sha = tag_commit(src['url'], tag)
        manifest = manifest_at(repo, sha, src['path'])
        if manifest.get('version') != tag.lstrip('v'):
            sys.exit(f"{entry['name']}: {tag} carries plugin.json version {manifest.get('version')}")
        if manifest.get('description') != entry.get('description'):
            readme = readme.replace(entry['description'], manifest['description'])
        for field in SYNCED_FIELDS:
            if field in manifest:
                entry[field] = manifest[field]
        moved.append(f"{entry['name']} {src['ref']} {tag}")
        notes.append(f"Pinned to `{entry['name']}` {tag}")
        src['ref'], src['sha'], entry['version'] = tag, sha, manifest['version']
    if not moved:
        return
    with open(MARKETPLACE, 'w') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)
        f.write('\n')
    open('README.md', 'w').write(readme)
    add_changelog_lines(notes)
    print('\n'.join(moved))


if __name__ == '__main__':
    main()
