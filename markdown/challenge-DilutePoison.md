# Dilute Miasma

Each adventurer that fails a Dexterity check takes additional Poison damage.

## Effect

Each adventurer that fails a Dexterity check takes additional Poison damage.

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
  "IconName": "\"Icons3_40\"",
  "Label": "\"@quest_challenge_dilute_poison\"",
  "Description": "\"@quest_challenge_dilute_poison_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item9 in dp.Party)\n\t\t\t{\n\t\t\t\tif (!item9.SkillTest(EquipStat.Dexterity, dp.IndividualDifficulty))\n\t\t\t\t{\n\t\t\t\t\tfloat damageReduction = item9.GetDamageReduction(AdventurerTrait.PoisonResist);\n\t\t\t\t\titem9.TakeDamage((float)dp.GetDungeonDamage(0.6f) * damageReduction, dp, ignoreArmor: true);\n\t\t\t\t\t_showChallenge(DilutePoison, item9, damageReduction < 1f);\n\t\t\t\t}\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:344`
