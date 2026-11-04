# Tendril of Sholrath

Stage 8 of Tomb of Sholrath.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 10000 |
| Base Health | 40 |

## Challenges

| Challenge |
| --- |
| [Tank Shadow Damage](challenge-TankShadowDamage.md) |
| [Waking Nightmare](challenge-WakingNightmare.md) |

## Dungeon

| Dungeon |
| --- |
| [Tomb of Sholrath](dungeon-endgame.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_98\" }",
  "BaseDifficulty": "10000",
  "BaseHealth": "40L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.TankShadowDamage,\n\t\t\t\tQuestChallenge.WakingNightmare\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew FragmentedNightmareReward(),\n\t\t\t\tnew DistilledNightmareReward()\n\t\t\t}",
  "OnStageCompleted": "(DungeonProgress dp) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"EndgameDefeated\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Endgame.cs:105`
