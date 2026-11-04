# Arena

Organize fights of man versus man or man versus monster. Earn big money for spectacular battles and train your adventurers at the same time.

## Research effect

Organize fights of man versus man or man versus monster. Earn big money for spectacular battles and train your adventurers at the same time.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arena |
| Type | Flow Element |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Alchemist](tech-alchemist.md) |

## Additional condition

Requires war progress: Bastion

## Campaign condition

eastern:4 (campaign ID : completed stage)

## Leads to

| Research |
| --- |
| [Fight Announcer](tech-arena_automation.md) |
| [Arena · second add-on slot](tech-arena_automation_2.md) |
| [Arena · third add-on slot](tech-arena_automation_3.md) |
| [Fight Purse](tech-arena_cashier.md) |
| [Fight To The Death](tech-arena_blood_sport.md) |
| [War: Hidden Enemies](tech-war_effort_yensburg.md) |
| [Temple of the Last Rite](tech-dungeon_temple.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"alchemist\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons2_0\"",
  "ForceRootNode": "true",
  "CostTier": "9",
  "CostCurrency": "CurrencyCollection.GoldDucat",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"eastern\", 4)",
  "CustomRequirementDesc": "\"@arena_unlock\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Arena.cs:11`
- `Assets.Source.Player/TechNode.cs:1`
