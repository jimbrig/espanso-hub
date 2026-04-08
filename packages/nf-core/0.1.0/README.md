# nf-core related commands for espanso

## What is nf-core?

[nf-core](https://nf-co.re/) is a community effort for building high-quality, reproducible bioinformatics pipelines with Nextflow.  
It provides:

- Standardized pipeline structure
- Automated linting and CI checks
- Consistent documentation and release practices
- Shared best practices across many pipelines

## What this espanso package is for

This package adds quick text expansions for frequent nf-core comments used in:

- GitHub pull request reviews
- GitHub issues
- Slack support and collaboration

The goal is to make repeated feedback faster, clearer, and more consistent.

## Trigger discovery

Most triggers in this package start with `:nfc-`.

Type `:nfc-` in any text field where Espanso is active (for example GitHub or Slack) to see and use the nf-core shortcuts quickly.

## Available triggers

### Code quality and linting

- `:nfc-lint` -> Suggests running `nextflow lint -format -sort-declarations -spaces 4 -harshil-alignment`.

### Module development and configuration

- `:nfc-name` -> Requests process naming aligned with nf-core module naming conventions.
- `:nfc-input` -> Suggests combining inputs into a single tuple for correct pairing.
- `:nfc-outname` -> Recommends output naming via `ext-prefix` using `${prefix}`.
- `:nfc-ont` -> Request to add ontologies to the meta map.
- `:nfc-extargs` -> Asks to include `ext.args` in `main.nf.test` with a docs reference.
- `:nfc-conf` -> Points to using custom config files for parameter/tool argument adjustments.
- `:nfc-versions` -> Provides a `process.out.findAll { key, val -> key.startsWith('versions') }` snippet for versions outputs.
- `:nfc-topics` -> Requests migrating versions output to topics with docs link.

### Testing and snapshots

- `:nfc-sanitize` -> Suggests `snapshot(sanitizeOutput(process.out)).match()` for cleaner snapshots via `nft-utils`.
- `:nfc-snap` -> Requests additional output files to be included in snapshots.
- `:nfc-stub` -> Suggests `snapshot(sanitizeOutput(process.out)).match()` specifically for stub assertions.
- `:nfc-nftbam` -> Recommends `nft-bam` checks, including `.getReadsMD5()` for unstable whole-file md5s.
- `:nfc-nftvcf` -> Recommends using `nft-vcf` to validate VCF content.

### Infrastructure and tools

- `:nfc-docker` -> Recommends uploading custom containers to nf-core `quay.io` and requesting via `#request-core`.

### Community and contribution guidelines

- `:nfc-join` -> Asks contributors to join the nf-core GitHub org to enable CI on PRs.
- `:nfc-one` -> Recommends one module per PR for easier review.
- `:nfc-forceone` -> Requests splitting large PRs into one PR per module/subworkflow.
- `:nfc-thanks` -> Posts a thank-you note and indicates review comments were added.

### Debugging and support

- `:nfc-info` -> Requests `nextflow.log`, sample sheet, and run command for troubleshooting.

### Additional trigger in this package

- `:prtodo` -> Expands to `-commenter:@me -review:changes-requested` (GitHub PR search filter).

## Typical usage

1. Type a configured trigger in GitHub or Slack.
2. Let espanso expand it into the full comment.
3. Adjust project-specific details before sending.

## Notes

- Keep expansions short, respectful, and actionable.
- Prefer links to nf-core docs when suggesting standards.
- Update triggers regularly as team conventions evolve.