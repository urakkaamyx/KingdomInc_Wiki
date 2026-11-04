# Supply Depot · artisans

Supply Depot · artisans is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | supply_depot_quality |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Supply Depot](tech-supply_depot.md) |
| [Rapid Delivery](tech-supply_depot_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"SupplyDepot\", \"callSource\": \"source/Assets.Source.Player.Tech/T1SupplyDepot.cs\", \"callLine\": 57, \"id\": \"supply_depot_quality\", \"previous\": \"supply_depot_automation_2\", \"tier\": 4, \"name\": \"Supply Depot · artisans\", \"icon\": \"Icons_118\", \"addon\": \"ResArtisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"supply_depot\", \"requires\": [\"supply_depot\", \"supply_depot_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:57`
