# Track Switch

Adds a second output to the Switch that's active when the lever is in the lower position.

## Research effect

Adds a second output to the Switch that's active when the lever is in the lower position.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | track_switch_2 |
| Type | Utility |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Switch](tech-track_switch.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Utility",
  "Previous": "\"track_switch\"",
  "RelativePosition": "new Vector2Int(225, 60)",
  "IconName": "\"Icons_73\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tforeach (TrackSwitch element in ply.GetElements<TrackSwitch>())\n\t\t\t\t{\n\t\t\t\t\telement.UpdateTrackSwitch();\n\t\t\t\t\tif ((bool)element.World)\n\t\t\t\t\t{\n\t\t\t\t\t\telement.World.UpdateIO();\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3WarEffort.cs:58`
- `Assets.Source.Player/TechNode.cs:1`
