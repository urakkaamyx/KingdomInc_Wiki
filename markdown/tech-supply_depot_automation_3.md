# Supply Depot · third add-on slot

Supply Depot · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_depot_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |
| [Rapid Delivery](tech-supply_depot_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"SupplyDepot\", \"callSource\": \"source/Assets.Source.Player.Tech/T1SupplyDepot.cs\", \"callLine\": 57, \"id\": \"supply_depot_automation_3\", \"previous\": \"supply_depot_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Supply Depot · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"supply_depot\", \"requires\": [\"supply_depot\", \"supply_depot_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:57`
