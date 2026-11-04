# Forest Floor

Stage 1 of Feral Den.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 1400 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Exhausting](challenge-Exhausting.md) |

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
  "EnemySprites": "new List<string> { \"AnimationFrames_35\", \"AnimationFrames_36\", \"AnimationFrames_37\" }",
  "BaseDifficulty": "1400",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Exhausting }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 35)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/FeralDen.cs:19`
