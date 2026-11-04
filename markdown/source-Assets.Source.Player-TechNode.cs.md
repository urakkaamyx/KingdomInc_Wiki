# TechNode — source reference

Assets.Source.Player/TechNode.cs · 324 lines · 584 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public class TechNode |
| 9 | public delegate void OnTechNodeUnlock(GamePlayer player) |
| 11 | public delegate bool TechMatchesPlayer(GamePlayer player) |
| 13 | public const double BaseCost = 400.0 |
| 21 | public static TechNode CriticalCraft |
| 23 | public readonly string Identifier |
| 25 | public readonly int Ordinal |
| 27 | public TechNodeType NodeType |
| 29 | public string Name |
| 31 | public string Description |
| 33 | public string IconName |
| 35 | public Vector2Int AbsolutePosition |
| 37 | public Vector2Int RelativePosition |
| 39 | public int CostTier |
| 41 | public TechMatchesPlayer Hidden |
| 43 | public IEnumerable<Currency> CostCurrency |
| 45 | public double CostMultiplier = 1.0 |
| 47 | public double GoldMultiplier = 1.0 |
| 49 | public TechNode Root |
| 51 | public TechNode Previous |
| 53 | public List<string> AdditionalRequirements |
| 55 | public bool ForceRootNode |
| 57 | public TechNode OverrideRootNode |
| 59 | public bool DevMode |
| 63 | public TechMatchesPlayer CustomRequirement |
| 65 | public string CustomRequirementDesc |
| 67 | public OnTechNodeUnlock OnUnlock |
| 69 | public static int Count => _currentOrdinal |
| 71 | public static IEnumerable<TechNode> Nodes => _orderedTech |
| 73 | public Vector2Int Position |
| 85 | public CurrencyCollection Cost { private get; set; } |
| 87 | public IEnumerable<TechNode> AllRequirements |
| 114 | public bool IsPurchased => GamePlayer.Current.HasTech(this) |
| 116 | public bool IsAvailable |
| 128 | public bool IsLocked |
| 151 | public Sprite Icon => SpriteLibrary.Get(IconName) |
| 153 | public IEnumerable<TechNode> AvailableTech |
| 167 | public bool IsRootNode |
| 179 | public bool HasChildNodes |
| 235 | public TechNode(string id) |
| 244 | public CurrencyCollection GetCost() |
| 258 | public void ResetCost() |
| 263 | public double GetDefaultCostMultiplier() |
| 280 | public static TechNode Add(TechNode node) |
| 299 | public static TechNode Get(string id) |
| 305 | public static TechNode Get(int ordinal) |
| 310 | public static implicit operator string(TechNode node) |
| 315 | public static implicit operator TechNode(string id) |
| 320 | public static implicit operator bool(TechNode node) |

## Documented by

