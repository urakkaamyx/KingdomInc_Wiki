# Open Battle

Difficulty is reduced by 50% for adventurers with the Fighter archetype.

## Effect

Difficulty is reduced by 50% for adventurers with the Fighter archetype.

## Appears on quests

| Quest |
| --- |
| [Shield of the Innocent](quest-shield_innocent.md) |
| [Farmstead Liberator](quest-farmstead_liberator.md) |
| [Mine Sweep](quest-clear_mines.md) |

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
  "IconName": "\"Icons_167\"",
  "Label": "\"@quest_challenge_fighter\"",
  "Description": "\"@quest_challenge_fighter_desc\"",
  "CalcDifficulty": "(QuestProgress qp, HumanItemData adv, float current) => (!adv.HasArchetype(AdventurerArchetype.Fighter)) ? current : (current * 0.5f)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:96`
