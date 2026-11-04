# Feral Den

A natural cave formation buried deep within the Byrgenwald Forest. Some mysterious force inside twists the forest animals into monstrous abominations.

## Research effect

A natural cave formation buried deep within the Byrgenwald Forest. Some mysterious force inside twists the forest animals into monstrous abominations.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_feral_den |
| Type | Dungeon |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Alchemist](tech-alchemist.md) |

## Leads to

| Research |
| --- |
| [Panacea Amulet](tech-amulet_of_poison_prot.md) |
| [Identify Plants](tech-identify_plants.md) |
| [Elixir of Fire Resistance](tech-fire_resist_potion.md) |
| [Elixir of Shadow Resistance](tech-shadow_resist_potion.md) |
| [Elixir of Poison Resistance](tech-poison_resist_potion.md) |
| [Stoneskin Elixir](tech-armor_potion.md) |
| [Greater Healing Potion](tech-greater_healing_potion.md) |
| [Elixir of Mastery](tech-stats_potion.md) |
| [Elixir of Alacrity](tech-swiftness_potion.md) |
| [Elixir of Regeneration](tech-regen_potion.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Dungeon",
  "Previous": "\"alchemist\"",
  "RelativePosition": "new Vector2Int(-450, 17)",
  "IconName": "\"Icons2_2\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.UnlockDungeon(\"feral_den\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Alchemist.cs:24`
- `Assets.Source.Player/TechNode.cs:1`
