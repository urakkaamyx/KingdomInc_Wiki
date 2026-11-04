# Clear Rubble

Drains energy from all party members unless any adventurer succeeds on a Strength check.

## Effect

Drains energy from all party members unless any adventurer succeeds on a Strength check.

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
  "IconName": "\"Icons2_185\"",
  "Label": "\"@quest_challenge_clear_rubble\"",
  "Description": "\"@quest_challenge_clear_rubble_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.15f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item2 in dp.Party)\n\t\t\t{\n\t\t\t\tif (item2.SkillTest(EquipStat.Strength, dp.IndividualDifficulty))\n\t\t\t\t{\n\t\t\t\t\t_showChallenge(ClearRubble, item2, success: true);\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tforeach (HumanItemData item3 in dp.Party)\n\t\t\t{\n\t\t\t\titem3.LoseEnergyDungeon(dp.Stage.EnergyCost, dp);\n\t\t\t\t_showChallenge(ClearRubble, item3, success: false);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:180`
