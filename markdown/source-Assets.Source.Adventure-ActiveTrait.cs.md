# ActiveTrait — source reference

Assets.Source.Adventure/ActiveTrait.cs · 103 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public struct ActiveTrait(CombatantItemData self, AdventurerTrait trait, float quality) |
| 10 | public readonly CombatantItemData Self = self |
| 12 | public readonly AdventurerTrait Trait = trait |
| 14 | public readonly float Quality = quality |
| 16 | public string Description => Trait.GetDescription(this) |
| 18 | public float CalcStat(EquipStat stat, float current) |
| 23 | public float CalcSkillTest(EquipStat stat, float current) |
| 28 | public float CalcDamageDone(float current, object target) |
| 33 | public float CalcDamageTaken(float current, object target) |
| 38 | public float CalcHealingDone(float current, object target) |
| 43 | public float CalcHealingTaken(float current, object target) |
| 48 | public float CalcEnergyLoss(float current, object target) |
| 53 | public float CalcTraining(float current, object context) |
| 58 | public void WarTick(WarProgress context) |
| 63 | public void QuestTick(QuestProgress context) |
| 68 | public void ArenaTick(Arena context) |
| 73 | public void DungeonCombatTick(DungeonProgress context) |
| 78 | public void DungeonHealingTick(DungeonProgress context) |
| 83 | public void ApplyGroupBuffs(CombatantItemData ally, object context) |
| 88 | public static void ApplyBuffs(IReadOnlyList<CombatantItemData> party, CombatantItemData applyTo, object context) |
| 96 | public static void ApplyBuffs(IReadOnlyList<CombatantItemData> party, object context) |

## Documented by

| Wiki article |
| --- |
| [Traits and party buffs](traits-and-party-buffs.md) |

## Sources

- `Assets.Source.Adventure/ActiveTrait.cs:1`
