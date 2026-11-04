# Private Collection

Stage 7 of Timeless Archive.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 6200 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Animated Guardians](challenge-AnimatedGuardians.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Ducat | 60 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Timeless Archive](dungeon-archive.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_79\", \"AnimationFrames_80\", \"AnimationFrames_81\" }",
  "BaseDifficulty": "6200",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.AnimatedGuardians }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 60)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:97`
