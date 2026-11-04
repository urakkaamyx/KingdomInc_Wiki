# Scroll of Second Wind

Even just holding it makes you feel revitalized. Reading the scroll will restore energy to the entire party.

## In the game

Even just holding it makes you feel revitalized. Reading the scroll will restore energy to the entire party.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | scroll_of_energy |
| Item type | Equipment |
| Slot | Scroll |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Energy | 15 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Scroll of Second Wind](recipe-scroll_of_energy.md) | [Scribe](building-Scribe.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_62\"",
  "Slot": "EquipmentSlot.Scroll",
  "BaseStats": "new StatSet { (stat: EquipStat.Energy, amt: 15) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@scroll_of_energy\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@scroll_of_energy_trait\", (float)scrollEnergyAmt * trait.Quality),\n\t\t\t\tIconName = \"Icons3_62\",\n\t\t\t\tQuestTick = (ActiveTrait trait, QuestProgress quest) =>\n\t\t\t\t{\n\t\t\t\t\t_restoreEnergy(trait, quest.Parent.Contents, scrollEnergyAmt);\n\t\t\t\t},\n\t\t\t\tDungeonHealingTick = (ActiveTrait trait, DungeonProgress dungeon) =>\n\t\t\t\t{\n\t\t\t\t\t_restoreEnergy(trait, dungeon.Party, scrollEnergyAmt);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:354`
