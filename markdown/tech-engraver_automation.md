# Runic Apprentice

Unlocks the first Upgrade slot for your Engraver.

Unlocks the Worker upgrade to automate production.

## Research effect

Unlocks the first Upgrade slot for your Engraver.

Unlocks the Worker upgrade to automate production.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engraver_automation |
| Type | Upgrade Slot |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |

## Leads to

| Research |
| --- |
| [Engraver · second add-on slot](tech-engraver_automation_2.md) |
| [Engraver · overseers](tech-engraver_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Engraver\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Engraver.cs\", \"callLine\": 23, \"id\": \"engraver_automation\", \"root\": \"engraver\", \"tier\": 3, \"name\": \"Runic Apprentice\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"engraver\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Engraver.cs:23`
