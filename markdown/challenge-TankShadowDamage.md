# Extinguish Hope

Deals heavy Shadow damage to the tank.

## Effect

Deals heavy Shadow damage to the tank.

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
  "IconName": "\"Icons2_170\"",
  "Label": "\"@quest_challenge_tank_shadow_dmg\"",
  "Description": "\"@quest_challenge_tank_shadow_dmg_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tCombatantItemData combatantItemData = dp.GetTank() ?? dp.GetRandomTarget();\n\t\t\tfloat damageReduction = combatantItemData.GetDamageReduction(AdventurerTrait.ShadowResist);\n\t\t\tint dungeonDamage = dp.GetDungeonDamage(2f);\n\t\t\tcombatantItemData.TakeDamage(dungeonDamage, dp, ignoreArmor: true);\n\t\t\t_showChallenge(TankShadowDamage, combatantItemData, damageReduction < 1f);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:145`
