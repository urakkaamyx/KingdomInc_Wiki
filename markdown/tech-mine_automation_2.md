# Mine · second add-on slot

Mine · second add-on slot is a tier 3 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |
| [Drudge Miners](tech-mine_automation.md) |
| [War Effort](tech-war_effort.md) |

## Leads to

| Research |
| --- |
| [Mine · artisans](tech-mine_quality.md) |
| [Mine · third add-on slot](tech-mine_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"Mine\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Mine.cs\", \"callLine\": 73, \"id\": \"mine_automation_2\", \"previous\": \"mine_automation\", \"tier\": 3, \"additional\": [\"war_effort\"], \"name\": \"Mine · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"mine\", \"requires\": [\"mine\", \"mine_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Mine.cs:73`
