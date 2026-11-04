# Catacombs Defeated

Steam achievement trigger CatacombsDefeated. The nearby conditions below identify when the game calls it.

## Trigger context: Catacombs

```csharp
 118  			{
 119  				new CurrencyReward(Currency.Ducat, 120),
 120  				new ItemReward("demonic_writings", 1f, 2)
 121  			},
 122  			OnStageCompleted = (DungeonProgress dp) =>
 123  			{
 124  				SteamAchievement.Trigger("CatacombsDefeated");
 125  			}
 126  		});
```

## Sources

- `Assets.Source.Adventure.Dungeons/Catacombs.cs:124`
