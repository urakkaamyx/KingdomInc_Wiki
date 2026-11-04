# Kitchen · overseers

Kitchen · overseers is a tier 8 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | kitchen_productivity |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Kitchen](tech-kitchen.md) |
| [Sous Chef](tech-kitchen_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Kitchen\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Kitchen.cs\", \"callLine\": 19, \"id\": \"kitchen_productivity\", \"previous\": \"kitchen_automation\", \"additional\": [\"war_effort\"], \"tier\": 8, \"name\": \"Kitchen · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"kitchen\", \"requires\": [\"kitchen\", \"kitchen_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Kitchen.cs:19`
