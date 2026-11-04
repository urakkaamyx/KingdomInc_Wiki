# Supply Depot

Supplies a variety of raw materials in small quantities.

## Purpose

Supplies a variety of raw materials in small quantities.

## Building reference

| Property | Value |
| --- | --- |
| Type | SupplyDepot |
| Category | Resource |
| Inheritance | SupplyDepot → ResourceElement → FlowElement |
| Research required | [Supply Depot](tech-supply_depot.md) |

## Resource selections

| Resource | Unlock |
| --- | --- |
| [Softwood Plank](item-wood_plank.md) | [Supply Wood Plank](tech-supply_wood_plank.md) |
| [Linen Cloth](item-linen_cloth.md) | [Supply Linen Cloth](tech-supply_linen_cloth.md) |
| [Rough Leather](item-rough_leather.md) | [Supply Rough Leather](tech-supply_rough_leather.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Crate Carriers](tech-supply_depot_automation.md) | 1 |
| [Supply Depot · second add-on slot](tech-supply_depot_automation_2.md) | 3 |
| [Supply Depot · overseers](tech-supply_depot_productivity.md) | 4 |
| [Supply Depot · artisans](tech-supply_depot_quality.md) | 4 |
| [Supply Depot · third add-on slot](tech-supply_depot_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Default Label | Supply Depot |
| Default Icon Name | Icons 16 |
| Action Label | Click to choose a new material to supply. |
| Music Track | Minimal Dungeon LOOP BPM100 |
| Label | DefaultLabel |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "SupplyDepot",
  "Inherited behavior": "SupplyDepot → ResourceElement → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/SupplyDepot.cs:6`
