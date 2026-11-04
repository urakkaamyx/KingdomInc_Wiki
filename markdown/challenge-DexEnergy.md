# Tight Squeeze

Adventurers that fail a Dexterity check will lose additional energy.

## Effect

Adventurers that fail a Dexterity check will lose additional energy.

## Appears on quests

| Quest |
| --- |
| [Mercurial Reagents](quest-mercurial_reagents.md) |

## Behavior hooks

This definition changes execute quest. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Triggered | true |
| Triggered | true |
| Trigger chance | 0.05f (default, applies only to triggered challenges) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_7\"",
  "Label": "\"@quest_challenge_dex_energy\"",
  "Description": "\"@quest_challenge_dex_energy_desc\"",
  "Triggered": "true",
  "ExecuteQuest": "(QuestProgress qp) =>\n\t\t{\n\t\t\tforeach (HumanItemData content3 in qp.Parent.Contents)\n\t\t\t{\n\t\t\t\tif (!content3.SkillTest(EquipStat.Dexterity, qp.Quest.Difficulty))\n\t\t\t\t{\n\t\t\t\t\tcontent3.LoseEnergy(qp.CalculateEnergyCost(content3, 15f), qp);\n\t\t\t\t}\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:71`
