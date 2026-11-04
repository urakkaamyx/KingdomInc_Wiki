# Farm

Allows you to cultivate your own food, raise animals, and grow powerful reagents directly from the soil.

## Purpose

Allows you to cultivate your own food, raise animals, and grow powerful reagents directly from the soil.

## Building reference

| Property | Value |
| --- | --- |
| Type | Farm |
| Category | Resource |
| Inheritance | Farm → ResourceElement → FlowElement |
| Research required | [Farm](tech-farm.md) |

## Resource selections

| Resource | Unlock |
| --- | --- |
| [Cattle](item-cattle.md) | [Cattle Husbandry](tech-farm_cattle.md) |
| [Wheat](item-wheat.md) | [Wheat Cultivation](tech-farm_wheat.md) |
| [Flax](item-flax.md) | [Flax Cultivation](tech-farm_flax.md) |
| [Cotton](item-cotton.md) | [Cotton Cultivation](tech-farm_cotton.md) |
| [Salamander](item-salamander.md) | [Salamander Husbandry](tech-farm_salamander.md) |
| [Stalker](item-stalker.md) | [Stalker Husbandry](tech-farm_stalker.md) |
| [Onion](item-onion.md) | [Onion Cultivation](tech-farm_onion.md) |
| [Soothing Herbs](item-soothing_herbs.md) | [Herb Cultivation](tech-farm_soothing_herbs.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Farmhand](tech-farm_automation.md) | 7 |
| [Farm · second add-on slot](tech-farm_automation_2.md) | 8 |
| [Farm · overseers](tech-farm_productivity.md) | 8 |
| [Farm · artisans](tech-farm_quality.md) | 9 |
| [Farm · third add-on slot](tech-farm_automation_3.md) | 9 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Default Label | Farm |
| Default Icon Name | Icons 182 |
| Action Label | Click to choose a new material to extract. |
| Music Track | Explore The Forest LOOP BPM130 |
| Label | DefaultLabel |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Farm",
  "Inherited behavior": "Farm → ResourceElement → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Farm.cs:6`
