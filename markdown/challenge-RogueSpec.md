# Stealth Mission

Difficulty is reduced by 50% for adventurers with the Rogue archetype.

## Effect

Difficulty is reduced by 50% for adventurers with the Rogue archetype.

## Appears on quests

| Quest |
| --- |
| [Bank "Heist"](quest-bank_heist.md) |
| [Byrgenwald Expedition](quest-byrgenwald_expedition.md) |

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
  "IconName": "\"Icons_168\"",
  "Label": "\"@quest_challenge_rogue\"",
  "Description": "\"@quest_challenge_rogue_desc\"",
  "CalcDifficulty": "(QuestProgress qp, HumanItemData adv, float current) => (!adv.HasArchetype(AdventurerArchetype.Rogue)) ? current : (current * 0.5f)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:104`
