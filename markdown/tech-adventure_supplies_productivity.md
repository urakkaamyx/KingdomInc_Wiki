# Adventure Supplies · overseers

Adventure Supplies · overseers is a tier 6 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventure_supplies_productivity |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Potion Dispenser](tech-adventure_supplies_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"AdventureSupplies\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurerSupplies.cs\", \"callLine\": 23, \"id\": \"adventure_supplies_productivity\", \"previous\": \"adventure_supplies_automation\", \"additional\": [\"war_effort\"], \"tier\": 6, \"name\": \"Adventure Supplies · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"adventure_supplies\", \"requires\": [\"adventure_supplies\", \"adventure_supplies_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:23`
