# Adventurer's Guild · third add-on slot

Adventurer's Guild · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventurers_guild_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Adventurer's Guild](tech-adventurers_guild.md) |
| [Automated Roster](tech-adventurers_guild_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"AdventurersGuild\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurersGuild.cs\", \"callLine\": 63, \"id\": \"adventurers_guild_automation_3\", \"previous\": \"adventurers_guild_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Adventurer's Guild · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"adventurers_guild\", \"requires\": [\"adventurers_guild\", \"adventurers_guild_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:63`
