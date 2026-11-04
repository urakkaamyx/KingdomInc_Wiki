# Leatherworker · second add-on slot

Leatherworker · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | leatherworker_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Leatherworker](tech-leatherworker.md) |
| [Honest Craftmanship](tech-leatherworker_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Leatherworker · artisans](tech-leatherworker_quality.md) |
| [Leatherworker · third add-on slot](tech-leatherworker_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Leatherworker\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Leatherworker.cs\", \"callLine\": 94, \"id\": \"leatherworker_automation_2\", \"previous\": \"leatherworker_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Leatherworker · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"leatherworker\", \"requires\": [\"leatherworker\", \"leatherworker_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:94`
