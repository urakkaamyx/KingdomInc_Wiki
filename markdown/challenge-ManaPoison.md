# Mana Scourge

Deals massive Poison damage to a random target unless any adventurer succeeds on a Magic check.

## Effect

Deals massive Poison damage to a random target unless any adventurer succeeds on a Magic check.

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
  "IconName": "\"Icons3_79\"",
  "Label": "\"@quest_challenge_mana_poison\"",
  "Description": "\"@quest_challenge_mana_poison_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item14 in dp.Party)\n\t\t\t{\n\t\t\t\tif (item14.SkillTest(EquipStat.Magic, dp.GroupTestDifficulty))\n\t\t\t\t{\n\t\t\t\t\t_showChallenge(ManaPoison, item14, success: true);\n\t\t\t\t\treturn;\n\t\t\t\t}\n\t\t\t}\n\t\t\tCombatantItemData randomTarget = dp.GetRandomTarget();\n\t\t\tfloat damageReduction = randomTarget.GetDamageReduction(AdventurerTrait.PoisonResist);\n\t\t\trandomTarget.TakeDamage((float)dp.GetDungeonDamage(1.5f) * damageReduction, dp, ignoreArmor: true);\n\t\t\t_showChallenge(ManaPoison, randomTarget, success: false);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:538`
