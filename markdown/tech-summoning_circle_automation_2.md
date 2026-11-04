# Summoning Circle · second add-on slot

Summoning Circle · second add-on slot is a tier 9 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | summoning_circle_automation_2 |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Summoning Circle](tech-summoning_circle.md) |
| [Mad Hermit](tech-summoning_circle_automation.md) |
| [War Effort](tech-war_effort.md) |
| [Dungeon](tech-dungeon.md) |

## Leads to

| Research |
| --- |
| [Summoning Circle · artisans](tech-summoning_circle_quality.md) |
| [Summoning Circle · third add-on slot](tech-summoning_circle_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 28, \"generated\": true, \"building\": \"SummoningCircle\", \"callSource\": \"source/Assets.Source.Player.Tech/T8SummoningCircle.cs\", \"callLine\": 25, \"id\": \"summoning_circle_automation_2\", \"previous\": \"summoning_circle_automation\", \"tier\": 9, \"additional\": [\"war_effort\", \"dungeon\"], \"name\": \"Summoning Circle · second add-on slot\", \"icon\": \"Icons_18\", \"slotCount\": 2, \"root\": \"summoning_circle\", \"requires\": [\"summoning_circle\", \"summoning_circle_automation\", \"war_effort\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:28`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:25`
