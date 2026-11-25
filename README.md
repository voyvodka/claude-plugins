# voyvodka/claude-plugins

A catalog of Claude Code plugins. Each plugin lives in its own repository — this repository holds
only the marketplace listing, so one registration covers all of them.

## Install

```
/plugin install project-flow --marketplace voyvodka/claude-plugins
/plugin install site-triage --marketplace voyvodka/claude-plugins
```

The first line adds this catalog and installs the plugin in one command; the second reuses the catalog
it added. That form needs Claude Code 2.1.275 or later (from the shell, `claude plugin install …
--marketplace …` needs 2.1.292). On an older version, register the catalog first:

```
/plugin marketplace add voyvodka/claude-plugins
/plugin install project-flow@voyvodka
/plugin install site-triage@voyvodka
```

## Updates

Claude Code leaves background auto-update **off** for third-party marketplaces like this one, and
the catalog cannot turn it on for you. To have new releases arrive by themselves, run `/plugin`, open
the **Marketplaces** tab, select `voyvodka` and turn on auto-update. Updates then land shortly after a
session starts; run `/reload-plugins` when Claude Code says a plugin was updated, or start a new
session.

Without it, update by hand: **Marketplaces** › `voyvodka` › **Update marketplace** in `/plugin`
updates every plugin installed from this catalog, and `claude plugin update project-flow@voyvodka`
updates one from the shell. A bare `claude plugin marketplace update` refreshes the listing only and
leaves installed plugins where they are. See
[Keep plugins updated](https://code.claude.com/docs/en/discover-plugins#keep-plugins-updated)
(checked 2026-11-25).

Each entry is pinned to a release tag and to that tag's commit (`ref` and `sha`), so an update
gives you a version that was tagged and released, not whatever `main` held at that moment, and a
tag moved afterwards cannot change what is installed. CI clones every source at its pinned ref and
validates the plugin there, so a broken `path` fails here rather than at install time. A plugin
release reaches you only once its pin here moves to it; the `pin-bump` workflow checks each
plugin's latest release daily and proposes the move as a pull request.

Each entry resolves to a subdirectory of the plugin's own repository.

## Plugins

| Plugin | What it does | Source |
|---|---|---|
| **project-flow** | Carry a project from a rough idea to shipped code through six approval-gated phases: detect state, interrogate the idea, research market and stack, lock decisions into docs, scaffold AI tooling, then build in increments | [claude-project-flow](https://github.com/voyvodka/claude-project-flow) |
| **site-triage** | Diagnose why a live site is not indexed, fix it, and verify the fix — plus discoverability scaffolding, Cloudflare Workers deployment, and repository hardening. Every technical claim carries its verification date and source. | [site-triage](https://github.com/voyvodka/site-triage) |

The wording above is copied from `marketplace.json` verbatim, so what this table says is exactly
what `/plugin` shows. Change one and change the other.

> **`project` was renamed to `project-flow` in 3.0.0.** The catalog carries a `renames` entry, so
> Claude Code v2.1.193+ rewrites your settings and tells you it did. The source is remote, so expect
> `Plugin "project-flow" not cached at <path>` in the `/plugin` Errors tab once (the
> `plugin-cache-miss` error) and a single `/plugin install`.

## Why a separate catalog

The plugins are unrelated tools with their own release cadence, so they keep their own
repositories, issues, and versions. Without a catalog, using both means adding two marketplaces and
running every update command twice — which is how one machine ends up running two different
versions of the same plugin without noticing.

## Licence

Each plugin carries its own licence in its own repository. This catalog is MIT — see
[LICENSE](LICENSE).
