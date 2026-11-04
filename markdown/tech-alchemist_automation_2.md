# Alchemist · second add-on slot

Alchemist · second add-on slot is a tier 10 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | alchemist_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Alchemist](tech-alchemist.md) |
| [Autobrewery](tech-alchemist_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Alchemist · artisans](tech-alchemist_quality.md) |
| [Alchemist · third add-on slot](tech-alchemist_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Alchemist\", \"callSource\": \"source/Assets.Source.Player.Tech/T9Alchemist.cs\", \"callLine\": 23, \"id\": \"alchemist_automation_2\", \"previous\": \"alchemist_automation\", \"tier\": 10, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Alchemist · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"alchemist\", \"requires\": [\"alchemist\", \"alchemist_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T9Alchemist.cs:23`
