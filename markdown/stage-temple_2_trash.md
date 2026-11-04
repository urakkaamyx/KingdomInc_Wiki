# The Great Pyramid

Stage 3 of Temple of the Last Rite.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Status Text | Scaling the Great Pyramid |
| Base Difficulty | 2400 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Desert Sun](challenge-DesertSun.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 45 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Temple of the Last Rite](dungeon-temple.md) |

<details><summary>Implementation fields</summary>

```json
{
  "StatusText": "\"@temple_2_trash_status\"",
  "EnemySprites": "new List<string> { \"AnimationFrames_24\", \"AnimationFrames_25\" }",
  "BaseDifficulty": "2400",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.DesertSun }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Temple.cs:45`
