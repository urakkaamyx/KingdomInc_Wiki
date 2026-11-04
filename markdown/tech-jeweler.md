# Jeweler

Creates finely crafted rings and amulets imbued with magical energy.

## Research effect

Creates finely crafted rings and amulets imbued with magical energy.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | jeweler |
| Type | Flow Element |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Dungeon](tech-dungeon.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Identify Gemstones](tech-identify_gem.md) |

## Leads to

| Research |
| --- |
| [Engraved Jewelry](tech-engrave_jewelry_quality.md) |
| [Grinding Wheel](tech-jeweler_automation.md) |
| [Jeweler · second add-on slot](tech-jeweler_automation_2.md) |
| [Jeweler · overseers](tech-jeweler_productivity.md) |
| [Jeweler · artisans](tech-jeweler_quality.md) |
| [Jeweler · third add-on slot](tech-jeweler_automation_3.md) |
| [Identify Gemstones](tech-identify_gem.md) |
| [Empty Setting](tech-gem_setting.md) |
| [Elegant Ring](tech-simple_ring.md) |
| [Ring of Strength](tech-ring_of_strength.md) |
| [Ring of Dexterity](tech-ring_of_dexterity.md) |
| [Ring of Magic](tech-ring_of_magic.md) |
| [Ring of Wisdom](tech-ring_of_wisdom.md) |
| [Ring of Health](tech-ring_of_health.md) |
| [Ring of Protection](tech-ring_of_armor.md) |
| [Band of the Cyclops](tech-ring_of_strength_2.md) |
| [Serpentine Band](tech-ring_of_dexterity_2.md) |
| [Monsoon Band](tech-ring_of_magic_2.md) |
| [Band of Tranquility](tech-ring_of_wisdom_2.md) |
| [Undying Band](tech-ring_of_health_2.md) |
| [Leaden Band](tech-ring_of_armor_2.md) |
| [Amulet of Vitality](tech-amulet_of_healing.md) |
| [Amulet of Vigor](tech-amulet_of_energy.md) |
| [Amulet of Fire Protection](tech-amulet_of_fire_prot.md) |
| [Amulet of Dark Tidings](tech-amulet_of_shadow_prot.md) |
| [Panacea Amulet](tech-amulet_of_poison_prot.md) |
| [Lifebloom Amulet](tech-lifebloom_amulet.md) |
| [Necklace of Fireballs](tech-fireball_amulet.md) |
| [Medallion of Excellence](tech-stats_amulet.md) |
| [Prayer Beads](tech-prayer_beads.md) |
| [Treasury](tech-treasury.md) |
| [Summoning Circle](tech-summoning_circle.md) |
| [Alchemist](tech-alchemist.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"dungeon\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_198\"",
  "ForceRootNode": "true",
  "CostMultiplier": "1.5",
  "CostCurrency": "CurrencyCollection.GoldDucat",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"identify_gem\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
