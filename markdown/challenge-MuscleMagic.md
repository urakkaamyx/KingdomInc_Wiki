# Muscle Magic

Each adventurer that fails a Strength check takes additional damage.

## Effect

Each adventurer that fails a Strength check takes additional damage.

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
  "IconName": "\"Icons3_80\"",
  "Label": "\"@quest_challenge_muscle_magic\"",
  "Description": "\"@quest_challenge_muscle_magic_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item16 in dp.Party)\n\t\t\t{\n\t\t\t\tif (!item16.SkillTest(EquipStat.Strength, dp.IndividualDifficulty))\n\t\t\t\t{\n\t\t\t\t\titem16.TakeDamage(dp.GetDungeonDamage(0.8f), dp);\n\t\t\t\t\t_showChallenge(MuscleMagic, item16, success: false);\n\t\t\t\t}\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:602`
