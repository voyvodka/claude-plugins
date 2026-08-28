# Changelog

All notable changes to this catalog are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

This file tracks the **catalog**, not the plugins it lists — each plugin keeps its own changelog in
its own repository.

## [Unreleased]

### Changed

- **Both plugins are now pinned to a release tag** (`ref: v2.8.0`, `ref: v0.3.0`) instead of
  resolving against whatever `main` happened to be at install time. Installing during a push, or
  during a half-finished change, previously produced whatever HEAD was at that moment.
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

[Unreleased]: https://github.com/voyvodka/claude-plugins/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/voyvodka/claude-plugins/releases/tag/v1.0.0
