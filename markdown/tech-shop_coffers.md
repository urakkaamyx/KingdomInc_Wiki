# Item Shop coffers

Unlocks the Coffers upgrade to allow the Shop to accumulate more gold per collection cycle.

## Research effect

Unlocks the Coffers upgrade to allow the Shop to accumulate more gold per collection cycle.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shop_coffers |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Item Shop](tech-shop.md) |
| [Slick Salesman](tech-shop_automation_2.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 175, \"generated\": true, \"building\": \"Shop\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Shop.cs\", \"callLine\": 50, \"id\": \"shop_coffers\", \"previous\": \"shop_automation_2\", \"additional\": [\"war_effort\"], \"tier\": 3, \"name\": \"Item Shop coffers\", \"icon\": \"Icons_120\", \"addon\": \"Coffers\", \"root\": \"shop\", \"requires\": [\"shop\", \"shop_automation_2\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:175`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Shop.cs:50`
