# Belgor the Infernal

Stage 2 of Tomb of Sholrath.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 7200 |
| Base Health | 40 |

## Challenges

| Challenge |
| --- |
| [Pyroclasm](challenge-Pyroclasm.md) |
| [Tank Fire Damage](challenge-TankFireDamage.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Faith | 1750 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Tomb of Sholrath](dungeon-endgame.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_86\" }",
  "BaseDifficulty": "7200",
  "BaseHealth": "40L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.Pyroclasm,\n\t\t\t\tQuestChallenge.TankFireDamage\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Faith, 1750)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Endgame.cs:30`
