# Adventure Supplies · artisans

Adventure Supplies · artisans is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventure_supplies_quality |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Overseas Import](tech-adventure_supplies_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"AdventureSupplies\", \"callSource\": \"source/Assets.Source.Player.Tech/T5AdventurerSupplies.cs\", \"callLine\": 23, \"id\": \"adventure_supplies_quality\", \"previous\": \"adventure_supplies_automation_2\", \"tier\": 7, \"name\": \"Adventure Supplies · artisans\", \"icon\": \"Icons_118\", \"addon\": \"ResArtisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"adventure_supplies\", \"requires\": [\"adventure_supplies\", \"adventure_supplies_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T5AdventurerSupplies.cs:23`
