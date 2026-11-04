# Indulgence Equip

Steam achievement trigger IndulgenceEquip. The nearby conditions below identify when the game calls it.

## Trigger context: CombatantItemData

```csharp
 168  		CurrentHealth -= Mathf.RoundToInt(dmg);
 169  		if (CurrentHealth <= 0)
 170  		{
 171  			CurrentHealth = 0;
 172  			if (this is HumanItemData humanItemData && humanItemData.GetEquippedItem(EquipmentSlot.Scroll)?.Type.Identifier == "indulgence")
 173  			{
 174  				SteamAchievement.Trigger("IndulgenceEquip");
 175  			}
 176  			return true;
```

## Sources

- `Assets.Source.Items.Data/CombatantItemData.cs:174`
