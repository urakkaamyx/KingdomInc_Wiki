# Lifebloom Amulet

Exudes a gentle soothing aura that intermittently heals the wearer's allies for a small amount.

## In the game

Exudes a gentle soothing aura that intermittently heals the wearer's allies for a small amount.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | lifebloom_amulet |
| Item type | Equipment |
| Slot | Amulet |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Wisdom | 20 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Lifebloom Amulet](recipe-lifebloom_amulet.md) | [Jeweler](building-Jeweler.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_213\"",
  "Slot": "EquipmentSlot.Amulet",
  "BaseStats": "new StatSet { (stat: EquipStat.Wisdom, amt: 20) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@lifebloom_amulet_trait\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@lifebloom_amulet_trait_desc\", 2f * trait.Quality / 2f),\n\t\t\t\tIconName = \"Icons2_213\",\n\t\t\t\tArenaTick = (ActiveTrait trait, Arena arena) =>\n\t\t\t\t{\n\t\t\t\t\t_lifebloomEffect(trait, new List<CombatantItemData> { trait.Self }, 1f, arena);\n\t\t\t\t},\n\t\t\t\tQuestTick = (ActiveTrait trait, QuestProgress quest) =>\n\t\t\t\t{\n\t\t\t\t\t_lifebloomEffect(trait, quest.Parent.Contents, 0.5f, quest);\n\t\t\t\t},\n\t\t\t\tWarTick = (ActiveTrait trait, WarProgress war) =>\n\t\t\t\t{\n\t\t\t\t\t_lifebloomEffect(trait, war.Soldiers, 4 / war.Soldiers.Count, war);\n\t\t\t\t},\n\t\t\t\tDungeonHealingTick = (ActiveTrait trait, DungeonProgress dungeon) =>\n\t\t\t\t{\n\t\t\t\t\t_lifebloomEffect(trait, dungeon.Combatants, 0.8f, dungeon);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier8.cs:237`
