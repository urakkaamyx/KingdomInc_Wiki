# Herald of the Legion

Stage 8 of Yensburg Catacombs.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 5000 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Tank Fire Damage](challenge-TankFireDamage.md) |
| [Reaping Strike](challenge-ReapingStrike.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 120 | Currency |
| [Demonic Writings](item-demonic_writings.md) | 2 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Yensburg Catacombs](dungeon-catacombs.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_66\" }",
  "BaseDifficulty": "5000",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.TankFireDamage,\n\t\t\t\tQuestChallenge.ReapingStrike\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 120),\n\t\t\t\tnew ItemReward(\"demonic_writings\", 1f, 2)\n\t\t\t}",
  "OnStageCompleted": "(DungeonProgress dp) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"CatacombsDefeated\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Catacombs.cs:107`
