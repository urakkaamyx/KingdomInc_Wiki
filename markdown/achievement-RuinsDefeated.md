# Ruins Defeated

Steam achievement trigger RuinsDefeated. The nearby conditions below identify when the game calls it.

## Trigger context: Ruins

```csharp
 119  			{
 120  				new ItemReward("ancient_gem", 1f, 16),
 121  				new ItemReward("observer_eye", 1f, 8)
 122  			},
 123  			OnStageCompleted = (DungeonProgress dp) =>
 124  			{
 125  				SteamAchievement.Trigger("RuinsDefeated");
 126  			}
 127  		});
```

## Sources

- `Assets.Source.Adventure.Dungeons/Ruins.cs:125`
