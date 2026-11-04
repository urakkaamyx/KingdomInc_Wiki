# Obsidian Fortress

Stage 5 of Tomb of Sholrath.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 8400 |
| Base Health | 50 |

## Challenges

| Challenge |
| --- |
| [Animated Guardians](challenge-AnimatedGuardians.md) |

## Rewards

| Reward | Base amount | Rule |
| --- | --- | --- |
| Faith | 1100 | Currency |

## Dungeon

| Dungeon |
| --- |
| [Tomb of Sholrath](dungeon-endgame.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_91\", \"AnimationFrames_92\", \"AnimationFrames_93\" }",
  "BaseDifficulty": "8400",
  "BaseHealth": "50L",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.AnimatedGuardians }",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Faith, 1100)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Endgame.cs:70`
