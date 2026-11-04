# Extinguish the Ritual

Spies in Yensburg have discovered a network of occult rituals being carried out in the dark places of the city. Send in someone with knowledge of the occult to put a stop to these blasphemous practices.

## Objective

Spies in Yensburg have discovered a network of occult rituals being carried out in the dark places of the city. Send in someone with knowledge of the occult to put a stop to these blasphemous practices.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 700 |
| Base Duration | 180 |
| Required Tech | extinguish_ritual |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Cleric Spec](challenge-ClericSpec.md) |
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
  "IconName": "\"Icons2_107\"",
  "Difficulty": "700",
  "BaseDuration": "180",
  "RequiredTech": "\"extinguish_ritual\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.ClericSpec,\n\t\t\t\tQuestChallenge.Dangerous\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 110),\n\t\t\t\titem\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 45),\n\t\t\t\titem\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/AdvancementQuests.cs:152`
