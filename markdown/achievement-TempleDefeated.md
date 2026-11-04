# Temple Defeated

Steam achievement trigger TempleDefeated. The nearby conditions below identify when the game calls it.

## Trigger context: Temple

```csharp
 119  			{
 120  				new ItemReward("symbiote_reagent", 1f, 6),
 121  				new ItemReward("dark_essence", 1f, 6)
 122  			},
 123  			OnStageCompleted = (DungeonProgress dp) =>
 124  			{
 125  				SteamAchievement.Trigger("TempleDefeated");
 126  			}
 127  		});
```

## Sources

- `Assets.Source.Adventure.Dungeons/Temple.cs:125`
