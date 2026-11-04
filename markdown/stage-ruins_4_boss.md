# Watcher of Tomorrows

Stage 8 of Ruins of Arlingen.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 2000 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Tank Shadow Damage](challenge-TankShadowDamage.md) |
| [Scatter Beam](challenge-ScatterBeam.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| [Ancient Gemstone](item-ancient_gem.md) | 16 | Base quality 1f |
| [Eye of the Watcher](item-observer_eye.md) | 8 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Ruins of Arlingen](dungeon-ruins.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_19\" }",
  "BaseDifficulty": "2000",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.TankShadowDamage,\n\t\t\t\tQuestChallenge.ScatterBeam\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew ItemReward(\"ancient_gem\", 1f, 16),\n\t\t\t\tnew ItemReward(\"observer_eye\", 1f, 8)\n\t\t\t}",
  "OnStageCompleted": "(DungeonProgress dp) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"RuinsDefeated\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Ruins.cs:108`
