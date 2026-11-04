# SelectDungeonRow — source reference

Assets.Behaviour.UI.Dungeon/SelectDungeonRow.cs · 74 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class SelectDungeonRow : MonoBehaviour, IPointerClickHandler, IEventSystemHandler |
| 37 | public DungeonType Dungeon |
| 39 | public void SetDungeon(DungeonType dt, bool selected) |
| 62 | public void OnPointerClick(PointerEventData eventData) |
| 70 | public void InspectDungeon() |

## Documented by

| Wiki article |
| --- |
| [Dungeon selection and expedition display](dungeon-panel-controls.md) |

## Sources

- `Assets.Behaviour.UI.Dungeon/SelectDungeonRow.cs:1`
