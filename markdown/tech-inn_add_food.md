# Bed and Breakfast

Adds a second input to the Inn for Food items. 

Adventurers resting in the Inn will consume food to speed up healing and recover Energy based on the quality of the food.

## Research effect

Adds a second input to the Inn for Food items. 

Adventurers resting in the Inn will consume food to speed up healing and recover Energy based on the quality of the food.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | inn_add_food |
| Type | Utility |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Inn](tech-inn.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Root": "\"inn\"",
  "RelativePosition": "new Vector2Int(-315, 45)",
  "IconName": "\"Icons_160\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (Inn element in ply.GetElements<Inn>())\n\t\t\t\t{\n\t\t\t\t\telement.UpdateFoodInput();\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Inn.cs:20`
- `Assets.Source.Player/TechNode.cs:1`
