# Dungeon runs, stages, loot, and retreat

The five-adventurer expedition loop and what happens between fights.

## Starting

A dungeon node needs five Adventurer inputs, an available selected dungeon, no active party, and the full supply currency payment. It consumes all five inputs and applies party buffs. Ticks occur every two seconds; this tick interval is fixed in Dungeon.Update rather than divided by the node’s Speed.

Each dungeon has eight stages, alternating nonboss and boss. Stage health = BaseHealth × StageDifficulty. Nightmare endgame adds its own health multiplier. Every active combat tick increments StageTick, then adds random party base damage ÷ 1.2 to ×1.2 to stage progress. Challenges and combat traits execute next.

Ordinary party damage follows: at least one hit occurs, with a 50% continuation chance after each hit. That gives an average two hits but no fixed maximum. Dead/Exhausted members are then removed. Losing the last member records a wipe and resets the run.

## Damage and boss escalation

Dungeon damage rolls between integer StageDifficulty ÷ 50 and integer StageDifficulty ÷ 33, multiplied by the requested hazard multiplier. On boss stages the multiplier also gains ×(1 + 0.015 × StageTick). This grows every active combat tick, so stalled boss fights become more dangerous.

Normal hits use tank-targeting odds. Individual challenges can bypass armor, target everyone, consume energy, or impose separate skill checks.

## Loot and between-stage healing

Reaching stage health sets three cooldown ticks before looting. Before granting rewards, all ItemReward outputs for the stage must exist and have no buffered items. A blocked output delays loot and energy payment, then retries.

Successful loot grants every stage reward, deducts the stage EnergyCost from each member (default 10), invokes the stage callback, and increments clear count. After limit-break checks, healing traits and the first full Healer can act. A cleared stage advances when the standard Healer has no eligible wounded target.

The final stage records victory and clears the party before the normal healing phase. Successful expeditions do not output the adventurers. A wipe or victory sets five cooldown ticks and resets stage progress to the beginning.

## Retreat and extra loot

Retreat refunds each supply currency by the fraction 1 − zero-based CurrentStage ÷ total stages, truncating each refund to an integer. It clears the party and run with two cooldown ticks. Changing dungeon selection mid-run invokes retreat.

Trash Loot upgrades independently give a 5% × upgrade-count chance each nonboss combat tick to award 25% of every Ducat reward on that stage. This explicit 0.25 reward call does not use the node CoinLootMultiplier. Normal stage currency rewards do use the coin multiplier, which grows by 0.1 per coin upgrade.

## Sources

- `Assets.Source.Flow.Elements/Dungeon.cs:61`
- `Assets.Source.Flow.Elements/Dungeon.cs:207`
- `Assets.Source.Flow.Elements/Dungeon.cs:200`
- `Assets.Source.Adventure/DungeonProgress.cs:83`
- `Assets.Source.Adventure/DungeonProgress.cs:324`
- `Assets.Source.Adventure/DungeonProgress.cs:277`
- `Assets.Source.Adventure/DungeonStage.cs:23`
- `Assets.Source.Adventure.Rewards/CurrencyReward.cs:31`
