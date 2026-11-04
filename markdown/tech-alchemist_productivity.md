# Alchemist · overseers

Alchemist · overseers is a tier 10 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | alchemist_productivity |
| Type | Upgrade Slot |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Alchemist](tech-alchemist.md) |
| [Autobrewery](tech-alchemist_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Alchemist\", \"callSource\": \"source/Assets.Source.Player.Tech/T9Alchemist.cs\", \"callLine\": 23, \"id\": \"alchemist_productivity\", \"previous\": \"alchemist_automation\", \"additional\": [\"war_effort\"], \"tier\": 10, \"name\": \"Alchemist · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"alchemist\", \"requires\": [\"alchemist\", \"alchemist_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T9Alchemist.cs:23`
