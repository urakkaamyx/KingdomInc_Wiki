# Inner Sanctum

Stage 7 of Temple of the Last Rite.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 3000 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Arcane Traps](challenge-ArcaneTraps.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 60 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Temple of the Last Rite](dungeon-temple.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_31\", \"AnimationFrames_32\", \"AnimationFrames_33\" }",
  "BaseDifficulty": "3000",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.ArcaneTraps }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Temple.cs:98`
