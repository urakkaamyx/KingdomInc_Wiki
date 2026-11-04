# HumanItemData — source reference

Assets.Source.Items.Data/HumanItemData.cs · 446 lines · 9 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public class HumanItemData : CombatantItemData |
| 13 | public readonly List<InventoryItem> Equipment = new List<InventoryItem>() |
| 15 | public int TrainingCount |
| 17 | public int QuestCount |
| 19 | public int ArenaCount |
| 21 | public int SpecialCount |
| 23 | public bool HasWeapon |
| 38 | public bool HasDualWield |
| 54 | public bool HasShield |
| 69 | public int DistanceRank |
| 85 | public HumanItemType HumanType => Item.Type as HumanItemType |
| 87 | public HumanItemData(InventoryItem item) |
| 92 | public void AddEquipment(InventoryItem item) |
| 106 | public bool CanEquipItem(InventoryItem item, bool replace) |
| 119 | public List<InventoryItem> GetConflictingItems(InventoryItem item) |
| 197 | public InventoryItem GetEquippedItem(EquipmentSlot slot) |
| 209 | public override int GetStat(EquipStat s) |
| 244 | public override int GetCombatPower() |
| 254 | public EquipStat GetCombatStat() |
| 274 | protected override IEnumerable<ActiveTrait> EnumerateTraits() |
| 314 | public void ActivityCompleted() |
| 324 | public void ConsumeFood() |
| 329 | public void RemoveEquipment(EquipmentSlot slot) |
| 339 | public bool HasArchetype(AdventurerArchetype type) |
| 344 | public bool HasWeaponStat(EquipStat stat) |
| 354 | public bool HasWeaponType(WeaponType type) |
| 366 | public bool HasArmorType(ArmorType armor) |
| 397 | public bool DefaultHealingSpell(IEnumerable<CombatantItemData> party, object context) |
| 415 | public override void DataToJson(JsonObject data) |
| 437 | public override void DataFromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Equip All Slots](achievement-EquipAllSlots.md) |
| [Achievements, Steam statistics, and integration](achievements-and-steam.md) |
| [Adventurer classes and advancement routes](class-progression.md) |
| [Combat stats and power](combat-stats.md) |
| [Energy, death, and dungeon limit breaks](energy-death-and-limit-break.md) |
| [Equipment slots, hands, and armor affinity](equipment-slots-and-hands.md) |
| [Prestige perks and refunds](prestige-perks.md) |
| [Tanks, healers, and party formation](tank-and-healer.md) |
| [Traits and party buffs](traits-and-party-buffs.md) |

## Sources

- `Assets.Source.Items.Data/HumanItemData.cs:1`
