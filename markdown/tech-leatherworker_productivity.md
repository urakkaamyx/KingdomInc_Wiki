# Leatherworker · overseers

Leatherworker · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | leatherworker_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Leatherworker](tech-leatherworker.md) |
| [Honest Craftmanship](tech-leatherworker_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Leatherworker\", \"callSource\": \"source/Assets.Source.Player.Tech/T2Leatherworker.cs\", \"callLine\": 94, \"id\": \"leatherworker_productivity\", \"previous\": \"leatherworker_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Leatherworker · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"leatherworker\", \"requires\": [\"leatherworker\", \"leatherworker_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T2Leatherworker.cs:94`
