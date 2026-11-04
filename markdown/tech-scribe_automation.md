# Enchanted Quill

Unlocks the first Upgrade slot for your Scribe.

Unlocks the Worker upgrade to automatically write scrolls and tomes.

## Research effect

Unlocks the first Upgrade slot for your Scribe.

Unlocks the Worker upgrade to automatically write scrolls and tomes.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | scribe_automation |
| Type | Upgrade Slot |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |

## Leads to

| Research |
| --- |
| [Scribe · second add-on slot](tech-scribe_automation_2.md) |
| [Scribe · overseers](tech-scribe_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Scribe\", \"callSource\": \"source/Assets.Source.Player.Tech/T10Scribe.cs\", \"callLine\": 23, \"id\": \"scribe_automation\", \"root\": \"scribe\", \"tier\": 10, \"name\": \"Enchanted Quill\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"scribe\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T10Scribe.cs:23`
