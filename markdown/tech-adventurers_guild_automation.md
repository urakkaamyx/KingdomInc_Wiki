# Reception Desk

Unlocks the first Upgrade slot for your Adventurer's Guild.

Unlocks the Worker upgrade to automatically recruit adventurers.

## Research effect

Unlocks the first Upgrade slot for your Adventurer's Guild.

Unlocks the Worker upgrade to automatically recruit adventurers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventurers_guild_automation |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventurer's Guild](tech-adventurers_guild.md) |

## Leads to

| Research |
| --- |
| [Adventurer's Guild · second add-on slot](tech-adventurers_guild_automation_2.md) |
| [Adventurer's Guild · overseers](tech-adventurers_guild_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"AdventurersGuild\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurersGuild.cs\", \"callLine\": 63, \"id\": \"adventurers_guild_automation\", \"root\": \"adventurers_guild\", \"tier\": 5, \"name\": \"Reception Desk\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"adventurers_guild\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:63`
