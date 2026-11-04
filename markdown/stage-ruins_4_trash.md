# Solitary Confinement

Stage 7 of Ruins of Arlingen.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 1800 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Exhausting](challenge-Exhausting.md) |

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
  "EnemySprites": "new List<string> { \"AnimationFrames_16\", \"AnimationFrames_17\", \"AnimationFrames_18\" }",
  "BaseDifficulty": "1800",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Exhausting }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 25)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Ruins.cs:98`
