# Hall of Bones

Stage 3 of Yensburg Catacombs.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 3800 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Caltrops](challenge-Caltrops.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 45 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Yensburg Catacombs](dungeon-catacombs.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_55\", \"AnimationFrames_56\", \"AnimationFrames_57\" }",
  "BaseDifficulty": "3800",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Caltrops }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Catacombs.cs:45`
