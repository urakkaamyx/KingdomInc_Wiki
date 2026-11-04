# Carpenter · overseers

Carpenter · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | carpenter_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Carpenter](tech-carpenter.md) |
| [Only Hammers](tech-carpenter_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Carpenter\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Carpenter.cs\", \"callLine\": 157, \"id\": \"carpenter_productivity\", \"previous\": \"carpenter_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Carpenter · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"carpenter\", \"requires\": [\"carpenter\", \"carpenter_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Carpenter.cs:157`
