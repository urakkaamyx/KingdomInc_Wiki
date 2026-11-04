# Archive Defeated

Steam achievement trigger ArchiveDefeated. The nearby conditions below identify when the game calls it.

## Trigger context: Archive

```csharp
 118  			{
 119  				new CurrencyReward(Currency.Ducat, 120),
 120  				new ItemReward("heretic_tech", 1f, 2)
 121  			},
 122  			OnStageCompleted = (DungeonProgress dp) =>
 123  			{
 124  				SteamAchievement.Trigger("ArchiveDefeated");
 125  			}
 126  		});
```

## Sources

- `Assets.Source.Adventure.Dungeons/Archive.cs:124`
