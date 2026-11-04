# Item Shop · third add-on slot

Item Shop · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shop_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Item Shop](tech-shop.md) |
| [Slick Salesman](tech-shop_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"Shop\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Shop.cs\", \"callLine\": 51, \"id\": \"shop_automation_3\", \"previous\": \"shop_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Item Shop · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"shop\", \"requires\": [\"shop\", \"shop_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Shop.cs:51`
