# Scroll of Disintegration

This scroll's magic can be repeatedly evoked to deal heavy damage to powerful foes.

## In the game

This scroll's magic can be repeatedly evoked to deal heavy damage to powerful foes.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | scroll_of_damage |
| Item type | Equipment |
| Slot | Scroll |

## Base stats

These are definition values before quality, training, equipment, enhancements and active traits.

| Stat | Base amount |
| --- | --- |
| Combat Power | 30 |

## Produced by

| Recipe | Station | Base seconds |
| --- | --- | --- |
| [Scroll of Disintegration](recipe-scroll_of_damage.md) | [Scribe](building-Scribe.md) | 3.0 |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons3_63\"",
  "Slot": "EquipmentSlot.Scroll",
  "BaseStats": "new StatSet { (stat: EquipStat.CombatPower, amt: 30) }",
  "EquipTrait": "new AdventurerTrait\n\t\t\t{\n\t\t\t\tDisplayName = \"@scroll_of_damage\",\n\t\t\t\tDescription = \"@scroll_of_damage_effect\",\n\t\t\t\tIconName = \"Icons3_63\",\n\t\t\t\tDungeonCombatTick = (ActiveTrait trait, DungeonProgress dungeon) =>\n\t\t\t\t{\n\t\t\t\t\tif (dungeon.Stage.IsBoss && dungeon.StageTick == 5)\n\t\t\t\t\t{\n\t\t\t\t\t\tdungeon.StageProgress += trait.Self.GetCombatPower() * 4;\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Tier10.cs:334`
