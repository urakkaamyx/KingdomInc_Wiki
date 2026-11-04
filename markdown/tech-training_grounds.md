# Training Grounds

Increases the quality of your humans, and allows adventurers to train in a specific class when properly equipped.

## Research effect

Increases the quality of your humans, and allows adventurers to train in a specific class when properly equipped.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds |
| Type | Flow Element |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventurer's Guild](tech-adventurers_guild.md) |

## Leads to

| Research |
| --- |
| [Drill Sergeant](tech-training_grounds_automation.md) |
| [Training Grounds · second add-on slot](tech-training_grounds_automation_2.md) |
| [Training Grounds · artisans](tech-training_grounds_quality.md) |
| [Workout Snack](tech-training_grounds_food.md) |
| [Specialized Training](tech-training_grounds_spec.md) |
| [Group Exercise](tech-training_grounds_slot.md) |
| [Portal to Swolevania](tech-training_grounds_slot_2.md) |
| [Training Dummy](tech-training_grounds_dummy.md) |
| [Boot Camp Heroics](tech-boot_camp.md) |
| [Armory](tech-armory.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"adventurers_guild\"",
  "RelativePosition": "new Vector2Int(-630, 0)",
  "IconName": "\"Icons_137\"",
  "ForceRootNode": "true",
  "CostMultiplier": "2.0",
  "CostCurrency": "CurrencyCollection.GoldMedal",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:11`
- `Assets.Source.Player/TechNode.cs:1`
