# War Eastern

Steam achievement trigger WarEastern. The nearby conditions below identify when the game calls it.

## Trigger context: East

```csharp
  61  					ProgressAmount = 250,
  62  					EnemyDamage = 36,
  63  					StartStrength = 8000,
  64  					EndStrength = 10000,
  65  					OnComplete = () =>
  66  					{
  67  						SteamAchievement.Trigger("WarEastern");
  68  					}
  69  				}
```

## Sources

- `Assets.Source.Adventure.Wars/East.cs:67`
