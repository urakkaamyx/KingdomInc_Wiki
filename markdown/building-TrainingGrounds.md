# Training Grounds

Increases the quality of your humans, and allows adventurers to train in a specific class when properly equipped.

## Purpose

Increases the quality of your humans, and allows adventurers to train in a specific class when properly equipped.

## Building reference

| Property | Value |
| --- | --- |
| Type | TrainingGrounds |
| Category | Utility |
| Inheritance | TrainingGrounds → FlowElement |
| Research required | [Training Grounds](tech-training_grounds.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Drill Sergeant](tech-training_grounds_automation.md) | 5 |
| [Training Grounds · second add-on slot](tech-training_grounds_automation_2.md) | 6 |
| [Training Grounds · artisans](tech-training_grounds_quality.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Capacity | 3 + (_slot1 ? 1 : 0) + (_slot2 ? 1 : 0) |
| Tick Count | 10 |
| Tick Delay | 2f |
| Label | Training Grounds |
| Category | ElementCategory.Utility |
| Icon Name | Icons 137 |
| Music Track | Deep Dungeon LOOP BPM90 |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "TrainingGrounds",
  "Inherited behavior": "TrainingGrounds → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/TrainingGrounds.cs:11`
