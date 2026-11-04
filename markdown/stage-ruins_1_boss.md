# Crull the Defiler

Stage 2 of Ruins of Arlingen.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 1300 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Tank Fire Damage](challenge-TankFireDamage.md) |
| [Acid Rain](challenge-AcidRain.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 50 | Currency |
| [Ancient Gemstone](item-ancient_gem.md) | 8 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Ruins of Arlingen](dungeon-ruins.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_3\" }",
  "BaseDifficulty": "1300",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.TankFireDamage,\n\t\t\t\tQuestChallenge.AcidRain\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 50),\n\t\t\t\tnew ItemReward(\"ancient_gem\", 1f, 8)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Ruins.cs:29`
