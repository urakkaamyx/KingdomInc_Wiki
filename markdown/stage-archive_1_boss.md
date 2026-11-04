# Champion of the Vault

Stage 2 of Timeless Archive.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 5300 |
| Base Health | 40 |

## Challenges

| Challenge |
| --- |
| [Reaping Strike](challenge-ReapingStrike.md) |
| [Barreling Charge](challenge-BarrelingCharge.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 90 | Currency |
| [Heretic Mago-tech](item-heretic_tech.md) | 1 | Base quality 1 |

## Dungeon

| Dungeon |
| --- |
| [Timeless Archive](dungeon-archive.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_70\" }",
  "BaseDifficulty": "5300",
  "BaseHealth": "40L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.ReapingStrike,\n\t\t\t\tQuestChallenge.BarrelingCharge\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 90),\n\t\t\t\tnew ItemReward(\"heretic_tech\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:29`
