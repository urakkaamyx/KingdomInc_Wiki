# Shrine · overseers

Shrine · overseers is a tier 12 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shrine_productivity |
| Type | Upgrade Slot |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Shrine](tech-shrine.md) |
| [Prayer Wheel](tech-shrine_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Shrine\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Shrine.cs\", \"callLine\": 26, \"id\": \"shrine_productivity\", \"previous\": \"shrine_automation\", \"additional\": [\"war_effort\"], \"tier\": 12, \"name\": \"Shrine · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"shrine\", \"requires\": [\"shrine\", \"shrine_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Shrine.cs:26`
