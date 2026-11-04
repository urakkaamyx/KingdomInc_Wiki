# Technology tier 11: Faith, undead, and endgame

Shrine follows Scribe and requires Yensburg war stage 2. It grants prayer_1 and uses Faith for many recipes/upgrades. Graveyard grants burial/fallen-hero utilities; Necromancer follows it and grants shambler. Catacombs requires Yensburg stage 3, North war Yensburg stage 4, Archive North stage 1, and endgame North stage 4. Distiller additionally checks endgame completion.

## Branch overview

Shrine follows Scribe and requires Yensburg war stage 2. It grants prayer_1 and uses Faith for many recipes/upgrades. Graveyard grants burial/fallen-hero utilities; Necromancer follows it and grants shambler. Catacombs requires Yensburg stage 3, North war Yensburg stage 4, Archive North stage 1, and endgame North stage 4. Distiller additionally checks endgame completion.

The group follows its source-class prefix, not necessarily its numeric price tier. Rows show internal IDs, all explicitly declared dependencies, cost overrides and automatic technology grants. Inherited/default values follow Technology requirements and Technology cost formula. Shared helper nodes are described in Automation technology and in the branch notes.

## Graveyard branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| graveyard | FlowElement | ; Previous shrine | — | — | Inherited/default | simple_burial, fallen_heroes | T11Graveyard.cs:10 |
| fallen_heroes | Utility | Root graveyard;  | — | — | CostCurrency=GoldFaith | — | T11Graveyard.cs:28 |
| simple_burial | Recipe | Root graveyard;  | — | — | CostCurrency=GoldFaith | — | T11Graveyard.cs:36 |
| officiated_burial | Recipe | Root graveyard;  | — | — | CostCurrency=GoldFaith | — | T11Graveyard.cs:43 |
| state_funeral | Recipe | Root graveyard;  | — | — | CostCurrency=GoldFaith | — | T11Graveyard.cs:50 |

```csharp
57: TechNodeHelper.AddDefaultUpgrades("Graveyard");
58: TechNode.Get("graveyard_productivity").Hidden = (GamePlayer ply) => true;
59: TechNode.Get("graveyard_automation").CostCurrency = CurrencyCollection.GoldFaith;
60: TechNode.Get("graveyard_automation_2").CostCurrency = CurrencyCollection.GoldFaith;
61: TechNode.Get("graveyard_automation_3").CostCurrency = CurrencyCollection.GoldFaith;
62: TechNode.Get("graveyard_quality").CostCurrency = CurrencyCollection.GoldFaith;
```

## Necromancer branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| necromancer | FlowElement | ; Previous graveyard | — | — | Inherited/default | shambler | T11Necromancer.cs:9 |
| shambler | Recipe | Root necromancer;  | — | — | Inherited/default | — | T11Necromancer.cs:22 |
| skeletal_archer | Recipe | Root necromancer;  | — | — | Inherited/default | — | T11Necromancer.cs:28 |
| skeletal_berserker | Recipe | Root necromancer;  | — | — | Inherited/default | — | T11Necromancer.cs:34 |
| skeletal_mage | Recipe | Root necromancer;  | — | — | Inherited/default | — | T11Necromancer.cs:40 |
| hulking_monstrosity | Recipe | Root necromancer;  | — | — | Inherited/default | — | T11Necromancer.cs:46 |
| cr_necrolyte | Recipe | Root necromancer;  | — | — | Inherited/default | — | T11Necromancer.cs:52 |

```csharp
21: TechNodeHelper.AddDefaultUpgrades("Necromancer", hasEquipment: false);
```

## Shrine branch

The source excerpts below identify shared helper creation and later overrides. These modify the explicit rows or add helper-generated research. Full helper rules are in Automation technology.

