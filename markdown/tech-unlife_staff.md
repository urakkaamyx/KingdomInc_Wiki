# Unlife Staff

A mockery of the natural world. Demonic vines shoot out to entrap the wielder's foes, forcing them to bow in submission.

## Research effect

A mockery of the natural world. Demonic vines shoot out to entrap the wielder's foes, forcing them to bow in submission.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | unlife_staff |
| Type | Recipe |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |
| [Timeless Archive](tech-dungeon_archive.md) |

## Related item

| Item |
| --- |
| [Unlife Staff](item-unlife_staff.md) |

## Related recipe

| Recipe |
| --- |
| [Unlife Staff](recipe-unlife_staff.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"shrine\"",
  "IconName": "\"Icons3_32\"",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "AdditionalRequirements": "new List<string> { \"dungeon_archive\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:183`
- `Assets.Source.Player/TechNode.cs:1`
