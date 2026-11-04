# Barracks · third add-on slot

Barracks · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | barracks_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Barracks](tech-barracks.md) |
| [Structured Recruitment](tech-barracks_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"Barracks\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Barracks.cs\", \"callLine\": 26, \"id\": \"barracks_automation_3\", \"previous\": \"barracks_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Barracks · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"barracks\", \"requires\": [\"barracks\", \"barracks_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Barracks.cs:26`
