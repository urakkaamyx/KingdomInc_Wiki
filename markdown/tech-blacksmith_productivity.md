# Blacksmith · overseers

Blacksmith · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blacksmith_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Apprenticeship](tech-blacksmith_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Blacksmith\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Blacksmith.cs\", \"callLine\": 23, \"id\": \"blacksmith_productivity\", \"previous\": \"blacksmith_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Blacksmith · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"blacksmith\", \"requires\": [\"blacksmith\", \"blacksmith_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:23`
