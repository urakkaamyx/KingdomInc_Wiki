# Starting a kingdom

The exact new-game state and first production chain.

## Starting state

A new player receives mine and forge technologies, the iron_ingot recipe, and mine_iron_ore through the mine callback. Iron-ore resource capacity starts at 1. The only placed machine is a Forge configured for iron ingots at world position (-128,64), with five iron-ore items buffered in its first input. There is one workflow and no initial currency grant in CreateNewPlayer.

Shop is a free technology after Forge, but is not explicitly pre-purchased by CreateNewPlayer. Blacksmith grants iron_armor; Supply Depot additionally requires Mine automation and grants the wood-plank supply technology. Technology grants do not place machines.

## New Game and Continue

The main menu clears the in-memory player. New Game calls Bootstrap.InitNewGame; Continue loads the newest save by filesystem last-write time. GameManager tries the latest save if no in-memory player exists and creates a new player only if no latest save exists. A corrupt newest save can raise a load error; LoadLatestSave does not search older files automatically.

## Every workflow runs

WorldFlowManager starts and updates GamePlayer with Unity Time.deltaTime. Player resource quota recalculates on roughly 0.1-second ticks, war progress on roughly 2-second ticks, and GameTime counts simulated seconds. Every workflow is updated, including workflows not currently selected.

## Sources

- `Assets.Source.Player/GamePlayer.cs:985`
- `Assets.Source.Player.Tech/T1Mine.cs:11`
- `Assets.Source.Player.Tech/T1SupplyDepot.cs:11`
- `Assets.Behaviour/GameManager.cs:11`
- `Assets.Behaviour.UI.MainMenu/MainMenuUI.cs:88`
- `Assets.Source.Player/GamePlayer.cs:141`
