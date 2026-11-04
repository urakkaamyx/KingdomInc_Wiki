# Mad Hermit

Unlocks the first Upgrade slot for your Summoning Circle.

Unlocks the Worker upgrade to automatically perform summoning rituals.

## Research effect

Unlocks the first Upgrade slot for your Summoning Circle.

Unlocks the Worker upgrade to automatically perform summoning rituals.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | summoning_circle_automation |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Summoning Circle](tech-summoning_circle.md) |

## Leads to

| Research |
| --- |
| [Summoning Circle · second add-on slot](tech-summoning_circle_automation_2.md) |
| [Summoning Circle · overseers](tech-summoning_circle_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"SummoningCircle\", \"callSource\": \"source/Assets.Source.Player.Tech/T8SummoningCircle.cs\", \"callLine\": 25, \"id\": \"summoning_circle_automation\", \"root\": \"summoning_circle\", \"tier\": 8, \"name\": \"Mad Hermit\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"summoning_circle\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:25`
