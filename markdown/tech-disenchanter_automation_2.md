# Disenchanter · second add-on slot

Disenchanter · second add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | disenchanter_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Disenchanter](tech-disenchanter.md) |
| [Mana Vacuum](tech-disenchanter_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Aether Collector](tech-disenchanter_passive.md) |
| [Disenchanter · third add-on slot](tech-disenchanter_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Disenchanter\", \"callSource\": \"source/Assets.Source.Player.Tech/T6Disenchanter.cs\", \"callLine\": 32, \"id\": \"disenchanter_automation_2\", \"previous\": \"disenchanter_automation\", \"tier\": 7, \"additional\": [\"war_effort\", \"quest_board\"], \"name\": \"Disenchanter · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"disenchanter\", \"requires\": [\"disenchanter\", \"disenchanter_automation\", \"war_effort\", \"quest_board\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T6Disenchanter.cs:32`
