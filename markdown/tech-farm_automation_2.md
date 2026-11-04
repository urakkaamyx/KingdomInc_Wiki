# Farm · second add-on slot

Farm · second add-on slot is a tier 8 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |
| [Farmhand](tech-farm_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Farm · artisans](tech-farm_quality.md) |
| [Farm · third add-on slot](tech-farm_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Farm\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Farm.cs\", \"callLine\": 35, \"id\": \"farm_automation_2\", \"previous\": \"farm_automation\", \"tier\": 8, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Farm · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"farm\", \"requires\": [\"farm\", \"farm_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Farm.cs:35`
