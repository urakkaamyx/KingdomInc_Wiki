# No Waiting Around

Allows you to set up a timeout to allow adventurers to pass through if no equipment is available.

## Research effect

Allows you to set up a timeout to allow adventurers to pass through if no equipment is available.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | outfitter_timeout |
| Type | Utility |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Self Service](tech-outfitter_automation.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"outfitter_automation\"",
  "RelativePosition": "new Vector2Int(-180, 0)",
  "IconName": "\"Icons_75\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Barracks.cs:65`
- `Assets.Source.Player/TechNode.cs:1`
