# Mine · artisans

Unlocks the Prospector upgrade to increase the quality of mined items, at an additional cost per item.

## Research effect

Unlocks the Prospector upgrade to increase the quality of mined items, at an additional cost per item.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_quality |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |
| [Motivated Workers](tech-mine_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Mine\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Mine.cs\", \"callLine\": 73, \"id\": \"mine_quality\", \"previous\": \"mine_automation_2\", \"tier\": 4, \"name\": \"Mine · artisans\", \"icon\": \"Icons_118\", \"addon\": \"MineArtisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"mine\", \"requires\": [\"mine\", \"mine_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Mine.cs:73`
