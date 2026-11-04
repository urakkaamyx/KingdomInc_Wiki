# Quest Board

Offers a wide variety of Quests for your adventurers to undertake and earn rewards.

## Purpose

Offers a wide variety of Quests for your adventurers to undertake and earn rewards.

## Building reference

| Property | Value |
| --- | --- |
| Type | QuestBoard |
| Category | Consumption |
| Inheritance | QuestBoard → FlowElement |
| Research required | [Quest Board](tech-quest_board.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Quest Receptionist](tech-quest_board_automation.md) | 5 |
| [Quest Board · second add-on slot](tech-quest_board_automation_2.md) | 6 |
| [Quest Board · third add-on slot](tech-quest_board_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Quest Board |
| Category | ElementCategory.Consumption |
| Icon Name | SelectedQuest?.Quest.IconName ?? "Icons_136" |
| Music Track | Middle Earth LOOP BPM90 |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "QuestBoard",
  "Inherited behavior": "QuestBoard → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/QuestBoard.cs:17`
