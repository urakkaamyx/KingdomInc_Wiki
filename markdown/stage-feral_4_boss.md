# Gnawtooth the Toxiferous

Stage 8 of Feral Den.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 2900 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Inject Poison](challenge-InjectPoison.md) |
| [Extract Vigor](challenge-ExtractVigor.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| [Toxin Sample](item-toxin_sample.md) | 20 | Base quality 1f |
| [Unidentified Plants](item-unidentified_plants.md) | 60 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Feral Den](dungeon-feral_den.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_50\" }",
  "BaseDifficulty": "2900",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.InjectPoison,\n\t\t\t\tQuestChallenge.ExtractVigor\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew ItemReward(\"toxin_sample\", 1f, 20),\n\t\t\t\tnew ItemReward(\"unidentified_plants\", 1f, 60)\n\t\t\t}",
  "OnStageCompleted": "(DungeonProgress dp) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"FeralDefeated\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/FeralDen.cs:107`
