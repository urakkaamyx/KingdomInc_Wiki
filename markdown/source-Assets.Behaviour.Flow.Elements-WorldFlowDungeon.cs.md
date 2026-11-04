# WorldFlowDungeon — source reference

Assets.Behaviour.Flow.Elements/WorldFlowDungeon.cs · 211 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 16 | public class WorldFlowDungeon : MonoBehaviour, ITooltipTitleSource, ITooltipCustomSource |
| 36 | public Dungeon Element { get; private set; } |
| 147 | public void SetDungeon(DungeonType d) |
| 165 | public void OpenDungeonPopup() |
| 172 | public void DelayOpenDungeonPopup() |
| 183 | public void OpenDungeonDetails() |
| 195 | public string GetTooltipTitle() |
| 200 | public void AddTooltipCustomContent(UITooltip tooltip) |

## Documented by

| Wiki article |
| --- |
| [Dungeon selection and expedition display](dungeon-panel-controls.md) |

## Sources

- `Assets.Behaviour.Flow.Elements/WorldFlowDungeon.cs:1`
