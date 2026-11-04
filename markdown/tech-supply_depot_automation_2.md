# Supply Depot · second add-on slot

Supply Depot · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_depot_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |
| [Crate Carriers](tech-supply_depot_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Supply Depot · artisans](tech-supply_depot_quality.md) |
| [Supply Depot · third add-on slot](tech-supply_depot_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"SupplyDepot\", \"callSource\": \"source/Assets.Source.Player.Tech/T1SupplyDepot.cs\", \"callLine\": 57, \"id\": \"supply_depot_automation_2\", \"previous\": \"supply_depot_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Supply Depot · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"supply_depot\", \"requires\": [\"supply_depot\", \"supply_depot_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:57`
