# Cognitohazard

Deals additional damage to all present unless any adventurer succeeds on a Magic check.

## Effect

Deals additional damage to all present unless any adventurer succeeds on a Magic check.

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
  "IconName": "\"Icons3_81\"",
  "Label": "\"@quest_challenge_animated_books\"",
  "Description": "\"@quest_challenge_animated_books_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.15f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item17 in dp.Party)\n\t\t\t{\n\t\t\t\tif (item17.SkillTest(EquipStat.Magic, dp.GroupTestDifficulty))\n\t\t\t\t{\n\t\t\t\t\t_showChallenge(AnimatedBooks, item17, success: true);\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tforeach (HumanItemData item18 in dp.Party)\n\t\t\t{\n\t\t\t\titem18.TakeDamage(dp.GetDungeonDamage(0.5f), dp);\n\t\t\t\t_showChallenge(AnimatedBooks, item18, success: false);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:622`
