# Aiding the Refugees

As refugees were driven westward towards Yensburg, they ended up in a refugee camp that has been set up in the city's slums. Send in a team that has experience in dealing with the disease and misery that reign there.

## Objective

As refugees were driven westward towards Yensburg, they ended up in a refugee camp that has been set up in the city's slums. Send in a team that has experience in dealing with the disease and misery that reign there.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 620 |
| Base Duration | 180 |
| Required Tech | aid_refugees |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Cleric Spec](challenge-ClericSpec.md) |
| [Exhausting](challenge-Exhausting.md) |

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
  "IconName": "\"Icons2_109\"",
  "Difficulty": "620",
  "BaseDuration": "180",
  "RequiredTech": "\"aid_refugees\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.ClericSpec,\n\t\t\t\tQuestChallenge.Exhausting\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 95),\n\t\t\t\titem\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 38),\n\t\t\t\titem\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/AdvancementQuests.cs:175`
