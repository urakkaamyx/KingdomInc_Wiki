# Dungeon selection and expedition display

Inspect stages, boss health, wipe counts, parties, and retreat controls.

## Select a dungeon

The selection popup lists DungeonType.Unlocked, not every dungeon defined in code. Rows show icon, description and TotalSupplyCost, which includes nightmare scaling where applicable. Left click assigns it to the world machine; Inspect opens the detailed dungeon panel instead.

## Dungeon tabs and stage nodes

Detailed panels create tabs for unlocked dungeons, split after three tabs. Clicking a progress node selects a visible stage for inspection; it does not move the expedition to that stage. Each stage displays its difficulty, challenges, rewards, completion count and wipe count. A cleared-stage label appears when current stage is later.

## Active versus inspected stage

The party is displayed on the active stage, sorted by DistanceRank. Other inspected stages hide party sprites. Active trash stages show walking and scrolling backgrounds; active bosses show fighting and boss-health progress; a finished stage is idle. The progress tracker follows the current expedition, even when another stage is being inspected.

## Retreat and status

Retreat is offered while the party has members and calls DungeonProgress.DoRetreat. Empty parties show Waiting to Start. StatusText, stage counters and party indicators update frequently. Companion trait art can appear beside an adventurer without creating another combatant entry. Challenge badges indicate success and fade; boss hit/death colors are visual feedback.

## Presentation data

WorldDungeonSprite pairs IDs with machine backgrounds; DungeonScrollingBackground pairs IDs with a default and optional per-stage background. Scrolling uses tiled images and only runs during an active trash fight. These structures contain art selections rather than hidden rewards.

## Sources

- `Assets.Behaviour.UI.Dungeon/DungeonMenu.cs:125`
- `Assets.Behaviour.UI.Dungeon/DungeonMenuAdventurer.cs:28`
- `Assets.Behaviour.UI.Dungeon/DungeonMenuBackgroundScroll.cs:25`
- `Assets.Behaviour.UI.Dungeon/DungeonMenuBoss.cs:26`
- `Assets.Behaviour.UI.Dungeon/DungeonMenuProgressNode.cs:24`
- `Assets.Behaviour.UI.Dungeon/DungeonMenuTab.cs:28`
- `Assets.Behaviour.UI.Dungeon/DungeonScrollingBackground.cs:8`
- `Assets.Behaviour.UI.Dungeon/SelectDungeonPopup.cs:20`
- `Assets.Behaviour.UI.Dungeon/SelectDungeonRow.cs:39`
- `Assets.Behaviour.Flow.Elements/WorldFlowDungeon.cs:38`
- `Assets.Behaviour.Flow.Elements/WorldDungeonSprite.cs:7`
- `Assets.Source.Adventure/DungeonType.cs:81`
- `Assets.Source.Adventure/DungeonMetadata.cs:13`
