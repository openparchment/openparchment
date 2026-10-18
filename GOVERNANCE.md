# Governance

Status: draft. Open Parchment is intended to become a non-profit, community-governed standard. Until a formal home exists, this page describes how decisions are made.

## Principles

- **Nobody owns Open Parchment.** No company, association or institution, including the founder's own projects, gets special access or terms.
- **Producers have a reserved voice.** Changes that affect producer records require review by at least one producer or producer organization.
- **Open by default.** Proposals, discussion and decisions happen in public issues.

## How changes happen

1. **Propose.** Open an issue describing the change and which question in [QUESTIONS.md](QUESTIONS.md) it serves.
2. **Discuss.** At least 14 days for changes to the core schema; 7 days for vocabulary changes.
3. **Decide.** Maintainers decide by consensus. If consensus fails, a simple majority of maintainers decides, and the reasoning is recorded in the issue.
4. **Release.** Changes ship in a versioned release with a changelog entry.

## Versioning

- **Minor versions** (0.2 to 0.3, or 1.1 to 1.2) may only add optional fields, entities or vocabulary terms. Existing valid records stay valid.
- **Major versions** may make breaking changes. They are rare, announced at least 90 days ahead, and published with a migration guide.
- **Fields are deprecated before removal**, and removed only in a major version.
- **Extensions** use the `ext:<org>.<name>` prefix so anyone can add fields without forking the standard.

## Maintainers

- Initial maintainer: the founder.
- Goal for v1.0: at least five maintainers from different parts of the supply chain, including at least one producer or producer organization, and at most one person from any single organization.
- Maintainers disclose any commercial interest in products built on Open Parchment and recuse themselves from decisions that specifically affect those products.

## Contributions

- Specification, schemas and vocabularies are licensed CC BY 4.0; code is Apache 2.0.
- Contributions are accepted under the [Developer Certificate of Origin](https://developercertificate.org/): sign off each commit (`git commit -s`) to certify you have the right to contribute it under these licenses.
