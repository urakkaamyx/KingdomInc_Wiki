# Barracks · second add-on slot

Barracks · second add-on slot is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | barracks_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Barracks](tech-barracks.md) |
| [Recruitment Officer](tech-barracks_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Barracks · artisans](tech-barracks_quality.md) |
| [Barracks · third add-on slot](tech-barracks_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Barracks\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Barracks.cs\", \"callLine\": 26, \"id\": \"barracks_automation_2\", \"previous\": \"barracks_automation\", \"tier\": 4, \"additional\": [\"war_effort\"], \"name\": \"Barracks · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"barracks\", \"requires\": [\"barracks\", \"barracks_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Barracks.cs:26`
