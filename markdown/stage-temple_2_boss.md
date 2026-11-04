# Crystallax

Stage 4 of Temple of the Last Rite.

## Stage values

Base health and base difficulty are definition values; the selected dungeon level applies additional scaling.

| Property | Base value |
| --- | --- |
| Base Difficulty | 2600 |
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
| [Mercurial Flux](item-mercurial_flux.md) | 90 | Base quality 1f |

## Dungeon

| Dungeon |
| --- |
| [Temple of the Last Rite](dungeon-temple.md) |

<details><summary>Implementation fields</summary>

```json
{
  "EnemySprites": "new List<string> { \"AnimationFrames_26\" }",
  "BaseDifficulty": "2600",
  "BaseHealth": "30L",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.BrutalSlam,\n\t\t\t\tQuestChallenge.FlailingStrike\n\t\t\t}",
  "Rewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ducat, 90),\n\t\t\t\tnew ItemReward(\"mercurial_flux\", 1f, 90)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Dungeons/Temple.cs:56`
