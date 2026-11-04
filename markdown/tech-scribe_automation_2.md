# Scribe · second add-on slot

Scribe · second add-on slot is a tier 11 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | scribe_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |
| [Enchanted Quill](tech-scribe_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Scribe · artisans](tech-scribe_quality.md) |
| [Scribe · third add-on slot](tech-scribe_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Scribe\", \"callSource\": \"source/Assets.Source.Player.Tech/T10Scribe.cs\", \"callLine\": 23, \"id\": \"scribe_automation_2\", \"previous\": \"scribe_automation\", \"tier\": 11, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Scribe · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"scribe\", \"requires\": [\"scribe\", \"scribe_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T10Scribe.cs:23`
