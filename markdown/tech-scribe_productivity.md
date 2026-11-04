# Scribe · overseers

Scribe · overseers is a tier 11 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | scribe_productivity |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |
| [Enchanted Quill](tech-scribe_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Scribe\", \"callSource\": \"source/Assets.Source.Player.Tech/T10Scribe.cs\", \"callLine\": 23, \"id\": \"scribe_productivity\", \"previous\": \"scribe_automation\", \"additional\": [\"war_effort\"], \"tier\": 11, \"name\": \"Scribe · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"scribe\", \"requires\": [\"scribe\", \"scribe_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T10Scribe.cs:23`
