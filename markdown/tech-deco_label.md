# Label

Attach a name to parts of your workflow to remind yourself of their purpose.

## Research effect

Attach a name to parts of your workflow to remind yourself of their purpose.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | deco_label |
| Type | Decoration |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Decorations](tech-tech_deco.md) |

## Leads to

| Research |
| --- |
| [Sticker](tech-deco_sticker.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Decoration",
  "Previous": "\"tech_deco\"",
  "RelativePosition": "new Vector2Int(-180, 0)",
  "IconName": "\"Icons_32\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Mine.cs:96`
- `Assets.Source.Player/TechNode.cs:1`
