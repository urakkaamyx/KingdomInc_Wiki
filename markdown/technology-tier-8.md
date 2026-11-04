# Technology tier 8: Dungeons and jewelry

Dungeon requires Eastern war stage 2 and uses Gold plus Rings before Ducats are available. It grants and unlocks Ruins. Jeweler follows Dungeon and uses Ducats. Summoning Circle requires Eastern war stage 3 and opens summoned combatants.

## Branch overview

Dungeon requires Eastern war stage 2 and uses Gold plus Rings before Ducats are available. It grants and unlocks Ruins. Jeweler follows Dungeon and uses Ducats. Summoning Circle requires Eastern war stage 3 and opens summoned combatants.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Dungeon branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| dungeon | FlowElement | ; Previous farm | — | eastern war stage 2 | CostTier=8; CostCurrency=GoldRing; CostMultiplier=5.0 | dungeon_ruins | T8Dungeon.cs:10 |
| dungeon_ruins | Dungeon | Root dungeon;  | — | — | Inherited/default | — | T8Dungeon.cs:31 |
| dungeon_trash_loot | UpgradeSlot | ; Previous dungeon_automation | — | — | Inherited/default | — | T8Dungeon.cs:37 |
| dungeon_coin_loot | UpgradeSlot | ; Previous dungeon_automation | — | — | Inherited/default | — | T8Dungeon.cs:48 |
| dungeon_limit_break | UpgradeSlot | ; Previous dungeon_automation_2 | — | — | CostTier=9; CostMultiplier=5.0 | — | T8Dungeon.cs:59 |
| dungeon_item_loot | UpgradeSlot | ; Previous dungeon_automation_2 | — | — | Inherited/default | — | T8Dungeon.cs:72 |
| dungeon_limit_break_2 | UpgradeSlot | ; Previous dungeon_limit_break | shrine | — | CostTier=11; CostCurrency=GoldFaith; CostMultiplier=2.5 | — | T8Dungeon.cs:83 |
| guildhouse | FlowElement | ; Previous dungeon | — | — | CostCurrency=GoldCrown | — | T8Dungeon.cs:98 |
| guildhouse_unlock_channels | Utility | ; Previous guildhouse | portal | Always hidden | CostCurrency=GoldMana; CostMultiplier=2.0 | — | T8Dungeon.cs:106 |
| guildhouse_conscripts | Utility | ; Previous guildhouse | — | — | CostCurrency=GoldCrown; CostMultiplier=2.0 | — | T8Dungeon.cs:117 |
| mercenary_guild | FlowElement | ; Previous guildhouse | — | — | CostCurrency=GoldDucat | — | T8Dungeon.cs:126 |
| mercenary_conscripts | Utility | ; Previous mercenary_guild | — | — | CostCurrency=GoldDucat; CostMultiplier=2.0 | — | T8Dungeon.cs:134 |

```csharp
28: TechNode.Add(TechNodeHelper.UpgradeWorker("Dungeon"));
29: TechNode.Add(TechNodeHelper.UpgradeSlot2("Dungeon", allowMultiWorkers: false));
30: TechNode.Add(TechNodeHelper.UpgradeSlot3("Dungeon"));
```

## Jeweler branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| jeweler | FlowElement | ; Previous dungeon | — | — | CostCurrency=GoldDucat; CostMultiplier=1.5 | identify_gem | T8Jeweler.cs:10 |
| identify_gem | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:25 |
| gem_setting | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:31 |
| simple_ring | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:37 |
| ring_of_strength | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:43 |
| ring_of_dexterity | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:49 |
| ring_of_magic | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:55 |
| ring_of_wisdom | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:61 |
| ring_of_health | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:67 |
| ring_of_armor | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:73 |
| ring_of_strength_2 | Recipe | Root jeweler;  | dungeon_temple | — | Inherited/default | — | T8Jeweler.cs:79 |
| ring_of_dexterity_2 | Recipe | Root jeweler;  | dungeon_temple | — | Inherited/default | — | T8Jeweler.cs:86 |
| ring_of_magic_2 | Recipe | Root jeweler;  | dungeon_temple | — | Inherited/default | — | T8Jeweler.cs:93 |
| ring_of_wisdom_2 | Recipe | Root jeweler;  | dungeon_temple | — | Inherited/default | — | T8Jeweler.cs:100 |
| ring_of_health_2 | Recipe | Root jeweler;  | dungeon_temple | — | Inherited/default | — | T8Jeweler.cs:107 |
| ring_of_armor_2 | Recipe | Root jeweler;  | dungeon_temple | — | Inherited/default | — | T8Jeweler.cs:114 |
| amulet_of_healing | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:121 |
| amulet_of_energy | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:127 |
| amulet_of_fire_prot | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:133 |
| amulet_of_shadow_prot | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:139 |
| amulet_of_poison_prot | Recipe | Root jeweler;  | dungeon_feral_den | — | Inherited/default | — | T8Jeweler.cs:145 |
| lifebloom_amulet | Recipe | Root jeweler;  | alchemist | — | Inherited/default | — | T8Jeweler.cs:152 |
| fireball_amulet | Recipe | Root jeweler;  | alchemist | — | Inherited/default | — | T8Jeweler.cs:159 |
| stats_amulet | Recipe | Root jeweler;  | — | — | Inherited/default | — | T8Jeweler.cs:166 |
| prayer_beads | Recipe | Root jeweler;  | shrine | — | CostTier=11; CostCurrency=GoldFaith; CostMultiplier=0.5 | — | T8Jeweler.cs:172 |
| treasury | FlowElement | ; Previous jeweler | — | — | Inherited/default | — | T8Jeweler.cs:182 |

