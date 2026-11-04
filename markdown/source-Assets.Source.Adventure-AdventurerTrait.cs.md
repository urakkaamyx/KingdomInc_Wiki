# AdventurerTrait — source reference

Assets.Source.Adventure/AdventurerTrait.cs · 673 lines · 58 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class AdventurerTrait |
| 12 | public delegate float TraitModifyStat(ActiveTrait trait, EquipStat stat, float currentValue) |
| 14 | public delegate float TraitModifyValue(ActiveTrait trait, float currentValue, object context) |
| 16 | public delegate void TraitModifyWar(ActiveTrait trait, WarProgress progress) |
| 18 | public delegate void TraitModifyQuest(ActiveTrait trait, QuestProgress progress) |
| 20 | public delegate void TraitModifyArena(ActiveTrait trait, Arena arena) |
| 22 | public delegate void TraitModifyDungeon(ActiveTrait trait, DungeonProgress progress) |
| 24 | public delegate void TraitModifyAlly(ActiveTrait trait, CombatantItemData ally, object context) |
| 26 | public delegate string TraitGetDescription(ActiveTrait trait) |
| 28 | public string DisplayName |
| 30 | public string IconName |
| 32 | public string CompanionSprite |
| 34 | public TraitGetDescription GetDescription |
| 36 | public TraitModifyStat CalcStat |
| 38 | public TraitModifyStat CalcSkillTest |
| 40 | public TraitModifyValue CalcDamageDone |
| 42 | public TraitModifyValue CalcDamageTaken |
| 44 | public TraitModifyValue CalcHealingDone |
| 46 | public TraitModifyValue CalcHealingTaken |
| 48 | public TraitModifyValue CalcEnergyLoss |
| 50 | public TraitModifyValue CalcTraining |
| 52 | public TraitModifyWar WarTick |
| 54 | public TraitModifyQuest QuestTick |
| 56 | public TraitModifyArena ArenaTick |
| 58 | public TraitModifyDungeon DungeonCombatTick |
| 60 | public TraitModifyDungeon DungeonHealingTick |
| 62 | public TraitModifyAlly ApplyGroupBuffs |
| 64 | public static AdventurerTrait Healer = new AdventurerTrait |
| 71 | public static AdventurerTrait MinorHealer = new AdventurerTrait |
| 94 | public static AdventurerTrait Tank = new AdventurerTrait |
| 102 | public static AdventurerTrait ArchetypeFighter = new AdventurerTrait |
| 109 | public static AdventurerTrait ArchetypeRogue = new AdventurerTrait |
| 116 | public static AdventurerTrait ArchetypeMage = new AdventurerTrait |
| 123 | public static AdventurerTrait ArchetypeCleric = new AdventurerTrait |
| 130 | public static AdventurerTrait ClassGuardian = new AdventurerTrait |
| 138 | public static AdventurerTrait ClassBattlemaster = new AdventurerTrait |
| 146 | public static AdventurerTrait ClassThief = new AdventurerTrait |
| 154 | public static AdventurerTrait ClassRanger = new AdventurerTrait |
| 162 | public static AdventurerTrait ClassElementalist = new AdventurerTrait |
| 178 | public static AdventurerTrait ClassWarlock = new AdventurerTrait |
| 189 | public static AdventurerTrait ClassRitualist = new AdventurerTrait |
| 197 | public static AdventurerTrait ClassPriest = new AdventurerTrait |
| 205 | public static AdventurerTrait ClassPaladin = new AdventurerTrait |
| 220 | public static AdventurerTrait ClassBulwark = new AdventurerTrait |
| 239 | public static AdventurerTrait ClassBerserker = new AdventurerTrait |
| 247 | public static AdventurerTrait ClassReaver = new AdventurerTrait |
| 255 | public static AdventurerTrait ClassAssassin = new AdventurerTrait |
| 269 | public static AdventurerTrait ClassAssassinBuff = new AdventurerTrait |
| 277 | public static AdventurerTrait ClassSwashbuckler = new AdventurerTrait |
| 291 | public static AdventurerTrait ClassSwashbucklerBuff = new AdventurerTrait |
| 299 | public static AdventurerTrait ClassBeastMaster = new AdventurerTrait |
| 308 | public static AdventurerTrait ClassSurvivalist = new AdventurerTrait |
| 319 | public static AdventurerTrait ClassPyromancer = new AdventurerTrait |
| 330 | public static AdventurerTrait ClassLithomancer = new AdventurerTrait |
| 341 | public static AdventurerTrait ClassLithomancerBuff = new AdventurerTrait |
| 349 | public static AdventurerTrait ClassNecrolyte = new AdventurerTrait |
| 358 | public static AdventurerTrait ClassDemonologist = new AdventurerTrait |
| 367 | public static AdventurerTrait ClassShaman = new AdventurerTrait |
| 376 | public static AdventurerTrait ClassInquisitor = new AdventurerTrait |
| 384 | public static AdventurerTrait ClassEvangelist = new AdventurerTrait |
| 402 | public static AdventurerTrait ClassLightbringer = new AdventurerTrait |
| 416 | public static AdventurerTrait ClassLightbringerBuff = new AdventurerTrait |
| 428 | public static AdventurerTrait HealingPotion = new AdventurerTrait |
| 451 | public static AdventurerTrait HealingPotion2 = new AdventurerTrait |
| 476 | public static AdventurerTrait EnergyPotion = new AdventurerTrait |
| 499 | public static AdventurerTrait TrainingFood = new AdventurerTrait |
| 507 | public static AdventurerTrait FireResist = new AdventurerTrait |
| 514 | public static AdventurerTrait ShadowResist = new AdventurerTrait |
| 521 | public static AdventurerTrait PoisonResist = new AdventurerTrait |
| 528 | public static AdventurerTrait CriticalHit = new AdventurerTrait |
| 536 | public static AdventurerTrait StrengthSkillCrit = new AdventurerTrait |
| 544 | public static AdventurerTrait DexteritySkillCrit = new AdventurerTrait |
| 552 | public static AdventurerTrait MagicSkillCrit = new AdventurerTrait |
| 560 | public static AdventurerTrait WisdomSkillCrit = new AdventurerTrait |
| 568 | public static AdventurerTrait DivineProtectionAura = new AdventurerTrait |
| 579 | public static AdventurerTrait DivineProtection = new AdventurerTrait |
| 587 | public static AdventurerTrait DivineProtection2 = new AdventurerTrait |
| 595 | public static AdventurerTrait InjectPoison = new AdventurerTrait |
| 606 | public string Description { private get; set; } |
| 608 | public Sprite Icon => SpriteLibrary.Get(IconName) |
| 610 | public AdventurerTrait() |
| 664 | public static float Resist(float quality) |
| 669 | public static float Resist(ActiveTrait? trait) |

