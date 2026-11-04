# Uzgrim the Hermit

Stage 2 of Yensburg Catacombs.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 3200 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Mana Poison](challenge-ManaPoison.md) |
| [Tank Fire Damage](challenge-TankFireDamage.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 90 | Currency |
| [Demonic Writings](item-demonic_writings.md) | 1 | Base quality 1 |

## Dungeon

| Dungeon |
| --- |
| [Yensburg Catacombs](dungeon-catacombs.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_54\" }",
  "BaseDifficulty": "3200",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.ManaPoison,\n\t\t\t\tQuestChallenge.TankFireDamage\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 90),\n\t\t\t\tnew ItemReward(\"demonic_writings\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Catacombs.cs:29`
