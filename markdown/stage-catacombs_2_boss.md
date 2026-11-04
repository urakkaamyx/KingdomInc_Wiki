# Bone Golem

Stage 4 of Yensburg Catacombs.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 4100 |
| Base Health | 30 |

## Challenges

| Challenge |
| --- |
| [Brutal Slam](challenge-BrutalSlam.md) |
| [Flailing Strike](challenge-FlailingStrike.md) |

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
  "EnemySprites": "new List<string> { \"AnimationFrames_58\" }",
  "BaseDifficulty": "4100",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.BrutalSlam,\n\t\t\t\tQuestChallenge.FlailingStrike\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 90),\n\t\t\t\tnew ItemReward(\"demonic_writings\")\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Catacombs.cs:55`
