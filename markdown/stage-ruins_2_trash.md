# Armory Wing

Stage 3 of Ruins of Arlingen.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 1300 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Arcane Traps](challenge-ArcaneTraps.md) |

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
  "EnemySprites": "new List<string> { \"AnimationFrames_4\", \"AnimationFrames_5\", \"AnimationFrames_10\" }",
  "BaseDifficulty": "1300",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.ArcaneTraps }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 25)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Ruins.cs:45`
