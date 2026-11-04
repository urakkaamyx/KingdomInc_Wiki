# CraftingRecipe — source reference

Assets.Source.Items/CraftingRecipe.cs · 373 lines · 230 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 14 | public class CraftingRecipe |
| 20 | public readonly string Identifier |
| 22 | public string DisplayName |
| 24 | public string Description |
| 26 | public string IconName |
| 28 | public RecipeTag Tag |
| 30 | public CraftingReagent[] Reagents |
| 32 | public CraftingResult[] Results |
| 34 | public CurrencyCollection CraftingCost |
| 36 | public CurrencyCollection CraftingReward |
| 38 | public bool CostIncreasesValue = true |
| 40 | public double ValueMultiplier |
| 42 | public float BaseProductivity |
| 44 | public float CraftingTime |
| 46 | public float CraftingTimeMultiplier = 1f |
| 54 | public Action<CraftingInput> OnFinished |
| 56 | public static IReadOnlyList<CraftingRecipe> All => _orderedRecipes |
| 58 | public TechNode RequiredTech |
| 70 | public bool IsAvailable => GamePlayer.Current.HasTech(RequiredTech) |
| 72 | public long BaseValue |
| 101 | public int ReagentCount |
| 114 | public ItemType PreviewResultItem |
| 154 | public CraftingRecipe(string id) |
| 161 | public int GetReagentCount(ItemType item) |
| 174 | public int GetResultCount(ItemType item) |
| 187 | public int GetResultCount(ItemEnhancement enh) |
| 200 | public Dictionary<CraftingResult, float> GetProbabilisticResults() |
| 217 | public static void Add(CraftingRecipe cr) |
| 235 | public static CraftingRecipe Get(string id) |
| 240 | public void AddToTooltip(UITooltip tooltip, RecipeElement element) |
| 260 | public void AddResultsToTooltip(UITooltip tooltip, RecipeElement element) |
| 369 | public static implicit operator CraftingRecipe(string id) |

## Documented by

