# Experimental Summons

The cult that runs your Summoning Circle calls for help with some of their more obscure rituals. Specifically, they need a bodyguard to protect them in case the result of their summoning proves to be hard to control.

## Research effect

The cult that runs your Summoning Circle calls for help with some of their more obscure rituals. Specifically, they need a bodyguard to protect them in case the result of their summoning proves to be hard to control.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | experimental_summons |
| Type | Quest |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Quest Board](tech-quest_board.md) |
| [Summoning Circle](tech-summoning_circle.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.Quest",
  "Root": "\"quest_board\"",
  "IconName": "\"Icons2_144\"",
  "CostTier": "8",
  "AdditionalRequirements": "new List<string> { \"summoning_circle\" }"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:187`
- `Assets.Source.Player/TechNode.cs:1`
