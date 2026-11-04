# TechNodeHelper — source reference

Assets.Source.Player/TechNodeHelper.cs · 201 lines · 151 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public static class TechNodeHelper |
| 10 | public static TechNode UpgradeWorker(string nodeType) |
| 28 | public static TechNode UpgradeSlot2(string nodeType, bool allowMultiWorkers = true) |
| 73 | public static TechNode UpgradeSlot3(string nodeType) |
| 94 | public static TechNode UpgradeQuality(string nodeType, string upgradeType = null) |
| 143 | public static TechNode UpgradeProductivity(string nodeType, bool hasEquipment, bool hasEnhancements) |
| 175 | public static TechNode UpgradeCoffers(string nodeType) |
| 193 | public static void AddDefaultUpgrades(string nodeType, bool hasEquipment = true, bool hasEnhancements = false, bool multiWorkerAllowed = true, string qualityUpgrade = null) |

## Documented by

| Wiki article |
| --- |
| [Automation and shared machine upgrades](automation-technology.md) |
| [Potion Dispenser](tech-adventure_supplies_automation.md) |
| [Adventure Supplies · second add-on slot](tech-adventure_supplies_automation_2.md) |
| [Adventure Supplies · third add-on slot](tech-adventure_supplies_automation_3.md) |
| [Adventure Supplies · overseers](tech-adventure_supplies_productivity.md) |
| [Adventure Supplies · artisans](tech-adventure_supplies_quality.md) |
| [Reception Desk](tech-adventurers_guild_automation.md) |
| [Adventurer's Guild · second add-on slot](tech-adventurers_guild_automation_2.md) |
| [Adventurer's Guild · third add-on slot](tech-adventurers_guild_automation_3.md) |
| [Adventurer's Guild · overseers](tech-adventurers_guild_productivity.md) |
| [Adventurer's Guild · artisans](tech-adventurers_guild_quality.md) |
| [Autobrewery](tech-alchemist_automation.md) |
| [Alchemist · second add-on slot](tech-alchemist_automation_2.md) |
| [Alchemist · third add-on slot](tech-alchemist_automation_3.md) |
| [Alchemist · overseers](tech-alchemist_productivity.md) |
| [Alchemist · artisans](tech-alchemist_quality.md) |
| [Fight Announcer](tech-arena_automation.md) |
| [Arena · second add-on slot](tech-arena_automation_2.md) |
| [Arena · third add-on slot](tech-arena_automation_3.md) |
| [Recruitment Officer](tech-barracks_automation.md) |
| [Barracks · second add-on slot](tech-barracks_automation_2.md) |
| [Barracks · third add-on slot](tech-barracks_automation_3.md) |
| [Barracks · overseers](tech-barracks_productivity.md) |
| [Barracks · artisans](tech-barracks_quality.md) |
| [Apprenticeship](tech-blacksmith_automation.md) |
| [Blacksmith · second add-on slot](tech-blacksmith_automation_2.md) |
| [Blacksmith · third add-on slot](tech-blacksmith_automation_3.md) |
| [Blacksmith · overseers](tech-blacksmith_productivity.md) |
| [Blacksmith · artisans](tech-blacksmith_quality.md) |
| [The Meat Man](tech-butcher_automation.md) |
| [Butcher · second add-on slot](tech-butcher_automation_2.md) |
| [Butcher · third add-on slot](tech-butcher_automation_3.md) |
| [Butcher · overseers](tech-butcher_productivity.md) |
| [Butcher · artisans](tech-butcher_quality.md) |
| [Wilderness Cookery](tech-campfire_automation.md) |
| [Campfire · second add-on slot](tech-campfire_automation_2.md) |
| [Campfire · third add-on slot](tech-campfire_automation_3.md) |
| [Campfire · overseers](tech-campfire_productivity.md) |
| [Campfire · artisans](tech-campfire_quality.md) |
| [Only Hammers](tech-carpenter_automation.md) |
| [Carpenter · second add-on slot](tech-carpenter_automation_2.md) |
| [Carpenter · third add-on slot](tech-carpenter_automation_3.md) |
| [Carpenter · overseers](tech-carpenter_productivity.md) |
| [Carpenter · artisans](tech-carpenter_quality.md) |
| [Mana Vacuum](tech-disenchanter_automation.md) |
| [Disenchanter · second add-on slot](tech-disenchanter_automation_2.md) |
| [Disenchanter · third add-on slot](tech-disenchanter_automation_3.md) |
| [Dungeon Keeper](tech-dungeon_automation.md) |
| [Dungeon · second add-on slot](tech-dungeon_automation_2.md) |
| [Dungeon · third add-on slot](tech-dungeon_automation_3.md) |
| [Leyline Guide](tech-enchanter_automation.md) |
| [Enchanter · second add-on slot](tech-enchanter_automation_2.md) |
| [Enchanter · third add-on slot](tech-enchanter_automation_3.md) |
| [Enchanter · overseers](tech-enchanter_productivity.md) |
| [Enchanter · artisans](tech-enchanter_quality.md) |
| [Runic Apprentice](tech-engraver_automation.md) |
| [Engraver · second add-on slot](tech-engraver_automation_2.md) |
| [Engraver · third add-on slot](tech-engraver_automation_3.md) |
| [Engraver · overseers](tech-engraver_productivity.md) |
| [Engraver · artisans](tech-engraver_quality.md) |
| [Farmhand](tech-farm_automation.md) |
| [Farm · second add-on slot](tech-farm_automation_2.md) |
| [Farm · third add-on slot](tech-farm_automation_3.md) |
| [Farm · overseers](tech-farm_productivity.md) |
| [Farm · artisans](tech-farm_quality.md) |
| [Cross-country Carriers](tech-forest_automation.md) |
| [Forest · second add-on slot](tech-forest_automation_2.md) |
| [Forest · third add-on slot](tech-forest_automation_3.md) |
| [Forest · overseers](tech-forest_productivity.md) |
| [Forest · artisans](tech-forest_quality.md) |
| [Forge Attendant](tech-forge_automation.md) |
| [Forge · second add-on slot](tech-forge_automation_2.md) |
| [Forge · third add-on slot](tech-forge_automation_3.md) |
| [Forge · overseers](tech-forge_productivity.md) |
| [Forge · artisans](tech-forge_quality.md) |
| [Gravedigger](tech-graveyard_automation.md) |
| [Graveyard · second add-on slot](tech-graveyard_automation_2.md) |
| [Graveyard · third add-on slot](tech-graveyard_automation_3.md) |
| [Graveyard · overseers](tech-graveyard_productivity.md) |
| [Graveyard · artisans](tech-graveyard_quality.md) |
| [Automaton](tech-inventor_automation.md) |
| [Inventor · second add-on slot](tech-inventor_automation_2.md) |
| [Inventor · third add-on slot](tech-inventor_automation_3.md) |
| [Inventor · overseers](tech-inventor_productivity.md) |
| [Inventor · artisans](tech-inventor_quality.md) |
| [Grinding Wheel](tech-jeweler_automation.md) |
| [Jeweler · second add-on slot](tech-jeweler_automation_2.md) |
| [Jeweler · third add-on slot](tech-jeweler_automation_3.md) |
| [Jeweler · overseers](tech-jeweler_productivity.md) |
| [Jeweler · artisans](tech-jeweler_quality.md) |
| [Sous Chef](tech-kitchen_automation.md) |
| [Kitchen · second add-on slot](tech-kitchen_automation_2.md) |
| [Kitchen · third add-on slot](tech-kitchen_automation_3.md) |
| [Kitchen · overseers](tech-kitchen_productivity.md) |
| [Kitchen · artisans](tech-kitchen_quality.md) |
| [Honest Craftmanship](tech-leatherworker_automation.md) |
| [Leatherworker · second add-on slot](tech-leatherworker_automation_2.md) |
| [Leatherworker · third add-on slot](tech-leatherworker_automation_3.md) |
| [Leatherworker · overseers](tech-leatherworker_productivity.md) |
| [Leatherworker · artisans](tech-leatherworker_quality.md) |
| [Drudge Miners](tech-mine_automation.md) |
| [Mine · second add-on slot](tech-mine_automation_2.md) |
| [Mine · third add-on slot](tech-mine_automation_3.md) |
| [Mine · overseers](tech-mine_productivity.md) |
| [Mine · artisans](tech-mine_quality.md) |
| [Novice Necromancer](tech-necromancer_automation.md) |
| [Necromancer · second add-on slot](tech-necromancer_automation_2.md) |
| [Necromancer · third add-on slot](tech-necromancer_automation_3.md) |
| [Necromancer · overseers](tech-necromancer_productivity.md) |
| [Necromancer · artisans](tech-necromancer_quality.md) |
| [Quest Receptionist](tech-quest_board_automation.md) |
| [Quest Board · second add-on slot](tech-quest_board_automation_2.md) |
| [Quest Board · third add-on slot](tech-quest_board_automation_3.md) |
| [Requisition Officer](tech-requisition_office_automation.md) |
| [Requisition Office · second add-on slot](tech-requisition_office_automation_2.md) |
| [Requisition Office · third add-on slot](tech-requisition_office_automation_3.md) |
| [Tactical Waitstaff](tech-restaurant_automation.md) |
| [Restaurant · second add-on slot](tech-restaurant_automation_2.md) |
| [Restaurant · third add-on slot](tech-restaurant_automation_3.md) |
| [Enchanted Quill](tech-scribe_automation.md) |
| [Scribe · second add-on slot](tech-scribe_automation_2.md) |
| [Scribe · third add-on slot](tech-scribe_automation_3.md) |
| [Scribe · overseers](tech-scribe_productivity.md) |
| [Scribe · artisans](tech-scribe_quality.md) |
| [Shop Attendant](tech-shop_automation.md) |
| [Item Shop · second add-on slot](tech-shop_automation_2.md) |
| [Item Shop · third add-on slot](tech-shop_automation_3.md) |
| [Item Shop coffers](tech-shop_coffers.md) |
| [Prayer Wheel](tech-shrine_automation.md) |
| [Shrine · second add-on slot](tech-shrine_automation_2.md) |
| [Shrine · third add-on slot](tech-shrine_automation_3.md) |
| [Shrine · overseers](tech-shrine_productivity.md) |
| [Shrine · artisans](tech-shrine_quality.md) |
| [Mad Hermit](tech-summoning_circle_automation.md) |
| [Summoning Circle · second add-on slot](tech-summoning_circle_automation_2.md) |
| [Summoning Circle · third add-on slot](tech-summoning_circle_automation_3.md) |
| [Summoning Circle · overseers](tech-summoning_circle_productivity.md) |
| [Summoning Circle · artisans](tech-summoning_circle_quality.md) |
| [Crate Carriers](tech-supply_depot_automation.md) |
| [Supply Depot · second add-on slot](tech-supply_depot_automation_2.md) |
| [Supply Depot · third add-on slot](tech-supply_depot_automation_3.md) |
| [Supply Depot · overseers](tech-supply_depot_productivity.md) |
| [Supply Depot · artisans](tech-supply_depot_quality.md) |
| [Animated Scissors](tech-tailor_automation.md) |
| [Tailor · second add-on slot](tech-tailor_automation_2.md) |
| [Tailor · third add-on slot](tech-tailor_automation_3.md) |
| [Tailor · overseers](tech-tailor_productivity.md) |
| [Tailor · artisans](tech-tailor_quality.md) |
| [Drill Sergeant](tech-training_grounds_automation.md) |
| [Training Grounds · second add-on slot](tech-training_grounds_automation_2.md) |
| [Training Grounds · artisans](tech-training_grounds_quality.md) |

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:1`
