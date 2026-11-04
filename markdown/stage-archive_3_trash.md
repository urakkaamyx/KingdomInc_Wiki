# Holding Cells

Stage 5 of Timeless Archive.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 5700 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Clear Rubble](challenge-ClearRubble.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 45 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Timeless Archive](dungeon-archive.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_75\", \"AnimationFrames_76\", \"AnimationFrames_77\" }",
  "BaseDifficulty": "5700",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.ClearRubble }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:71`
