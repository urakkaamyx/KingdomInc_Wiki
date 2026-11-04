# Sanctum of Saint Ilonia

Stage 7 of Yensburg Catacombs.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 4700 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Arcane Traps](challenge-ArcaneTraps.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 60 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Yensburg Catacombs](dungeon-catacombs.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_63\", \"AnimationFrames_64\", \"AnimationFrames_65\" }",
  "BaseDifficulty": "4700",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.ArcaneTraps }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Catacombs.cs:97`
