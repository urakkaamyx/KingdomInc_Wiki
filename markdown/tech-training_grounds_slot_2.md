# Portal to Swolevania

Adds an additional training slot to the Training Grounds.

## Research effect

Adds an additional training slot to the Training Grounds.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds_slot_2 |
| Type | Utility |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Training Grounds](tech-training_grounds.md) |
| [Group Exercise](tech-training_grounds_slot.md) |
| [Enchanter](tech-enchanter.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"training_grounds_slot\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "CostTier": "6",
  "CostMultiplier": "5.0",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "IconName": "\"Icons2_54\"",
  "AdditionalRequirements": "new List<string> { \"enchanter\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (TrainingGrounds element2 in ply.GetElements<TrainingGrounds>())\n\t\t\t\t{\n\t\t\t\t\telement2.UpdateSlotCount();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:59`
- `Assets.Source.Player/TechNode.cs:1`
