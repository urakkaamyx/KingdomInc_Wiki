# Item Shop

Sells most items on the open market for a fair price.

## Purpose

Sells most items on the open market for a fair price.

## Building reference

| Property | Value |
| --- | --- |
| Type | Shop |
| Category | Consumption |
| Inheritance | Shop → FlowElement |
| Research required | [Item Shop](tech-shop.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Shop Attendant](tech-shop_automation.md) | 1 |
| [Item Shop · second add-on slot](tech-shop_automation_2.md) | 3 |
| [Item Shop coffers](tech-shop_coffers.md) | 3 |
| [Item Shop · third add-on slot](tech-shop_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Item Shop |
| Icon Name | Icons 3 |
| Music Track | This Town LOOP BPM130 |
| Category | ElementCategory.Consumption |
| Stackable | true |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Shop",
  "Inherited behavior": "Shop → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Shop.cs:14`
