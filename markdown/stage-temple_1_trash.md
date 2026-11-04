# Temple Grounds

Stage 1 of Temple of the Last Rite.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 2200 |
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
  "EnemySprites": "new List<string> { \"AnimationFrames_20\", \"AnimationFrames_21\", \"AnimationFrames_22\" }",
  "BaseDifficulty": "2200",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.DesertSun }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Temple.cs:19`
