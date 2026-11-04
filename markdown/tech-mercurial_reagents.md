# Mercurial Reagents

Your enchanters have petitioned for a greater supply of Mercurial Flux. With it, they will be able to aid in the crafting of powerful Arcanite equipment. Unfortunately, this rare catalyst can only be found deep inside a claustrophobic cave network.

## Research effect

Your enchanters have petitioned for a greater supply of Mercurial Flux. With it, they will be able to aid in the crafting of powerful Arcanite equipment. Unfortunately, this rare catalyst can only be found deep inside a claustrophobic cave network.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mercurial_reagents |
| Type | Quest |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Arcanite Ingot](tech-arcanium_ingot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Quest",
  "Root": "\"quest_board\"",
  "IconName": "\"Icons2_4\"",
  "AdditionalRequirements": "new List<string> { \"arcanium_ingot\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:140`
- `Assets.Source.Player/TechNode.cs:1`
