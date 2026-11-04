# Magic Affinity

Difficulty is reduced by 50% for adventurers with the Mage archetype.

## Effect

Difficulty is reduced by 50% for adventurers with the Mage archetype.

## Appears on quests

| Quest |
| --- |
| [Elemental Eradication](quest-elemental_eradication.md) |
| [Experimental Summons](quest-experimental_summons.md) |
| [Decursing the Library](quest-dispel_library.md) |

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
  "IconName": "\"Icons_165\"",
  "Label": "\"@quest_challenge_mage\"",
  "Description": "\"@quest_challenge_mage_desc\"",
  "CalcDifficulty": "(QuestProgress qp, HumanItemData adv, float current) => (!adv.HasArchetype(AdventurerArchetype.Mage)) ? current : (current * 0.5f)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:112`
