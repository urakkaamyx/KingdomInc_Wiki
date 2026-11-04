# Adventure Supplies · third add-on slot

Adventure Supplies · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventure_supplies_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Overseas Import](tech-adventure_supplies_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"AdventureSupplies\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurerSupplies.cs\", \"callLine\": 23, \"id\": \"adventure_supplies_automation_3\", \"previous\": \"adventure_supplies_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Adventure Supplies · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"adventure_supplies\", \"requires\": [\"adventure_supplies\", \"adventure_supplies_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:23`
