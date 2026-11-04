# Forest · overseers

Forest · overseers is a tier 5 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest_productivity |
| Type | Upgrade Slot |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |
| [Cross-country Carriers](tech-forest_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Forest\", \"callSource\": \"source/Assets.Source.Player.Tech/T4Forest.cs\", \"callLine\": 39, \"id\": \"forest_productivity\", \"previous\": \"forest_automation\", \"additional\": [\"war_effort\"], \"tier\": 5, \"name\": \"Forest · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"forest\", \"requires\": [\"forest\", \"forest_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T4Forest.cs:39`
