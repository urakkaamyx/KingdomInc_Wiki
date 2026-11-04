# Decorations

Unlocks the ability to place colored background boxes to organize your workflow.

## Research effect

Unlocks the ability to place colored background boxes to organize your workflow.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tech_deco |
| Type | Decoration |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |

## Leads to

| Research |
| --- |
| [Label](tech-deco_label.md) |
| [Container Duplication](tech-container_clone.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Decoration",
  "Previous": "\"mine\"",
  "RelativePosition": "new Vector2Int(45, 225)",
  "IconName": "\"Icons_31\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tif ((bool)GameUI.Instance)\n\t\t\t\t{\n\t\t\t\t\tGameUI.Instance.UpdateBuildBarButtons();\n\t\t\t\t\tTutorialUI.Instance?.ShowDecoArrow(show: true);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Mine.cs:81`
- `Assets.Source.Player/TechNode.cs:1`
