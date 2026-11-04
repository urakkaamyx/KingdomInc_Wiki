# Potion Dispenser

Unlocks the first Upgrade slot for your Adventure Supplies.

Unlocks the Worker upgrade to automatically distribute supplies.

## Research effect

Unlocks the first Upgrade slot for your Adventure Supplies.

Unlocks the Worker upgrade to automatically distribute supplies.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventure_supplies_automation |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |

## Leads to

| Research |
| --- |
| [Adventure Supplies · second add-on slot](tech-adventure_supplies_automation_2.md) |
| [Adventure Supplies · overseers](tech-adventure_supplies_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"AdventureSupplies\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurerSupplies.cs\", \"callLine\": 23, \"id\": \"adventure_supplies_automation\", \"root\": \"adventure_supplies\", \"tier\": 5, \"name\": \"Potion Dispenser\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"adventure_supplies\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:23`
