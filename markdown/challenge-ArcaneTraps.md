# Arcane Traps

Deals heavy damage to a random party member unless any adventurer succeeds on a Magic check.

## Effect

Deals heavy damage to a random party member unless any adventurer succeeds on a Magic check.

## Behavior hooks

This definition changes execute dungeon. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Triggered | true |
| Trigger Chance | 0.15 |
| Triggered | true |
| Trigger chance | 0.15f |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_186\"",
  "Label": "\"@quest_challenge_magical_traps\"",
  "Description": "\"@quest_challenge_magical_traps_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.15f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item4 in dp.Party)\n\t\t\t{\n\t\t\t\tif (item4.SkillTest(EquipStat.Magic, dp.GroupTestDifficulty))\n\t\t\t\t{\n\t\t\t\t\t_showChallenge(ArcaneTraps, item4, success: true);\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tCombatantItemData randomTarget = dp.GetRandomTarget();\n\t\t\trandomTarget.TakeDamage(dp.GetDungeonDamage(1.5f), dp);\n\t\t\t_showChallenge(ArcaneTraps, randomTarget, success: false);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:205`
