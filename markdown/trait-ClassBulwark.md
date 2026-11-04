# Bulwark

Bulwark is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, calc stat. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@bulwark\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@bulwark_trait_desc\", GameMath.FormatPercentage(trait.Quality))",
  "IconName": "\"Icons2_113\"",
  "CalcStat": "(ActiveTrait trait, EquipStat stat, float current) =>\n\t\t{\n\t\t\tif (stat == EquipStat.Armor)\n\t\t\t{\n\t\t\t\tInventoryItem equippedItem = ((HumanItemData)trait.Self).GetEquippedItem(EquipmentSlot.OffHand);\n\t\t\t\tif (equippedItem?.Type is WeaponItemType { WeaponType: WeaponType.Shield })\n\t\t\t\t{\n\t\t\t\t\tcurrent += (float)equippedItem.GetAppraiserStat(AppraiserStat.Armor) * trait.Quality;\n\t\t\t\t}\n\t\t\t}\n\t\t\treturn current;\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:220`
