# DungeonMenuAdventurer — source reference

Assets.Behaviour.UI.Dungeon/DungeonMenuAdventurer.cs · 119 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class DungeonMenuAdventurer : WorldFlowCombatant |
| 26 | protected DungeonMenuAdventurer _companion |
| 28 | protected override void Start() |
| 34 | protected override void OnDisable() |
| 44 | public void SetCombatantAndCompanion(CombatantItemData c) |
| 63 | public override void SetAnimationState(WorldFlowCombatantState state) |
| 72 | public void ShowChallenge(QuestChallenge challenge, bool success) |

## Documented by

| Wiki article |
| --- |
| [Dungeon selection and expedition display](dungeon-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Dungeon/DungeonMenuAdventurer.cs:1`
