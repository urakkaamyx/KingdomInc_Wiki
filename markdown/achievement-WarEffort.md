# War Effort

Steam achievement trigger WarEffort. The nearby conditions below identify when the game calls it.

## Trigger context: WarEffort

```csharp
  93  	{
  94  		if (WarType != null && WarType.CanProgress() && Inputs[0].ConsumeItem()?.Data is CombatantItemData combatantItemData)
  95  		{
  96  			CleanupSoldier(combatantItemData);
  97  			Soldiers.Add(combatantItemData);
  98  			WarType.Progress.Soldiers.Add(combatantItemData);
  99  			SteamAchievement.Trigger("WarEffort");
 100  			ActiveTrait.ApplyBuffs(Soldiers, combatantItemData, WarType.Progress);
 101  			if (CurrentSoldier == null)
```

## Sources

- `Assets.Source.Flow.Elements/WarEffort.cs:99`
