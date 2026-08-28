# voyvodka/claude-plugins

A catalog of Claude Code plugins. Each plugin lives in its own repository — this repository holds
only the marketplace listing, so one registration covers all of them.

## Install

```
/plugin marketplace add voyvodka/claude-plugins
/plugin install project@voyvodka
/plugin install web-launcher@voyvodka
```

Then `/plugin marketplace update voyvodka` to pick up new entries.

Each entry is pinned to a release tag, so an update gives you a version that was tagged and
released, not whatever `main` held at that moment. CI clones every source at its pinned ref and
validates the plugin there, so a broken `path` fails here rather than at install time.

Each entry resolves to a subdirectory of the plugin's own repository.

## Plugins

| Plugin | What it does | Source |
|---|---|---|
| **project** | Carry a project from a rough idea to shipped code through six approval-gated phases: detect state, interrogate the idea, research market and stack, lock decisions into docs, scaffold AI tooling, then build in increments | [claude-project-flow](https://github.com/voyvodka/claude-project-flow) |
| **web-launcher** | Diagnose why a live site is not indexed, fix it, and verify the fix — plus discoverability scaffolding, Cloudflare Workers deployment, and repository hardening. Every technical claim carries its verification date and source. | [web-launcher](https://github.com/voyvodka/web-launcher) |

The wording above is copied from `marketplace.json` verbatim, so what this table says is exactly
what `/plugin` shows. Change one and change the other.

## Why a separate catalog

The plugins are unrelated tools with their own release cadence, so they keep their own
repositories, issues, and versions. Without a catalog, using both means adding two marketplaces and
running every update command twice — which is how one machine ends up running two different
versions of the same plugin without noticing.

## Licence

Each plugin carries its own licence in its own repository. This catalog is MIT — see
[LICENSE](LICENSE).
