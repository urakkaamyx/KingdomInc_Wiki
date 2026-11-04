# Chilling Howl

Drains energy from all party members unless any adventurer succeeds on a Wisdom check.

## Effect

Drains energy from all party members unless any adventurer succeeds on a Wisdom check.

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
  "IconName": "\"Icons3_42\"",
  "Label": "\"@quest_challenge_chilling_howl\"",
  "Description": "\"@quest_challenge_chilling_howl_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item10 in dp.Party)\n\t\t\t{\n\t\t\t\tif (item10.SkillTest(EquipStat.Wisdom, dp.GroupTestDifficulty))\n\t\t\t\t{\n\t\t\t\t\t_showChallenge(ChillingHowl, item10, success: true);\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tforeach (HumanItemData item11 in dp.Party)\n\t\t\t{\n\t\t\t\titem11.LoseEnergyDungeon(dp.Stage.EnergyCost, dp);\n\t\t\t\t_showChallenge(ChillingHowl, item11, success: false);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:385`
