# CombatantItemData — source reference

Assets.Source.Items.Data/CombatantItemData.cs · 404 lines · 12 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class CombatantItemData : ItemData |
| 12 | public const float BaselineArmor = 200f |
| 14 | public int Level |
| 16 | public float Health01 = 1f |
| 18 | public float Energy01 = 1f |
| 20 | protected readonly StatSet Stats = new StatSet() |
| 24 | public bool LimitBreak |
| 26 | public int MaxHealth => GetStat(EquipStat.Health) |
| 28 | public int MaxEnergy => GetStat(EquipStat.Energy) |
| 30 | public int CurrentHealth |
| 42 | public bool Dead => Health01 <= 0f |
| 44 | public bool Exhausted |
| 56 | public int CurrentEnergy |
| 68 | public CombatantItemType CombatantType => Item.Type as CombatantItemType |
| 70 | public CombatantItemData(InventoryItem item) |
| 75 | public override void Initialize() |
| 98 | public override void SetMinimumRolls() |
| 109 | public override void SetMaximumRolls() |
| 120 | public void AddStat(EquipStat s, int amt) |
| 125 | public virtual int GetStat(EquipStat s) |
| 139 | public bool SkillTest(EquipStat stat, float difficulty) |
| 149 | public bool TakeDamage(float dmg, object context, bool ignoreArmor = false) |
| 181 | public void Heal(float amt, object context) |
| 190 | public bool LoseEnergy(float amt, object context) |
| 207 | public bool LoseEnergyDungeon(float amt, DungeonProgress dungeon) |
| 223 | public (int min, int max) GetRollRange(EquipStat s, int statBase) |
| 233 | public virtual int GetCombatPower() |
| 238 | public virtual int GetBaseDamage(object target) |
| 243 | public virtual float GetDamageMultiplier(object target) |
| 253 | public float GetDamageReduction(AdventurerTrait resist) |
| 263 | public virtual int GetBaseHealing(CombatantItemData target) |
| 271 | public virtual float GetHealingMultiplier(CombatantItemData target) |
| 281 | public IEnumerable<ActiveTrait> GetTraits(bool mutable) |
| 294 | public void RefreshTraits(bool clearBuffs) |
| 304 | protected virtual IEnumerable<ActiveTrait> EnumerateTraits() |
| 316 | public bool HasTrait(AdventurerTrait trait) |
| 328 | public ActiveTrait? GetTrait(AdventurerTrait trait) |
| 340 | public void AddTraining(float addQuality, object context) |
| 349 | public void ApplyBuffs(CombatantItemData target, object context) |
| 357 | public void ApplyBuff(AdventurerTrait buff, float quality) |
| 363 | public void RemoveBuff(AdventurerTrait buff) |
| 368 | public override void DataToJson(JsonObject data) |
| 376 | public override void DataFromJson(JsonObject data) |
| 396 | public static float ArmorDamageReduction(float armor) |

## Documented by

| Wiki article |
| --- |
| [Indulgence Equip](achievement-IndulgenceEquip.md) |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |
| [Armor and damage reduction](armor-and-damage.md) |
| [Combat stats and power](combat-stats.md) |
| [Energy, death, and dungeon limit breaks](energy-death-and-limit-break.md) |
| [Arena battles, training, and rewards](production-arena.md) |
| [Shrines, prayer, and Faith](production-shrine-faith.md) |
| [Training Grounds and diminishing returns](production-training.md) |
| [Skill tests and elemental resistances](skill-tests-and-resistances.md) |
| [Tanks, healers, and party formation](tank-and-healer.md) |
| [Training Grounds and quality growth](training-grounds-mechanics.md) |
| [Traits and party buffs](traits-and-party-buffs.md) |

## Sources

- `Assets.Source.Items.Data/CombatantItemData.cs:1`
