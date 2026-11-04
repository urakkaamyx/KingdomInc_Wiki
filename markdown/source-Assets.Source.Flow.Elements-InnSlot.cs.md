# InnSlot — source reference

Assets.Source.Flow.Elements/InnSlot.cs · 70 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public class InnSlot : TrainingGroundsSlot |
| 10 | public new readonly Inn Parent |
| 12 | public InventoryItem Food |
| 14 | public InnSlot(Inn parent) |
| 20 | public override bool Tick(bool useFood) |
| 43 | public override JsonValue ToJson() |
| 60 | public static InnSlot FromJson(Inn parent, JsonValue json) |

## Documented by

| Wiki article |
| --- |
| [Inns, healing, and food](production-inn.md) |

## Sources

- `Assets.Source.Flow.Elements/InnSlot.cs:1`
