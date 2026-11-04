# WorldFlowCombatant — source reference

Assets.Behaviour.Flow/WorldFlowCombatant.cs · 178 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public class WorldFlowCombatant : MonoBehaviour |
| 12 | protected CanvasGroup _group |
| 15 | protected Image _character |
| 26 | protected WorldFlowCombatantState _animationState |
| 36 | public CombatantItemData Combatant { get; private set; } |
| 38 | public bool IsVisible => _group.alpha > 0f |
| 40 | protected virtual void Start() |
| 96 | protected virtual void OnDisable() |
| 102 | public virtual void SetCombatant(CombatantItemData c) |
| 120 | public void Clear() |
| 125 | public virtual void SetAnimationState(WorldFlowCombatantState state) |

## Documented by

| Wiki article |
| --- |
| [Character, training, recovery, and Arena displays](character-and-training-displays.md) |

## Sources

- `Assets.Behaviour.Flow/WorldFlowCombatant.cs:1`
