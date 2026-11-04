# Automation and shared machine upgrades

Worker, extra slots, quality, and productivity research.

## Default family

AddDefaultUpgrades creates Worker, second slot, productivity, quality, and third slot technologies. Some branches use custom subsets or replace prices afterward. These researches allow upgrades or slots; they do not purchase and install the actual worker or upgrade on every machine.

## Requirements and effects

| Suffix | Requirements | Effect | Cost tier |
| --- | --- | --- | --- |
| _automation | Root machine | One slot and Worker upgrade available | Inherit root |
| _automation_2 | Worker tech, war_effort, plus tier currency-system prerequisites | Two slots | max(worker tier+1,3); multiplier 3 |
| _productivity | Worker tech and war_effort | Overseer upgrade available | max(worker tier+1,4) |
| _quality | Second-slot tech; forest war stage 2 | Artisan variant available | max(second-slot tier+1,4) |
| _automation_3 | Second-slot tech and dungeon | Three slots | max(second-slot tier+1,7); multiplier 3 |
| _coffers | Second-slot tech and war_effort | Coffers upgrade available | 3 |

## Additional slot-two requirements

The helper starts with war_effort. Based on DEFAULT tier currency, it then adds requisition_office for Requisition, war_effort for Medals, quest_board for Rings, or dungeon for Ducats. Duplicated war_effort entries are possible. Later per-node currency overrides do not recalculate that list.

## Quality variants

Mine, resource suppliers, Forest, Farm, Barracks recruiting, and Training Grounds use specialized Artisan types. Normal crafting uses Artisan. Productivity wording depends on whether the machine processes equipment and enhancements. Individual machine branches can substitute specialized upgrades and slot rules. The tier articles preserve helper calls and post-creation overrides.

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNodeHelper.cs:50`
- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNodeHelper.cs:193`
