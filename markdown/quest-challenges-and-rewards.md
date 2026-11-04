# Quest challenges, rewards, and permanent discounts

What specialization markers and quest hazards actually do, including first-clear economics.

## Quest hazards

Triggered challenges independently roll each whole quest progress tick. Dangerous has the default 5% trigger chance: each participant takes random ordinary damage around (15 + quest difficulty ÷ 50) × (quest difficulty ÷ participant base damage), with a ÷1.3 to ×1.3 range.

Exhausting triggers every progress tick and adds 10% of the normal quest energy cost. Dexterity Energy triggers at the default 5% chance; each participant failing a Dexterity test against raw quest difficulty pays 15 times normal quest energy cost.

Fighter, Rogue, and Mage specialization markers halve effective difficulty for matching archetypes. Cleric specialization quarters it. These alter progress contribution and the low-performance penalty, but Dangerous and Dexterity Energy use the raw quest difficulty. Increase Duration is a descriptive marker; the actual duration formula is the quest’s DurationMultiplier.

## First and repeat rewards

Currency and item rewards are granted once per completed group, not once per participant. Advancement rewards inspect every group member and change only exact matching class types. First-clear and repeat reward lists can differ.

Currency reward count is rounded after multiplying by the board or dungeon’s CoinLootMultiplier. Item reward count is fixed. Item quality uses the output element’s quality: when above 1, it rolls reward quality × random((1 + element quality) ÷ 2, element quality). The default reward quality is 1.

Each Quest Item Loot and Dungeon Item Loot upgrade contributes +0.1 element quality. It improves the quality of reward items rather than multiplying their declared counts.

## Permanent economic rewards

Clear Mines first sets the Iron Ore discount flag; the resource cost multiplier becomes 0.25. Each repeat multiplies it by another 0.95: 0.25 × 0.95^repeat counter. Its difficulty is 470, base duration 180, and duration multiplier 1.05.

Forest Evangelism first halves forest-worker cost, with each repeat multiplying by another 0.95: 0.5 × 0.95^repeat counter. It has difficulty 600, base duration 180, duration multiplier 1.05, and the Cleric specialization marker. These discounts multiply other applicable cost calculations.

## Quest roster

Ordinary quests are Patrol Market, Exterminate Rats, Dispel Library, Clear Mines, Forest Evangelism, and Mercurial Reagents. Eight further quests provide the intermediate class branches. Use each quest’s entity page for exact first/repeat items and research gates.

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:31`
- `Assets.Source.Adventure/QuestChallenge.cs:48`
- `Assets.Source.Adventure/QuestChallenge.cs:71`
- `Assets.Source.Adventure/QuestChallenge.cs:120`
- `Assets.Source.Adventure.Quests/SimpleQuests.cs:65`
- `Assets.Source.Player/GamePlayer.cs:422`
- `Assets.Source.Player/ForestSettings.cs:30`
- `Assets.Source.Adventure.Rewards/ItemReward.cs:47`
- `Assets.Source.Adventure.Rewards/CurrencyReward.cs:36`
- `Assets.Source.Flow.Upgrades/QuestItemLoot.cs:18`
- `Assets.Source.Flow.Upgrades/DungeonItemLoot.cs:15`
