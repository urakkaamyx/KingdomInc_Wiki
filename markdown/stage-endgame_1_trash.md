# Lake of Fire

Stage 1 of Tomb of Sholrath.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 6400 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Pyroclasm](challenge-Pyroclasm.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Faith | 800 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Tomb of Sholrath](dungeon-endgame.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_83\", \"AnimationFrames_84\", \"AnimationFrames_85\" }",
  "BaseDifficulty": "6400",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Pyroclasm }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Faith, 800)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Endgame.cs:20`
