# Panacea Amulet

Creates a detoxifying aura that protects the wearer and their allies from even the most vile poisons.

## Research effect

Creates a detoxifying aura that protects the wearer and their allies from even the most vile poisons.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | amulet_of_poison_prot |
| Type | Recipe |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |
| [Feral Den](tech-dungeon_feral_den.md) |

## Related item

| Item |
| --- |
| [Panacea Amulet](item-amulet_of_poison_prot.md) |

## Related recipe

| Recipe |
| --- |
| [Panacea Amulet](recipe-amulet_of_poison_prot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons2_218\"",
  "AdditionalRequirements": "new List<string> { \"dungeon_feral_den\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:145`
- `Assets.Source.Player/TechNode.cs:1`
