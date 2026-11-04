# Wilderness Evangelism

The rugged inhabitants of Byrgenwald Forest would be a great addition to Yensburg's workforce. Send out emissaries to proselytize to them and convince them of their new purpose.

## Objective

The rugged inhabitants of Byrgenwald Forest would be a great addition to Yensburg's workforce. Send out emissaries to proselytize to them and convince them of their new purpose.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 600 |
| Base Duration | 180 |
| Required Tech | forest_evangelism |
| Duration Multiplier | 1.05 |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Cleric Spec](challenge-ClericSpec.md) |
| [Increase Duration](challenge-IncreaseDuration.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Custom Reward | "@quest_reward_forest_worker", "Icons_65", (FlowElement qb | Special reward |
| Ring | 50 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Custom Reward | "@quest_reward_forest_worker_2", "Icons_65", (FlowElement qb | Special reward |
| Ring | 20 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_205\"",
  "Difficulty": "600",
  "BaseDuration": "180",
  "RequiredTech": "\"forest_evangelism\"",
  "DurationMultiplier": "1.05f",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.ClericSpec,\n\t\t\t\tQuestChallenge.IncreaseDuration\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CustomReward(\"@quest_reward_forest_worker\", \"Icons_65\", (FlowElement qb) =>\n\t\t\t\t{\n\t\t\t\t\tRegister.SetFlag(\"forest_worker_quest_discount\");\n\t\t\t\t}),\n\t\t\t\tnew CurrencyReward(Currency.Ring, 50)\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CustomReward(\"@quest_reward_forest_worker_2\", \"Icons_65\", (FlowElement qb) =>\n\t\t\t\t{\n\t\t\t\t\tRegister.AddCounter(\"forest_worker_quest_discount_2\");\n\t\t\t\t}),\n\t\t\t\tnew CurrencyReward(Currency.Ring, 20)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/SimpleQuests.cs:95`
