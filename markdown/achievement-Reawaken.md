# Reawaken

Steam achievement trigger Reawaken. The nearby conditions below identify when the game calls it.

## Trigger context: PrestigeUI

```csharp
  62  			_igMenu.gameObject.SetActive(value: true);
  63  		}
  64  	}
  65  
  66  	public void DoStartNewGame()
  67  	{
  68  		SteamAchievement.Trigger("Reawaken");
  69  		UISounds.CraftFinished();
  70  		GamePlayer.Current.DoAscension();
```

## Sources

- `Assets.Behaviour.UI.Prestige/PrestigeUI.cs:68`
