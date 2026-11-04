# Venom Injector

Deals heavy Poison damage to the tank, plus additional Poison damage over time if they don't have Poison Resistance.

## Effect

Deals heavy Poison damage to the tank, plus additional Poison damage over time if they don't have Poison Resistance.

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
  "IconName": "\"Icons3_45\"",
  "Label": "\"@quest_challenge_inject_poison\"",
  "Description": "\"@quest_challenge_inject_poison_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tCombatantItemData combatantItemData = dp.GetTank() ?? dp.GetRandomTarget();\n\t\t\tfloat damageReduction = combatantItemData.GetDamageReduction(AdventurerTrait.PoisonResist);\n\t\t\tfloat dmg = (float)dp.GetDungeonDamage(2f) * damageReduction;\n\t\t\tcombatantItemData.TakeDamage(dmg, dp, ignoreArmor: true);\n\t\t\t_showChallenge(TankFireDamage, combatantItemData, damageReduction < 1f);\n\t\t\tif (damageReduction >= 1f)\n\t\t\t{\n\t\t\t\tcombatantItemData.ApplyBuff(AdventurerTrait.InjectPoison, 1f);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:430`
