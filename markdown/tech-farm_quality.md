# Farm · artisans

Unlocks the Fertilizer upgrade to increase the quality of farm items, at an additional cost per item.

## Research effect

Unlocks the Fertilizer upgrade to increase the quality of farm items, at an additional cost per item.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm_quality |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |
| [Honest Work](tech-farm_automation_2.md) |

## Additional condition

Requires war progress: Byrgenwald College

## Campaign condition

forest:2 (campaign ID : completed stage)

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 94, \"generated\": true, \"building\": \"Farm\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Farm.cs\", \"callLine\": 35, \"id\": \"farm_quality\", \"previous\": \"farm_automation_2\", \"tier\": 9, \"name\": \"Farm · artisans\", \"icon\": \"Icons_118\", \"addon\": \"FarmArtisan\", \"warGate\": \"forest:2\", \"conditionText\": \"Requires war progress: Byrgenwald College\", \"root\": \"farm\", \"requires\": [\"farm\", \"farm_automation_2\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:94`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Farm.cs:35`
