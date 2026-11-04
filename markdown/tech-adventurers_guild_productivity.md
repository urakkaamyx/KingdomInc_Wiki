# Adventurer's Guild · overseers

Adventurer's Guild · overseers is a tier 6 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventurers_guild_productivity |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Adventurer's Guild](tech-adventurers_guild.md) |
| [Reception Desk](tech-adventurers_guild_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"AdventurersGuild\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurersGuild.cs\", \"callLine\": 63, \"id\": \"adventurers_guild_productivity\", \"previous\": \"adventurers_guild_automation\", \"additional\": [\"war_effort\"], \"tier\": 6, \"name\": \"Adventurer's Guild · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"adventurers_guild\", \"requires\": [\"adventurers_guild\", \"adventurers_guild_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:63`
