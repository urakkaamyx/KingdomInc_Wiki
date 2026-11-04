# Mine

Provides raw metal ores to your kingdom.

## Purpose

Provides raw metal ores to your kingdom.

## Building reference

| Property | Value |
| --- | --- |
| Type | Mine |
| Category | Resource |
| Inheritance | Mine → ResourceElement → FlowElement |
| Research required | [Mine](tech-mine.md) |

## Resource selections

| Resource | Unlock |
| --- | --- |
| [Iron Ore](item-iron_ore.md) | [Mine Iron Ore](tech-mine_iron_ore.md) |
| [Sapphire](item-sapphire.md) | [Mine Sapphire](tech-mine_sapphire.md) |
| [Gold Ore](item-gold_ore.md) | [Mine Gold Ore](tech-mine_gold_ore.md) |
| [Silver Ore](item-silver_ore.md) | [Mine Silver Ore](tech-mine_silver_ore.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Drudge Miners](tech-mine_automation.md) | 1 |
| [Mine · second add-on slot](tech-mine_automation_2.md) | 3 |
| [Mine · overseers](tech-mine_productivity.md) | 4 |
| [Mine · artisans](tech-mine_quality.md) | 4 |
| [Mine · third add-on slot](tech-mine_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Default Label | Mine |
| Default Icon Name | Icons 1 |
| Action Label | Click to choose a new material to mine. |
| Music Track | Adventure Puzzle LOOP BPM120 |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Mine",
  "Inherited behavior": "Mine → ResourceElement → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Mine.cs:6`
