# Changelog

All notable changes to this catalog are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

This file tracks the **catalog**, not the plugins it lists — each plugin keeps its own changelog in
its own repository.

## [Unreleased]

## [2.1.0] - 2026-08-28

### Changed

- Pinned to `project-flow` v3.0.1 and `web-launcher` v0.3.1. Both are patch releases fixing checks
  and instructions that could pass or mislead; pinning means they do not reach anyone until this
  bump merges, which is the cost the pinning change accepted and the reason the CI version check
  exists.

## [2.0.1] - 2026-08-28

### Added

- CI also asserts that the `name` in each source's `plugin.json` matches the name the catalog
  declares. The version and ref were already checked three ways; the name was not, so a rename that
  updated the manifest and not the catalog — or the reverse — would have passed.

### Fixed

- The v1.1.0 changes had no version heading of their own and sat under `[2.0.0]`, which claimed the
  tag-pinning work shipped in 2.0.0 when it shipped a release earlier. Split apart.

## [2.0.0] - 2026-08-28

### Changed

- **`project` is renamed to `project-flow`.** BREAKING for anyone with the old name in
  `enabledPlugins`: install is now `/plugin install project-flow@voyvodka`. A top-level `renames`
  entry maps the old name to the new one, so Claude Code v2.1.193+ rewrites user, project and local
  settings automatically and reports the change. The source is remote, so expect one
  `plugin-cache-miss` and a single `/plugin install`. Older Claude Code reports `plugin-not-found`
  for the old name.

  `renames` is append-only history — the entry stays even after everyone has migrated, because it is
  what makes the old name resolvable at all.
- The entry now points at `plugins/project-flow` at `ref: v3.0.0`.

## [1.1.0] - 2026-08-28

### Changed

- **Both plugins are now pinned to a release tag** (at the time, `ref: v2.8.0` and `ref: v0.3.0`)
  instead of resolving against whatever `main` happened to be at install time. Installing during a
  push, or during a half-finished change, previously produced whatever HEAD was at that moment.
  **This adds a release step**: after tagging a plugin, bump its `version` and `ref` here and merge,
  or the new release does not reach anyone.

### Added

- CI now clones each `git-subdir` source at its pinned ref, checks the `path` exists, runs
  `claude plugin validate --strict` inside it, and asserts three-way version agreement between the
  tag, the catalog entry and the plugin's own `plugin.json`. Validating this repo's manifest said
  nothing about whether the plugins it points at still existed — a renamed or deleted `path` would
  have kept CI green until a user hit the broken install.

## [1.0.0] - 2026-08-28

### Added

- `LICENSE` — the README claimed MIT with no licence file to back it, so the catalog read as
  unlicensed to GitHub and to any licence scanner.
- `.github/workflows/validate.yml` — runs `claude plugin validate . --strict` on every push and
  pull request. Until now a malformed `marketplace.json` would have shipped silently.
- `.github/dependabot.yml` — monthly `github-actions` updates, which is what keeps the pinned
  action SHAs in the workflow from going stale.

### Fixed

- `$schema` in `marketplace.json` pointed at `anthropic.com/claude-code/marketplace.schema.json`,
  which redirects to a marketing page rather than a schema. Now points at the real SchemaStore
  entry, so editors can actually validate the file.
- The plugin table in the README was a hand-written paraphrase of `marketplace.json` and had
  already drifted from it. It now quotes the manifest verbatim.

[Unreleased]: https://github.com/voyvodka/claude-plugins/compare/v2.1.0...HEAD
[2.1.0]: https://github.com/voyvodka/claude-plugins/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/voyvodka/claude-plugins/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/voyvodka/claude-plugins/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/voyvodka/claude-plugins/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/voyvodka/claude-plugins/releases/tag/v1.0.0
