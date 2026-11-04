# Blacksmith · second add-on slot

Blacksmith · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blacksmith_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Apprenticeship](tech-blacksmith_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Blacksmith · artisans](tech-blacksmith_quality.md) |
| [Blacksmith · third add-on slot](tech-blacksmith_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Blacksmith\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Blacksmith.cs\", \"callLine\": 23, \"id\": \"blacksmith_automation_2\", \"previous\": \"blacksmith_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Blacksmith · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"blacksmith\", \"requires\": [\"blacksmith\", \"blacksmith_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:23`
