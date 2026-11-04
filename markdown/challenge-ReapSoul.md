# Reap Soul

Drains a massive amount of energy from a random target unless they succeed on a Wisdom check.

## Effect

Drains a massive amount of energy from a random target unless they succeed on a Wisdom check.

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
  "IconName": "\"Icons3_84\"",
  "Label": "\"@quest_challenge_reap_soul\"",
  "Description": "\"@quest_challenge_reap_soul_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tCombatantItemData randomTarget = dp.GetRandomTarget();\n\t\t\tbool flag = randomTarget.SkillTest(EquipStat.Wisdom, dp.IndividualDifficulty);\n\t\t\tif (!flag)\n\t\t\t{\n\t\t\t\trandomTarget.LoseEnergyDungeon(30f, dp);\n\t\t\t}\n\t\t\t_showChallenge(ReapSoul, randomTarget, flag);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:662`
