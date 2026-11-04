# Mine · overseers

Mine · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |
| [Drudge Miners](tech-mine_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Mine\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Mine.cs\", \"callLine\": 73, \"id\": \"mine_productivity\", \"previous\": \"mine_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Mine · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"mine\", \"requires\": [\"mine\", \"mine_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Mine.cs:73`
