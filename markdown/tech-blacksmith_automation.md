# Apprenticeship

Unlocks the first Upgrade slot for your Blacksmith.

Unlocks the Worker upgrade to automate blacksmithing.

## Research effect

Unlocks the first Upgrade slot for your Blacksmith.

Unlocks the Worker upgrade to automate blacksmithing.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blacksmith_automation |
| Type | Upgrade Slot |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |

## Leads to

| Research |
| --- |
| [Blacksmith · second add-on slot](tech-blacksmith_automation_2.md) |
| [Blacksmith · overseers](tech-blacksmith_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Blacksmith\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Blacksmith.cs\", \"callLine\": 23, \"id\": \"blacksmith_automation\", \"root\": \"blacksmith\", \"tier\": 1, \"name\": \"Apprenticeship\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"blacksmith\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:23`
