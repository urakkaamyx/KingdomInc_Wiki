# Equip All Slots

Steam achievement trigger EquipAllSlots. The nearby conditions below identify when the game calls it.

## Trigger context: HumanItemData

```csharp
  96  			Equipment.Remove(conflictingItem);
  97  		}
  98  		Equipment.Add(item);
  99  		RefreshTraits(clearBuffs: false);
 100  		if (Equipment.Count >= GameConstants.EquipmentCount)
 101  		{
 102  			SteamAchievement.Trigger("EquipAllSlots");
 103  		}
 104  	}
```

## Sources

- `Assets.Source.Items.Data/HumanItemData.cs:102`
