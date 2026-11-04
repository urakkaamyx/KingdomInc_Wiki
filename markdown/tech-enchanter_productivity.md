# Enchanter · overseers

Enchanter · overseers is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | enchanter_productivity |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Enchanter](tech-enchanter.md) |
| [Leyline Guide](tech-enchanter_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Enchanter\", \"callSource\": \"source/Assets.Source.Player.Tech/T6Enchanter.cs\", \"callLine\": 29, \"id\": \"enchanter_productivity\", \"previous\": \"enchanter_automation\", \"additional\": [\"war_effort\"], \"tier\": 7, \"name\": \"Enchanter · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"enchanter\", \"requires\": [\"enchanter\", \"enchanter_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T6Enchanter.cs:29`
