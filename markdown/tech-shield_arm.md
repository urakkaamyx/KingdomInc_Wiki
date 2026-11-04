# Puppet Shield

A clockwork arm that straps to the wearer's back, holding a small round shield. Its rudimentary mago-tech brain predicts and blocks incoming enemy attacks.

## Research effect

A clockwork arm that straps to the wearer's back, holding a small round shield. Its rudimentary mago-tech brain predicts and blocks incoming enemy attacks.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shield_arm |
| Type | Recipe |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |

## Related item

| Item |
| --- |
| [Puppet Shield](item-shield_arm.md) |

## Related recipe

| Recipe |
| --- |
| [Puppet Shield](recipe-shield_arm.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"inventor\"",
  "IconName": "\"Icons3_54\"",
  "CostCurrency": "CurrencyCollection.GoldIngenuity"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:149`
- `Assets.Source.Player/TechNode.cs:1`
