# Tech List View

Adds an additional list view to the Tech Tree, so you can view an ordered list of available tech alongside the tree view.

## Research effect

Adds an additional list view to the Tech Tree, so you can view an ordered list of available tech alongside the tree view.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | global_tech_upgrade |
| Type | Utility |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventurer's Guild](tech-adventurers_guild.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"adventurers_guild\"",
  "RelativePosition": "new Vector2Int(315, 45)",
  "CostMultiplier": "3.0",
  "IconName": "\"Icons_175\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tif ((bool)TechTreeMenu.Instance)\n\t\t\t\t{\n\t\t\t\t\tTechTreeMenu.Instance.UpdateTechListButton(newUnlock: true);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:48`
- `Assets.Source.Player/TechNode.cs:1`
