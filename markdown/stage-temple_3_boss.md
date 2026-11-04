# Amun the Orchestrator

Stage 6 of Temple of the Last Rite.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 2800 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Tank Shadow Damage](challenge-TankShadowDamage.md) |
| [Tremors](challenge-Tremors.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 90 | Currency |
| [Precursor Symbiont](item-symbiote_reagent.md) | 8 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Temple of the Last Rite](dungeon-temple.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_30\" }",
  "BaseDifficulty": "2800",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.TankShadowDamage,\n\t\t\t\tQuestChallenge.Tremors\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 90),\n\t\t\t\tnew ItemReward(\"symbiote_reagent\", 1f, 8)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Temple.cs:82`
