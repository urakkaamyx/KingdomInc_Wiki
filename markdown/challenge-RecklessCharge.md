# Reckless Charge

Deals heavy damage to a single target unless any adventurer succeeds on a Strength check.

## Effect

Deals heavy damage to a single target unless any adventurer succeeds on a Strength check.

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
  "Label": "\"@quest_challenge_reckless_charge\"",
  "Description": "\"@quest_challenge_reckless_charge_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item7 in dp.Party)\n\t\t\t{\n\t\t\t\tif (item7.SkillTest(EquipStat.Strength, dp.GroupTestDifficulty))\n\t\t\t\t{\n\t\t\t\t\t_showChallenge(RecklessCharge, item7, success: true);\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tCombatantItemData randomTarget = dp.GetRandomTarget();\n\t\t\trandomTarget.TakeDamage(dp.GetDungeonDamage(2f), dp);\n\t\t\t_showChallenge(RecklessCharge, randomTarget, success: false);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:301`
