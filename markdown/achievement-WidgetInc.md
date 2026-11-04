# Widget Inc

Steam achievement trigger WidgetInc. The nearby conditions below identify when the game calls it.

## Trigger context: Inventor

```csharp
  34  			Results = new CraftingResult[1]
  35  			{
  36  				new CraftingResult("widget", 1)
  37  			},
  38  			OnFinished = (CraftingInput ci) =>
  39  			{
  40  				SteamAchievement.Trigger("WidgetInc");
  41  			}
  42  		});
```

## Sources

- `Assets.Source.Items.Recipes/Inventor.cs:40`
