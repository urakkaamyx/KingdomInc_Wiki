# Butcher · overseers

Butcher · overseers is a tier 8 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | butcher_productivity |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Butcher](tech-butcher.md) |
| [The Meat Man](tech-butcher_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Butcher\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Butcher.cs\", \"callLine\": 23, \"id\": \"butcher_productivity\", \"previous\": \"butcher_automation\", \"additional\": [\"war_effort\"], \"tier\": 8, \"name\": \"Butcher · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"butcher\", \"requires\": [\"butcher\", \"butcher_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Butcher.cs:23`
