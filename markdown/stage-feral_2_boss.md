# Alpha Beast

Stage 4 of Feral Den.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 2000 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Reckless Charge](challenge-RecklessCharge.md) |
| [Dilute Poison](challenge-DilutePoison.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 70 | Currency |
| [Unidentified Plants](item-unidentified_plants.md) | 40 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Feral Den](dungeon-feral_den.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_42\" }",
  "BaseDifficulty": "2000",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.RecklessCharge,\n\t\t\t\tQuestChallenge.DilutePoison\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 70),\n\t\t\t\tnew ItemReward(\"unidentified_plants\", 1f, 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/FeralDen.cs:55`