## Documented by

| Wiki article |
| --- |
| [Armor and damage reduction](armor-and-damage.md) |
| [Class trait effects](class-trait-reference.md) |
| [Combat stats and power](combat-stats.md) |
| [Dungeon challenge reference](dungeon-hazard-reference.md) |
| [Skill tests and elemental resistances](skill-tests-and-resistances.md) |
| [Adventure potions, auras, scrolls, and rescue effects](special-adventure-equipment.md) |
| [Tanks, healers, and party formation](tank-and-healer.md) |
| [Cleric](trait-ArchetypeCleric.md) |
| [Fighter](trait-ArchetypeFighter.md) |
| [Mage](trait-ArchetypeMage.md) |
| [Rogue](trait-ArchetypeRogue.md) |
| [Assassin](trait-ClassAssassin.md) |
| [Assassin](trait-ClassAssassinBuff.md) |
| [Battlemaster](trait-ClassBattlemaster.md) |
| [Beast Master](trait-ClassBeastMaster.md) |
| [Berserker](trait-ClassBerserker.md) |
| [Bulwark](trait-ClassBulwark.md) |
| [Demonologist](trait-ClassDemonologist.md) |
| [Elementalist](trait-ClassElementalist.md) |
| [Evangelist](trait-ClassEvangelist.md) |
| [Guardian](trait-ClassGuardian.md) |
| [Inquisitor](trait-ClassInquisitor.md) |
| [Lightbringer](trait-ClassLightbringer.md) |
| [Lightbringer](trait-ClassLightbringerBuff.md) |
| [Lithomancer](trait-ClassLithomancer.md) |
| [Lithomancer](trait-ClassLithomancerBuff.md) |
| [Necrolyte](trait-ClassNecrolyte.md) |
| [Paladin](trait-ClassPaladin.md) |
| [Priest](trait-ClassPriest.md) |
| [Pyromancer](trait-ClassPyromancer.md) |
| [Ranger](trait-ClassRanger.md) |
| [Reaver](trait-ClassReaver.md) |
| [Ritualist](trait-ClassRitualist.md) |
| [Shaman](trait-ClassShaman.md) |
| [Survivalist](trait-ClassSurvivalist.md) |
| [Swashbuckler](trait-ClassSwashbuckler.md) |
| [Swashbuckler](trait-ClassSwashbucklerBuff.md) |
| [Thief](trait-ClassThief.md) |
| [Warlock](trait-ClassWarlock.md) |
| [Critical Hit](trait-CriticalHit.md) |
| [Alacrity](trait-DexteritySkillCrit.md) |
| [Divine Protection](trait-DivineProtection.md) |
| [Divine Protection](trait-DivineProtection2.md) |
| [Pontiff's Ring](trait-DivineProtectionAura.md) |
| [Revitalizing Potion](trait-EnergyPotion.md) |
| [Fire Resistance](trait-FireResist.md) |
| [Healer](trait-Healer.md) |
| [Healing Potion](trait-HealingPotion.md) |
| [Greater Healing Potion](trait-HealingPotion2.md) |
| [Venom Injector](trait-InjectPoison.md) |
| [Detect Magic](trait-MagicSkillCrit.md) |
| [Minor Healing](trait-MinorHealer.md) |
| [Poison Resistance](trait-PoisonResist.md) |
| [Shadow Resistance](trait-ShadowResist.md) |
| [Giant Strength](trait-StrengthSkillCrit.md) |
| [Tank](trait-Tank.md) |
| [Rations](trait-TrainingFood.md) |
| [Intuition](trait-WisdomSkillCrit.md) |

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:1`
