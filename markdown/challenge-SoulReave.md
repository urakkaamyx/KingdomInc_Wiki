# Soul Reave

Drains a large amount of energy from a random party member unless any adventurer succeeds on a Wisdom check.

## Effect

Drains a large amount of energy from a random party member unless any adventurer succeeds on a Wisdom check.

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
  "IconName": "\"Icons2_188\"",
  "Label": "\"@quest_challenge_soul_reave\"",
  "Description": "\"@quest_challenge_soul_reave_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item5 in dp.Party)\n\t\t\t{\n\t\t\t\tif (item5.SkillTest(EquipStat.Wisdom, dp.GroupTestDifficulty))\n\t\t\t\t{\n\t\t\t\t\t_showChallenge(SoulReave, item5, success: true);\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tCombatantItemData randomTarget = dp.GetRandomTarget();\n\t\t\trandomTarget.LoseEnergyDungeon(dp.Stage.EnergyCost * 2f, dp);\n\t\t\t_showChallenge(SoulReave, randomTarget, success: false);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:243`