| Identifier | Type | Root / previous | Additional tech | Special gate / visibility | Declared cost overrides | Granted tech on unlock | Source line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| shrine | FlowElement | ; Previous scribe | — | yensburg war stage 2 | CostTier=11 | prayer_1 | T11Shrine.cs:11 |
| prayer_1 | Recipe | Root shrine;  | — | — | CostMultiplier=0.5 | — | T11Shrine.cs:31 |
| blessed_prayer_beads | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith; CostMultiplier=0.5 | — | T11Shrine.cs:38 |
| prayer_2 | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith; CostMultiplier=0.5 | — | T11Shrine.cs:46 |
| indulgence | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith; CostMultiplier=0.5 | — | T11Shrine.cs:54 |
| blessed_arms | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith | — | T11Shrine.cs:62 |
| blessed_equipment | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith | — | T11Shrine.cs:69 |
| pontiff_ring | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith | — | T11Shrine.cs:76 |
| martyr_relic | Recipe | Root shrine;  | graveyard | — | CostCurrency=GoldFaith | — | T11Shrine.cs:83 |
| cr_paladin | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith | — | T11Shrine.cs:91 |
| cr_shaman | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith | — | T11Shrine.cs:98 |
| cr_evangelist | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith | — | T11Shrine.cs:105 |
| cr_lightbringer | Recipe | Root shrine;  | — | — | CostCurrency=GoldFaith | — | T11Shrine.cs:112 |
| purified_tech | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:119 |
| vanquisher_sword | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:127 |
| blighted_dagger | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:135 |
| blink_rapier | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:143 |
| flenser_greatsword | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:151 |
| unblinking_axe | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:159 |
| deadeye_bow | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:167 |
| fragment_staff | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:175 |
| unlife_staff | Recipe | Root shrine;  | dungeon_archive | — | CostCurrency=GoldFaith | — | T11Shrine.cs:183 |
| cleansed_nightmare | Recipe | Root shrine;  | nightmare_distiller | — | CostTier=12 | — | T11Shrine.cs:191 |
| dungeon_catacombs | Dungeon | ; Previous shrine | — | yensburg war stage 3 | Inherited/default | — | T11Shrine.cs:199 |
| war_effort_north | War | ; Previous shrine | — | yensburg war stage 4 | CostTier=12 | — | T11Shrine.cs:212 |
| dungeon_archive | Dungeon | ; Previous war_effort_north | — | north war stage 1 | Inherited/default | — | T11Shrine.cs:227 |
| dungeon_endgame | Dungeon | ; Previous war_effort_north | — | north war stage 4 | CostTier=12 | — | T11Shrine.cs:240 |
| nightmare_distiller | FlowElement | ; Previous dungeon_endgame | — | Final endgame CompletedCount > 0 | Inherited/default | — | T11Shrine.cs:254 |

```csharp
26: TechNodeHelper.AddDefaultUpgrades("Shrine", hasEquipment: true, hasEnhancements: true);
27: foreach (TechNode item in new List<TechNode> { "shrine_productivity", "shrine_automation_2", "shrine_quality", "shrine_automation_3" })
29: item.CostCurrency = CurrencyCollection.GoldFaith;
```

## Sources

- `Assets.Source.Player/TechNode.cs:280`
- `Assets.Source.Player.Tech/T11Graveyard.cs:10`
- `Assets.Source.Player.Tech/T11Graveyard.cs:28`
- `Assets.Source.Player.Tech/T11Graveyard.cs:36`
- `Assets.Source.Player.Tech/T11Graveyard.cs:43`
- `Assets.Source.Player.Tech/T11Graveyard.cs:50`
- `Assets.Source.Player.Tech/T11Necromancer.cs:9`
- `Assets.Source.Player.Tech/T11Necromancer.cs:22`
- `Assets.Source.Player.Tech/T11Necromancer.cs:28`
- `Assets.Source.Player.Tech/T11Necromancer.cs:34`
- `Assets.Source.Player.Tech/T11Necromancer.cs:40`
- `Assets.Source.Player.Tech/T11Necromancer.cs:46`
- `Assets.Source.Player.Tech/T11Necromancer.cs:52`
- `Assets.Source.Player.Tech/T11Shrine.cs:11`
- `Assets.Source.Player.Tech/T11Shrine.cs:31`
- `Assets.Source.Player.Tech/T11Shrine.cs:38`
- `Assets.Source.Player.Tech/T11Shrine.cs:46`
- `Assets.Source.Player.Tech/T11Shrine.cs:54`
- `Assets.Source.Player.Tech/T11Shrine.cs:62`
- `Assets.Source.Player.Tech/T11Shrine.cs:69`
- `Assets.Source.Player.Tech/T11Shrine.cs:76`
- `Assets.Source.Player.Tech/T11Shrine.cs:83`
- `Assets.Source.Player.Tech/T11Shrine.cs:91`
- `Assets.Source.Player.Tech/T11Shrine.cs:98`
- `Assets.Source.Player.Tech/T11Shrine.cs:105`
- `Assets.Source.Player.Tech/T11Shrine.cs:112`
- `Assets.Source.Player.Tech/T11Shrine.cs:119`
- `Assets.Source.Player.Tech/T11Shrine.cs:127`
- `Assets.Source.Player.Tech/T11Shrine.cs:135`
- `Assets.Source.Player.Tech/T11Shrine.cs:143`
- `Assets.Source.Player.Tech/T11Shrine.cs:151`
- `Assets.Source.Player.Tech/T11Shrine.cs:159`
- `Assets.Source.Player.Tech/T11Shrine.cs:167`
- `Assets.Source.Player.Tech/T11Shrine.cs:175`
- `Assets.Source.Player.Tech/T11Shrine.cs:183`
- `Assets.Source.Player.Tech/T11Shrine.cs:191`
- `Assets.Source.Player.Tech/T11Shrine.cs:199`
- `Assets.Source.Player.Tech/T11Shrine.cs:212`
- `Assets.Source.Player.Tech/T11Shrine.cs:227`
- `Assets.Source.Player.Tech/T11Shrine.cs:240`
- `Assets.Source.Player.Tech/T11Shrine.cs:254`
