# Farmstead Liberator

Gangs of orcs and other marauders have occupied much of the farmland that surrounds Yensburg, enslaving the farmers and exporting the produce back to their homeland. Eradicate these squatters from your lands.

## Objective

Gangs of orcs and other marauders have occupied much of the farmland that surrounds Yensburg, enslaving the farmers and exporting the produce back to their homeland. Eradicate these squatters from your lands.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 640 |
| Base Duration | 180 |
| Required Tech | farmstead_liberator |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Fighter Spec](challenge-FighterSpec.md) |
| [Dangerous](challenge-Dangerous.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 110 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 45 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_182\"",
  "Difficulty": "640",
  "BaseDuration": "180",
  "RequiredTech": "\"farmstead_liberator\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.FighterSpec,\n\t\t\t\tQuestChallenge.Dangerous\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 110),\n\t\t\t\titem\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 45),\n\t\t\t\titem\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/AdvancementQuests.cs:35`
