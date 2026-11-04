# Iron Sword

A simple iron sword, suitable for any initiate knight or rookie adventurer.

## Research effect

A simple iron sword, suitable for any initiate knight or rookie adventurer.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | iron_sword |
| Type | Recipe |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Supply Depot](tech-supply_depot.md) |

## Related item

| Item |
| --- |
| [Iron Sword](item-iron_sword.md) |

## Related recipe

| Recipe |
| --- |
| [Iron Sword](recipe-iron_sword.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons_6\"",
  "AdditionalRequirements": "new List<string> { \"supply_depot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:36`
- `Assets.Source.Player/TechNode.cs:1`
