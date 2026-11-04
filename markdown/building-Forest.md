# Forest

Hunters, loggers and foragers provide a wide variety of supplies to your kingdom.

## Purpose

Hunters, loggers and foragers provide a wide variety of supplies to your kingdom.

## Building reference

| Property | Value |
| --- | --- |
| Type | Forest |
| Category | Resource |
| Inheritance | Forest → FlowElement |
| Research required | [Forest](tech-forest.md) |

## Resource selections

| Resource | Unlock |
| --- | --- |
| [Softwood Log](item-wood_log.md) | [Harvest Wood Log](tech-forest_wood_log.md) |
| [Wolf Hide](item-wolf_hide.md) | [Wolf Hunt](tech-forest_wolf_hide.md) |
| [Small Bird Egg](item-bird_egg.md) | [Harvest Bird Eggs](tech-forest_bird_egg.md) |
| [Boar Meat](item-boar_meat.md) | [Boar Hunt](tech-forest_boar_meat.md) |
| [Wild Lettuce](item-lettuce.md) | [Harvest Lettuce](tech-forest_lettuce.md) |
| [Resin](item-resin.md) | [Harvest Resin](tech-forest_resin.md) |
| [Bone](item-bone.md) | [Harvest Bone](tech-forest_bone.md) |
| [Mushroom](item-mushroom.md) | [Harvest Mushrooms](tech-forest_mushroom.md) |
| [Ancient Wood Log](item-ancient_wood_log.md) | [Harvest Ancient Wood](tech-forest_ancient_wood.md) |
| [Supple Leather](item-supple_leather.md) | [Stalker Hunt](tech-forest_supple_leather.md) |
| [Wild Onion](item-wild_onion.md) | [Harvest Wild Onion](tech-forest_wild_onion.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Cross-country Carriers](tech-forest_automation.md) | 4 |
| [Forest · second add-on slot](tech-forest_automation_2.md) | 5 |
| [Forest · overseers](tech-forest_productivity.md) | 5 |
| [Forest · artisans](tech-forest_quality.md) | 6 |
| [Forest · third add-on slot](tech-forest_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Forest |
| Category | ElementCategory.Resource |
| Icon | SelectedResource?.GetIcon() ?? base.Icon |
| Icon Name | Icons 65 |
| Music Track | Explore The Forest LOOP BPM130 |
| Output Per Second | 1f * Speed |
| Stackable | true |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Forest",
  "Inherited behavior": "Forest → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Forest.cs:13`