```csharp
24: TechNodeHelper.AddDefaultUpgrades("Jeweler");
```

## SummoningCircle branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| summoning_circle | FlowElement | ; Previous jeweler | — | eastern war stage 3 | CostMultiplier=4.0 | summon_gremlin | T8SummoningCircle.cs:10 |
| summon_gremlin | Recipe | Root summoning_circle;  | — | — | Inherited/default | — | T8SummoningCircle.cs:26 |
| summon_hellspawn | Recipe | Root summoning_circle;  | — | — | Inherited/default | — | T8SummoningCircle.cs:32 |
| summon_observer | Recipe | Root summoning_circle;  | — | — | Inherited/default | — | T8SummoningCircle.cs:38 |
| summon_cherub | Recipe | Root summoning_circle;  | shrine | — | CostTier=11; CostCurrency=GoldFaith; CostMultiplier=0.5 | — | T8SummoningCircle.cs:44 |
| summon_valkyrie | Recipe | Root summoning_circle;  | shrine | — | CostTier=11; CostCurrency=GoldFaith; CostMultiplier=0.5 | — | T8SummoningCircle.cs:55 |
| summon_arbiter | Recipe | Root summoning_circle;  | shrine | — | CostTier=11; CostCurrency=GoldFaith | — | T8SummoningCircle.cs:66 |
| cr_demonologist | Recipe | Root summoning_circle;  | scribe | — | CostTier=10 | — | T8SummoningCircle.cs:76 |

```csharp
25: TechNodeHelper.AddDefaultUpgrades("SummoningCircle", hasEquipment: false);
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T8Dungeon.cs:10`
- `Assets.Source.Player.Tech/T8Dungeon.cs:31`
- `Assets.Source.Player.Tech/T8Dungeon.cs:37`
- `Assets.Source.Player.Tech/T8Dungeon.cs:48`
- `Assets.Source.Player.Tech/T8Dungeon.cs:59`
- `Assets.Source.Player.Tech/T8Dungeon.cs:72`
- `Assets.Source.Player.Tech/T8Dungeon.cs:83`
- `Assets.Source.Player.Tech/T8Dungeon.cs:98`
- `Assets.Source.Player.Tech/T8Dungeon.cs:106`
- `Assets.Source.Player.Tech/T8Dungeon.cs:117`
- `Assets.Source.Player.Tech/T8Dungeon.cs:126`
- `Assets.Source.Player.Tech/T8Dungeon.cs:134`
- `Assets.Source.Player.Tech/T8Jeweler.cs:10`
- `Assets.Source.Player.Tech/T8Jeweler.cs:25`
- `Assets.Source.Player.Tech/T8Jeweler.cs:31`
- `Assets.Source.Player.Tech/T8Jeweler.cs:37`
- `Assets.Source.Player.Tech/T8Jeweler.cs:43`
- `Assets.Source.Player.Tech/T8Jeweler.cs:49`
- `Assets.Source.Player.Tech/T8Jeweler.cs:55`
- `Assets.Source.Player.Tech/T8Jeweler.cs:61`
- `Assets.Source.Player.Tech/T8Jeweler.cs:67`
- `Assets.Source.Player.Tech/T8Jeweler.cs:73`
- `Assets.Source.Player.Tech/T8Jeweler.cs:79`
- `Assets.Source.Player.Tech/T8Jeweler.cs:86`
- `Assets.Source.Player.Tech/T8Jeweler.cs:93`
- `Assets.Source.Player.Tech/T8Jeweler.cs:100`
- `Assets.Source.Player.Tech/T8Jeweler.cs:107`
- `Assets.Source.Player.Tech/T8Jeweler.cs:114`
- `Assets.Source.Player.Tech/T8Jeweler.cs:121`
- `Assets.Source.Player.Tech/T8Jeweler.cs:127`
- `Assets.Source.Player.Tech/T8Jeweler.cs:133`
- `Assets.Source.Player.Tech/T8Jeweler.cs:139`
- `Assets.Source.Player.Tech/T8Jeweler.cs:145`
- `Assets.Source.Player.Tech/T8Jeweler.cs:152`
- `Assets.Source.Player.Tech/T8Jeweler.cs:159`
- `Assets.Source.Player.Tech/T8Jeweler.cs:166`
- `Assets.Source.Player.Tech/T8Jeweler.cs:172`
- `Assets.Source.Player.Tech/T8Jeweler.cs:182`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:10`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:26`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:32`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:38`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:44`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:55`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:66`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:76`
