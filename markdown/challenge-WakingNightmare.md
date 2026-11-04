# Waking Nightmare

Deals shadow damage to, and drains energy from, all party members.

## Effect

Deals shadow damage to, and drains energy from, all party members.

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
  "IconName": "\"Icons3_85\"",
  "Label": "\"@quest_challenge_waking_nightmare\"",
  "Description": "\"@quest_challenge_waking_nightmare_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.25f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item19 in dp.Party)\n\t\t\t{\n\t\t\t\tfloat damageReduction = item19.GetDamageReduction(AdventurerTrait.ShadowResist);\n\t\t\t\titem19.LoseEnergyDungeon(10f * damageReduction, dp);\n\t\t\t\titem19.TakeDamage((float)dp.GetDungeonDamage(0.5f) * damageReduction, dp, ignoreArmor: true);\n\t\t\t\t_showChallenge(WakingNightmare, item19, damageReduction < 1f);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:681`
