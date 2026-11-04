# Adventure Supplies

A globally renowned company that provides the adventurous customer with basic adventuring goods.

## Purpose

A globally renowned company that provides the adventurous customer with basic adventuring goods.

## Building reference

| Property | Value |
| --- | --- |
| Type | AdventureSupplies |
| Category | Resource |
| Inheritance | AdventureSupplies → ResourceElement → FlowElement |
| Research required | [Adventure Supplies](tech-adventure_supplies.md) |

## Resource selections

| Resource | Unlock |
| --- | --- |
| [Healing Potion](item-healing_potion.md) | [Supply healing potion](tech-supply_healing_potion.md) |
| [Revitalizing Potion](item-energy_potion.md) | [Supply energy potion](tech-supply_energy_potion.md) |
| [Rations](item-rations.md) | [Supply rations](tech-supply_rations.md) |
| [Training Sword](item-training_sword.md) | [Training Sword](tech-training_sword.md) |
| [Elixir of Fire Resistance](item-fire_resist_potion.md) | [Supply fire resist potion](tech-supply_fire_resist_potion.md) |
| [Elixir of Shadow Resistance](item-shadow_resist_potion.md) | [Supply shadow resist potion](tech-supply_shadow_resist_potion.md) |
| [Glass Vial](item-glass_vial.md) | [Glass Vial](tech-glass_vial.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Potion Dispenser](tech-adventure_supplies_automation.md) | 5 |
| [Adventure Supplies · second add-on slot](tech-adventure_supplies_automation_2.md) | 6 |
| [Adventure Supplies · overseers](tech-adventure_supplies_productivity.md) | 6 |
| [Adventure Supplies · artisans](tech-adventure_supplies_quality.md) | 7 |
| [Adventure Supplies · third add-on slot](tech-adventure_supplies_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Default Label | Adventure Supplies |
| Default Icon Name | Icons 218 |
| Action Label | Click to choose a new material to supply. |
| Music Track | This Town LOOP BPM130 |
| Label | DefaultLabel |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "AdventureSupplies",
  "Inherited behavior": "AdventureSupplies → ResourceElement → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/AdventureSupplies.cs:6`
