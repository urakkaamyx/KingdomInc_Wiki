# Spiritual Leader

Difficulty is reduced by 75% for adventurers with the Cleric archetype.

## Effect

Difficulty is reduced by 75% for adventurers with the Cleric archetype.

## Appears on quests

| Quest |
| --- |
| [Extinguish the Ritual](quest-extinguish_ritual.md) |
| [Aiding the Refugees](quest-aid_refugees.md) |
| [Wilderness Evangelism](quest-forest_evangelism.md) |

## Behavior hooks

This definition changes calc difficulty. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Triggered | false (default) |
| Trigger chance | 0.05f (default, applies only to triggered challenges) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_166\"",
  "Label": "\"@quest_challenge_cleric\"",
  "Description": "\"@quest_challenge_cleric_desc\"",
  "CalcDifficulty": "(QuestProgress qp, HumanItemData adv, float current) => (!adv.HasArchetype(AdventurerArchetype.Cleric)) ? current : (current * 0.25f)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:120`
