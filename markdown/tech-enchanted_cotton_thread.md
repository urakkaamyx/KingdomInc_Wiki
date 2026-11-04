# Enchanted Thread

The magic woven into this thread prevent it from breaking even under severe strain.

## Research effect

The magic woven into this thread prevent it from breaking even under severe strain.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchanted_cotton_thread |
| Type | Recipe |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Cotton Cloth](tech-cotton_cloth.md) |

## Related item

| Item |
| --- |
| [Enchanted Thread](item-enchanted_cotton_thread.md) |

## Related recipe

| Recipe |
| --- |
| [Enchanted Thread](recipe-enchanted_cotton_thread.md) |

## Leads to

| Research |
| --- |
| [Embroidered Cotton](tech-embroidered_cotton.md) |
| [Embossed Leather](tech-embossed_leather.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"enchanter\"",
  "AdditionalRequirements": "new List<string> { \"cotton_cloth\" }",
  "IconName": "\"Icons2_29\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Enchanter.cs:42`
- `Assets.Source.Player/TechNode.cs:1`
