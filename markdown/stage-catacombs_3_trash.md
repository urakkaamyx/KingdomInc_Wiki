# Mausoleum of Heroes

Stage 5 of Yensburg Catacombs.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 4200 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Exhausting](challenge-Exhausting.md) |

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
  "EnemySprites": "new List<string> { \"AnimationFrames_59\", \"AnimationFrames_60\", \"AnimationFrames_61\" }",
  "BaseDifficulty": "4200",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Exhausting }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Catacombs.cs:71`
