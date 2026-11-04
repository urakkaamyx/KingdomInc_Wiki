# Vault Entrance

Stage 1 of Timeless Archive.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 5000 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Caltrops](challenge-Caltrops.md) |

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
  "EnemySprites": "new List<string> { \"AnimationFrames_67\", \"AnimationFrames_68\", \"AnimationFrames_69\" }",
  "BaseDifficulty": "5000",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Caltrops }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 45)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:19`
