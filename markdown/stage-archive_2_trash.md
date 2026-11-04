# Librarium

Stage 3 of Timeless Archive.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 5300 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Animated Books](challenge-AnimatedBooks.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 45 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Timeless Archive](dungeon-archive.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_71\", \"AnimationFrames_72\", \"AnimationFrames_73\" }",
  "BaseDifficulty": "5300",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.AnimatedBooks }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:45`
