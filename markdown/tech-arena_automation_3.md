# Arena · third add-on slot

Arena · third add-on slot is a tier 11 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arena_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Arena](tech-arena.md) |
| [Hypogeum](tech-arena_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"Arena\", \"callSource\": \"source/Assets.Source.Player.Tech/T9Arena.cs\", \"callLine\": 25, \"id\": \"arena_automation_3\", \"previous\": \"arena_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 11, \"name\": \"Arena · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"arena\", \"requires\": [\"arena\", \"arena_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T9Arena.cs:25`
