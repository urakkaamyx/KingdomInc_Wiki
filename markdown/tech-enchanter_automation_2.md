# Enchanter · second add-on slot

Enchanter · second add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchanter_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Leyline Guide](tech-enchanter_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Enchanter · artisans](tech-enchanter_quality.md) |
| [Enchanter · third add-on slot](tech-enchanter_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Enchanter\", \"callSource\": \"source/Assets.Source.Player.Tech/T6Enchanter.cs\", \"callLine\": 29, \"id\": \"enchanter_automation_2\", \"previous\": \"enchanter_automation\", \"tier\": 7, \"additional\": [\"war_effort\", \"quest_board\"], \"name\": \"Enchanter · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"enchanter\", \"requires\": [\"enchanter\", \"enchanter_automation\", \"war_effort\", \"quest_board\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T6Enchanter.cs:29`
