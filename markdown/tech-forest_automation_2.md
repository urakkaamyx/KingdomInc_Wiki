# Forest · second add-on slot

Forest · second add-on slot is a tier 5 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |
| [Cross-country Carriers](tech-forest_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Forest · artisans](tech-forest_quality.md) |
| [Forest · third add-on slot](tech-forest_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Forest\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Forest.cs\", \"callLine\": 39, \"id\": \"forest_automation_2\", \"previous\": \"forest_automation\", \"tier\": 5, \"additional\": [\"war_effort\", \"quest_board\"], \"name\": \"Forest · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"forest\", \"requires\": [\"forest\", \"forest_automation\", \"war_effort\", \"quest_board\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Forest.cs:39`
