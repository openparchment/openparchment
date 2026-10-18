# Changelog

## v0.2 (draft, 2026-10-18)

**Added**
- `Harvest` entity: the producer's season story (narrative, structured conditions such as heavy rain or drying problems, relative volume, media), written once and linked from many lots.
- `IdentityLink` entity: joins identifiers at each handoff (`sameAs`, `derivedFrom`, `partOf`, `mergedInto`) with `confirmed` or `probable` confidence and evidence.
- `registration` on Producer, Harvest and Lot: who registered the record and its claim status (`self_registered`, `unclaimed`, `claimed`, `disputed`). Required.
- `localizedText` for stories and notes, keeping the author's original language with optional translations.
- `media` for photos, videos and voice notes, with transcripts.
- `Lot.harvestRecord` and `Lot.lotStory`.
- Process vocabulary with English, Spanish and Portuguese labels and definitions (`vocabulary/process.v0.2.json`).
- [QUESTIONS.md](QUESTIONS.md), [ID-POLICY.md](ID-POLICY.md), [GOVERNANCE.md](GOVERNANCE.md).
- `tools/validate.py` to validate every example against its schema version.

**Changed**
- `Producer.selfDescribed.story` is now `localizedText` (replaces `story` + `storyLang`).
- Id pattern now includes `harvest` and `link`.

**Breaking (pre-1.0)**
- `registration` is required on Producer and Lot. v0.1 records need a registration block to validate against v0.2.

## v0.1 (draft, 2026-10-18)

- Initial Producer (with Farm), Lot, Roast and Tasting schemas, shared definitions, fictional examples and a starter flavor crosswalk.
