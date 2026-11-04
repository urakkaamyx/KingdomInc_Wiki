# Stalker Stew

Deliciously oniony. Just don't ask about the other ingredient.

## Research effect

Deliciously oniony. Just don't ask about the other ingredient.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | stalker_stew |
| Type | Recipe |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |
| [Butcher Stalker](tech-butcher_stalker.md) |

## Related item

| Item |
| --- |
| [Stalker Stew](item-stalker_stew.md) |

## Related recipe

| Recipe |
| --- |
| [Stalker Stew](recipe-stalker_stew.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"kitchen\"",
  "IconName": "\"Icons2_179\"",
  "AdditionalRequirements": "new List<string> { \"butcher_stalker\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Kitchen.cs:38`
- `Assets.Source.Player/TechNode.cs:1`
