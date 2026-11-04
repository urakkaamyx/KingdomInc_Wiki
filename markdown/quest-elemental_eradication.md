# Elemental Eradication

For generations, the elementals of Midlake have lived in relatively harmony with the surrounding human settlements. Their recent unprovoked aggression calls for them to be culled once and for all.

## Objective

For generations, the elementals of Midlake have lived in relatively harmony with the surrounding human settlements. Their recent unprovoked aggression calls for them to be culled once and for all.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 640 |
| Base Duration | 180 |
| Required Tech | elemental_eradication |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Mage Spec](challenge-MageSpec.md) |
| [Dangerous](challenge-Dangerous.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Mana | 100 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 40 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_143\"",
  "Difficulty": "640",
  "BaseDuration": "180",
  "RequiredTech": "\"elemental_eradication\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.MageSpec,\n\t\t\t\tQuestChallenge.Dangerous\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Mana, 100),\n\t\t\t\titem\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 40),\n\t\t\t\titem\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/AdvancementQuests.cs:106`
