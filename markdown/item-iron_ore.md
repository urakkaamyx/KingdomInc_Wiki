# Iron Ore

Raw iron ore, straight from the ground, ready to be refined.

## In the game

Raw iron ore, straight from the ground, ready to be refined.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | iron_ore |
| Item type | Resource |
| Resource Value | 100 |
| Quota Amount | 0.5 |
| Tag | Mine |

## Gathering

| Building | Research | Quota step |
| --- | --- | --- |
| [Mine](building-Mine.md) | [Mine Iron Ore](tech-mine_iron_ore.md) | 0.5 |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Iron Ingot](recipe-iron_ingot.md) | 1 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_11\"",
  "ResourceValue": "100L",
  "QuotaAmount": "0.5",
  "Tag": "ResourceTag.Mine"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier1.cs:9`
