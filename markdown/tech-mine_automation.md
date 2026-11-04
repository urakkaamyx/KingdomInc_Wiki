# Drudge Miners

Unlocks the first Upgrade slot for your Mines.

Unlocks the Worker upgrade to automate ore production.

## Research effect

Unlocks the first Upgrade slot for your Mines.

Unlocks the Worker upgrade to automate ore production.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_automation |
| Type | Upgrade Slot |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |

## Leads to

| Research |
| --- |
| [Mine · second add-on slot](tech-mine_automation_2.md) |
| [Mine · overseers](tech-mine_productivity.md) |
| [Supply Depot](tech-supply_depot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Mine\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Mine.cs\", \"callLine\": 73, \"id\": \"mine_automation\", \"root\": \"mine\", \"tier\": 1, \"name\": \"Drudge Miners\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"mine\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Mine.cs:73`
