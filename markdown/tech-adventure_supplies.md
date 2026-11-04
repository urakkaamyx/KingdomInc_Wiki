# Adventure Supplies

A globally renowned company that provides the adventurous customer with basic adventuring goods.

## Research effect

A globally renowned company that provides the adventurous customer with basic adventuring goods.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventure_supplies |
| Type | Flow Element |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Supply healing potion](tech-supply_healing_potion.md) |
| [Supply rations](tech-supply_rations.md) |

## Leads to

| Research |
| --- |
| [Potion Dispenser](tech-adventure_supplies_automation.md) |
| [Adventure Supplies · second add-on slot](tech-adventure_supplies_automation_2.md) |
| [Adventure Supplies · overseers](tech-adventure_supplies_productivity.md) |
| [Adventure Supplies · artisans](tech-adventure_supplies_quality.md) |
| [Adventure Supplies · third add-on slot](tech-adventure_supplies_automation_3.md) |
| [Healing Potion](tech-supply_healing_potion.md) |
| [Revitalizing Potion](tech-supply_energy_potion.md) |
| [Rations](tech-supply_rations.md) |
| [Training Sword](tech-training_sword.md) |
| [Elixir of Fire Resistance](tech-supply_fire_resist_potion.md) |
| [Elixir of Shadow Resistance](tech-supply_shadow_resist_potion.md) |
| [Glass Vial](tech-glass_vial.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"quest_board\"",
  "RelativePosition": "new Vector2Int(630, -90)",
  "IconName": "\"Icons_218\"",
  "CostCurrency": "CurrencyCollection.GoldRing",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"supply_healing_potion\");\n\t\t\t\tply.AddTech(\"supply_rations\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
