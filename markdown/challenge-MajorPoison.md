# Concentrated Miasma

Deals minor Poison damage to the entire party.

## Effect

Deals minor Poison damage to the entire party.

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
  "IconName": "\"Icons3_41\"",
  "Label": "\"@quest_challenge_concentrated_poison\"",
  "Description": "\"@quest_challenge_concentrated_poison_desc\"",
  "Triggered": "true",
  "TriggerChance": "0.15f",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tusing List<HumanItemData>.Enumerator enumerator = dp.Party.GetEnumerator();\n\t\t\tif (enumerator.MoveNext())\n\t\t\t{\n\t\t\t\tHumanItemData current = enumerator.Current;\n\t\t\t\tfloat damageReduction = current.GetDamageReduction(AdventurerTrait.PoisonResist);\n\t\t\t\tcurrent.TakeDamage((float)dp.GetDungeonDamage(0.6f) * damageReduction, dp, ignoreArmor: true);\n\t\t\t\t_showChallenge(MajorPoison, current, damageReduction < 1f);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:365`
