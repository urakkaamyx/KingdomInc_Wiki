# Scroll of Healing

The scroll's magic is consumed upon use to restore a large amount of health.

## In the game

The scroll's magic is consumed upon use to restore a large amount of health.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | scroll_of_healing |
| Item type | Equipment |
| Slot | Scroll |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Health | 30 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Scroll of Healing](recipe-scroll_of_healing.md) | [Scribe](building-Scribe.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_60\"",
  "Slot": "EquipmentSlot.Scroll",
  "BaseStats": "new StatSet { (stat: EquipStat.Health, amt: 30) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@scroll_of_healing\",\n\t\t\t\tIconName = \"Icons3_60\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@healing_potion_effect\", (float)scrollHealingAmt * trait.Quality),\n\t\t\t\tWarTick = (ActiveTrait trait, WarProgress war) =>\n\t\t\t\t{\n\t\t\t\t\t_healingScroll(trait, scrollHealingAmt, war);\n\t\t\t\t},\n\t\t\t\tQuestTick = (ActiveTrait trait, QuestProgress q) =>\n\t\t\t\t{\n\t\t\t\t\t_healingScroll(trait, scrollHealingAmt, q);\n\t\t\t\t},\n\t\t\t\tArenaTick = (ActiveTrait trait, Arena a) =>\n\t\t\t\t{\n\t\t\t\t\t_healingScroll(trait, scrollHealingAmt, a);\n\t\t\t\t},\n\t\t\t\tDungeonHealingTick = (ActiveTrait trait, DungeonProgress d) =>\n\t\t\t\t{\n\t\t\t\t\t_healingScroll(trait, scrollHealingAmt, d);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:281`
