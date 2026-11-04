# Cashier

Unlocks a new Upgrade for your Shops.

Increases the sell value of items by {0}.

## Research effect

Unlocks a new Upgrade for your Shops.

Increases the sell value of items by {0}.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shop_cashier |
| Type | Upgrade Slot |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Item Shop](tech-shop.md) |
| [Shop Attendant](tech-shop_automation.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"shop_automation\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "Description": "Translation.TranslateOnly(\"@shop_cashier_desc\", GameMath.FormatPercentage(0.05000000074505806))",
  "IconName": "\"Icons_119\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Shop\", \"Cashier\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Shop.cs:37`
- `Assets.Source.Player/TechNode.cs:1`
