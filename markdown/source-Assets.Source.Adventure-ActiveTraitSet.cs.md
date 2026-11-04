# ActiveTraitSet — source reference

Assets.Source.Adventure/ActiveTraitSet.cs · 84 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class ActiveTraitSet : IEnumerable<ActiveTrait>, IEnumerable |
| 14 | public bool Initialized { get; private set; } |
| 16 | public void Clear(bool clearBuffs) |
| 27 | public void Add(ActiveTrait trait) |
| 46 | public void AddBuff(ActiveTrait trait) |
| 55 | public void RemoveBuff(AdventurerTrait trait) |
| 67 | public void ApplyBuffs() |
| 75 | public IEnumerator<ActiveTrait> GetEnumerator() |

## Documented by

| Wiki article |
| --- |
| [Traits and party buffs](traits-and-party-buffs.md) |

## Sources

- `Assets.Source.Adventure/ActiveTraitSet.cs:1`
