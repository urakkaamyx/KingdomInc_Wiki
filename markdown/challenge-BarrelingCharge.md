# Barreling Charge

Deals heavy damage to a random adventurer unless they succeed on a Dexterity check.

## Effect

Deals heavy damage to a random adventurer unless they succeed on a Dexterity check.

## Behavior hooks

This definition changes execute dungeon. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Triggered | true |
| Trigger Chance | 0.25 |
| Triggered | true |
| Trigger chance | 0.25f |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_191\"",
  "Label": "\"@quest_challenge_barreling_charge\"",
  "Description": "\"@quest_challenge_barreling_charge_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tCombatantItemData randomTarget = dp.GetRandomTarget();\n\t\t\tbool flag = randomTarget.SkillTest(EquipStat.Dexterity, dp.IndividualDifficulty);\n\t\t\tif (!flag)\n\t\t\t{\n\t\t\t\trandomTarget.TakeDamage(dp.GetDungeonDamage(1.5f), dp);\n\t\t\t}\n\t\t\t_showChallenge(BarrelingCharge, randomTarget, flag);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:583`
