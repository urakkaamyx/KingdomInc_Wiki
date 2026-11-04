# Full Enhance

Steam achievement trigger FullEnhance. The nearby conditions below identify when the game calls it.

## Trigger context: EquipmentItemData

```csharp
 139  				flag = false;
 140  				break;
 141  			}
 142  		}
 143  		if (flag)
 144  		{
 145  			SteamAchievement.Trigger("FullEnhance");
 146  		}
 147  	}
```

## Sources

- `Assets.Source.Items.Data/EquipmentItemData.cs:145`
