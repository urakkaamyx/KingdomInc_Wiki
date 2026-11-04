# Feral Defeated

Steam achievement trigger FeralDefeated. The nearby conditions below identify when the game calls it.

## Trigger context: FeralDen

```csharp
 118  			{
 119  				new ItemReward("toxin_sample", 1f, 20),
 120  				new ItemReward("unidentified_plants", 1f, 60)
 121  			},
 122  			OnStageCompleted = (DungeonProgress dp) =>
 123  			{
 124  				SteamAchievement.Trigger("FeralDefeated");
 125  			}
 126  		});
```

## Sources

- `Assets.Source.Adventure.Dungeons/FeralDen.cs:124`
