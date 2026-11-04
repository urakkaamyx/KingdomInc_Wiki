# Den Entrance

Stage 3 of Feral Den.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 1700 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Clear Rubble](challenge-ClearRubble.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 35 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Feral Den](dungeon-feral_den.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_39\", \"AnimationFrames_40\", \"AnimationFrames_41\" }",
  "BaseDifficulty": "1700",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.ClearRubble }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 35)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/FeralDen.cs:45`
