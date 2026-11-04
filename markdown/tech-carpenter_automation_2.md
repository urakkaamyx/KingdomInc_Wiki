# Carpenter · second add-on slot

Carpenter · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | carpenter_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Only Hammers](tech-carpenter_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Carpenter · artisans](tech-carpenter_quality.md) |
| [Carpenter · third add-on slot](tech-carpenter_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Carpenter\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Carpenter.cs\", \"callLine\": 157, \"id\": \"carpenter_automation_2\", \"previous\": \"carpenter_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Carpenter · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"carpenter\", \"requires\": [\"carpenter\", \"carpenter_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Carpenter.cs:157`
