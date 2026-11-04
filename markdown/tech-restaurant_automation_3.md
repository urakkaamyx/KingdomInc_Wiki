# Restaurant · third add-on slot

Restaurant · third add-on slot is a tier 9 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | restaurant_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Restaurant](tech-restaurant.md) |
| [24/7 Service](tech-restaurant_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"Restaurant\", \"callSource\": \"source/Assets.Source.Player.Tech/T7Kitchen.cs\", \"callLine\": 56, \"id\": \"restaurant_automation_3\", \"previous\": \"restaurant_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 9, \"name\": \"Restaurant · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"restaurant\", \"requires\": [\"restaurant\", \"restaurant_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T7Kitchen.cs:56`
