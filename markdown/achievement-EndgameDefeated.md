# Endgame Defeated

Steam achievement trigger EndgameDefeated. The nearby conditions below identify when the game calls it.

## Trigger context: Endgame

```csharp
 116  			{
 117  				new FragmentedNightmareReward(),
 118  				new DistilledNightmareReward()
 119  			},
 120  			OnStageCompleted = (DungeonProgress dp) =>
 121  			{
 122  				SteamAchievement.Trigger("EndgameDefeated");
 123  			}
 124  		});
```

## Sources

- `Assets.Source.Adventure.Dungeons/Endgame.cs:122`
