# Recruitment Officer

Unlocks the first Upgrade slot for your Barracks.

Unlocks the Worker upgrade to automate recruitment.

## Research effect

Unlocks the first Upgrade slot for your Barracks.

Unlocks the Worker upgrade to automate recruitment.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | barracks_automation |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Barracks](tech-barracks.md) |

## Leads to

| Research |
| --- |
| [Barracks · second add-on slot](tech-barracks_automation_2.md) |
| [Barracks · overseers](tech-barracks_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Barracks\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Barracks.cs\", \"callLine\": 26, \"id\": \"barracks_automation\", \"root\": \"barracks\", \"tier\": 3, \"name\": \"Recruitment Officer\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"barracks\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Barracks.cs:26`
