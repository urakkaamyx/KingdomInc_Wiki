# Patient Zero

Stage 6 of Feral Den.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 2400 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Major Poison](challenge-MajorPoison.md) |
| [Chilling Howl](challenge-ChillingHowl.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 70 | Currency |
| [Toxin Sample](item-toxin_sample.md) | 12 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Feral Den](dungeon-feral_den.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_46\" }",
  "BaseDifficulty": "2400",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.MajorPoison,\n\t\t\t\tQuestChallenge.ChillingHowl\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 70),\n\t\t\t\tnew ItemReward(\"toxin_sample\", 1f, 12)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/FeralDen.cs:81`
