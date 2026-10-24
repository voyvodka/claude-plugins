# Changelog

All notable changes to this catalog are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

This file tracks the **catalog**, not the plugins it lists — each plugin keeps its own changelog in
its own repository.

## [Unreleased]

## [3.0.5] - 2026-10-25

### Changed

- Pinned to `project-flow` v3.2.2 (#16)
- Pinned to `site-triage` v1.1.2 (#16)

## [3.0.4] - 2026-10-25

### Changed

- Pinned to `project-flow` v3.2.1 (#15)

## [3.0.3] - 2026-10-24

### Changed

- Pinned to `site-triage` v1.1.1 (#14)

## [3.0.2] - 2026-10-24

### Changed

- Pinned to `project-flow` v3.2.0 (#13)

## [3.0.1] - 2026-10-24

### Changed

- Pinned to `site-triage` v1.1.0 (#12)

## [3.0.0] - 2026-10-14

### Changed

- **`web-launcher` is renamed to `site-triage`.** BREAKING: install with
  `/plugin install site-triage@voyvodka`. Claude Code v2.1.193+ updates existing settings
  automatically; older versions report `plugin-not-found`.
- The entry now points at `voyvodka/site-triage`, `plugins/site-triage`, `ref: v1.0.0`.

## [2.1.4] - 2026-10-14

### Changed

- README leads with the one-step install, `/plugin install <name> --marketplace
  voyvodka/claude-plugins` (Claude Code 2.1.275 or later), and keeps the two-step form for older
  versions.
- Pinned to `project-flow` v3.1.1 and `web-launcher` v0.4.0.

## [2.1.3] - 2026-09-25

### Changed

- Pinned to `project-flow` v3.1.0.

## [2.1.2] - 2026-09-25

### Added

- CI checks the changelog's link footer: every release needs a link ref, and `[Unreleased]`
  compares from the newest release.

### Changed

- Pinned to `project-flow` v3.0.3 and `web-launcher` v0.3.3.

### Fixed

- The link footer is repaired: `[2.1.1]` added, `[Unreleased]` compares from the newest release.

## [2.1.1] - 2026-09-08

### Added

- Each entry now carries `license`, `homepage`, `repository` and `keywords`, searchable in
  `/plugin`, and is marked `strict`.
- CI checks that each entry's description, licence and keywords match the plugin's `plugin.json`.
- CI checks the changelog's structure: Keep a Changelog section names, no repeated section within a
  version, an `[Unreleased]` section, and one dated heading per version.

### Changed

- Pinned to `project-flow` v3.0.2 and `web-launcher` v0.3.2.

## [2.1.0] - 2026-08-28

### Changed

- Pinned to `project-flow` v3.0.1 and `web-launcher` v0.3.1, patch releases fixing checks and
  instructions that could pass or mislead.

## [2.0.1] - 2026-08-28

### Added

- CI checks that the `name` in each source's `plugin.json` matches the catalog entry's name.

### Fixed

- The v1.1.0 changes now have their own version heading instead of sitting under `[2.0.0]`.

## [2.0.0] - 2026-08-28

### Changed

- **`project` is renamed to `project-flow`.** BREAKING: install with
  `/plugin install project-flow@voyvodka`. Claude Code v2.1.193+ updates existing settings
  automatically; older versions report `plugin-not-found`.
- The entry now points at `plugins/project-flow` at `ref: v3.0.0`.

## [1.1.0] - 2026-08-28

### Added

- CI clones each source at its pinned ref, runs `claude plugin validate --strict` on it, and checks
  that the tag, catalog entry and `plugin.json` versions agree.

### Changed

- **Both plugins are now pinned to a release tag** (then `ref: v2.8.0` and `ref: v0.3.0`) instead
  of `main`; a new plugin release reaches users once the catalog pins it.

## [1.0.0] - 2026-08-28

### Added

- `LICENSE` file (MIT).
- `.github/workflows/validate.yml` runs `claude plugin validate . --strict` on every push and pull
  request.
- `.github/dependabot.yml` for monthly `github-actions` updates.

### Fixed

- `$schema` in `marketplace.json` now points at the SchemaStore entry instead of a marketing page.
- The README plugin table now quotes `marketplace.json` verbatim.

[Unreleased]: https://github.com/voyvodka/claude-plugins/compare/v3.0.5...HEAD
[3.0.5]: https://github.com/voyvodka/claude-plugins/compare/v3.0.4...v3.0.5
[3.0.4]: https://github.com/voyvodka/claude-plugins/compare/v3.0.3...v3.0.4
[3.0.3]: https://github.com/voyvodka/claude-plugins/compare/v3.0.2...v3.0.3
[3.0.2]: https://github.com/voyvodka/claude-plugins/compare/v3.0.1...v3.0.2
[3.0.1]: https://github.com/voyvodka/claude-plugins/compare/v3.0.0...v3.0.1
[3.0.0]: https://github.com/voyvodka/claude-plugins/compare/v2.1.4...v3.0.0
[2.1.4]: https://github.com/voyvodka/claude-plugins/compare/v2.1.3...v2.1.4
[2.1.3]: https://github.com/voyvodka/claude-plugins/compare/v2.1.2...v2.1.3
[2.1.2]: https://github.com/voyvodka/claude-plugins/compare/v2.1.1...v2.1.2
[2.1.1]: https://github.com/voyvodka/claude-plugins/compare/v2.1.0...v2.1.1
[2.1.0]: https://github.com/voyvodka/claude-plugins/compare/v2.0.1...v2.1.0
[2.0.1]: https://github.com/voyvodka/claude-plugins/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/voyvodka/claude-plugins/compare/v1.1.0...v2.0.0
[1.1.0]: https://github.com/voyvodka/claude-plugins/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/voyvodka/claude-plugins/releases/tag/v1.0.0
