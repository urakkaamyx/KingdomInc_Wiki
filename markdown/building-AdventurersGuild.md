# Adventurer's Guild

Allows you to recruit rookie adventurers, ready for training and questing.

## Purpose

Allows you to recruit rookie adventurers, ready for training and questing.

## Building reference

| Property | Value |
| --- | --- |
| Type | AdventurersGuild |
| Category | Resource |
| Inheritance | AdventurersGuild → ResourceElement → FlowElement |
| Research required | [Adventurer's Guild](tech-adventurers_guild.md) |

## Resource selections

| Resource | Unlock |
| --- | --- |
| [Adventurer](item-adventurer.md) | [Recruit Adventurers](tech-recruit_adventurer.md) |

## Upgrade research

| Research | Tier |
| --- | --- |
| [Reception Desk](tech-adventurers_guild_automation.md) | 5 |
| [Adventurer's Guild · second add-on slot](tech-adventurers_guild_automation_2.md) | 6 |
| [Adventurer's Guild · overseers](tech-adventurers_guild_productivity.md) | 6 |
| [Adventurer's Guild · artisans](tech-adventurers_guild_quality.md) | 7 |
| [Adventurer's Guild · third add-on slot](tech-adventurers_guild_automation_3.md) | 7 |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Default Label | Adventurer's Guild |
| Default Icon Name | Icons 67 |
| Action Label | Click to choose a type of adventurers to recruit. |
| Music Track | Kingdom Wonder LOOP BPM70 |
| Label | DefaultLabel |
| Output Per Second | (_warProgressed ? 0.5f : 0f) * Speed |
| Quality Resource Cost | 2f |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "AdventurersGuild",
  "Inherited behavior": "AdventurersGuild → ResourceElement → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/AdventurersGuild.cs:6`
