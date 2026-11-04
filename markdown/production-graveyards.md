# Graveyards and burial services

Burials turn human remains into buried remains and may generate Faith.

## Burial recipes

Simple Burial consumes one human remains and one coffin. It uses a threefold time multiplier and outputs buried remains at the craft's rolled quality.

Officiated Burial adds a cleric-archetype human, uses a sixfold time multiplier, returns that cleric with 0.15 training and the shared prayer energy cost, and generates Faith from a base of 100.

State Funeral consumes human remains, a gilded coffin, and a cleric plus 15 Crowns. It uses a tenfold time multiplier, adds 0.2 to the buried remains' craft quality, trains the cleric by 0.3, and produces Faith from a base of 290.

## Special outputs

All three burial recipes set BaseProductivity to −999. Their buried-remains creator only returns an item when the first output buffer currently contains fewer than three items; otherwise that particular result is null.

Because buried-remains output is a custom result rather than a fixed item result, this limit is checked at completion separately from the recipe building's general output-capacity test. Plan a downstream sink for buried remains when using funerals primarily for Faith.

## Clerics and Faith

Officiating uses Shrine.OutputCleric and Shrine.OutputFaith. Clerics gain escalating SpecialCount energy costs, and exhausted clerics disappear instead of returning. Faith scales with rolled craft quality and max(1, Wisdom ÷ 350), then is rounded and credited directly.

## Sources

- `Assets.Source.Flow.Elements/Graveyard.cs:14`
- `Assets.Source.Items.Recipes/Graveyard.cs:12`
- `Assets.Source.Items.Recipes/Graveyard.cs:27`
- `Assets.Source.Items.Recipes/Graveyard.cs:47`
- `Assets.Source.Items.Recipes/Graveyard.cs:73`
- `Assets.Source.Items.Recipes/Shrine.cs:370`
- `Assets.Source.Items.Recipes/Shrine.cs:385`
