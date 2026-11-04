# Tactical Waitstaff

Unlocks the first Upgrade slot for your Restaurant.

Unlocks the Worker upgrade to automatically sell food.

## Research effect

Unlocks the first Upgrade slot for your Restaurant.

Unlocks the Worker upgrade to automatically sell food.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | restaurant_automation |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Restaurant](tech-restaurant.md) |

## Leads to

| Research |
| --- |
| [Restaurant · second add-on slot](tech-restaurant_automation_2.md) |
| [Big Tippers](tech-restaurant_big_tippers.md) |
| [Royal Assent](tech-restaurant_crowns.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Restaurant\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Kitchen.cs\", \"callLine\": 54, \"id\": \"restaurant_automation\", \"root\": \"restaurant\", \"tier\": 7, \"name\": \"Tactical Waitstaff\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"restaurant\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Kitchen.cs:54`
