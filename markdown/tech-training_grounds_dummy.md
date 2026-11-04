# Training Dummy

Adds a second input to the Training Grounds. Creatures created by the Summoning Circle can be inserted here to serve as target practice, doubling the effectiveness of the Training Grounds.

## Research effect

Adds a second input to the Training Grounds. Creatures created by the Summoning Circle can be inserted here to serve as target practice, doubling the effectiveness of the Training Grounds.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | training_grounds_dummy |
| Type | Utility |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Training Grounds](tech-training_grounds.md) |
| [Group Exercise](tech-training_grounds_slot.md) |
| [Summoning Circle](tech-summoning_circle.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"training_grounds_slot\"",
  "RelativePosition": "new Vector2Int(-180, 0)",
  "CostTier": "8",
  "CostMultiplier": "6.0",
  "IconName": "\"Icons_217\"",
  "AdditionalRequirements": "new List<string> { \"summoning_circle\" }",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (TrainingGrounds element3 in ply.GetElements<TrainingGrounds>())\n\t\t\t\t{\n\t\t\t\t\telement3.UpdateInput();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:77`
- `Assets.Source.Player/TechNode.cs:1`
