# Identifier and registration policy

Status: draft for v0.2. Plain-language rules first; the schema follows them.

## The rules

1. **Every producer, farm, harvest, lot, roast, tasting and identity link gets one permanent Open Parchment id**, in the form `op:<entity>:<slug>`.
2. **Ids are never reused, reassigned or recycled.** If a record is a duplicate, it is merged into the canonical record with a `mergedInto` identity link, and the old id keeps resolving.
3. **An id belongs to its subject, not to whoever created it.** A producer's id belongs to the producer, even if a cooperative, exporter, importer or roaster created it. If a farmer changes cooperatives or buyers, their id and history go with them.

## Who can register a record

- **The subject themselves** (`claimStatus: self_registered`), for example a producer signing up directly or over WhatsApp.
- **A registrar acting on the subject's behalf** (`claimStatus: unclaimed`), for example a washing station registering its member farmers, or an importer creating lot records from its paperwork. The record always shows who registered it.

Registrars must:
- Only register people and lots they have a real relationship with.
- Publish the minimum by default: name, region, and the registrar. Phone numbers, exact locations and plot boundaries stay private unless the subject chooses otherwise.
- Never use registration to restrict the subject, for example by making the record depend on remaining a member.

## Claiming

- A subject can claim an unclaimed record through the web, WhatsApp, SMS, or their cooperative.
- Claims are verified with the lightest method that is reliable for that context: a code sent to a phone number the registrar already holds, confirmation by the cooperative, or an existing buyer vouching.
- Once claimed (`claimStatus: claimed`), the subject controls the record: what is public, what is corrected, and who may add to it.
- Anyone can flag a record as `disputed`. Disputes are resolved by the maintainers, with the subject's word weighted most heavily for facts about themselves.

## Joining identifiers

- Open Parchment does not replace ICO marks, importer lot codes, certifier ids, auction lot numbers or roaster SKUs. It stores them as `thirdPartyIds` and joins them with `IdentityLink` records.
- **Whoever holds two codes at the same moment records the link** (exporter: producer lot to ICO mark; importer: ICO mark to importer code; roaster: importer code to SKU). Nobody has to join the whole chain.
- Automated matching may propose `probable` links. They are labeled as such and only become `confirmed` when a party who held both codes, or the subject, confirms them.

## Sensitive information

- Self-described characteristics (for example woman-owned or smallholder) are only ever recorded as the producer's own statement, with their consent, and are never inferred.
- Prices are optional. Nobody is required to disclose what they paid or were paid to participate.
- Records created from scraped or public web data are never published as registry records unless the subject or the source confirms them.
