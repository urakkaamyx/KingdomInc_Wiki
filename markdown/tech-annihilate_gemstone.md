# Annihilate Gemstone

Destroys the physical structure of an ancient gem, releasing the latent magic within.

## Research effect

Destroys the physical structure of an ancient gem, releasing the latent magic within.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | annihilate_gemstone |
| Type | Recipe |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Dungeon](tech-dungeon.md) |

## Related recipe

| Recipe |
| --- |
| [Annihilate Gemstone](recipe-annihilate_gemstone.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "IconName": "\"Icons2_195\"",
  "AdditionalRequirements": "new List<string> { \"dungeon\" }",
  "CostTier": "8"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:106`
- `Assets.Source.Player/TechNode.cs:1`
