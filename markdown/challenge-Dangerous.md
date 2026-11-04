# Dangerous!

The enemies encountered in this quest can inflict serious harm on your adventurers.

## Effect

The enemies encountered in this quest can inflict serious harm on your adventurers.

## Appears on quests

| Quest |
| --- |
| [Shield of the Innocent](quest-shield_innocent.md) |
| [Farmstead Liberator](quest-farmstead_liberator.md) |
| [Bank "Heist"](quest-bank_heist.md) |
| [Elemental Eradication](quest-elemental_eradication.md) |
| [Experimental Summons](quest-experimental_summons.md) |
| [Extinguish the Ritual](quest-extinguish_ritual.md) |
| [Patrol the Market](quest-patrol_market.md) |
| [Exterminate Rats!](quest-exterminate_rats.md) |
| [Decursing the Library](quest-dispel_library.md) |
| [Mine Sweep](quest-clear_mines.md) |

## Behavior hooks

This definition changes execute quest. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Triggered | true |
| Triggered | true |
| Trigger chance | 0.05f (default, applies only to triggered challenges) |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons_58\"",
  "Label": "\"@quest_challenge_dangerous\"",
  "Description": "\"@quest_challenge_dangerous_desc\"",
  "Triggered": "true",
  "ExecuteQuest": "(QuestProgress qp) =>\n\t\t{\n\t\t\tfloat num = 15f + (float)qp.Quest.Difficulty / 50f;\n\t\t\tforeach (HumanItemData content in qp.Parent.Contents)\n\t\t\t{\n\t\t\t\tfloat num2 = num * ((float)qp.Quest.Difficulty / (float)content.GetBaseDamage(qp));\n\t\t\t\tcontent.TakeDamage(Mathf.RoundToInt(SeededRandom.Global.RandomRange(num2 / 1.3f, num2 * 1.3f)), qp);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:31`
