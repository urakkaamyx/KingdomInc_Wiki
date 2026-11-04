# Consuming Shadows

Each adventurer that fails a Wisdom check takes additional Shadow damage.

## Effect

Each adventurer that fails a Wisdom check takes additional Shadow damage.

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
  "IconName": "\"Icons3_49\"",
  "Label": "\"@quest_challenge_consuming_shadows\"",
  "Description": "\"@quest_challenge_consuming_shadows_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.15f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item13 in dp.Party)\n\t\t\t{\n\t\t\t\tif (!item13.SkillTest(EquipStat.Wisdom, dp.IndividualDifficulty))\n\t\t\t\t{\n\t\t\t\t\tfloat damageReduction = item13.GetDamageReduction(AdventurerTrait.ShadowResist);\n\t\t\t\t\titem13.TakeDamage((float)dp.GetDungeonDamage(0.8f) * damageReduction, dp, ignoreArmor: true);\n\t\t\t\t\t_showChallenge(ConsumingShadows, item13, damageReduction < 1f);\n\t\t\t\t}\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:517`