| Wiki article |
| --- |
| [Crafting, recipes, and automatic work](production-crafting.md) |
| [Crafting workshops and their roles](production-workshops.md) |
| [Alchemical Experimentation recipe](recipe-alchemical_experiment.md) |
| [Amulet of Vigor recipe](recipe-amulet_of_energy.md) |
| [Amulet of Fire Protection recipe](recipe-amulet_of_fire_prot.md) |
| [Amulet of Vitality recipe](recipe-amulet_of_healing.md) |
| [Panacea Amulet recipe](recipe-amulet_of_poison_prot.md) |
| [Amulet of Dark Tidings recipe](recipe-amulet_of_shadow_prot.md) |
| [Crystalline Staff recipe](recipe-ancient_int_staff.md) |
| [Bulwark of Ancients recipe](recipe-ancient_shield.md) |
| [Staff of Sages recipe](recipe-ancient_wis_staff.md) |
| [Ancient Wood Longbow recipe](recipe-ancient_wood_bow.md) |
| [Ancient Wood Plank recipe](recipe-ancient_wood_plank.md) |
| [Ancient Wood Staff recipe](recipe-ancient_wood_staff.md) |
| [Ancient Woodcutter recipe](recipe-ancient_woodcutter.md) |
| [Annihilate Gemstone recipe](recipe-annihilate_gemstone.md) |
| [Arcanite Chestguard recipe](recipe-arcanium_armor.md) |
| [Arcanite Cleaver recipe](recipe-arcanium_battleaxe.md) |
| [Arcanite Backstabber recipe](recipe-arcanium_dagger.md) |
| [Arcanite Claymore recipe](recipe-arcanium_greatsword.md) |
| [Arcanite Casque recipe](recipe-arcanium_helm.md) |
| [Arcanite Ingot recipe](recipe-arcanium_ingot.md) |
| [Arcanite Blade recipe](recipe-arcanium_sword.md) |
| [Archbishop's Staff recipe](recipe-archbishop_staff.md) |
| [Archmage's Hat recipe](recipe-archmage_hat.md) |
| [Archmage's Robe recipe](recipe-archmage_robe.md) |
| [Archmage's Staff recipe](recipe-archmage_staff.md) |
| [Stoneskin Elixir recipe](recipe-armor_potion.md) |
| [Attuned Catalyst recipe](recipe-attuned_catalyst.md) |
| [Biological Experimentation recipe](recipe-biological_experiment.md) |
| [Blank Tome recipe](recipe-blank_tome.md) |
| [Blank Vellum recipe](recipe-blank_vellum.md) |
| [Blessed Armaments recipe](recipe-blessed_arms.md) |
| [Sanctified Equipment recipe](recipe-blessed_equipment.md) |
| [Blessed Prayer Beads recipe](recipe-blessed_prayer_beads.md) |
| [Blighted Dagger recipe](recipe-blighted_dagger.md) |
| [Ethereal Rapier recipe](recipe-blink_rapier.md) |
| [Seared Boar Steak recipe](recipe-boar_steak.md) |
| [Butcher Cattle recipe](recipe-butcher_cattle.md) |
| [Butcher Salamander recipe](recipe-butcher_salamander.md) |
| [Butcher Stalker recipe](recipe-butcher_stalker.md) |
| [Chainsaw recipe](recipe-chainsaw.md) |
| [Cleansed Nightmare recipe](recipe-cleansed_nightmare.md) |
| [Coffin recipe](recipe-coffin.md) |
| [Hardboiled Egg recipe](recipe-cooked_egg.md) |
| [Cotton Cloth recipe](recipe-cotton_cloth.md) |
| [Scholar's Hat recipe](recipe-cotton_hat.md) |
| [Scholar's Robe recipe](recipe-cotton_robe.md) |
| [Anatomy Lesson recipe](recipe-cr_assassin.md) |
| [Feeding the Wildlife recipe](recipe-cr_beast_master.md) |
| [Demonic Initiation recipe](recipe-cr_demonologist.md) |
| [Preaching to the Choir recipe](recipe-cr_evangelist.md) |
| [Prayer of Light recipe](recipe-cr_lightbringer.md) |
| [Rock Carving for Dummies recipe](recipe-cr_lithomancer.md) |
| [Introduction to Necromancy recipe](recipe-cr_necrolyte.md) |
| [Guardian's Pledge recipe](recipe-cr_paladin.md) |
| [Pyromancy and You: An Introduction recipe](recipe-cr_pyromancer.md) |
| [Commune with Nature recipe](recipe-cr_shaman.md) |
| [Study on Phytotoxins recipe](recipe-cr_survivalist.md) |
| [Assassin's Goggles recipe](recipe-crit_goggles.md) |
| [Crystalized Mana recipe](recipe-crystal_mana.md) |
| [Deadeye Bow recipe](recipe-deadeye_bow.md) |
| [Decoded Writings recipe](recipe-decoded_writings.md) |
| [Demonsteel Armor recipe](recipe-demonsteel_armor.md) |
| [Demonsteel Helm recipe](recipe-demonsteel_helm.md) |
| [Doodad recipe](recipe-doodad.md) |
| [Embossed Mask recipe](recipe-embossed_hat.md) |
| [Embossed Leather recipe](recipe-embossed_leather.md) |
| [Embossed Vest recipe](recipe-embossed_vest.md) |
| [Embroidered Cotton recipe](recipe-embroidered_cotton.md) |
| [Enchant Armor - Protection recipe](recipe-enchant_armor_armor.md) |
| [Enchant Armor: Vigor recipe](recipe-enchant_armor_energy.md) |
| [Enchant Shield - Shadow Ward recipe](recipe-enchant_armor_shadow_resist.md) |
| [Enchant Armor: Stats recipe](recipe-enchant_armor_stats.md) |
| [Enchant Armor - Giant Strength recipe](recipe-enchant_armor_strength_skill_crit.md) |
| [Enchant Food: Deliciousness recipe](recipe-enchant_food_quality.md) |
| [Imbue Dark Essence recipe](recipe-enchant_item_quality.md) |
| [Enchant Shield - Protection recipe](recipe-enchant_shield_armor.md) |
| [Enchant Weapon - Critical Hit recipe](recipe-enchant_weapon_crit.md) |
| [Enchant Weapon: Power recipe](recipe-enchant_weapon_power.md) |
| [Enchanted Thread recipe](recipe-enchanted_cotton_thread.md) |
| [Enchanted Ink recipe](recipe-enchanted_ink.md) |
| [Revitalizing Potion recipe](recipe-energy_potion.md) |
| [Engrave Heavy Armor: Defense recipe](recipe-engrave_heavy_armor_armor.md) |
| [Engrave Heavy Armor: Health recipe](recipe-engrave_heavy_armor_health.md) |
| [Engraved Jewelry recipe](recipe-engrave_jewelry_quality.md) |
| [Embroider Clothing: Defense recipe](recipe-engrave_light_armor_armor.md) |
| [Embroider Clothing: Dexterity recipe](recipe-engrave_light_armor_dex.md) |
| [Embroider Clothing: Health recipe](recipe-engrave_light_armor_health.md) |
| [Embroider Clothing: Magic recipe](recipe-engrave_light_armor_mag.md) |
| [Embroider Clothing: Wisdom recipe](recipe-engrave_light_armor_wis.md) |
| [Engrave Weapon: Dexterity recipe](recipe-engrave_weapon_dex.md) |
| [Engrave Weapon: Magic recipe](recipe-engrave_weapon_mag.md) |
| [Engrave Weapon: Strength recipe](recipe-engrave_weapon_str.md) |
| [Engrave Weapon: Wisdom recipe](recipe-engrave_weapon_wis.md) |
| [Elixir of Fire Resistance recipe](recipe-fire_resist_potion.md) |
| [Necklace of Fireballs recipe](recipe-fireball_amulet.md) |
| [Flenser's Sword recipe](recipe-flenser_greatsword.md) |
| [Splintered Staff recipe](recipe-fragment_staff.md) |
| [Empty Setting recipe](recipe-gem_setting.md) |
| [Gilded Coffin recipe](recipe-gilded_coffin.md) |
| [Gizmo recipe](recipe-gizmo.md) |
| [Parade Armor recipe](recipe-gold_armor.md) |
| [Sapphire Crown recipe](recipe-gold_crown.md) |
| [Gold Ingot recipe](recipe-gold_ingot.md) |
| [Ceremonial Sword recipe](recipe-gold_sword.md) |
| [Gold Wire recipe](recipe-gold_wire.md) |
| [Golem Gauntlets recipe](recipe-golem_gauntlets.md) |
| [Greater Healing Potion recipe](recipe-greater_healing_potion.md) |
| [Hamburger recipe](recipe-hamburger.md) |
| [Healing Potion recipe](recipe-healing_potion.md) |
| [Malignant Cover recipe](recipe-hellish_cover.md) |
| [Malignant Mask recipe](recipe-hellish_mask.md) |
| [Hulking Monstrosity recipe](recipe-hulking_monstrosity.md) |
| [Identify Gemstones recipe](recipe-identify_gem.md) |
| [Identify Plants recipe](recipe-identify_plants.md) |
| [Indulgence recipe](recipe-indulgence.md) |
| [Possessed Shield recipe](recipe-infected_shield.md) |
| [Initiate's Hat recipe](recipe-initiate_hat.md) |
| [Initiate's Staff recipe](recipe-initiate_staff.md) |
| [Iron Armor recipe](recipe-iron_armor.md) |
| [Iron Battleaxe recipe](recipe-iron_battleaxe.md) |
| [Iron Dagger recipe](recipe-iron_dagger.md) |
| [Iron Greatsword recipe](recipe-iron_greatsword.md) |
| [Iron Helm recipe](recipe-iron_helm.md) |
| [Iron Ingot recipe](recipe-iron_ingot.md) |
| [Iron Rapier recipe](recipe-iron_rapier.md) |
| [Iron Sword recipe](recipe-iron_sword.md) |
| [Lifebloom Amulet recipe](recipe-lifebloom_amulet.md) |
| [Linen Cloth recipe](recipe-linen_cloth.md) |
| [Linen Padding recipe](recipe-linen_padding.md) |
| [Mad Scribblings recipe](recipe-mad_scribblings.md) |
| [Relic of the Martyr recipe](recipe-martyr_relic.md) |
| [Mechanical Experimentation recipe](recipe-mechanical_experiment.md) |
| [Leyline Goggles recipe](recipe-mind_goggles.md) |
| [Mushroom Stew recipe](recipe-mushroom_stew.md) |
| [Nightmare Casing recipe](recipe-nightmare_casing.md) |
| [Nightmare Collector recipe](recipe-nightmare_collector.md) |
| [Officiated Burial recipe](recipe-officiated_burial.md) |
| [Petrified Shield recipe](recipe-petrified_shield.md) |
| [Petrified Wood recipe](recipe-petrified_wood.md) |
| [Elixir of Poison Resistance recipe](recipe-poison_resist_potion.md) |
| [Pontiff's Ring recipe](recipe-pontiff_ring.md) |
| [Simple Prayer recipe](recipe-prayer_1.md) |
| [Ritual Prayer recipe](recipe-prayer_2.md) |
| [Prayer Beads recipe](recipe-prayer_beads.md) |
| [Primal Cover recipe](recipe-primal_cover.md) |
| [Primal Leather recipe](recipe-primal_leather.md) |
| [Primal Mask recipe](recipe-primal_mask.md) |
| [Primal String recipe](recipe-primal_string.md) |
| [Dark Prophet's Hood recipe](recipe-prophet_hood.md) |
| [Dark Prophet's Robe recipe](recipe-prophet_robe.md) |
| [Purified Mago-tech recipe](recipe-purified_tech.md) |
| [Reconstructed Nightmare recipe](recipe-reconstructed_nightmare.md) |
| [Elixir of Regeneration recipe](recipe-regen_potion.md) |
| [Reinforced Wooden Shield recipe](recipe-reinforced_wooden_shield.md) |
| [Ring of Protection recipe](recipe-ring_of_armor.md) |
| [Leaden Band recipe](recipe-ring_of_armor_2.md) |
| [Ring of Dexterity recipe](recipe-ring_of_dexterity.md) |
| [Serpentine Band recipe](recipe-ring_of_dexterity_2.md) |
| [Ring of Health recipe](recipe-ring_of_health.md) |
| [Undying Band recipe](recipe-ring_of_health_2.md) |
| [Ring of Magic recipe](recipe-ring_of_magic.md) |
| [Monsoon Band recipe](recipe-ring_of_magic_2.md) |
| [Ring of Strength recipe](recipe-ring_of_strength.md) |
| [Band of the Cyclops recipe](recipe-ring_of_strength_2.md) |
| [Ring of Wisdom recipe](recipe-ring_of_wisdom.md) |
| [Band of Tranquility recipe](recipe-ring_of_wisdom_2.md) |
| [Rough Leather recipe](recipe-rough_leather.md) |
| [Rough Leather Hat recipe](recipe-rough_leather_hat.md) |
| [Rough String recipe](recipe-rough_string.md) |
| [Rough Vest recipe](recipe-rough_vest.md) |
| [Simple Salad recipe](recipe-salad.md) |
| [Salamander Skewer recipe](recipe-salamander_skewer.md) |
| [Scroll of Radiance recipe](recipe-scroll_of_aoe_healing.md) |
| [Scroll of Disintegration recipe](recipe-scroll_of_damage.md) |
| [Scroll of Second Wind recipe](recipe-scroll_of_energy.md) |
| [Scroll of Healing recipe](recipe-scroll_of_healing.md) |
| [Elixir of Shadow Resistance recipe](recipe-shadow_resist_potion.md) |
| [Undead Shambler recipe](recipe-shambler.md) |
| [Puppet Shield recipe](recipe-shield_arm.md) |
| [Silver Ingot recipe](recipe-silver_ingot.md) |
| [Silver Thread recipe](recipe-silver_thread.md) |
| [Simple Burial recipe](recipe-simple_burial.md) |
| [Elegant Ring recipe](recipe-simple_ring.md) |
| [Simple Robe recipe](recipe-simple_robe.md) |
| [Simple Wooden Shield recipe](recipe-simple_wooden_shield.md) |
| [Skeletal Archer recipe](recipe-skeletal_archer.md) |
| [Skeletal Berserker recipe](recipe-skeletal_berserker.md) |
| [Skeletal Archmage recipe](recipe-skeletal_mage.md) |
| [Softwood Bow recipe](recipe-softwood_bow.md) |
| [Softwood Warstaff recipe](recipe-softwood_warstaff.md) |
| [Stalker Stew recipe](recipe-stalker_stew.md) |
| [State Funeral recipe](recipe-state_funeral.md) |
| [Medallion of Excellence recipe](recipe-stats_amulet.md) |
| [Elixir of Mastery recipe](recipe-stats_potion.md) |
| [Summon Arbiter recipe](recipe-summon_arbiter.md) |
| [Summon Cherub recipe](recipe-summon_cherub.md) |
| [Summon Gremlin recipe](recipe-summon_gremlin.md) |
| [Summon Hellspawn recipe](recipe-summon_hellspawn.md) |
| [Summon Watcher recipe](recipe-summon_observer.md) |
| [Summon Valkyrie recipe](recipe-summon_valkyrie.md) |
| [Supple String recipe](recipe-supple_string.md) |
| [Elixir of Alacrity recipe](recipe-swiftness_potion.md) |
| [Sinister Prodigy recipe](recipe-symbiote_breeding.md) |
| [Tinker recipe](recipe-tinker.md) |
| [Tinkersteel recipe](recipe-tinkersteel.md) |
| [Tinkersteel Armor recipe](recipe-tinkersteel_armor.md) |
| [Tinkersteel Battleaxe recipe](recipe-tinkersteel_axe.md) |
| [Tinkersteel Dagger recipe](recipe-tinkersteel_dagger.md) |
| [Tinkersteel Greatsword recipe](recipe-tinkersteel_greatsword.md) |
| [Tinkersteel Helm recipe](recipe-tinkersteel_helm.md) |
| [Tinkersteel Rapier recipe](recipe-tinkersteel_rapier.md) |
| [Tinkersteel Sword recipe](recipe-tinkersteel_sword.md) |
| [Libram of Awakening recipe](recipe-tome_of_energy.md) |
| [Apothecary's Tome recipe](recipe-tome_of_health.md) |
| [Manual of Self-Improvement recipe](recipe-tome_of_stats.md) |
| [Transmute Metals recipe](recipe-transmute_metals.md) |
| [Triune Protector recipe](recipe-triune_shield.md) |
| [Trueshot Bow recipe](recipe-trueshot_bow.md) |
| [Cyclopean Battleaxe recipe](recipe-unblinking_axe.md) |
| [Unlife Staff recipe](recipe-unlife_staff.md) |
| [Vanquisher's Sword recipe](recipe-vanquisher_sword.md) |
| [Widget recipe](recipe-widget.md) |
| [Staff of the Wild recipe](recipe-wild_staff.md) |
| [Winged Boots recipe](recipe-winged_boots.md) |
| [Witch Hood recipe](recipe-witch_hood.md) |
| [Witch Robe recipe](recipe-witch_robe.md) |
| [Witchcloth recipe](recipe-witchcloth.md) |
| [Softwood Plank recipe](recipe-wood_plank.md) |

## Sources

- `Assets.Source.Items/CraftingRecipe.cs:1`
