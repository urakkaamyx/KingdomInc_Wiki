# Tailor · second add-on slot

Tailor · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tailor_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |
| [Animated Scissors](tech-tailor_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Tailor · artisans](tech-tailor_quality.md) |
| [Tailor · third add-on slot](tech-tailor_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Tailor\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Tailor.cs\", \"callLine\": 85, \"id\": \"tailor_automation_2\", \"previous\": \"tailor_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Tailor · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"tailor\", \"requires\": [\"tailor\", \"tailor_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Tailor.cs:85`
