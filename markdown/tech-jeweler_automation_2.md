# Jeweler · second add-on slot

Jeweler · second add-on slot is a tier 9 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | jeweler_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |
| [Grinding Wheel](tech-jeweler_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Jeweler · artisans](tech-jeweler_quality.md) |
| [Jeweler · third add-on slot](tech-jeweler_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Jeweler\", \"callSource\": \"source/Assets.Source.Player.Tech/T8Jeweler.cs\", \"callLine\": 24, \"id\": \"jeweler_automation_2\", \"previous\": \"jeweler_automation\", \"tier\": 9, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Jeweler · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"jeweler\", \"requires\": [\"jeweler\", \"jeweler_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8Jeweler.cs:24`
