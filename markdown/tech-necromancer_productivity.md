# Necromancer · overseers

Necromancer · overseers is a tier 12 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | necromancer_productivity |
| Type | Upgrade Slot |
| Cost tier | 12 |

## Prerequisites

| Required research |
| --- |
| [Necromancer](tech-necromancer.md) |
| [Novice Necromancer](tech-necromancer_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Necromancer\", \"callSource\": \"source/Assets.Source.Player.Tech/T11Necromancer.cs\", \"callLine\": 21, \"id\": \"necromancer_productivity\", \"previous\": \"necromancer_automation\", \"additional\": [\"war_effort\"], \"tier\": 12, \"name\": \"Necromancer · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"necromancer\", \"requires\": [\"necromancer\", \"necromancer_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T11Necromancer.cs:21`
