# Pelonnar the Dragonlord

Stage 6 of Timeless Archive.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 6200 |
| Base Health | 40 |

## Challenges

| Challenge |
| --- |
| [Acid Rain](challenge-AcidRain.md) |
| [Chilling Howl](challenge-ChillingHowl.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 90 | Currency |
| [Heretic Mago-tech](item-heretic_tech.md) | 2 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Timeless Archive](dungeon-archive.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_78\" }",
  "BaseDifficulty": "6200",
  "BaseHealth": "40L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.AcidRain,\n\t\t\t\tQuestChallenge.ChillingHowl\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 90),\n\t\t\t\tnew ItemReward(\"heretic_tech\", 1f, 2)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:81`
