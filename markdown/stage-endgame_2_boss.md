# The Last High Priest

Stage 4 of Tomb of Sholrath.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 8000 |
| Base Health | 40 |

## Challenges

| Challenge |
| --- |
| [Desert Sun](challenge-DesertSun.md) |
| [Mana Poison](challenge-ManaPoison.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Faith | 1900 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Tomb of Sholrath](dungeon-endgame.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_90\" }",
  "BaseDifficulty": "8000",
  "BaseHealth": "40L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.DesertSun,\n\t\t\t\tQuestChallenge.ManaPoison\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Faith, 1900)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Endgame.cs:55`
