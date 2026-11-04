# Mushroom Stew

A hearty stew that fortifies both body and mind. Overconsumption may lead to hallucinations.

## Research effect

A hearty stew that fortifies both body and mind. Overconsumption may lead to hallucinations.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mushroom_stew |
| Type | Recipe |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Campfire](tech-campfire.md) |
| [Harvest Bone](tech-forest_bone.md) |
| [Harvest Mushrooms](tech-forest_mushroom.md) |

## Related item

| Item |
| --- |
| [Mushroom Stew](item-mushroom_stew.md) |

## Related recipe

| Recipe |
| --- |
| [Mushroom Stew](recipe-mushroom_stew.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Recipe",
  "Root": "\"campfire\"",
  "AdditionalRequirements": "new List<string> { \"forest_bone\", \"forest_mushroom\" }",
  "IconName": "\"Icons_129\""
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Campfire.cs:40`
- `Assets.Source.Player/TechNode.cs:1`
