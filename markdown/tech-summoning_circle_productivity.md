# Summoning Circle · overseers

Summoning Circle · overseers is a tier 9 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | summoning_circle_productivity |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Summoning Circle](tech-summoning_circle.md) |
| [Mad Hermit](tech-summoning_circle_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"SummoningCircle\", \"callSource\": \"source/Assets.Source.Player.Tech/T8SummoningCircle.cs\", \"callLine\": 25, \"id\": \"summoning_circle_productivity\", \"previous\": \"summoning_circle_automation\", \"additional\": [\"war_effort\"], \"tier\": 9, \"name\": \"Summoning Circle · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"summoning_circle\", \"requires\": [\"summoning_circle\", \"summoning_circle_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T8SummoningCircle.cs:25`
