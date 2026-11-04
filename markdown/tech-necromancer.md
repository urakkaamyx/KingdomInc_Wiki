# Necromancer

A shady figure who will "appropriate" corpses from a conveniently situated graveyard for their sinister experiments.

## Research effect

A shady figure who will "appropriate" corpses from a conveniently situated graveyard for their sinister experiments.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | necromancer |
| Type | Flow Element |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Graveyard](tech-graveyard.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Undead Shambler](tech-shambler.md) |

## Leads to

| Research |
| --- |
| [Flesh Sculptor](tech-refiner_human.md) |
| [Novice Necromancer](tech-necromancer_automation.md) |
| [Necromancer · second add-on slot](tech-necromancer_automation_2.md) |
| [Necromancer · overseers](tech-necromancer_productivity.md) |
| [Necromancer · artisans](tech-necromancer_quality.md) |
| [Necromancer · third add-on slot](tech-necromancer_automation_3.md) |
| [Undead Shambler](tech-shambler.md) |
| [Skeletal Archer](tech-skeletal_archer.md) |
| [Skeletal Berserker](tech-skeletal_berserker.md) |
| [Skeletal Archmage](tech-skeletal_mage.md) |
| [Hulking Monstrosity](tech-hulking_monstrosity.md) |
| [Introduction to Necromancy](tech-cr_necrolyte.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"graveyard\"",
  "RelativePosition": "new Vector2Int(-630, 0)",
  "IconName": "\"Icons2_42\"",
  "ForceRootNode": "true",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"shambler\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Necromancer.cs:9`
- `Assets.Source.Player/TechNode.cs:1`
