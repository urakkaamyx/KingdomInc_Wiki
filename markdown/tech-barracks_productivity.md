# Barracks · overseers

Barracks · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | barracks_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Barracks](tech-barracks.md) |
| [Recruitment Officer](tech-barracks_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Barracks\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Barracks.cs\", \"callLine\": 26, \"id\": \"barracks_productivity\", \"previous\": \"barracks_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Barracks · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"barracks\", \"requires\": [\"barracks\", \"barracks_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Barracks.cs:26`
