# Alchemist

Prepares a wide variety of potions to support your adventurers in combat.

## Research effect

Prepares a wide variety of potions to support your adventurers in combat.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | alchemist |
| Type | Flow Element |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Healing Potion](tech-healing_potion.md) |

## Leads to

| Research |
| --- |
| [Byrgenwald Expedition](tech-byrgenwald_expedition.md) |
| [Extinguish the Ritual](tech-extinguish_ritual.md) |
| [Glass Vial](tech-glass_vial.md) |
| [Herb Cultivation](tech-farm_soothing_herbs.md) |
| [Lifebloom Amulet](tech-lifebloom_amulet.md) |
| [Necklace of Fireballs](tech-fireball_amulet.md) |
| [Autobrewery](tech-alchemist_automation.md) |
| [Alchemist · second add-on slot](tech-alchemist_automation_2.md) |
| [Alchemist · overseers](tech-alchemist_productivity.md) |
| [Alchemist · artisans](tech-alchemist_quality.md) |
| [Alchemist · third add-on slot](tech-alchemist_automation_3.md) |
| [Feral Den](tech-dungeon_feral_den.md) |
| [Attuned Catalyst](tech-attuned_catalyst.md) |
| [Transmute Metals](tech-transmute_metals.md) |
| [Healing Potion](tech-healing_potion.md) |
| [Revitalizing Potion](tech-energy_potion.md) |
| [Identify Plants](tech-identify_plants.md) |
| [Elixir of Fire Resistance](tech-fire_resist_potion.md) |
| [Elixir of Shadow Resistance](tech-shadow_resist_potion.md) |
| [Elixir of Poison Resistance](tech-poison_resist_potion.md) |
| [Stoneskin Elixir](tech-armor_potion.md) |
| [Greater Healing Potion](tech-greater_healing_potion.md) |
| [Elixir of Mastery](tech-stats_potion.md) |
| [Elixir of Alacrity](tech-swiftness_potion.md) |
| [Elixir of Regeneration](tech-regen_potion.md) |
| [Arena](tech-arena.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"jeweler\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_222\"",
  "ForceRootNode": "true",
  "CostTier": "9",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"healing_potion\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
