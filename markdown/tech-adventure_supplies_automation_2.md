# Adventure Supplies · second add-on slot

Adventure Supplies · second add-on slot is a tier 6 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventure_supplies_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Potion Dispenser](tech-adventure_supplies_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Adventure Supplies · artisans](tech-adventure_supplies_quality.md) |
| [Adventure Supplies · third add-on slot](tech-adventure_supplies_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"AdventureSupplies\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurerSupplies.cs\", \"callLine\": 23, \"id\": \"adventure_supplies_automation_2\", \"previous\": \"adventure_supplies_automation\", \"tier\": 6, \"additional\": [\"war_effort\", \"quest_board\"], \"name\": \"Adventure Supplies · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"adventure_supplies\", \"requires\": [\"adventure_supplies\", \"adventure_supplies_automation\", \"war_effort\", \"quest_board\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:23`
