# Equipment slots, hands, and armor affinity

Slot unlocks, weapon conflicts, equipment rolls, and enhancements.

## Unlocks

Head, Chest, Main Hand, and Off Hand are available by default. Food requires Campfire, Adventure Supplies, or Kitchen; Potion requires Adventure Supplies or Alchemist; Amulet/Ring require Jeweler; Trinket requires Inventor; Scroll requires Scribe.

The equipment gate supports a per-type EquipmentAllowed predicate, but the extracted source contains no assignments to it. Class affinity is primarily an advancement or trait condition rather than a general ban on other equipment.

## Weapon handling

Greatsword, Bow, Rifle, Staff, and Battleaxe are two-handed. Sword and Dagger are ambidextrous. Shield, Tome, and Focus are Off Hand. Bow, Rifle, Staff, and Wand are ranged for distance rank.

HasWeapon requires a main-hand WeaponItemType. HasDualWield counts more than one such weapon entry. HasShield searches for any Shield weapon. Adding equipment removes conflicts and refreshes traits.

## Equipment and enhancements

Equipment stat ranges are floor(base × 0.9 × item quality) to ceil(base × 1.1 × item quality). Integer rolls exclude the upper endpoint when bounds differ. Updating equipment quality rerolls these base stats. Enhancement stats are added afterward.

Without multi-enhancement research only one enhancement is allowed. With it, one enhancement per EnhancementType is allowed; duplicate types remain disallowed. Equipment and enhancement traits also contribute their own effects.

Each flat enhancement stat is round(declared enhancement stat × enhancement quality) before being added to the equipment. This differs from the equipment’s own rolled base stats. Quality-adding enhancements affect the item through their crafting workflow; trait quality remains the enhancement source’s quality.

## Sources

- `Assets.Source.Items.Data/HumanItemData.cs:23`
- `Assets.Source.Items.Data/HumanItemData.cs:38`
- `Assets.Source.Items.Data/HumanItemData.cs:132`
- `Assets.Source.Items.Type/HumanItemType.cs:204`
- `Assets.Source.Items/WeaponTypeExtensions.cs:16`
- `Assets.Source.Items.Data/EquipmentItemData.cs:87`
- `Assets.Source.Items.Data/EquipmentItemData.cs:105`
- `SeededRandom.cs:41`
- `Assets.Source.Items/ItemEnhancementData.cs:22`
