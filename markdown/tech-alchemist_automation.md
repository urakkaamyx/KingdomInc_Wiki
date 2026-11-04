# Autobrewery

Unlocks the first Upgrade slot for your Alchemist.

Unlocks the Worker upgrade to automatically brew potions.

## Research effect

Unlocks the first Upgrade slot for your Alchemist.

Unlocks the Worker upgrade to automatically brew potions.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | alchemist_automation |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Alchemist](tech-alchemist.md) |

## Leads to

| Research |
| --- |
| [Alchemist · second add-on slot](tech-alchemist_automation_2.md) |
| [Alchemist · overseers](tech-alchemist_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Alchemist\", \"callSource\": \"source/Assets.Source.Player.Tech/T9Alchemist.cs\", \"callLine\": 23, \"id\": \"alchemist_automation\", \"root\": \"alchemist\", \"tier\": 9, \"name\": \"Autobrewery\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"alchemist\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T9Alchemist.cs:23`
