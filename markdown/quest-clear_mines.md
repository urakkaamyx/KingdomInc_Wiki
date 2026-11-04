# Mine Sweep

The network of mine tunnels that supply most of Yensburg's raw iron ore have been overrun by kobolds, causing significant supply bottlenecks. Clear out the vermin and restore access to a greater stockpile of iron.

## Objective

The network of mine tunnels that supply most of Yensburg's raw iron ore have been overrun by kobolds, causing significant supply bottlenecks. Clear out the vermin and restore access to a greater stockpile of iron.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 470 |
| Base Duration | 180 |
| Required Tech | clear_mines |
| Duration Multiplier | 1.05 |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Fighter Spec](challenge-FighterSpec.md) |
| [Dangerous](challenge-Dangerous.md) |
| [Increase Duration](challenge-IncreaseDuration.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Custom Reward | "@quest_reward_clear_mines", "Icons_11", (FlowElement qb | Special reward |
| Ring | 50 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Custom Reward | "@quest_reward_clear_mines_2", "Icons_11", (FlowElement qb | Special reward |
| Ring | 20 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_202\"",
  "Difficulty": "470",
  "BaseDuration": "180",
  "RequiredTech": "\"clear_mines\"",
  "DurationMultiplier": "1.05f",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.FighterSpec,\n\t\t\t\tQuestChallenge.Dangerous,\n\t\t\t\tQuestChallenge.IncreaseDuration\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CustomReward(\"@quest_reward_clear_mines\", \"Icons_11\", (FlowElement qb) =>\n\t\t\t\t{\n\t\t\t\t\tRegister.SetFlag(\"iron_ore_quest_discount\");\n\t\t\t\t}),\n\t\t\t\tnew CurrencyReward(Currency.Ring, 50)\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CustomReward(\"@quest_reward_clear_mines_2\", \"Icons_11\", (FlowElement qb) =>\n\t\t\t\t{\n\t\t\t\t\tRegister.AddCounter(\"iron_ore_quest_discount_2\");\n\t\t\t\t}),\n\t\t\t\tnew CurrencyReward(Currency.Ring, 20)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/SimpleQuests.cs:65`
