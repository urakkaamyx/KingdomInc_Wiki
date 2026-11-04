# Container Duplication

[Q] or [Middle-click] to copy a Container and everything anchored to it.

## Research effect

[Q] or [Middle-click] to copy a Container and everything anchored to it.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | container_clone |
| Type | Utility |
| Cost tier | 2 |

## Prerequisites

| Required research |
| --- |
| [Clone Tool](tech-clone_tool.md) |
| [Decorations](tech-tech_deco.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"clone_tool\"",
  "AdditionalRequirements": "new List<string> { \"tech_deco\" }",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons_64\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:252`
- `Assets.Source.Player/TechNode.cs:1`
