# Gold Earned1

Steam achievement trigger GoldEarned1. The nearby conditions below identify when the game calls it.

## Trigger context: GamePlayer

```csharp
 181  		_currencyCount[(int)c] += amt;
 182  		if (isIncome)
 183  		{
 184  			_currencyEarned[(int)c] += amt;
 185  			if (c == Currency.Gold)
 186  			{
 187  				SteamAchievement.Trigger("GoldEarned1");
 188  				SteamStatsManager.Set(SteamStatType.GoldEarned, (int)(_currencyEarned[0] / 10000));
 189  			}
```

## Sources

- `Assets.Source.Player/GamePlayer.cs:187`
