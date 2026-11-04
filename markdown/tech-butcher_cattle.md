# Butcher Cattle

Turns a whole animal carcass into tasty meat and useful leather.

## Research effect

Turns a whole animal carcass into tasty meat and useful leather.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | butcher_cattle |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Butcher](tech-butcher.md) |

## Related recipe

| Recipe |
| --- |
| [Butcher Cattle](recipe-butcher_cattle.md) |

## Leads to

| Research |
| --- |
| [Hamburger](tech-hamburger.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"butcher\"",
  "IconName": "\"Icons_190\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Butcher.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
