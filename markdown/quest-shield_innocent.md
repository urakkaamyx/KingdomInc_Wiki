# Shield of the Innocent

The brewing war in the East has displaced many people, driving them towards Yensburg while being chased by marauding orcs. Defend the fleeing refugees and make sure they are safe from harm.

## Objective

The brewing war in the East has displaced many people, driving them towards Yensburg while being chased by marauding orcs. Defend the fleeing refugees and make sure they are safe from harm.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 620 |
| Base Duration | 180 |
| Required Tech | shield_innocent |
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
| Ring | 95 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 38 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_113\"",
  "Difficulty": "620",
  "BaseDuration": "180",
  "RequiredTech": "\"shield_innocent\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.FighterSpec,\n\t\t\t\tQuestChallenge.Dangerous\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 95),\n\t\t\t\titem\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 38),\n\t\t\t\titem\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/AdvancementQuests.cs:12`
