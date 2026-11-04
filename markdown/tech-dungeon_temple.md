# Temple of the Last Rite

Ages ago, a profane ritual was carried out here to imprison an ancient evil. Now, sinister forces are working to undo the ritual's magic.

## Research effect

Ages ago, a profane ritual was carried out here to imprison an ancient evil. Now, sinister forces are working to undo the ritual's magic.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_temple |
| Type | Dungeon |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Arena](tech-arena.md) |

## Leads to

| Research |
| --- |
| [Imbue Dark Essence](tech-enchant_item_quality.md) |
| [Sinister Prodigy](tech-symbiote_breeding.md) |
| [Band of the Cyclops](tech-ring_of_strength_2.md) |
| [Serpentine Band](tech-ring_of_dexterity_2.md) |
| [Monsoon Band](tech-ring_of_magic_2.md) |
| [Band of Tranquility](tech-ring_of_wisdom_2.md) |
| [Undying Band](tech-ring_of_health_2.md) |
| [Leaden Band](tech-ring_of_armor_2.md) |
| [Hoard](tech-hoard.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Dungeon",
  "Previous": "\"arena\"",
  "RelativePosition": "new Vector2Int(450, 17)",
  "IconName": "\"Icons2_3\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.UnlockDungeon(\"temple\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Arena.cs:65`
- `Assets.Source.Player/TechNode.cs:1`
