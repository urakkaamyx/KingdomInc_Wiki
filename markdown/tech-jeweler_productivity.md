# Jeweler · overseers

Jeweler · overseers is a tier 9 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | jeweler_productivity |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |
| [Grinding Wheel](tech-jeweler_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Jeweler\", \"callSource\": \"source/Assets.Source.Player.Tech/T8Jeweler.cs\", \"callLine\": 24, \"id\": \"jeweler_productivity\", \"previous\": \"jeweler_automation\", \"additional\": [\"war_effort\"], \"tier\": 9, \"name\": \"Jeweler · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"jeweler\", \"requires\": [\"jeweler\", \"jeweler_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8Jeweler.cs:24`
