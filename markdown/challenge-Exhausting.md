# Exhausting

Drains additional energy over time.

## Effect

Drains additional energy over time.

## Appears on quests

| Quest |
| --- |
| [Byrgenwald Expedition](quest-byrgenwald_expedition.md) |
| [Aiding the Refugees](quest-aid_refugees.md) |
| [Mercurial Reagents](quest-mercurial_reagents.md) |

## Behavior hooks

This definition changes execute quest, execute dungeon. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Triggered | true |
| Trigger Chance | 1 |
| Triggered | true |
| Trigger chance | 1f |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_6\"",
  "Label": "\"@quest_challenge_exhausting\"",
  "Description": "\"@quest_challenge_exhausting_desc\"",
  "Triggered": "true",
  "TriggerChance": "1f",
  "ExecuteQuest": "(QuestProgress qp) =>\n\t\t{\n\t\t\tforeach (HumanItemData content2 in qp.Parent.Contents)\n\t\t\t{\n\t\t\t\tcontent2.LoseEnergy(qp.CalculateEnergyCost(content2, 0.1f), qp);\n\t\t\t}\n\t\t}",
  "ExecuteDungeon": "(DungeonProgress dp) =>\n\t\t{\n\t\t\tforeach (HumanItemData item in dp.Party)\n\t\t\t{\n\t\t\t\titem.LoseEnergyDungeon(dp.Stage.EnergyCost / 20f, dp);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:48`
