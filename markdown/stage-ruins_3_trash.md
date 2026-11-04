# Cell Block Z

Stage 5 of Ruins of Arlingen.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Status Text | Breaching {0} |
| Base Difficulty | 1600 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Caltrops](challenge-Caltrops.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 25 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Ruins of Arlingen](dungeon-ruins.md) |

<details><summary>Implementation fields</summary>

```json
{
  "StatusText": "\"@ruins_3_trash_status\"",
  "EnemySprites": "new List<string> { \"AnimationFrames_12\", \"AnimationFrames_13\", \"AnimationFrames_14\" }",
  "BaseDifficulty": "1600",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Caltrops }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 25)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Ruins.cs:71`
