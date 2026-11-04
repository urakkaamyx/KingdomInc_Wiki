# Upgrade Armor

Steam achievement trigger UpgradeArmor. The nearby conditions below identify when the game calls it.

## Trigger context: Scribe

```csharp
 228  			Results = new CraftingResult[1]
 229  			{
 230  				new CraftingResult("demonsteel_helm", 1)
 231  			},
 232  			OnFinished = (CraftingInput ci) =>
 233  			{
 234  				SteamAchievement.Trigger("UpgradeArmor");
 235  			}
 236  		});
```

## Trigger context: Scribe

```csharp
 246  			Results = new CraftingResult[1]
 247  			{
 248  				new CraftingResult("demonsteel_armor", 1)
 249  			},
 250  			OnFinished = (CraftingInput ci) =>
 251  			{
 252  				SteamAchievement.Trigger("UpgradeArmor");
 253  			}
 254  		});
```

## Trigger context: Scribe

```csharp
 264  			Results = new CraftingResult[1]
 265  			{
 266  				new CraftingResult("infected_shield", 1)
 267  			},
 268  			OnFinished = (CraftingInput ci) =>
 269  			{
 270  				SteamAchievement.Trigger("UpgradeArmor");
 271  			}
 272  		});
```

## Trigger context: Scribe

```csharp
 282  			Results = new CraftingResult[1]
 283  			{
 284  				new CraftingResult("hellish_mask", 1)
 285  			},
 286  			OnFinished = (CraftingInput ci) =>
 287  			{
 288  				SteamAchievement.Trigger("UpgradeArmor");
 289  			}
 290  		});
```

## Trigger context: Scribe

```csharp
 300  			Results = new CraftingResult[1]
 301  			{
 302  				new CraftingResult("hellish_cover", 1)
 303  			},
 304  			OnFinished = (CraftingInput ci) =>
 305  			{
 306  				SteamAchievement.Trigger("UpgradeArmor");
 307  			}
 308  		});
```

## Trigger context: Scribe

```csharp
 318  			Results = new CraftingResult[1]
 319  			{
 320  				new CraftingResult("archmage_hat", 1)
 321  			},
 322  			OnFinished = (CraftingInput ci) =>
 323  			{
 324  				SteamAchievement.Trigger("UpgradeArmor");
 325  			}
 326  		});
```

## Trigger context: Scribe

```csharp
 336  			Results = new CraftingResult[1]
 337  			{
 338  				new CraftingResult("archmage_robe", 1)
 339  			},
 340  			OnFinished = (CraftingInput ci) =>
 341  			{
 342  				SteamAchievement.Trigger("UpgradeArmor");
 343  			}
 344  		});
```

## Sources

- `Assets.Source.Items.Recipes/Scribe.cs:234`
- `Assets.Source.Items.Recipes/Scribe.cs:252`
- `Assets.Source.Items.Recipes/Scribe.cs:270`
- `Assets.Source.Items.Recipes/Scribe.cs:288`
- `Assets.Source.Items.Recipes/Scribe.cs:306`
- `Assets.Source.Items.Recipes/Scribe.cs:324`
- `Assets.Source.Items.Recipes/Scribe.cs:342`
