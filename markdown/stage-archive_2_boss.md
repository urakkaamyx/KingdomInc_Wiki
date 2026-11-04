# Cannaan the Librarian

Stage 4 of Timeless Archive.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 5700 |
| Base Health | 40 |

## Challenges

| Challenge |
| --- |
| [Brutal Slam](challenge-BrutalSlam.md) |
| [Muscle Magic](challenge-MuscleMagic.md) |

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
  "EnemySprites": "new List<string> { \"AnimationFrames_74\" }",
  "BaseDifficulty": "5700",
  "BaseHealth": "40L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.BrutalSlam,\n\t\t\t\tQuestChallenge.MuscleMagic\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 90),\n\t\t\t\tnew ItemReward(\"heretic_tech\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:55`
