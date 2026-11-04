# TrainingGroundsSlot — source reference

Assets.Source.Flow.Elements/TrainingGroundsSlot.cs · 110 lines · 3 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class TrainingGroundsSlot : IJsonSource |
| 11 | public readonly TrainingGrounds Parent |
| 13 | public InventoryItem Human |
| 15 | public int TickCount |
| 17 | public int TicksRemaining |
| 19 | public HumanItemData HumanData => Human.Data as HumanItemData |
| 21 | public bool HasFood => HumanData.GetEquippedItem(EquipmentSlot.Food) != null |
| 23 | public float Progress |
| 36 | public TrainingGroundsSlot(TrainingGrounds parent) |
| 41 | public virtual bool Tick(bool useFood) |
| 88 | public virtual JsonValue ToJson() |
| 101 | public static TrainingGroundsSlot FromJson(TrainingGrounds parent, JsonValue json) |

## Documented by

| Wiki article |
| --- |
| [Adventurer classes and advancement routes](class-progression.md) |
| [Training Grounds and diminishing returns](production-training.md) |
| [Training Grounds and quality growth](training-grounds-mechanics.md) |

## Sources

- `Assets.Source.Flow.Elements/TrainingGroundsSlot.cs:1`
