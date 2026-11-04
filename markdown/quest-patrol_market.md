# Patrol the Market

The market square in Yensburg is visited by thousands every week - and crime is rife. Help out the city guard by patrolling the market for pickpockets and other petty criminals.

## Objective

The market square in Yensburg is visited by thousands every week - and crime is rife. Help out the city guard by patrolling the market for pickpockets and other petty criminals.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 160 |
| Base Duration | 120 |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Dangerous](challenge-Dangerous.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 50 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 20 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_146\"",
  "Difficulty": "160",
  "BaseDuration": "120",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Dangerous }",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 50)\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 20)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/SimpleQuests.cs:12`
