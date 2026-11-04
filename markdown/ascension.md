# Ascension and what carries over

Reawakening retains selected research and nightmare investments while rebuilding the kingdom.

## Entering prestige

The nightmare display becomes visible when total nightmares exceed zero. Awaken writes autosave-prestige and opens the Prestige scene. Starting a new kingdom from there triggers Reawaken and calls DoAscension.

## Retained and reset state

| State | DoAscension result |
| --- | --- |
| AscensionCount | Previous value +1 |
| NightmareCount | Retained |
| NightmareCountActive | Set to total NightmareCount |
| NightmareProgress | Retained |
| Prestige point allocations | Retained |
| Purchased Utility and UpgradeSlot research | Retained via AddTech |
| Other tech types | New-player grants only |
| Currency, income totals, resources, resource upgrades | New-player state |
| Machines, workflows, pipes, inventories, Armory, Portal | New-player state |
| War, quest, dungeon metadata, GameTime | New-player state |
| NightmareActive | Default true |
| Flow/tech zoom | 4 above 1,400 screen pixels high; otherwise 3 |

## Retained research runs callbacks

Retained technologies go through AddTech again, so OnUnlock effects run for the new player. A Utility that adds workflows or machine capabilities can have those effects again. The retention filter checks the exact NodeType, not whether the name sounds like automation.

## Active nightmare display

NightmareCountActive is an ascension snapshot used to display newly gained nightmares as a +difference. Endgame multipliers use total NightmareCount, so newly earned nightmares can affect later runs before ascending.

## Sources

- `Assets.Source.Player/GamePlayer.cs:675`
- `Assets.Behaviour.UI.Prestige/NightmareDisplay.cs:46`
- `Assets.Behaviour.UI.Prestige/NightmareDisplay.cs:33`
- `Assets.Behaviour.UI.Prestige/PrestigeUI.cs:66`
- `Assets.Source.Adventure.Dungeons/Endgame.cs:142`
