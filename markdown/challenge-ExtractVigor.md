# Extract Vigor

Drains energy from a random party member.

## Effect

Drains energy from a random party member.

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
  "IconName": "\"Icons3_44\"",
  "Label": "\"@quest_challenge_extract_vigor\"",
  "Description": "\"@quest_challenge_extract_vigor_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tCombatantItemData randomTarget = dp.GetRandomTarget();\n\t\t\trandomTarget.LoseEnergyDungeon(dp.Stage.EnergyCost / 2f, dp);\n\t\t\t_showChallenge(ExtractVigor, randomTarget, success: false);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:451`
