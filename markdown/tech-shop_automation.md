# Shop Attendant

Unlocks the first Upgrade slot for your Shops.

Unlocks the Worker upgrade to automatically collect profits.

## Research effect

Unlocks the first Upgrade slot for your Shops.

Unlocks the Worker upgrade to automatically collect profits.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shop_automation |
| Type | Upgrade Slot |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Item Shop](tech-shop.md) |

## Leads to

| Research |
| --- |
| [Cashier](tech-shop_cashier.md) |
| [Item Shop · second add-on slot](tech-shop_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Shop\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Shop.cs\", \"callLine\": 36, \"id\": \"shop_automation\", \"root\": \"shop\", \"tier\": 1, \"name\": \"Shop Attendant\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"shop\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Shop.cs:36`
