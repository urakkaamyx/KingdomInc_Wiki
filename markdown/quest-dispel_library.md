# Decursing the Library

The Grand Library of Yensburg has been overtaken by enchanted books. Dispel the ancient magic that animates the books and reclaim access to the library.

## Objective

The Grand Library of Yensburg has been overtaken by enchanted books. Dispel the ancient magic that animates the books and reclaim access to the library.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 460 |
| Base Duration | 180 |
| Required Tech | dispel_library |
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
| Mana | 3000 | Currency |
| Ring | 50 | Currency |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| Mana | 1200 | Currency |
| Ring | 20 | Currency |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_164\"",
  "Difficulty": "460",
  "BaseDuration": "180",
  "RequiredTech": "\"dispel_library\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.MageSpec,\n\t\t\t\tQuestChallenge.Dangerous\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Mana, 3000),\n\t\t\t\tnew CurrencyReward(Currency.Ring, 50)\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew CurrencyReward(Currency.Mana, 1200),\n\t\t\t\tnew CurrencyReward(Currency.Ring, 20)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/SimpleQuests.cs:43`
