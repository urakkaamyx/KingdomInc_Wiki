# Achievements, Steam statistics, and integration

Every direct achievement trigger, statistic threshold, and source limitation.

## Direct triggers

These are actual Steam IDs, not invented display names. Criteria are verified at call sites. Recipe-family IDs can have multiple call sites; the table cites the first.

| Steam ID | Criterion | First trigger source |
| --- | --- | --- |
| AllNodes | Purchase all non-developer, non-hidden FlowElement nodes. | Assets.Source.Player/GamePlayer.cs:319 |
| AllRecipes | Purchase all non-developer, non-hidden Recipe nodes. | Assets.Source.Player/GamePlayer.cs:315 |
| AllTech | Purchase every non-developer, non-hidden technology considered by the current player check. | Assets.Source.Player/GamePlayer.cs:311 |
| ArchiveDefeated | Complete Archive final boss. | Assets.Source.Adventure.Dungeons/Archive.cs:124 |
| CatacombsDefeated | Complete Catacombs final boss. | Assets.Source.Adventure.Dungeons/Catacombs.cs:124 |
| EndgameDefeated | Complete endgame dungeon final boss. | Assets.Source.Adventure.Dungeons/Endgame.cs:122 |
| EquipAllSlots | After AddEquipment, the equipped-item count reaches at least 10 (the EquipmentSlot enum count). | Assets.Source.Items.Data/HumanItemData.cs:102 |
| FeralDefeated | Complete Feral Den final boss. | Assets.Source.Adventure.Dungeons/FeralDen.cs:124 |
| FullEnhance | AddEnhancement leaves all three slots occupied: Engrave, Enchant, Blessing. | Assets.Source.Items.Data/EquipmentItemData.cs:145 |
| GoldEarned1 | Process Gold income through GamePlayer.AddCurrency with isIncome=true; normally the first earned Gold. | Assets.Source.Player/GamePlayer.cs:187 |
| IndulgenceEquip | A human reaches zero health in damage handling with indulgence in the Scroll slot. | Assets.Source.Items.Data/CombatantItemData.cs:174 |
| Reawaken | Start the new kingdom from Prestige. | Assets.Behaviour.UI.Prestige/PrestigeUI.cs:68 |
| RuinsDefeated | Complete Ruins final boss. | Assets.Source.Adventure.Dungeons/Ruins.cs:125 |
| TempleDefeated | Complete Temple final boss. | Assets.Source.Adventure.Dungeons/Temple.cs:125 |
| UpgradeArmor | Complete any of these recipes: demonsteel_helm, demonsteel_armor, infected_shield, hellish_mask, hellish_cover, archmage_hat, archmage_robe. | Assets.Source.Items.Recipes/Scribe.cs:234 |
| UpgradeWeapon | Complete any of these recipes: vanquisher_sword, blighted_dagger, blink_rapier, flenser_greatsword, unblinking_axe, deadeye_bow, fragment_staff, unlife_staff. | Assets.Source.Items.Recipes/Shrine.cs:218 |
| WarEastern | Complete Eastern war stage 4. | Assets.Source.Adventure.Wars/East.cs:67 |
| WarEffort | WarEffort consumes a combatant and adds it to an active war. | Assets.Source.Flow.Elements/WarEffort.cs:99 |
| WarNorth | Complete North war stage 4. | Assets.Source.Adventure.Wars/North.cs:64 |
| WarYensburg | Complete Yensburg war stage 4. | Assets.Source.Adventure.Wars/Yensburg.cs:67 |
| WidgetInc | Finish the direct widget recipe at Inventor; the callback is not attached to tinker. | Assets.Source.Items.Recipes/Inventor.cs:40 |

## Statistic thresholds

| Statistic | Thresholds in source | Gameplay meaning |
| --- | --- | --- |
| GoldEarned | 500; 5,000; 50,000 | Earned raw Gold / 10,000, so thresholds are 5m; 50m; 500m raw units = 500; 5,000; 50,000 displayed gold coins. |
| QuestsCompleted | 1; 25; 250; 2,500 | Quest completions |
| BossesKilled | 1; 25; 250; 2,500 | Dungeon boss stages |
| DistilledNightmare | 5; 10; 25; 50; 100 | Total NightmareCount |

## Backend limits

SteamStat updates once per simulated second and stores immediately on threshold crossings. SteamStatsManager also stores every 300 seconds and at quit. The backend definition table mapping statistic tiers to achievement display names/IDs is absent from this source; those names are not fabricated.

Gold sends player earned total/10,000 through a monotonic Set. Quest and boss counters use Add and can accumulate in the Steam account separately from a kingdom save. Ascension resets player income history but does not lower an already higher Steam statistic through Set.

## Steam lifecycle

SteamManager initializes Steamworks and requests relaunch under application ID 4538080 when necessary, runs callbacks, and shuts down the API on destruction. SteamAchievement.Trigger de-duplicates IDs in a process-local HashSet before checking Initialized and calling GetAchievement, SetAchievement and StoreStats. An uninitialized trigger is not sent by that call.

Steam overlay pauses simulation. SaveGame handles local files without a Steam Cloud synchronization API in that path; client configuration may still synchronize files externally, so source alone cannot certify Cloud support.

## Sources

- `Assets.Source.Player/SteamAchievement.cs:11`
- `Assets.Source.Player/SteamStat.cs:44`
- `Assets.Behaviour.Util/SteamStatsManager.cs:55`
- `Assets.Source.Player/GamePlayer.cs:188`
- `Assets.Source.Adventure/QuestProgress.cs:75`
- `Assets.Source.Adventure/DungeonProgress.cs:185`
- `SteamManager.cs:68`
- `Assets.Source.Items/EnhancementType.cs:3`
- `Assets.Behaviour.UI.Prestige/PrestigeUI.cs:68`
- `Assets.Source.Adventure.Dungeons/Archive.cs:124`
- `Assets.Source.Adventure.Dungeons/Catacombs.cs:124`
- `Assets.Source.Adventure.Dungeons/Endgame.cs:122`
- `Assets.Source.Adventure.Dungeons/FeralDen.cs:124`
- `Assets.Source.Adventure.Dungeons/Ruins.cs:125`
- `Assets.Source.Adventure.Dungeons/Temple.cs:125`
- `Assets.Source.Adventure.Wars/East.cs:67`
- `Assets.Source.Adventure.Wars/North.cs:64`
- `Assets.Source.Adventure.Wars/Yensburg.cs:67`
- `Assets.Source.Flow.Elements/WarEffort.cs:99`
- `Assets.Source.Items.Data/CombatantItemData.cs:174`
- `Assets.Source.Items.Data/EquipmentItemData.cs:145`
- `Assets.Source.Items.Data/HumanItemData.cs:102`
- `Assets.Source.Items.Recipes/Inventor.cs:40`
- `Assets.Source.Items.Recipes/Scribe.cs:234`
- `Assets.Source.Items.Recipes/Shrine.cs:218`
- `Assets.Source.Player/GamePlayer.cs:187`
- `Assets.Source.Player/GamePlayer.cs:311`
- `Assets.Source.Player/GamePlayer.cs:315`
- `Assets.Source.Player/GamePlayer.cs:319`
- `Assets.Source.Items/EquipmentSlot.cs:3`
