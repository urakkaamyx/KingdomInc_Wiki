# Class trait effects

Implemented role bonuses for every specialization, separate from power multipliers.

## Parent traits

Here q is trait quality, normally fixed at 1 for declared class traits. Final classes retain their parent trait.

| Trait | Effect |
| --- | --- |
| Guardian; Paladin/Bulwark retain it | With Shield: incoming damage ÷ (1 + 0.1q) |
| Battlemaster; Berserker/Reaver retain it | Combat Power bonus stat × (1 + 0.05q) |
| Thief; Assassin/Swashbuckler retain it | Dual wield damage multiplier × (1 + 0.1q) |
| Ranger; Beast Master/Survivalist retain it | Bow damage multiplier × (1 + 0.1q) |
| Elementalist; Pyromancer/Lithomancer retain it | Damage multiplier × (1 + 0.05q) |
| Warlock; Necrolyte/Demonologist retain it | Group Health buff × (1 + 0.1q) |
| Ritualist; Shaman/Inquisitor retain it | Damage multiplier × (1 + 0.2q) |
| Priest; Evangelist/Lightbringer retain it | Healing done × (1 + 0.1q) |

## Final effects

These add to retained parent traits.

| Class | Additional effect |
| --- | --- |
| Paladin | 50% chance per dungeon healing hook: heal lowest-health eligible ally other than self for base healing ÷ 20 |
| Bulwark | Armor gains actual offhand Shield Armor × q |
| Berserker | Without Heavy armor qualification: damage multiplier × (1 + 0.2q) |
| Reaver | While dual wielding: damage multiplier × (1 + 0.1q) |
| Assassin | Dungeon group buff: boss damage multiplier × (1 + 0.03q) |
| Swashbuckler | Dungeon Tank group buff: boss damage taken × (1 − 0.1q) |
| Beast Master, Necrolyte, Demonologist, Shaman | Dungeon damage multiplier gains +0.15q; companion is not a separate combatant |
| Survivalist | Group Poison resistance |
| Pyromancer | Group Fire resistance |
| Lithomancer | Group +50q Armor |
| Inquisitor | Combat Power bonus gains 0.5 × current Strength × q; Minor Healer role |
| Evangelist | 33.3% chance per dungeon healing hook: heal every member for base healing ÷ 40 |
| Lightbringer | Dungeon Tank group buff: healing received on boss stages × (1 + 0.1q) |

## Healer inheritance

Cleric, Ritualist, Priest, Shaman, Evangelist, and Lightbringer declare full Healer. Inquisitor instead has Minor Healer: 50% chance on dungeon-healing and war hooks to heal an eligible ally other than self for base healing ÷ 25. Fighter-archetype descendants can gain Tank through equipment regardless of branch.

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:130`
- `Assets.Source.Adventure/AdventurerTrait.cs:205`
- `Assets.Source.Adventure/AdventurerTrait.cs:255`
- `Assets.Source.Adventure/AdventurerTrait.cs:299`
- `Assets.Source.Adventure/AdventurerTrait.cs:376`
- `Assets.Source.Adventure/AdventurerTrait.cs:402`
- `Assets.Source.Items.Impl/Adventurers.cs:462`
