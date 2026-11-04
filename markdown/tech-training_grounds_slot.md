# Group Exercise

Adds an additional training slot to the Training Grounds.

## Research effect

Adds an additional training slot to the Training Grounds.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds_slot |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Training Grounds](tech-training_grounds.md) |

## Leads to

| Research |
| --- |
| [Portal to Swolevania](tech-training_grounds_slot_2.md) |
| [Training Dummy](tech-training_grounds_dummy.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"training_grounds\"",
  "RelativePosition": "new Vector2Int(-135, 315)",
  "CostMultiplier": "5.0",
  "CostCurrency": "CurrencyCollection.GoldRing",
  "IconName": "\"Icons2_55\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (TrainingGrounds element in ply.GetElements<TrainingGrounds>())\n\t\t\t\t{\n\t\t\t\t\telement.UpdateSlotCount();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:43`
- `Assets.Source.Player/TechNode.cs:1`
