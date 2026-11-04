# QuestChallenge — source reference

Assets.Source.Adventure/QuestChallenge.cs · 728 lines · 40 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class QuestChallenge |
| 13 | public delegate float QuestChallengeCalc(QuestProgress qp, HumanItemData adv, float current) |
| 15 | public string IconName |
| 17 | public string Label |
| 19 | public string Description |
| 21 | public bool Triggered |
| 23 | public float TriggerChance = 0.05f |
| 25 | public Action<QuestProgress> ExecuteQuest |
| 27 | public Action<DungeonProgress> ExecuteDungeon |
| 29 | public QuestChallengeCalc CalcDifficulty |
| 31 | public static readonly QuestChallenge Dangerous = new QuestChallenge |
| 48 | public static readonly QuestChallenge Exhausting = new QuestChallenge |
| 71 | public static readonly QuestChallenge DexEnergy = new QuestChallenge |
| 89 | public static readonly QuestChallenge IncreaseDuration = new QuestChallenge |
| 96 | public static readonly QuestChallenge FighterSpec = new QuestChallenge |
| 104 | public static readonly QuestChallenge RogueSpec = new QuestChallenge |
| 112 | public static readonly QuestChallenge MageSpec = new QuestChallenge |
| 120 | public static readonly QuestChallenge ClericSpec = new QuestChallenge |
| 128 | public static readonly QuestChallenge TankFireDamage = new QuestChallenge |
| 145 | public static readonly QuestChallenge TankShadowDamage = new QuestChallenge |
| 162 | public static readonly QuestChallenge AcidRain = new QuestChallenge |
| 180 | public static readonly QuestChallenge ClearRubble = new QuestChallenge |
| 205 | public static readonly QuestChallenge ArcaneTraps = new QuestChallenge |
| 228 | public static readonly QuestChallenge ReapingStrike = new QuestChallenge |
| 243 | public static readonly QuestChallenge SoulReave = new QuestChallenge |
| 266 | public static readonly QuestChallenge Caltrops = new QuestChallenge |
| 286 | public static readonly QuestChallenge FlailingStrike = new QuestChallenge |
| 301 | public static readonly QuestChallenge RecklessCharge = new QuestChallenge |
| 324 | public static readonly QuestChallenge ScatterBeam = new QuestChallenge |
| 344 | public static readonly QuestChallenge DilutePoison = new QuestChallenge |
| 365 | public static readonly QuestChallenge MajorPoison = new QuestChallenge |
| 385 | public static readonly QuestChallenge ChillingHowl = new QuestChallenge |
| 410 | public static readonly QuestChallenge Tremors = new QuestChallenge |
| 430 | public static readonly QuestChallenge InjectPoison = new QuestChallenge |
| 451 | public static readonly QuestChallenge ExtractVigor = new QuestChallenge |
| 466 | public static readonly QuestChallenge DesertSun = new QuestChallenge |
| 485 | public static readonly QuestChallenge VenomBarb = new QuestChallenge |
| 502 | public static readonly QuestChallenge BrutalSlam = new QuestChallenge |
| 517 | public static readonly QuestChallenge ConsumingShadows = new QuestChallenge |
| 538 | public static readonly QuestChallenge ManaPoison = new QuestChallenge |
| 562 | public static readonly QuestChallenge Pyroclasm = new QuestChallenge |
| 583 | public static readonly QuestChallenge BarrelingCharge = new QuestChallenge |
| 602 | public static readonly QuestChallenge MuscleMagic = new QuestChallenge |
| 622 | public static readonly QuestChallenge AnimatedBooks = new QuestChallenge |
| 647 | public static readonly QuestChallenge AnimatedGuardians = new QuestChallenge |
| 662 | public static readonly QuestChallenge ReapSoul = new QuestChallenge |
| 681 | public static readonly QuestChallenge WakingNightmare = new QuestChallenge |
| 700 | public void AddToTooltip(UITooltip tooltip) |
| 705 | public void ExecuteOnTick(QuestProgress qp) |
| 713 | public void ExecuteOnTick(DungeonProgress dp) |

## Documented by

| Wiki article |
| --- |
| [Acid Rain](challenge-AcidRain.md) |
| [Cognitohazard](challenge-AnimatedBooks.md) |
| [Animated Guardians](challenge-AnimatedGuardians.md) |
| [Arcane Traps](challenge-ArcaneTraps.md) |
| [Barreling Charge](challenge-BarrelingCharge.md) |
| [Brutal Slam](challenge-BrutalSlam.md) |
| [Tripping Hazard](challenge-Caltrops.md) |
| [Chilling Howl](challenge-ChillingHowl.md) |
| [Clear Rubble](challenge-ClearRubble.md) |
| [Spiritual Leader](challenge-ClericSpec.md) |
| [Consuming Shadows](challenge-ConsumingShadows.md) |
| [Dangerous!](challenge-Dangerous.md) |
| [Scorching Heat](challenge-DesertSun.md) |
| [Tight Squeeze](challenge-DexEnergy.md) |
| [Dilute Miasma](challenge-DilutePoison.md) |
| [Exhausting](challenge-Exhausting.md) |
| [Extract Vigor](challenge-ExtractVigor.md) |
| [Open Battle](challenge-FighterSpec.md) |
| [Flailing Strike](challenge-FlailingStrike.md) |
| [Compounding Effort](challenge-IncreaseDuration.md) |
| [Venom Injector](challenge-InjectPoison.md) |
| [Magic Affinity](challenge-MageSpec.md) |
| [Concentrated Miasma](challenge-MajorPoison.md) |
| [Mana Scourge](challenge-ManaPoison.md) |
| [Muscle Magic](challenge-MuscleMagic.md) |
| [Pyroclasm](challenge-Pyroclasm.md) |
| [Reap Soul](challenge-ReapSoul.md) |
| [Reaping Strike](challenge-ReapingStrike.md) |
| [Reckless Charge](challenge-RecklessCharge.md) |
| [Stealth Mission](challenge-RogueSpec.md) |
| [Scattershot Beams](challenge-ScatterBeam.md) |
| [Soul Reave](challenge-SoulReave.md) |
| [Gout of Flame](challenge-TankFireDamage.md) |
| [Extinguish Hope](challenge-TankShadowDamage.md) |
| [Tremors](challenge-Tremors.md) |
| [Venom Injector](challenge-VenomBarb.md) |
| [Waking Nightmare](challenge-WakingNightmare.md) |
| [Dungeon challenge reference](dungeon-hazard-reference.md) |
| [Quest challenges, rewards, and permanent discounts](quest-challenges-and-rewards.md) |
| [Skill tests and elemental resistances](skill-tests-and-resistances.md) |

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:1`
