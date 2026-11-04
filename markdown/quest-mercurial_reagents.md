# Mercurial Reagents

Your enchanters have petitioned for a greater supply of Mercurial Flux. With it, they will be able to aid in the crafting of powerful Arcanite equipment. Unfortunately, this rare catalyst can only be found deep inside a claustrophobic cave network.

## Objective

Your enchanters have petitioned for a greater supply of Mercurial Flux. With it, they will be able to aid in the crafting of powerful Arcanite equipment. Unfortunately, this rare catalyst can only be found deep inside a claustrophobic cave network.

## Quest parameters

Base duration is a progress target. Party damage, difficulty modifiers, repeat count, deaths and output blocking affect elapsed time.

| Property | Value |
| --- | --- |
| Difficulty | 320 |
| Base Duration | 180 |
| Required Tech | mercurial_reagents |
| Energy Per Tick | 0.2f (default) |
| Training Added | 0.12f (default) |

## Challenges

| Challenge |
| --- |
| [Dex Energy](challenge-DexEnergy.md) |
| [Exhausting](challenge-Exhausting.md) |

## First completion rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| [Mercurial Flux](item-mercurial_flux.md) | 80 | Base quality 1f |

## Repeat rewards

| Reward | Amount | Rule |
| --- | --- | --- |
| [Mercurial Flux](item-mercurial_flux.md) | 40 | Base quality 1f |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_4\"",
  "Difficulty": "320",
  "BaseDuration": "180",
  "RequiredTech": "\"mercurial_reagents\"",
  "Challenges": "new List<QuestChallenge>\n\t\t\t{\n\t\t\t\tQuestChallenge.DexEnergy,\n\t\t\t\tQuestChallenge.Exhausting\n\t\t\t}",
  "FirstRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew ItemReward(\"mercurial_flux\", 1f, 80)\n\t\t\t}",
  "RepeatableRewards": "new List<QuestReward>\n\t\t\t{\n\t\t\t\tnew ItemReward(\"mercurial_flux\", 1f, 40)\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure.Quests/SimpleQuests.cs:124`
