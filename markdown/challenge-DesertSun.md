# Scorching Heat

Deals minor Fire damage to the entire party.

## Effect

Deals minor Fire damage to the entire party.

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
  "Label": "\"@quest_challenge_desert_sun\"",
  "Description": "\"@quest_challenge_desert_sun_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tint dungeonDamage = dp.GetDungeonDamage(0.3f);\n\t\t\tforeach (CombatantItemData combatant2 in dp.Combatants)\n\t\t\t{\n\t\t\t\tfloat damageReduction = combatant2.GetDamageReduction(AdventurerTrait.FireResist);\n\t\t\t\tcombatant2.TakeDamage((float)dungeonDamage * damageReduction, dp, ignoreArmor: true);\n\t\t\t\t_showChallenge(DesertSun, combatant2, damageReduction < 1f);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:466`
