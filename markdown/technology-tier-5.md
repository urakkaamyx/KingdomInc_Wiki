# Technology tier 5: Adventurers and quests

Adventurers Guild requires Forest war stage 4. Training Grounds trains adventurers, Quest Board starts quests and Rings, and Adventure Supplies supplies consumables. Additional workflows, stacking, filtering, appraisal, accounting, and later quests are declared on this branch. Turtle Statue is always hidden.

## Branch overview

Adventurers Guild requires Forest war stage 4. Training Grounds trains adventurers, Quest Board starts quests and Rings, and Adventure Supplies supplies consumables. Additional workflows, stacking, filtering, appraisal, accounting, and later quests are declared on this branch. Turtle Statue is always hidden.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## AdventurersGuild branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| turtle_statue | FlowElement | ; Previous forest | — | Always hidden; forest war stage 4 | CostTier=5; CostCurrency=GoldMedal; CostMultiplier=8.0 | — | T5AdventurersGuild.cs:10 |
| adventurers_guild | FlowElement | ; Previous forest | — | forest war stage 4 | CostTier=5; CostCurrency=GoldMedal; CostMultiplier=2.0 | recruit_adventurer | T5AdventurersGuild.cs:24 |
| recruit_adventurer | Resource | Root adventurers_guild;  | — | — | Inherited/default | — | T5AdventurersGuild.cs:42 |
| global_tech_upgrade | Utility | ; Previous adventurers_guild | — | — | CostMultiplier=3.0 | — | T5AdventurersGuild.cs:48 |

```csharp
63: TechNodeHelper.AddDefaultUpgrades("AdventurersGuild", hasEquipment: false, hasEnhancements: false, multiWorkerAllowed: true, "RecruitArtisan");
```

## AdventurerSupplies branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| adventure_supplies | FlowElement | ; Previous quest_board | — | — | CostCurrency=GoldRing | supply_healing_potion, supply_rations | T5AdventurerSupplies.cs:10 |
| supply_healing_potion | Resource | Root adventure_supplies;  | — | — | Inherited/default | — | T5AdventurerSupplies.cs:24 |
| supply_energy_potion | Resource | Root adventure_supplies;  | — | — | Inherited/default | — | T5AdventurerSupplies.cs:36 |
| supply_rations | Resource | Root adventure_supplies;  | — | — | Inherited/default | — | T5AdventurerSupplies.cs:48 |
| training_sword | Resource | Root adventure_supplies;  | — | — | Inherited/default | — | T5AdventurerSupplies.cs:60 |
| supply_fire_resist_potion | Resource | Root adventure_supplies;  | dungeon | — | Inherited/default | — | T5AdventurerSupplies.cs:70 |
| supply_shadow_resist_potion | Resource | Root adventure_supplies;  | dungeon | — | CostTier=8 | — | T5AdventurerSupplies.cs:83 |
| glass_vial | Resource | Root adventure_supplies;  | alchemist | — | CostTier=8 | — | T5AdventurerSupplies.cs:97 |

```csharp
23: TechNodeHelper.AddDefaultUpgrades("AdventureSupplies", hasEquipment: false, hasEnhancements: false, multiWorkerAllowed: true, "ResArtisan");
```

## QuestBoard branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| quest_board | FlowElement | ; Previous adventurers_guild | — | — | CostCurrency=GoldMedal; CostMultiplier=1.0 | patrol_market | T5QuestBoard.cs:13 |
| quest_board_coins | UpgradeSlot | ; Previous quest_board_automation | — | — | CostCurrency=GoldRing | — | T5QuestBoard.cs:28 |
| quest_board_quality | UpgradeSlot | ; Previous quest_board_automation_2 | — | — | Inherited/default | — | T5QuestBoard.cs:42 |
| quest_board_training | UpgradeSlot | ; Previous quest_board_automation_3 | — | — | Inherited/default | — | T5QuestBoard.cs:55 |
| add_diagrams | Utility | ; Previous quest_board | — | — | CostMultiplier=5.0 | — | T5QuestBoard.cs:67 |
| element_stacking | Utility | ; Previous add_diagrams | — | — | CostMultiplier=8.0 | — | T5QuestBoard.cs:80 |
| filter | FlowElement | ; Previous add_diagrams | — | — | Inherited/default | — | T5QuestBoard.cs:88 |
| appraiser | FlowElement | ; Previous filter | — | — | Inherited/default | — | T5QuestBoard.cs:95 |
| accountant | FlowElement | ; Previous filter | — | — | Inherited/default | — | T5QuestBoard.cs:102 |
| patrol_market | Quest | Root quest_board;  | — | — | Inherited/default | — | T5QuestBoard.cs:109 |
| exterminate_rats | Quest | Root quest_board;  | — | — | Inherited/default | — | T5QuestBoard.cs:115 |
| clear_mines | Quest | Root quest_board;  | — | — | Inherited/default | — | T5QuestBoard.cs:121 |
| forest_evangelism | Quest | Root quest_board;  | — | — | Inherited/default | — | T5QuestBoard.cs:127 |
| dispel_library | Quest | Root quest_board;  | enchanter | — | Inherited/default | — | T5QuestBoard.cs:133 |
| mercurial_reagents | Quest | Root quest_board;  | arcanium_ingot | — | Inherited/default | — | T5QuestBoard.cs:140 |
| shield_innocent | Quest | Root quest_board;  | war_effort_east | — | CostTier=6 | — | T5QuestBoard.cs:147 |
| farmstead_liberator | Quest | Root quest_board;  | farm | — | CostTier=7 | — | T5QuestBoard.cs:155 |
| bank_heist | Quest | Root quest_board;  | dungeon | — | CostTier=8 | — | T5QuestBoard.cs:163 |
| byrgenwald_expedition | Quest | Root quest_board;  | alchemist | — | CostTier=9 | — | T5QuestBoard.cs:171 |
| elemental_eradication | Quest | Root quest_board;  | farm | — | CostTier=7 | — | T5QuestBoard.cs:179 |
| experimental_summons | Quest | Root quest_board;  | summoning_circle | — | CostTier=8 | — | T5QuestBoard.cs:187 |
| extinguish_ritual | Quest | Root quest_board;  | alchemist | — | CostTier=9 | — | T5QuestBoard.cs:195 |
| aid_refugees | Quest | Root quest_board;  | war_effort_east | — | CostTier=6 | — | T5QuestBoard.cs:203 |

