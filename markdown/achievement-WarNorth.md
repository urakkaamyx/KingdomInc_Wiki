# War North

Steam achievement trigger WarNorth. The nearby conditions below identify when the game calls it.

## Trigger context: North

```csharp
  58  					ProgressAmount = 250,
  59  					EnemyDamage = 47,
  60  					StartStrength = 19000,
  61  					EndStrength = 21000,
  62  					OnComplete = () =>
  63  					{
  64  						SteamAchievement.Trigger("WarNorth");
  65  					}
  66  				}
```

## Sources

- `Assets.Source.Adventure.Wars/North.cs:64`
