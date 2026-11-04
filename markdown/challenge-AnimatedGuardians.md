# Animated Guardians

Deals additional damage to random targets.

## Effect

Deals additional damage to random targets.

## Behavior hooks

This definition changes execute dungeon. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Triggered | true |
| Trigger Chance | 0.5 |
| Triggered | true |
| Trigger chance | 0.5f |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_82\"",
  "Label": "\"@quest_challenge_animated_guardians\"",
  "Description": "\"@quest_challenge_animated_guardians_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.5f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tCombatantItemData randomTarget = dp.GetRandomTarget();\n\t\t\trandomTarget.TakeDamage(dp.GetDungeonDamage(0.5f), dp);\n\t\t\t_showChallenge(AnimatedGuardians, randomTarget, success: false);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:647`
