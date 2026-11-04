# Brutal Slam

Deals heavy physical damage to the tank.

## Effect

Deals heavy physical damage to the tank.

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
  "IconName": "\"Icons3_48\"",
  "Label": "\"@quest_challenge_brutal_slam\"",
  "Description": "\"@quest_challenge_brutal_slam_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tCombatantItemData tank = dp.GetTank(orRandom: true);\n\t\t\ttank.TakeDamage(dp.GetDungeonDamage(1.5f), dp);\n\t\t\t_showChallenge(BrutalSlam, tank, success: false);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:502`
