# Dungeon

Send a party of five adventurers down into the depths to defeat evil and recover valuable loot.

## Purpose

Send a party of five adventurers down into the depths to defeat evil and recover valuable loot.

## Building reference

| Property | Value |
| --- | --- |
| Type | Dungeon |
| Category | Consumption |
| Inheritance | Dungeon → FlowElement |
| Research required | [Dungeon](tech-dungeon.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Dungeon Keeper](tech-dungeon_automation.md) | 8 |
| [Dungeon · second add-on slot](tech-dungeon_automation_2.md) | 9 |
| [Dungeon · third add-on slot](tech-dungeon_automation_3.md) | 10 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Dungeon |
| Category | ElementCategory.Consumption |
| Icon Name | Icons 195 |
| Icon | CurrentDungeon?.Dungeon.Icon ?? base.Icon |
| Music Track | Temple Explore LOOP BPM110 |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Dungeon",
  "Inherited behavior": "Dungeon → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Dungeon.cs:17`
