# Item Shop · second add-on slot

Item Shop · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shop_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Item Shop](tech-shop.md) |
| [Shop Attendant](tech-shop_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Item Shop coffers](tech-shop_coffers.md) |
| [Item Shop · third add-on slot](tech-shop_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Shop\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Shop.cs\", \"callLine\": 49, \"id\": \"shop_automation_2\", \"previous\": \"shop_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Item Shop · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"shop\", \"requires\": [\"shop\", \"shop_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Shop.cs:49`
