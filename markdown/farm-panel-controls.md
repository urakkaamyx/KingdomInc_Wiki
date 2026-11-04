# Farm plots and planting controls

Paint crops/animals, clear plots, copy a plot choice, and expand the field.

## Paint and clear

Click or drag a resource from the Farm list to pick up its ghost. Dropping on a plot sets that resource and keeps the ghost active for repeated planting. Dropping elsewhere cancels. Right click a plot with no planting ghost clears it; middle click a populated plot picks its resource for reuse. Closing Farm cancels the drag.

## Expansion

The panel creates each plot at 58-pixel spacing. A right-edge expansion adds a column while Width<6; bottom expansion adds a row. Buying uses GetPlotCost(numberOfNewPlots), enlarges field size, and rebuilds the panel. Width is capped in this interface by hiding column extensions at six; no equivalent height cap is visible in FarmMenu.

## Read yield and demand

Resource tooltips show description and PlotYield. The list compares demand/available quota, displays nonzero utilization as a percentage, and turns it red above 100%. Plot background details are deterministic from plot coordinates and a FarmMenuPlot seed; they are decorative, not differing soil statistics.

## Sources

- `Assets.Behaviour.UI.Farm/FarmMenu.cs:33`
- `Assets.Behaviour.UI.Farm/FarmMenuExtension.cs:22`
- `Assets.Behaviour.UI.Farm/FarmMenuGhost.cs:17`
- `Assets.Behaviour.UI.Farm/FarmMenuItem.cs:31`
- `Assets.Behaviour.UI.Farm/FarmMenuPlot.cs:32`
- `Assets.Source.Items.Type/FarmItemType.cs:13`
- `Assets.Source.Items.Type/ForestItemType.cs:19`
