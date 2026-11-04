# Scroll of Radiance

The scroll's magic is consumed upon use to restore a small amount of health to all party members.

## In the game

The scroll's magic is consumed upon use to restore a small amount of health to all party members.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | scroll_of_aoe_healing |
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
| [Scroll of Radiance](recipe-scroll_of_aoe_healing.md) | [Scribe](building-Scribe.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_61\"",
  "Slot": "EquipmentSlot.Scroll",
  "BaseStats": "new StatSet { (stat: EquipStat.Health, amt: 30) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@scroll_of_aoe_healing\",\n\t\t\t\tIconName = \"Icons3_61\",\n\t\t\t\tGetDescription = (ActiveTrait trait) => Translation.TranslateOnly(\"@scroll_of_aoe_healing_effect\", (float)aoeHealingAmt * trait.Quality),\n\t\t\t\tWarTick = (ActiveTrait trait, WarProgress war) =>\n\t\t\t\t{\n\t\t\t\t\t_aoeHealScroll(trait, war.Soldiers, 4 / war.Soldiers.Count, aoeHealingAmt, war);\n\t\t\t\t},\n\t\t\t\tQuestTick = (ActiveTrait trait, QuestProgress q) =>\n\t\t\t\t{\n\t\t\t\t\t_aoeHealScroll(trait, q.Parent.Contents, 1f, aoeHealingAmt, q);\n\t\t\t\t},\n\t\t\t\tDungeonHealingTick = (ActiveTrait trait, DungeonProgress d) =>\n\t\t\t\t{\n\t\t\t\t\t_aoeHealScroll(trait, d.Party, 1f, aoeHealingAmt, d);\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:310`
