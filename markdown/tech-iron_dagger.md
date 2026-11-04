# Iron Dagger

A simple iron dagger, for anyone wishing to train in the more subtle forms of combat.

## Research effect

A simple iron dagger, for anyone wishing to train in the more subtle forms of combat.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | iron_dagger |
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
| [Iron Dagger](item-iron_dagger.md) |

## Related recipe

| Recipe |
| --- |
| [Iron Dagger](recipe-iron_dagger.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"blacksmith\"",
  "IconName": "\"Icons_7\"",
  "AdditionalRequirements": "new List<string> { \"supply_depot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:43`
- `Assets.Source.Player/TechNode.cs:1`
