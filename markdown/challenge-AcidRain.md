# Acid Rain

Deals minor damage to the entire party.

## Effect

Deals minor damage to the entire party.

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
  "IconName": "\"Icons2_171\"",
  "Label": "\"@quest_challenge_acid_rain\"",
  "Description": "\"@quest_challenge_acid_rain_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.15f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tint dungeonDamage = dp.GetDungeonDamage(0.2f);\n\t\t\tforeach (CombatantItemData combatant in dp.Combatants)\n\t\t\t{\n\t\t\t\tcombatant.TakeDamage(dungeonDamage, dp);\n\t\t\t\t_showChallenge(AcidRain, combatant, success: false);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:162`
