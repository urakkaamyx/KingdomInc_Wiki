# Adventurer's Guild · second add-on slot

Adventurer's Guild · second add-on slot is a tier 6 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventurers_guild_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Adventurer's Guild](tech-adventurers_guild.md) |
| [Reception Desk](tech-adventurers_guild_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Quest Board](tech-quest_board.md) |

## Leads to

| Research |
| --- |
| [Adventurer's Guild · artisans](tech-adventurers_guild_quality.md) |
| [Adventurer's Guild · third add-on slot](tech-adventurers_guild_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"AdventurersGuild\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurersGuild.cs\", \"callLine\": 63, \"id\": \"adventurers_guild_automation_2\", \"previous\": \"adventurers_guild_automation\", \"tier\": 6, \"additional\": [\"war_effort\", \"quest_board\"], \"name\": \"Adventurer's Guild · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"adventurers_guild\", \"requires\": [\"adventurers_guild\", \"adventurers_guild_automation\", \"war_effort\", \"quest_board\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:63`
