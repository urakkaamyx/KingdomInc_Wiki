# Supply Depot · overseers

Supply Depot · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_depot_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |
| [Crate Carriers](tech-supply_depot_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"SupplyDepot\", \"callSource\": \"source/Assets.Source.Player.Tech/T1SupplyDepot.cs\", \"callLine\": 57, \"id\": \"supply_depot_productivity\", \"previous\": \"supply_depot_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Supply Depot · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"supply_depot\", \"requires\": [\"supply_depot\", \"supply_depot_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:57`
