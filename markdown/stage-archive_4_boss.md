# The Mad Archivist

Stage 8 of Timeless Archive.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 6600 |
| Base Health | 40 |

## Challenges

| Challenge |
| --- |
| [Consuming Shadows](challenge-ConsumingShadows.md) |
| [Extract Vigor](challenge-ExtractVigor.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 120 | Currency |
| [Heretic Mago-tech](item-heretic_tech.md) | 2 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Timeless Archive](dungeon-archive.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_82\" }",
  "BaseDifficulty": "6600",
  "BaseHealth": "40L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.ConsumingShadows,\n\t\t\t\tQuestChallenge.ExtractVigor\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 120),\n\t\t\t\tnew ItemReward(\"heretic_tech\", 1f, 2)\n\t\t\t}",
  "OnStageCompleted": "(DungeonProgress dp) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"ArchiveDefeated\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:107`
