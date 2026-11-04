# Bank "Heist"

The Central Bank of Yensburg holds a vast number of gold and silver bars that technically belong to you, but withdrawing them would mean years of paperwork. Thankfully, there's an easier way of getting your hands on them.

## Objective

The Central Bank of Yensburg holds a vast number of gold and silver bars that technically belong to you, but withdrawing them would mean years of paperwork. Thankfully, there's an easier way of getting your hands on them.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 680 |
| Base Duration | 180 |
| Required Tech | bank_heist |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Rogue Spec](challenge-RogueSpec.md) |
| [Dangerous](challenge-Dangerous.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 150 | Base quality 1f |
| [Silver Ingot](item-silver_ingot.md) | 150 | Base quality 1f |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| [Gold Ingot](item-gold_ingot.md) | 50 | Base quality 1f |
| [Silver Ingot](item-silver_ingot.md) | 50 | Base quality 1f |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_204\"",
  "Difficulty": "680",
  "BaseDuration": "180",
  "RequiredTech": "\"bank_heist\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.RogueSpec,\n\t\t\t\tQuestChallenge.Dangerous\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew ItemReward(\"gold_ingot\", 1f, 150),\n\t\t\t\tnew ItemReward(\"silver_ingot\", 1f, 150),\n\t\t\t\titem\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew ItemReward(\"gold_ingot\", 1f, 50),\n\t\t\t\tnew ItemReward(\"silver_ingot\", 1f, 50),\n\t\t\t\titem\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/AdvancementQuests.cs:58`
