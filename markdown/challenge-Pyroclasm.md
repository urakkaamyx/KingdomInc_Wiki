# Pyroclasm

Lava covers every surface. Each adventurer that fails a Dexterity check takes additional Fire damage.

## Effect

Lava covers every surface. Each adventurer that fails a Dexterity check takes additional Fire damage.

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
  "IconName": "\"Icons3_47\"",
  "Label": "\"@quest_challenge_pyroclasm\"",
  "Description": "\"@quest_challenge_pyroclasm_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item15 in dp.Party)\n\t\t\t{\n\t\t\t\tif (!item15.SkillTest(EquipStat.Dexterity, dp.IndividualDifficulty))\n\t\t\t\t{\n\t\t\t\t\tfloat damageReduction = item15.GetDamageReduction(AdventurerTrait.FireResist);\n\t\t\t\t\titem15.TakeDamage((float)dp.GetDungeonDamage(0.8f) * damageReduction, dp, ignoreArmor: true);\n\t\t\t\t\t_showChallenge(Pyroclasm, item15, damageReduction < 1f);\n\t\t\t\t}\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:562`
