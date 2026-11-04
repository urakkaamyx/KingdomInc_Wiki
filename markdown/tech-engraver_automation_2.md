# Engraver · second add-on slot

Engraver · second add-on slot is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engraver_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Runic Apprentice](tech-engraver_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Engraver · artisans](tech-engraver_quality.md) |
| [Engraver · third add-on slot](tech-engraver_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Engraver\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Engraver.cs\", \"callLine\": 23, \"id\": \"engraver_automation_2\", \"previous\": \"engraver_automation\", \"tier\": 4, \"additional\": [\"war_effort\"], \"name\": \"Engraver · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"engraver\", \"requires\": [\"engraver\", \"engraver_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Engraver.cs:23`