```csharp
27: TechNode.Add(TechNodeHelper.UpgradeWorker("QuestBoard")).CostCurrency = CurrencyCollection.GoldRing;
41: TechNode.Add(TechNodeHelper.UpgradeSlot2("QuestBoard", allowMultiWorkers: false));
54: TechNode.Add(TechNodeHelper.UpgradeSlot3("QuestBoard"));
```

## TrainingGrounds branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| training_grounds | FlowElement | ; Previous adventurers_guild | — | — | CostCurrency=GoldMedal; CostMultiplier=2.0 | — | T5TrainingGrounds.cs:11 |
| training_grounds_food | Utility | Root training_grounds;  | — | — | CostMultiplier=6.0 | — | T5TrainingGrounds.cs:27 |
| training_grounds_spec | Utility | Root training_grounds;  | — | — | CostMultiplier=1.0 | — | T5TrainingGrounds.cs:35 |
| training_grounds_slot | Utility | Root training_grounds;  | — | — | CostCurrency=GoldRing; CostMultiplier=5.0 | — | T5TrainingGrounds.cs:43 |
| training_grounds_slot_2 | Utility | ; Previous training_grounds_slot | enchanter | — | CostTier=6; CostCurrency=GoldMana; CostMultiplier=5.0 | — | T5TrainingGrounds.cs:59 |
| training_grounds_dummy | Utility | ; Previous training_grounds_slot | summoning_circle | — | CostTier=8; CostMultiplier=6.0 | — | T5TrainingGrounds.cs:77 |
| boot_camp | Utility | Root training_grounds;  | — | — | CostMultiplier=4.0 | — | T5TrainingGrounds.cs:94 |
| armory | FlowElement | ; Previous training_grounds | — | — | Inherited/default | — | T5TrainingGrounds.cs:102 |
| armory_storage_cost | Utility | ; Previous armory | — | — | CostMultiplier=8.0 | — | T5TrainingGrounds.cs:109 |
| armory_unlock_channels | Utility | ; Previous armory | portal | — | CostCurrency=GoldMana; CostMultiplier=2.0 | — | T5TrainingGrounds.cs:117 |
| armory_overflow | Utility | ; Previous armory_unlock_channels | — | — | CostCurrency=GoldMana | — | T5TrainingGrounds.cs:127 |

```csharp
24: TechNode.Add(TechNodeHelper.UpgradeWorker("TrainingGrounds"));
25: TechNode.Add(TechNodeHelper.UpgradeSlot2("TrainingGrounds"));
26: TechNode.Add(TechNodeHelper.UpgradeQuality("TrainingGrounds", "TrainingArtisan"));
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:10`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:24`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:42`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:48`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:10`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:24`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:36`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:48`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:60`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:70`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:83`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:97`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:13`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:28`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:42`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:55`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:67`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:80`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:88`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:95`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:102`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:109`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:115`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:121`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:127`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:133`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:140`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:147`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:155`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:163`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:171`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:179`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:187`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:195`
- `Assets.Source.Player.Tech/T5QuestBoard.cs:203`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:11`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:27`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:35`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:43`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:59`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:77`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:94`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:102`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:109`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:117`
- `Assets.Source.Player.Tech/T5TrainingGrounds.cs:127`
