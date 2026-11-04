# Byrgenwald Expedition

The vast woods south of Yensburg have never been fully safe, but recently even travel over the Imperial Road has been fraught with danger. Drive off the wild creatures that threaten passage through the forest.

## Objective

The vast woods south of Yensburg have never been fully safe, but recently even travel over the Imperial Road has been fraught with danger. Drive off the wild creatures that threaten passage through the forest.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 700 |
| Base Duration | 180 |
| Required Tech | byrgenwald_expedition |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Rogue Spec](challenge-RogueSpec.md) |
| [Exhausting](challenge-Exhausting.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 120 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 50 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_123\"",
  "Difficulty": "700",
  "BaseDuration": "180",
  "RequiredTech": "\"byrgenwald_expedition\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.RogueSpec,\n\t\t\t\tQuestChallenge.Exhausting\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 120),\n\t\t\t\titem\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 50),\n\t\t\t\titem\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/AdvancementQuests.cs:83`
