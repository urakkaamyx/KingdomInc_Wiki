# Yensburg Catacombs

The labyrinthine tunnels beneath Yensburg Castle are still crawling with demonic entities. Send your adventurers down to clear them out and discover their origin.

## Research effect

The labyrinthine tunnels beneath Yensburg Castle are still crawling with demonic entities. Send your adventurers down to clear them out and discover their origin.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_catacombs |
| Type | Dungeon |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |

## Additional condition

Requires war progress: Castle District

## Campaign condition

yensburg:3 (campaign ID : completed stage)

## Leads to

| Research |
| --- |
| [Decoded Writings](tech-decoded_writings.md) |
| [Demonsteel Helm](tech-demonsteel_helm.md) |
| [Demonsteel Armor](tech-demonsteel_armor.md) |
| [Possessed Shield](tech-infected_shield.md) |
| [Malignant Mask](tech-hellish_mask.md) |
| [Malignant Cover](tech-hellish_cover.md) |
| [Archmage's Hat](tech-archmage_hat.md) |
| [Archmage's Robe](tech-archmage_robe.md) |
| [Dark Prophet's Hood](tech-prophet_hood.md) |
| [Dark Prophet's Robe](tech-prophet_robe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Dungeon",
  "Previous": "\"shrine\"",
  "RelativePosition": "new Vector2Int(450, 17)",
  "IconName": "\"Icons2_69\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.UnlockDungeon(\"catacombs\");\n\t\t\t}",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"yensburg\", 3)",
  "CustomRequirementDesc": "\"@dungeon_catacombs_unlock\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:199`
- `Assets.Source.Player/TechNode.cs:1`
