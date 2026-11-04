# All Nodes

Steam achievement trigger AllNodes. The nearby conditions below identify when the game calls it.

## Trigger context: GamePlayer

```csharp
 313  		if (flag2)
 314  		{
 315  			SteamAchievement.Trigger("AllRecipes");
 316  		}
 317  		if (flag3)
 318  		{
 319  			SteamAchievement.Trigger("AllNodes");
 320  		}
 321  	}
```

## Sources

- `Assets.Source.Player/GamePlayer.cs:319`
