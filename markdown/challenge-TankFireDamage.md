# Gout of Flame

Deals heavy Fire damage to the tank.

## Effect

Deals heavy Fire damage to the tank.

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
  "IconName": "\"Icons2_127\"",
  "Label": "\"@quest_challenge_tank_fire_dmg\"",
  "Description": "\"@quest_challenge_tank_fire_dmg_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tCombatantItemData combatantItemData = dp.GetTank() ?? dp.GetRandomTarget();\n\t\t\tfloat damageReduction = combatantItemData.GetDamageReduction(AdventurerTrait.FireResist);\n\t\t\tfloat dmg = (float)dp.GetDungeonDamage(2f) * damageReduction;\n\t\t\tcombatantItemData.TakeDamage(dmg, dp, ignoreArmor: true);\n\t\t\t_showChallenge(TankFireDamage, combatantItemData, damageReduction < 1f);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:128`
