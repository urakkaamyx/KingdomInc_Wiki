# Tinkersteel Helm

The continuous clicking of tiny gears slowly drives the wearer insane, but also serves to keep them focused.

## Research effect

The continuous clicking of tiny gears slowly drives the wearer insane, but also serves to keep them focused.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tinkersteel_helm |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Tinkersteel Helm](item-tinkersteel_helm.md) |

## Related recipe

| Recipe |
| --- |
| [Tinkersteel Helm](recipe-tinkersteel_helm.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons3_1\"",
  "CostTier": "10",
  "AdditionalRequirements": "new List<string> { \"inventor\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:162`
- `Assets.Source.Player/TechNode.cs:1`
