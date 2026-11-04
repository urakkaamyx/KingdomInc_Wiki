# Tremors

Each adventurer that fails a Dexterity check takes additional damage.

## Effect

Each adventurer that fails a Dexterity check takes additional damage.

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
  "IconName": "\"Icons3_43\"",
  "Label": "\"@quest_challenge_tremors\"",
  "Description": "\"@quest_challenge_caltrops_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.15f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item12 in dp.Party)\n\t\t\t{\n\t\t\t\tif (!item12.SkillTest(EquipStat.Dexterity, dp.IndividualDifficulty))\n\t\t\t\t{\n\t\t\t\t\titem12.TakeDamage(dp.GetDungeonDamage(0.4f), dp);\n\t\t\t\t\t_showChallenge(Tremors, item12, success: false);\n\t\t\t\t}\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:410`
