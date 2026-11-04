# Automaton

Unlocks the first Upgrade slot for your Inventor.

Unlocks the Worker upgrade to automatically create inventions.

## Research effect

Unlocks the first Upgrade slot for your Inventor.

Unlocks the Worker upgrade to automatically create inventions.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | inventor_automation |
| Type | Upgrade Slot |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |

## Leads to

| Research |
| --- |
| [Inventor · second add-on slot](tech-inventor_automation_2.md) |
| [Inventor · overseers](tech-inventor_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Inventor\", \"callSource\": \"source/Assets.Source.Player.Tech/T10Inventor.cs\", \"callLine\": 25, \"id\": \"inventor_automation\", \"root\": \"inventor\", \"tier\": 10, \"name\": \"Automaton\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"inventor\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T10Inventor.cs:25`
