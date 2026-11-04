# Crate Carriers

Unlocks the first Upgrade slot for your Supply Depots.

Unlocks the Worker upgrade to automate resource distribution.

## Research effect

Unlocks the first Upgrade slot for your Supply Depots.

Unlocks the Worker upgrade to automate resource distribution.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_depot_automation |
| Type | Upgrade Slot |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |

## Leads to

| Research |
| --- |
| [Supply Depot · second add-on slot](tech-supply_depot_automation_2.md) |
| [Supply Depot · overseers](tech-supply_depot_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"SupplyDepot\", \"callSource\": \"source/Assets.Source.Player.Tech/T1SupplyDepot.cs\", \"callLine\": 57, \"id\": \"supply_depot_automation\", \"root\": \"supply_depot\", \"tier\": 1, \"name\": \"Crate Carriers\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"supply_depot\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:57`
