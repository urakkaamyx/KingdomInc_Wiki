# Campfire · overseers

Campfire · overseers is a tier 5 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | campfire_productivity |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Campfire](tech-campfire.md) |
| [Wilderness Cookery](tech-campfire_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Campfire\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Campfire.cs\", \"callLine\": 56, \"id\": \"campfire_productivity\", \"previous\": \"campfire_automation\", \"additional\": [\"war_effort\"], \"tier\": 5, \"name\": \"Campfire · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"campfire\", \"requires\": [\"campfire\", \"campfire_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Campfire.cs:56`
