# Barracks, Adventurers Guilds, and mercenaries

Recruit quality, quotas, war gates, and character sale payouts.

## Recruiting

Barracks produces resources tagged Barracks at a base rate of 0.5 × Speed. Adventurers Guild produces Guild-tagged resources at 0.5 × Speed, but remains blocked until forest war stage 4, checked approximately once per second.

These are resource producers: recruit availability and global quota, per-order payment, worker automation, five-item output buffer, and productivity work as for other resources. Each Recruit Artisan adds 0.1 building Quality and adds 200% of recruit resource value in Gold to each paid order.

Human Quality prestige is added to the quality roll before a new recruit initializes its character data.

## Mercenary Guild eligibility

Mercenary Guild is intrinsically automatic. It accepts sellable Adventurers with positive SellValue and Quality strictly above 1. Mercenary Conscripts expands eligibility to other HumanItemType characters.

Characters are consumed when sold. The sale pays Gold equal to integer SellValue ÷ 2, plus a Ducat award based on that same halved gold value.

## Ducat formula

Let D = halved sale value ÷ 5,200. If D is below 1, award one Ducat with probability D. If D is at least 1, award integer(D), discarding the fractional remainder. Gold and Ducats are credited immediately, and the last five transactions are retained for inspection. Human SellValue includes the sell values of currently equipped items, so equipment contributes to both payouts.

## Sources

- `Assets.Source.Flow.Elements/Barracks.cs:18`
- `Assets.Source.Flow.Elements/AdventurersGuild.cs:22`
- `Assets.Source.Flow.Elements/AdventurersGuild.cs:35`
- `Assets.Source.Flow.Elements/ResourceElement.cs:121`
- `Assets.Source.Flow.Elements/MercenaryGuild.cs:25`
- `Assets.Source.Flow.Elements/MercenaryGuild.cs:46`
- `Assets.Source.Flow.Elements/MercenaryGuild.cs:81`
- `Assets.Source.Items.Type/HumanItemType.cs:109`
