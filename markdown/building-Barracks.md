# Barracks

Recruits Conscripts in service of the struggle against the many enemies that threaten Yensburg.

## Purpose

Recruits Conscripts in service of the struggle against the many enemies that threaten Yensburg.

## Building reference

| Property | Value |
| --- | --- |
| Type | Barracks |
| Category | Resource |
| Inheritance | Barracks → ResourceElement → FlowElement |
| Research required | [Barracks](tech-barracks.md) |

## Resource selections

| Resource | Unlock |
| --- | --- |
| [Conscript](item-conscript.md) | [Recruit Conscripts](tech-recruit_conscript.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Recruitment Officer](tech-barracks_automation.md) | 3 |
| [Barracks · second add-on slot](tech-barracks_automation_2.md) | 4 |
| [Barracks · overseers](tech-barracks_productivity.md) | 4 |
| [Barracks · artisans](tech-barracks_quality.md) | 5 |
| [Barracks · third add-on slot](tech-barracks_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Default Label | Barracks |
| Default Icon Name | Icons 60 |
| Action Label | Click to choose a type of soldiers to recruit. |
| Music Track | Deep Dungeon LOOP BPM90 |
| Label | DefaultLabel |
| Output Per Second | 0.5f * Speed |
| Quality Resource Cost | 2f |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Barracks",
  "Inherited behavior": "Barracks → ResourceElement → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Barracks.cs:6`
