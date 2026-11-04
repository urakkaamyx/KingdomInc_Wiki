# Adventurer's Guild · artisans

Adventurer's Guild · artisans is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventurers_guild_quality |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Adventurer's Guild](tech-adventurers_guild.md) |
| [Automated Roster](tech-adventurers_guild_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"AdventurersGuild\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurersGuild.cs\", \"callLine\": 63, \"id\": \"adventurers_guild_quality\", \"previous\": \"adventurers_guild_automation_2\", \"tier\": 7, \"name\": \"Adventurer's Guild · artisans\", \"icon\": \"Icons_118\", \"addon\": \"RecruitArtisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"adventurers_guild\", \"requires\": [\"adventurers_guild\", \"adventurers_guild_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:63`
