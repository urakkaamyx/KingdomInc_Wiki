# Experimental Summons

The cult that runs your Summoning Circle calls for help with some of their more obscure rituals. Specifically, they need a bodyguard to protect them in case the result of their summoning proves to be hard to control.

## Objective

The cult that runs your Summoning Circle calls for help with some of their more obscure rituals. Specifically, they need a bodyguard to protect them in case the result of their summoning proves to be hard to control.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 700 |
| Base Duration | 180 |
| Required Tech | experimental_summons |
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
| Ring | 110 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Ring | 45 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_144\"",
  "Difficulty": "700",
  "BaseDuration": "180",
  "RequiredTech": "\"experimental_summons\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.MageSpec,\n\t\t\t\tQuestChallenge.Dangerous\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 110),\n\t\t\t\titem\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Ring, 45),\n\t\t\t\titem\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/AdvancementQuests.cs:129`
