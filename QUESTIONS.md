# The questions Open Parchment must answer

Every field in the core standard has to help answer at least one of these. If a proposed field doesn't, it belongs in an extension, not the core.

## Producers
1. **How do buyers find me and credit me by name**, no matter how many hands my coffee passes through?
2. **How do I tell the story of this season once** and have it reach every roaster who buys any of my lots?
3. **Who has bought my coffee, and what did drinkers think of it?**
4. **What is public about me, and how do I change it?**

## Cooperatives, washing stations and exporters
5. **How do I register my members** so they are visible to buyers, without taking ownership of their identity?
6. **Which of my export lots (ICO marks) came from which farms?**

## Importers
7. **Which farm and producer did this ICO-marked lot come from**, and who says so?
8. **Can I show where this coffee was grown**, at the level of detail regulations and buyers require, with the producer's consent?

## Roasters
9. **What can I truthfully print about this coffee**, and whose claim is it?
10. **Which producers grow what I'm looking for** (variety, process, elevation, region, self-described ownership) and who imports them?
11. **When will this roast be at its best**, and for how long?

## Drinkers, apps and agents
12. **Which decaf coffees taste like vanilla cake** (or any flavor), and what decaf method was used?
13. **What in my cabinet will be at its peak this weekend?**
14. **Which woman-owned farms produce coffee similar to a producer I love?**
15. **How much was the farmer paid for this lot, at what stage, and who is making that claim?**

## How the v0.2 model answers them

| Question | Answered by |
|---|---|
| 1, 4, 5 | `Producer` with `registration`, `alternateNames`, `thirdPartyIds`, visibility controls |
| 2 | `Harvest` (narrative, conditions, media) linked from each `Lot.harvestRecord` |
| 3 | `Tasting.subject` and `Roast.lots` pointing back to the lot and producer |
| 6, 7 | `Lot.thirdPartyIds` and `IdentityLink` records joined at each handoff |
| 8 | `Farm.plotBoundary` with producer-controlled visibility |
| 9 | `provenance` on every record and claim |
| 10, 14 | `Lot` origin, varieties, process, elevation; `Producer.selfDescribed.ownership` |
| 11, 13 | `Roast.rest` plus `Roast.batches[].roastDate` |
| 12 | `Lot.decaf` (structured), `Tasting.descriptors`, `vocabulary/` crosswalk |
| 15 | `Lot.prices` with stage, payer, payee and provenance |
