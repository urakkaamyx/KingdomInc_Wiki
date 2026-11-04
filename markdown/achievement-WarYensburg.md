# War Yensburg

Steam achievement trigger WarYensburg. The nearby conditions below identify when the game calls it.

## Trigger context: Yensburg

```csharp
  61  					ProgressAmount = 250,
  62  					EnemyDamage = 44,
  63  					StartStrength = 13000,
  64  					EndStrength = 14000,
  65  					OnComplete = () =>
  66  					{
  67  						SteamAchievement.Trigger("WarYensburg");
  68  					}
  69  				}
```

## Sources

- `Assets.Source.Adventure.Wars/Yensburg.cs:67`