| Wiki article |
| --- |
| [Accountant](tech-accountant.md) |
| [Additional Workspace](tech-add_diagrams.md) |
| [Desperate Measures](tech-adv_to_war.md) |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Potion Dispenser](tech-adventure_supplies_automation.md) |
| [Adventure Supplies · second add-on slot](tech-adventure_supplies_automation_2.md) |
| [Adventure Supplies · third add-on slot](tech-adventure_supplies_automation_3.md) |
| [Adventure Supplies · overseers](tech-adventure_supplies_productivity.md) |
| [Adventure Supplies · artisans](tech-adventure_supplies_quality.md) |
| [Adventurer's Guild](tech-adventurers_guild.md) |
| [Reception Desk](tech-adventurers_guild_automation.md) |
| [Adventurer's Guild · second add-on slot](tech-adventurers_guild_automation_2.md) |
| [Adventurer's Guild · third add-on slot](tech-adventurers_guild_automation_3.md) |
| [Adventurer's Guild · overseers](tech-adventurers_guild_productivity.md) |
| [Adventurer's Guild · artisans](tech-adventurers_guild_quality.md) |
| [Aiding the Refugees](tech-aid_refugees.md) |
| [Alchemical Experimentation](tech-alchemical_experiment.md) |
| [Alchemist](tech-alchemist.md) |
| [Autobrewery](tech-alchemist_automation.md) |
| [Alchemist · second add-on slot](tech-alchemist_automation_2.md) |
| [Alchemist · third add-on slot](tech-alchemist_automation_3.md) |
| [Alchemist · overseers](tech-alchemist_productivity.md) |
| [Alchemist · artisans](tech-alchemist_quality.md) |
| [Amulet of Vigor](tech-amulet_of_energy.md) |
| [Amulet of Fire Protection](tech-amulet_of_fire_prot.md) |
| [Amulet of Vitality](tech-amulet_of_healing.md) |
| [Panacea Amulet](tech-amulet_of_poison_prot.md) |
| [Amulet of Dark Tidings](tech-amulet_of_shadow_prot.md) |
| [Crystalline Staff](tech-ancient_int_staff.md) |
| [Bulwark of Ancients](tech-ancient_shield.md) |
| [Staff of Sages](tech-ancient_wis_staff.md) |
| [Ancient Wood Longbow](tech-ancient_wood_bow.md) |
| [Ancient Wood Plank](tech-ancient_wood_plank.md) |
| [Ancient Wood Staff](tech-ancient_wood_staff.md) |
| [Ancient Woodcutter](tech-ancient_woodcutter.md) |
| [Annihilate Gemstone](tech-annihilate_gemstone.md) |
| [Appraiser](tech-appraiser.md) |
| [Arcanite Chestguard](tech-arcanium_armor.md) |
| [Arcanite Cleaver](tech-arcanium_battleaxe.md) |
| [Arcanite Backstabber](tech-arcanium_dagger.md) |
| [Arcanite Claymore](tech-arcanium_greatsword.md) |
| [Arcanite Casque](tech-arcanium_helm.md) |
| [Arcanite Ingot](tech-arcanium_ingot.md) |
| [Arcanite Blade](tech-arcanium_sword.md) |
| [Archbishop's Staff](tech-archbishop_staff.md) |
| [Archmage's Hat](tech-archmage_hat.md) |
| [Archmage's Robe](tech-archmage_robe.md) |
| [Archmage's Staff](tech-archmage_staff.md) |
| [Arena](tech-arena.md) |
| [Fight Announcer](tech-arena_automation.md) |
| [Arena · second add-on slot](tech-arena_automation_2.md) |
| [Arena · third add-on slot](tech-arena_automation_3.md) |
| [Fight To The Death](tech-arena_blood_sport.md) |
| [Fight Purse](tech-arena_cashier.md) |
| [Stoneskin Elixir](tech-armor_potion.md) |
| [Armory](tech-armory.md) |
| [Overflowing Armory](tech-armory_overflow.md) |
| [Frugal Quartermaster](tech-armory_storage_cost.md) |
| [Extradimensional Storage Space](tech-armory_unlock_channels.md) |
| [Attuned Catalyst](tech-attuned_catalyst.md) |
| [Bank "Heist"](tech-bank_heist.md) |
| [Barracks](tech-barracks.md) |
| [Recruitment Officer](tech-barracks_automation.md) |
| [Barracks · second add-on slot](tech-barracks_automation_2.md) |
| [Barracks · third add-on slot](tech-barracks_automation_3.md) |
| [Barracks · overseers](tech-barracks_productivity.md) |
| [Barracks · artisans](tech-barracks_quality.md) |
| [Biological Experimentation](tech-biological_experiment.md) |
| [Blacksmith](tech-blacksmith.md) |
| [Apprenticeship](tech-blacksmith_automation.md) |
| [Blacksmith · second add-on slot](tech-blacksmith_automation_2.md) |
| [Blacksmith · third add-on slot](tech-blacksmith_automation_3.md) |
| [Blacksmith · overseers](tech-blacksmith_productivity.md) |
| [Blacksmith · artisans](tech-blacksmith_quality.md) |
| [Blank Tome](tech-blank_tome.md) |
| [Blank Vellum](tech-blank_vellum.md) |
| [Blessed Armaments](tech-blessed_arms.md) |
| [Sanctified Equipment](tech-blessed_equipment.md) |
| [Blessed Prayer Beads](tech-blessed_prayer_beads.md) |
| [Blighted Dagger](tech-blighted_dagger.md) |
| [Ethereal Rapier](tech-blink_rapier.md) |
| [Seared Boar Steak](tech-boar_steak.md) |
| [Boot Camp Heroics](tech-boot_camp.md) |
| [Butcher](tech-butcher.md) |
| [The Meat Man](tech-butcher_automation.md) |
| [Butcher · second add-on slot](tech-butcher_automation_2.md) |
| [Butcher · third add-on slot](tech-butcher_automation_3.md) |
| [Butcher Cattle](tech-butcher_cattle.md) |
| [Butcher · overseers](tech-butcher_productivity.md) |
| [Butcher · artisans](tech-butcher_quality.md) |
| [Butcher Salamander](tech-butcher_salamander.md) |
| [Butcher Stalker](tech-butcher_stalker.md) |
| [Build Menu Search](tech-buy_menu_search.md) |
| [Byrgenwald Expedition](tech-byrgenwald_expedition.md) |
| [Campfire](tech-campfire.md) |
| [Wilderness Cookery](tech-campfire_automation.md) |
| [Campfire · second add-on slot](tech-campfire_automation_2.md) |
| [Campfire · third add-on slot](tech-campfire_automation_3.md) |
| [Campfire · overseers](tech-campfire_productivity.md) |
| [Campfire · artisans](tech-campfire_quality.md) |
| [Carpenter](tech-carpenter.md) |
| [Only Hammers](tech-carpenter_automation.md) |
| [Carpenter · second add-on slot](tech-carpenter_automation_2.md) |
| [Carpenter · third add-on slot](tech-carpenter_automation_3.md) |
| [Carpenter · overseers](tech-carpenter_productivity.md) |
| [Carpenter · artisans](tech-carpenter_quality.md) |
| [Chainsaw](tech-chainsaw.md) |
| [Cleansed Nightmare](tech-cleansed_nightmare.md) |
| [Mine Sweep](tech-clear_mines.md) |
| [Clone Tool](tech-clone_tool.md) |
| [Coffin](tech-coffin.md) |
| [Collector](tech-collector.md) |
| [Container Duplication](tech-container_clone.md) |
| [Hardboiled Egg](tech-cooked_egg.md) |
| [Cotton Cloth](tech-cotton_cloth.md) |
| [Scholar's Hat](tech-cotton_hat.md) |
| [Scholar's Robe](tech-cotton_robe.md) |
| [Anatomy Lesson](tech-cr_assassin.md) |
| [Feeding the Wildlife](tech-cr_beast_master.md) |
| [Demonic Initiation](tech-cr_demonologist.md) |
| [Preaching to the Choir](tech-cr_evangelist.md) |
| [Prayer of Light](tech-cr_lightbringer.md) |
| [Rock Carving for Dummies](tech-cr_lithomancer.md) |
| [Introduction to Necromancy](tech-cr_necrolyte.md) |
| [Guardian's Pledge](tech-cr_paladin.md) |
| [Pyromancy and You: An Introduction](tech-cr_pyromancer.md) |
| [Commune with Nature](tech-cr_shaman.md) |
| [Study on Phytotoxins](tech-cr_survivalist.md) |
| [Assassin's Goggles](tech-crit_goggles.md) |
| [Flash of Brilliance](tech-critical_craft.md) |
| [Crystalized Mana](tech-crystal_mana.md) |
| [Currency Exchange](tech-currency_exchange.md) |
| [Market Maker](tech-currency_exchange_tax.md) |
| [Deadeye Bow](tech-deadeye_bow.md) |
| [Label](tech-deco_label.md) |
| [Sticker](tech-deco_sticker.md) |
| [Decoded Writings](tech-decoded_writings.md) |
| [Demonsteel Armor](tech-demonsteel_armor.md) |
| [Demonsteel Helm](tech-demonsteel_helm.md) |
| [Dev Item Spawner](tech-dev_item_spawner.md) |
| [Disenchanter](tech-disenchanter.md) |
| [Mana Vacuum](tech-disenchanter_automation.md) |
| [Disenchanter · second add-on slot](tech-disenchanter_automation_2.md) |
| [Disenchanter · third add-on slot](tech-disenchanter_automation_3.md) |
| [Annihilation](tech-disenchanter_mana.md) |
| [Aether Collector](tech-disenchanter_passive.md) |
| [Decursing the Library](tech-dispel_library.md) |
| [Distributor](tech-distributor.md) |
| [Doodad](tech-doodad.md) |
| [Dungeon](tech-dungeon.md) |
| [Timeless Archive](tech-dungeon_archive.md) |
| [Dungeon Keeper](tech-dungeon_automation.md) |
| [Dungeon · second add-on slot](tech-dungeon_automation_2.md) |
| [Dungeon · third add-on slot](tech-dungeon_automation_3.md) |
| [Yensburg Catacombs](tech-dungeon_catacombs.md) |
| [Ancient Treasures](tech-dungeon_coin_loot.md) |
| [Tomb of Sholrath](tech-dungeon_endgame.md) |
| [Feral Den](tech-dungeon_feral_den.md) |
| [Perfectly Preserved](tech-dungeon_item_loot.md) |
| [Together As One](tech-dungeon_limit_break.md) |
| [Unshakable Devotion](tech-dungeon_limit_break_2.md) |
| [Ruins of Arlingen](tech-dungeon_ruins.md) |
| [Temple of the Last Rite](tech-dungeon_temple.md) |
| [Trash Loot](tech-dungeon_trash_loot.md) |
| [Quick Upgrade](tech-easy_node_upgrade.md) |
| [Stacked Elements](tech-element_stacking.md) |
| [Elemental Eradication](tech-elemental_eradication.md) |
| [Embossed Mask](tech-embossed_hat.md) |
| [Embossed Leather](tech-embossed_leather.md) |
| [Embossed Vest](tech-embossed_vest.md) |
| [Embroidered Cotton](tech-embroidered_cotton.md) |
| [Enchant Armor - Protection](tech-enchant_armor_armor.md) |
| [Enchant Armor: Vigor](tech-enchant_armor_energy.md) |
| [Enchant Shield - Shadow Ward](tech-enchant_armor_shadow_resist.md) |
| [Enchant Armor: Stats](tech-enchant_armor_stats.md) |
| [Enchant Armor - Giant Strength](tech-enchant_armor_strength_skill_crit.md) |
| [Enchant Food: Deliciousness](tech-enchant_food_quality.md) |
| [Imbue Dark Essence](tech-enchant_item_quality.md) |
| [Enchant Shield - Protection](tech-enchant_shield_armor.md) |
| [Enchant Weapon - Critical Hit](tech-enchant_weapon_crit.md) |
| [Enchant Weapon: Power](tech-enchant_weapon_power.md) |
| [Enchanted Thread](tech-enchanted_cotton_thread.md) |
| [Enchanted Ink](tech-enchanted_ink.md) |
| [Enchanter](tech-enchanter.md) |
| [Leyline Guide](tech-enchanter_automation.md) |
| [Enchanter · second add-on slot](tech-enchanter_automation_2.md) |
| [Enchanter · third add-on slot](tech-enchanter_automation_3.md) |
| [Enchanter · overseers](tech-enchanter_productivity.md) |
| [Enchanter · artisans](tech-enchanter_quality.md) |
| [Revitalizing Potion](tech-energy_potion.md) |
| [Engrave Heavy Armor: Defense](tech-engrave_heavy_armor_armor.md) |
| [Engrave Heavy Armor: Health](tech-engrave_heavy_armor_health.md) |
| [Engraved Jewelry](tech-engrave_jewelry_quality.md) |
| [Embroider Clothing: Defense](tech-engrave_light_armor_armor.md) |
| [Embroider Clothing: Dexterity](tech-engrave_light_armor_dex.md) |
| [Embroider Clothing: Health](tech-engrave_light_armor_health.md) |
| [Embroider Clothing: Magic](tech-engrave_light_armor_mag.md) |
| [Embroider Clothing: Wisdom](tech-engrave_light_armor_wis.md) |
| [Engrave Weapon: Dexterity](tech-engrave_weapon_dex.md) |
| [Engrave Weapon: Magic](tech-engrave_weapon_mag.md) |
| [Engrave Weapon: Strength](tech-engrave_weapon_str.md) |
| [Engrave Weapon: Wisdom](tech-engrave_weapon_wis.md) |
| [Engraver](tech-engraver.md) |
| [Runic Apprentice](tech-engraver_automation.md) |
| [Engraver · second add-on slot](tech-engraver_automation_2.md) |
| [Engraver · third add-on slot](tech-engraver_automation_3.md) |
| [Engraver · overseers](tech-engraver_productivity.md) |
| [Engraver · artisans](tech-engraver_quality.md) |
| [Min Max](tech-enhance_multiple.md) |
| [Experimental Summons](tech-experimental_summons.md) |
| [Exterminate Rats!](tech-exterminate_rats.md) |
| [Extinguish the Ritual](tech-extinguish_ritual.md) |
| [Fallen Heroes](tech-fallen_heroes.md) |
| [Farm](tech-farm.md) |
| [Farmhand](tech-farm_automation.md) |
| [Farm · second add-on slot](tech-farm_automation_2.md) |
| [Farm · third add-on slot](tech-farm_automation_3.md) |
| [Cattle Husbandry](tech-farm_cattle.md) |
| [Cotton Cultivation](tech-farm_cotton.md) |
| [Flax Cultivation](tech-farm_flax.md) |
| [Onion Cultivation](tech-farm_onion.md) |
| [Farm · overseers](tech-farm_productivity.md) |
| [Farm · artisans](tech-farm_quality.md) |
| [Salamander Husbandry](tech-farm_salamander.md) |
| [Herb Cultivation](tech-farm_soothing_herbs.md) |
| [Stalker Husbandry](tech-farm_stalker.md) |
| [Wheat Cultivation](tech-farm_wheat.md) |
| [Farmstead Liberator](tech-farmstead_liberator.md) |
| [Filter](tech-filter.md) |
| [Elixir of Fire Resistance](tech-fire_resist_potion.md) |
| [Necklace of Fireballs](tech-fireball_amulet.md) |
| [Flenser's Sword](tech-flenser_greatsword.md) |
| [Forest](tech-forest.md) |
| [Harvest Ancient Wood](tech-forest_ancient_wood.md) |
| [Cross-country Carriers](tech-forest_automation.md) |
| [Forest · second add-on slot](tech-forest_automation_2.md) |
| [Forest · third add-on slot](tech-forest_automation_3.md) |
| [Harvest Bird Eggs](tech-forest_bird_egg.md) |
| [Boar Hunt](tech-forest_boar_meat.md) |
| [Harvest Bone](tech-forest_bone.md) |
| [Wilderness Evangelism](tech-forest_evangelism.md) |
| [Harvest Lettuce](tech-forest_lettuce.md) |
| [Harvest Mushrooms](tech-forest_mushroom.md) |
| [Forest · overseers](tech-forest_productivity.md) |
| [Forest · artisans](tech-forest_quality.md) |
| [Harvest Resin](tech-forest_resin.md) |
| [Stalker Hunt](tech-forest_supple_leather.md) |
| [Harvest Wild Onion](tech-forest_wild_onion.md) |
| [Wolf Hunt](tech-forest_wolf_hide.md) |
| [Harvest Wood Log](tech-forest_wood_log.md) |
| [Animated Workforce](tech-forest_workforce.md) |
| [Forge](tech-forge.md) |
| [Forge Attendant](tech-forge_automation.md) |
| [Forge · second add-on slot](tech-forge_automation_2.md) |
| [Forge · third add-on slot](tech-forge_automation_3.md) |
| [Forge · overseers](tech-forge_productivity.md) |
| [Forge · artisans](tech-forge_quality.md) |
| [Splintered Staff](tech-fragment_staff.md) |
| [Empty Setting](tech-gem_setting.md) |
| [Gilded Coffin](tech-gilded_coffin.md) |
| [Gizmo](tech-gizmo.md) |
| [Glass Vial](tech-glass_vial.md) |
| [Tech List View](tech-global_tech_upgrade.md) |
| [Parade Armor](tech-gold_armor.md) |
| [Sapphire Crown](tech-gold_crown.md) |
| [Gold Ingot](tech-gold_ingot.md) |
| [Ceremonial Sword](tech-gold_sword.md) |
| [Gold Wire](tech-gold_wire.md) |
| [Golem Gauntlets](tech-golem_gauntlets.md) |
| [Graveyard](tech-graveyard.md) |
| [Gravedigger](tech-graveyard_automation.md) |
| [Graveyard · second add-on slot](tech-graveyard_automation_2.md) |
| [Graveyard · third add-on slot](tech-graveyard_automation_3.md) |
| [Graveyard · overseers](tech-graveyard_productivity.md) |
| [Graveyard · artisans](tech-graveyard_quality.md) |
| [Greater Healing Potion](tech-greater_healing_potion.md) |
| [Guildhouse](tech-guildhouse.md) |
| [Common Ground](tech-guildhouse_conscripts.md) |
| [Endless Hall of Doors](tech-guildhouse_unlock_channels.md) |
| [Hamburger](tech-hamburger.md) |
| [Healing Potion](tech-healing_potion.md) |
| [Malignant Cover](tech-hellish_cover.md) |
| [Malignant Mask](tech-hellish_mask.md) |
| [Hoard](tech-hoard.md) |
| [Hulking Monstrosity](tech-hulking_monstrosity.md) |
| [Identify Gemstones](tech-identify_gem.md) |
| [Identify Plants](tech-identify_plants.md) |
| [Incinerator](tech-incinerator.md) |
| [Indulgence](tech-indulgence.md) |
| [Possessed Shield](tech-infected_shield.md) |
| [Initiate's Hat](tech-initiate_hat.md) |
| [Initiate's Staff](tech-initiate_staff.md) |
| [Inn](tech-inn.md) |
| [Bed and Breakfast](tech-inn_add_food.md) |
| [Inspector](tech-inspector.md) |
| [Inventor](tech-inventor.md) |
| [Automaton](tech-inventor_automation.md) |
| [Inventor · second add-on slot](tech-inventor_automation_2.md) |
| [Inventor · third add-on slot](tech-inventor_automation_3.md) |
| [Inventor · overseers](tech-inventor_productivity.md) |
| [Inventor · artisans](tech-inventor_quality.md) |
| [Iron Armor](tech-iron_armor.md) |
| [Iron Battleaxe](tech-iron_battleaxe.md) |
| [Iron Dagger](tech-iron_dagger.md) |
| [Iron Greatsword](tech-iron_greatsword.md) |
| [Iron Helm](tech-iron_helm.md) |
| [Iron Ingot](tech-iron_ingot.md) |
| [Iron Rapier](tech-iron_rapier.md) |
| [Iron Sword](tech-iron_sword.md) |
| [Item List View](tech-item_list.md) |
| [Jeweler](tech-jeweler.md) |
| [Grinding Wheel](tech-jeweler_automation.md) |
| [Jeweler · second add-on slot](tech-jeweler_automation_2.md) |
| [Jeweler · third add-on slot](tech-jeweler_automation_3.md) |
| [Jeweler · overseers](tech-jeweler_productivity.md) |
| [Jeweler · artisans](tech-jeweler_quality.md) |
| [Kitchen](tech-kitchen.md) |
| [Sous Chef](tech-kitchen_automation.md) |
| [Kitchen · second add-on slot](tech-kitchen_automation_2.md) |
| [Kitchen · third add-on slot](tech-kitchen_automation_3.md) |
| [Kitchen · overseers](tech-kitchen_productivity.md) |
| [Kitchen · artisans](tech-kitchen_quality.md) |
| [Leatherworker](tech-leatherworker.md) |
| [Honest Craftmanship](tech-leatherworker_automation.md) |
| [Leatherworker · second add-on slot](tech-leatherworker_automation_2.md) |
| [Leatherworker · third add-on slot](tech-leatherworker_automation_3.md) |
| [Leatherworker · overseers](tech-leatherworker_productivity.md) |
| [Leatherworker · artisans](tech-leatherworker_quality.md) |
| [Library](tech-library.md) |
| [Lifebloom Amulet](tech-lifebloom_amulet.md) |
| [Linen Cloth](tech-linen_cloth.md) |
| [Linen Padding](tech-linen_padding.md) |
| [Luxury Shop](tech-luxury_shop.md) |
| [Mad Scribblings](tech-mad_scribblings.md) |
| [Manifold](tech-manifold.md) |
| [Relic of the Martyr](tech-martyr_relic.md) |
| [Mechanical Experimentation](tech-mechanical_experiment.md) |
| [Foreign Legion](tech-mercenary_conscripts.md) |
| [Mercenary Guild](tech-mercenary_guild.md) |
| [Mercurial Reagents](tech-mercurial_reagents.md) |
| [Leyline Goggles](tech-mind_goggles.md) |
| [Mine](tech-mine.md) |
| [Drudge Miners](tech-mine_automation.md) |
| [Mine · second add-on slot](tech-mine_automation_2.md) |
| [Mine · third add-on slot](tech-mine_automation_3.md) |
| [Mine Gold Ore](tech-mine_gold_ore.md) |
| [Mine Iron Ore](tech-mine_iron_ore.md) |
| [Mine · overseers](tech-mine_productivity.md) |
| [Mine · artisans](tech-mine_quality.md) |
| [Mine Sapphire](tech-mine_sapphire.md) |
| [Mine Silver Ore](tech-mine_silver_ore.md) |
| [Mushroom Stew](tech-mushroom_stew.md) |
| [Necromancer](tech-necromancer.md) |
| [Novice Necromancer](tech-necromancer_automation.md) |
| [Necromancer · second add-on slot](tech-necromancer_automation_2.md) |
| [Necromancer · third add-on slot](tech-necromancer_automation_3.md) |
| [Necromancer · overseers](tech-necromancer_productivity.md) |
| [Necromancer · artisans](tech-necromancer_quality.md) |
| [Nightmare Casing](tech-nightmare_casing.md) |
| [Nightmare Collector](tech-nightmare_collector.md) |
| [Nightmare Distiller](tech-nightmare_distiller.md) |
| [Officiated Burial](tech-officiated_burial.md) |
| [Outfitter](tech-outfitter.md) |
| [Bring A Snack](tech-outfitter_2.md) |
| [Self Service](tech-outfitter_automation.md) |
| [New Hotness](tech-outfitter_skip_replace.md) |
| [No Waiting Around](tech-outfitter_timeout.md) |
| [Pantry](tech-pantry.md) |
| [Deep Cavern Storage](tech-pantry_unlock_channels.md) |
| [Patrol the Market](tech-patrol_market.md) |
| [Petrified Shield](tech-petrified_shield.md) |
| [Petrified Wood](tech-petrified_wood.md) |
| [Elixir of Poison Resistance](tech-poison_resist_potion.md) |
| [Pontiff's Ring](tech-pontiff_ring.md) |
| [Portal](tech-portal.md) |
| [Mana Superconductors](tech-portal_cost_reduce.md) |
| [Stable Wormhole](tech-portal_cost_reduce_2.md) |
| [Overflowing Portal](tech-portal_overflow.md) |
| [Multidimensional Transportation](tech-portal_unlock_channels.md) |
| [Simple Prayer](tech-prayer_1.md) |
| [Ritual Prayer](tech-prayer_2.md) |
| [Prayer Beads](tech-prayer_beads.md) |
| [Primal Cover](tech-primal_cover.md) |
| [Primal Leather](tech-primal_leather.md) |
| [Primal Mask](tech-primal_mask.md) |
| [Primal String](tech-primal_string.md) |
| [Dark Prophet's Hood](tech-prophet_hood.md) |
| [Dark Prophet's Robe](tech-prophet_robe.md) |
| [Purified Mago-tech](tech-purified_tech.md) |
| [Quest Board](tech-quest_board.md) |
| [Quest Receptionist](tech-quest_board_automation.md) |
| [Quest Board · second add-on slot](tech-quest_board_automation_2.md) |
| [Quest Board · third add-on slot](tech-quest_board_automation_3.md) |
| [Negotiator](tech-quest_board_coins.md) |
| [Explorer](tech-quest_board_quality.md) |
| [Autodidact](tech-quest_board_training.md) |
| [Reconstructed Nightmare](tech-reconstructed_nightmare.md) |
| [Recruit Adventurers](tech-recruit_adventurer.md) |
| [Recruit Conscripts](tech-recruit_conscript.md) |
| [Refiner](tech-refiner.md) |
| [Metamorphosis](tech-refiner_demon.md) |
| [Flesh Sculptor](tech-refiner_human.md) |
| [Mana Sculptor](tech-refiner_mana.md) |
| [Elixir of Regeneration](tech-regen_potion.md) |
| [Reinforced Wooden Shield](tech-reinforced_wooden_shield.md) |
| [Requisition Office](tech-requisition_office.md) |
| [Requisition Officer](tech-requisition_office_automation.md) |
| [Requisition Office · second add-on slot](tech-requisition_office_automation_2.md) |
| [Requisition Office · third add-on slot](tech-requisition_office_automation_3.md) |
| [Agent](tech-requisition_office_cashier.md) |
| [Contractual Obligations](tech-requisition_office_contract.md) |
| [Mass Requisition](tech-requisition_office_contract_2.md) |
| [Overseas Export](tech-requisition_office_contract_3.md) |
| [Extradimensional Export](tech-requisition_office_contract_4.md) |
| [Red Tape Specialist](tech-requisition_office_passive.md) |
| [Reroll Contract](tech-requisition_office_reroll.md) |
| [Restaurant](tech-restaurant.md) |
| [Tactical Waitstaff](tech-restaurant_automation.md) |
| [Restaurant · second add-on slot](tech-restaurant_automation_2.md) |
| [Restaurant · third add-on slot](tech-restaurant_automation_3.md) |
| [Big Tippers](tech-restaurant_big_tippers.md) |
| [Royal Assent](tech-restaurant_crowns.md) |
| [Ring of Protection](tech-ring_of_armor.md) |
| [Leaden Band](tech-ring_of_armor_2.md) |
| [Ring of Dexterity](tech-ring_of_dexterity.md) |
| [Serpentine Band](tech-ring_of_dexterity_2.md) |
| [Ring of Health](tech-ring_of_health.md) |
| [Undying Band](tech-ring_of_health_2.md) |
| [Ring of Magic](tech-ring_of_magic.md) |
| [Monsoon Band](tech-ring_of_magic_2.md) |
| [Ring of Strength](tech-ring_of_strength.md) |
| [Band of the Cyclops](tech-ring_of_strength_2.md) |
| [Ring of Wisdom](tech-ring_of_wisdom.md) |
| [Band of Tranquility](tech-ring_of_wisdom_2.md) |
| [Rough Leather](tech-rough_leather.md) |
| [Rough Leather Hat](tech-rough_leather_hat.md) |
| [Rough String](tech-rough_string.md) |
| [Rough Vest](tech-rough_vest.md) |
| [Simple Salad](tech-salad.md) |
| [Salamander Skewer](tech-salamander_skewer.md) |
| [Scribe](tech-scribe.md) |
| [Enchanted Quill](tech-scribe_automation.md) |
| [Scribe · second add-on slot](tech-scribe_automation_2.md) |
| [Scribe · third add-on slot](tech-scribe_automation_3.md) |
| [Scribe · overseers](tech-scribe_productivity.md) |
| [Scribe · artisans](tech-scribe_quality.md) |
| [Scroll of Radiance](tech-scroll_of_aoe_healing.md) |
| [Scroll of Disintegration](tech-scroll_of_damage.md) |
| [Scroll of Second Wind](tech-scroll_of_energy.md) |
| [Scroll of Healing](tech-scroll_of_healing.md) |
| [Elixir of Shadow Resistance](tech-shadow_resist_potion.md) |
| [Undead Shambler](tech-shambler.md) |
| [Puppet Shield](tech-shield_arm.md) |
| [Shield of the Innocent](tech-shield_innocent.md) |
| [Item Shop](tech-shop.md) |
| [Shop Attendant](tech-shop_automation.md) |
| [Item Shop · second add-on slot](tech-shop_automation_2.md) |
| [Item Shop · third add-on slot](tech-shop_automation_3.md) |
| [Cashier](tech-shop_cashier.md) |
| [Item Shop coffers](tech-shop_coffers.md) |
| [Future Proofing](tech-shop_expansion.md) |
| [Shrine](tech-shrine.md) |
| [Prayer Wheel](tech-shrine_automation.md) |
| [Shrine · second add-on slot](tech-shrine_automation_2.md) |
| [Shrine · third add-on slot](tech-shrine_automation_3.md) |
| [Shrine · overseers](tech-shrine_productivity.md) |
| [Shrine · artisans](tech-shrine_quality.md) |
| [Silver Ingot](tech-silver_ingot.md) |
| [Silver Thread](tech-silver_thread.md) |
| [Simple Burial](tech-simple_burial.md) |
| [Elegant Ring](tech-simple_ring.md) |
| [Simple Robe](tech-simple_robe.md) |
| [Simple Wooden Shield](tech-simple_wooden_shield.md) |
| [Button](tech-single_button.md) |
| [Skeletal Archer](tech-skeletal_archer.md) |
| [Skeletal Berserker](tech-skeletal_berserker.md) |
| [Skeletal Archmage](tech-skeletal_mage.md) |
| [Softwood Bow](tech-softwood_bow.md) |
| [Softwood Warstaff](tech-softwood_warstaff.md) |
| [Stalker Stew](tech-stalker_stew.md) |
| [State Funeral](tech-state_funeral.md) |
| [Medallion of Excellence](tech-stats_amulet.md) |
| [Elixir of Mastery](tech-stats_potion.md) |
| [Stockpile](tech-stockpile.md) |
| [Dimensional Storage](tech-stockpile_capacity.md) |
| [Overflowing Stockpile](tech-stockpile_overflow.md) |
| [Summon Arbiter](tech-summon_arbiter.md) |
| [Summon Cherub](tech-summon_cherub.md) |
| [Summon Gremlin](tech-summon_gremlin.md) |
| [Summon Hellspawn](tech-summon_hellspawn.md) |
| [Summon Watcher](tech-summon_observer.md) |
| [Summon Valkyrie](tech-summon_valkyrie.md) |
| [Summoning Circle](tech-summoning_circle.md) |
| [Mad Hermit](tech-summoning_circle_automation.md) |
| [Summoning Circle · second add-on slot](tech-summoning_circle_automation_2.md) |
| [Summoning Circle · third add-on slot](tech-summoning_circle_automation_3.md) |
| [Summoning Circle · overseers](tech-summoning_circle_productivity.md) |
| [Summoning Circle · artisans](tech-summoning_circle_quality.md) |
| [Supple String](tech-supple_string.md) |
| [Supply Depot](tech-supply_depot.md) |
| [Crate Carriers](tech-supply_depot_automation.md) |
| [Supply Depot · second add-on slot](tech-supply_depot_automation_2.md) |
| [Supply Depot · third add-on slot](tech-supply_depot_automation_3.md) |
| [Supply Depot · overseers](tech-supply_depot_productivity.md) |
| [Supply Depot · artisans](tech-supply_depot_quality.md) |
| [Revitalizing Potion](tech-supply_energy_potion.md) |
| [Elixir of Fire Resistance](tech-supply_fire_resist_potion.md) |
| [Healing Potion](tech-supply_healing_potion.md) |
| [Supply Linen Cloth](tech-supply_linen_cloth.md) |
| [Rations](tech-supply_rations.md) |
| [Supply Rough Leather](tech-supply_rough_leather.md) |
| [Elixir of Shadow Resistance](tech-supply_shadow_resist_potion.md) |
| [Supply Wood Plank](tech-supply_wood_plank.md) |
| [Elixir of Alacrity](tech-swiftness_potion.md) |
| [Sinister Prodigy](tech-symbiote_breeding.md) |
| [Tailor](tech-tailor.md) |
| [Animated Scissors](tech-tailor_automation.md) |
| [Tailor · second add-on slot](tech-tailor_automation_2.md) |
| [Tailor · third add-on slot](tech-tailor_automation_3.md) |
| [Tailor · overseers](tech-tailor_productivity.md) |
| [Tailor · artisans](tech-tailor_quality.md) |
| [Decorations](tech-tech_deco.md) |
| [Timer](tech-timer_node.md) |
| [Tinker](tech-tinker.md) |
| [Tinkersteel](tech-tinkersteel.md) |
| [Tinkersteel Armor](tech-tinkersteel_armor.md) |
| [Tinkersteel Battleaxe](tech-tinkersteel_axe.md) |
| [Tinkersteel Dagger](tech-tinkersteel_dagger.md) |
| [Tinkersteel Greatsword](tech-tinkersteel_greatsword.md) |
| [Tinkersteel Helm](tech-tinkersteel_helm.md) |
| [Tinkersteel Rapier](tech-tinkersteel_rapier.md) |
| [Tinkersteel Sword](tech-tinkersteel_sword.md) |
| [Libram of Awakening](tech-tome_of_energy.md) |
| [Apothecary's Tome](tech-tome_of_health.md) |
| [Manual of Self-Improvement](tech-tome_of_stats.md) |
| [Switch](tech-track_switch.md) |
| [Track Switch](tech-track_switch_2.md) |
| [Training Grounds](tech-training_grounds.md) |
| [Drill Sergeant](tech-training_grounds_automation.md) |
| [Training Grounds · second add-on slot](tech-training_grounds_automation_2.md) |
| [Training Dummy](tech-training_grounds_dummy.md) |
| [Workout Snack](tech-training_grounds_food.md) |
| [Training Grounds · artisans](tech-training_grounds_quality.md) |
| [Group Exercise](tech-training_grounds_slot.md) |
| [Portal to Swolevania](tech-training_grounds_slot_2.md) |
| [Specialized Training](tech-training_grounds_spec.md) |
| [Training Sword](tech-training_sword.md) |
| [Transmute Metals](tech-transmute_metals.md) |
| [Treasury](tech-treasury.md) |
| [Triune Protector](tech-triune_shield.md) |
| [Trueshot Bow](tech-trueshot_bow.md) |
| [Turtle Statue](tech-turtle_statue.md) |
| [Cyclopean Battleaxe](tech-unblinking_axe.md) |
| [Unlife Staff](tech-unlife_staff.md) |
| [Area Move](tech-unlock_area_move.md) |
| [Node Duplication](tech-unlock_picker.md) |
| [Supply Network](tech-unlock_supply_window.md) |
| [Vanquisher's Sword](tech-vanquisher_sword.md) |
| [War Effort](tech-war_effort.md) |
| [War: Eastern Front](tech-war_effort_east.md) |
| [Southside Brigands](tech-war_effort_forest.md) |
| [War: Ironcrag Siege](tech-war_effort_north.md) |
| [Participation Trophy](tech-war_effort_passive.md) |
| [War: Hidden Enemies](tech-war_effort_yensburg.md) |
| [Widget](tech-widget.md) |
| [Staff of the Wild](tech-wild_staff.md) |
| [Winged Boots](tech-winged_boots.md) |
| [Witch Hood](tech-witch_hood.md) |
| [Witch Robe](tech-witch_robe.md) |
| [Witchcloth](tech-witchcloth.md) |
| [Softwood Plank](tech-wood_plank.md) |
| [Technology cost formula](technology-costs.md) |
| [Technology requirements and unlocking](technology-rules.md) |
| [Technology tier 1: Foundations](technology-tier-1.md) |
| [Technology tier 10: Invention and writing](technology-tier-10.md) |
| [Technology tier 11: Faith, undead, and endgame](technology-tier-11.md) |
| [Technology tier 2: Requisitions and crafts](technology-tier-2.md) |
| [Technology tier 3: Recruiting and war](technology-tier-3.md) |
| [Technology tier 4: Forest production](technology-tier-4.md) |
| [Technology tier 5: Adventurers and quests](technology-tier-5.md) |
| [Technology tier 6: Recovery and magic](technology-tier-6.md) |
| [Technology tier 7: Farming and dining](technology-tier-7.md) |
| [Technology tier 8: Dungeons and jewelry](technology-tier-8.md) |
| [Technology tier 9: Alchemy and arena](technology-tier-9.md) |

## Sources

- `Assets.Source.Player/TechNode.cs:1`
