# Sholrath's Chosen

Stage 8 of Temple of the Last Rite.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 3300 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Tank Shadow Damage](challenge-TankShadowDamage.md) |
| [Consuming Shadows](challenge-ConsumingShadows.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| [Precursor Symbiont](item-symbiote_reagent.md) | 6 | Base quality 1f |
| [Dark Essence](item-dark_essence.md) | 6 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Temple of the Last Rite](dungeon-temple.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_34\" }",
  "BaseDifficulty": "3300",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.TankShadowDamage,\n\t\t\t\tQuestChallenge.ConsumingShadows\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew ItemReward(\"symbiote_reagent\", 1f, 6),\n\t\t\t\tnew ItemReward(\"dark_essence\", 1f, 6)\n\t\t\t}",
  "OnStageCompleted": "(DungeonProgress dp) =>\n\t\t\t{\n\t\t\t\tSteamAchievement.Trigger(\"TempleDefeated\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Temple.cs:108`
