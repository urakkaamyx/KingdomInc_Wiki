# Identify Gemstones

Inspect ancient gemstones to determine their physical and magical characteristics.

Reminder: The Filter node can be used to disentangle the mixed output gems.

## Research effect

Inspect ancient gemstones to determine their physical and magical characteristics.

Reminder: The Filter node can be used to disentangle the mixed output gems.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | identify_gem |
| Type | Recipe |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |

## Related recipe

| Recipe |
| --- |
| [Identify Gemstones](recipe-identify_gem.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"jeweler\"",
  "IconName": "\"Icons_208\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Jeweler.cs:25`
- `Assets.Source.Player/TechNode.cs:1`
