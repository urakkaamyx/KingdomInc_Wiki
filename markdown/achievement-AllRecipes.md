# All Recipes

Steam achievement trigger AllRecipes. The nearby conditions below identify when the game calls it.

## Trigger context: GamePlayer

```csharp
 309  		if (flag)
 310  		{
 311  			SteamAchievement.Trigger("AllTech");
 312  		}
 313  		if (flag2)
 314  		{
 315  			SteamAchievement.Trigger("AllRecipes");
 316  		}
 317  		if (flag3)
```

## Sources

- `Assets.Source.Player/GamePlayer.cs:315`
