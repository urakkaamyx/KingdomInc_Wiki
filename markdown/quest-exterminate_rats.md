# Exterminate Rats!

Enormous invasive rats have been spotted in the harbor, possibly introduced from overseas. Several people have been found dead, gnawed to the bone. Exterminate the rats before they can establish a foothold!

## Objective

Enormous invasive rats have been spotted in the harbor, possibly introduced from overseas. Several people have been found dead, gnawed to the bone. Exterminate the rats before they can establish a foothold!

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 330 |
| Base Duration | 120 |
| Required Tech | exterminate_rats |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Dangerous](challenge-Dangerous.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 100 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 40 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_163\"",
  "Difficulty": "330",
  "BaseDuration": "120",
  "RequiredTech": "\"exterminate_rats\"",
  "Challenges": "new List<QuestChallenge> { QuestChallenge.Dangerous }",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 100)\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/SimpleQuests.cs:27`
