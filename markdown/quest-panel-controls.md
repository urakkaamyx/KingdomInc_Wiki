# Quest Board panel controls

Expand and accept quests, preview challenges, and read repeat rewards and party status.

## Choose or inspect

The Quest popup lists unlocked quests. The board’s current quest is marked, expanded, and moved to the top. Clicking a different collapsed row expands its description/challenges/rewards; the Accept button actually assigns it, updates the board IO, and closes the popup. Merely expanding does not accept.

## Live details

Difficulty, challenge icons and party contents are shown. Progress is refreshed roughly once per second; no tick progress hides the progress bar. Reward rows are rebuilt when completed count changes using GetRewards(completedCount), so first-clear and repeat rewards can differ. Completed-count text distinguishes never completed from repeated clears.

## Tooltips and party

Hover challenge icons for full challenge content; challenge rows show their description. Reward tooltips appear only if the reward supplies a TooltipTitle. Right-clicking a human in the party opens details and can return to this popup on closing. QuestBoardPopup refuses normal Cancel while a tooltip is active.

## World presentation

The world board selects a quest-specific background and character positions where supplied, otherwise its default art/layout. Adding adventurers fills visible slots; quest completion clears their sprites. These UI placements are not extra party members or combat bonuses.

## Sources

- `Assets.Behaviour.UI.Quests/QuestBoardPopup.cs:30`
- `Assets.Behaviour.UI.Quests/QuestBoardRow.cs:83`
- `Assets.Behaviour.UI.Quests/QuestChallengeIcon.cs:16`
- `Assets.Behaviour.UI.Quests/QuestChallengeRow.cs:20`
- `Assets.Behaviour.UI.Quests/QuestRewardRow.cs:23`
- `Assets.Behaviour.Flow.Elements/WorldFlowQuestBoard.cs:38`
- `Assets.Behaviour.Flow.Elements/QuestBackground.cs:8`
