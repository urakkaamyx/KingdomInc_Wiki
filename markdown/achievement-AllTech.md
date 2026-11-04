# All Tech

Steam achievement trigger AllTech. The nearby conditions below identify when the game calls it.

## Trigger context: GamePlayer

```csharp
 305  					flag3 &= isPurchased;
 306  				}
 307  			}
 308  		}
 309  		if (flag)
 310  		{
 311  			SteamAchievement.Trigger("AllTech");
 312  		}
 313  		if (flag2)
```

## Sources

- `Assets.Source.Player/GamePlayer.cs:311`
