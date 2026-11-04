# Tailor · overseers

Tailor · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | tailor_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Tailor](tech-tailor.md) |
| [Animated Scissors](tech-tailor_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Tailor\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Tailor.cs\", \"callLine\": 85, \"id\": \"tailor_productivity\", \"previous\": \"tailor_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Tailor · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"tailor\", \"requires\": [\"tailor\", \"tailor_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Tailor.cs:85`
