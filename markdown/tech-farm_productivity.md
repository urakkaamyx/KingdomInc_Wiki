# Farm · overseers

Farm · overseers is a tier 8 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_productivity |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |
| [Farmhand](tech-farm_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Farm\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Farm.cs\", \"callLine\": 35, \"id\": \"farm_productivity\", \"previous\": \"farm_automation\", \"additional\": [\"war_effort\"], \"tier\": 8, \"name\": \"Farm · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"farm\", \"requires\": [\"farm\", \"farm_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Farm.cs:35`
