# Perfectly Preserved

Unlocks a new Upgrade for your Dungeon.

Increases quality of looted items by 10%.

## Research effect

Unlocks a new Upgrade for your Dungeon.

Increases quality of looted items by 10%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_item_loot |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Dungeon](tech-dungeon.md) |
| [Support Staff](tech-dungeon_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"dungeon_automation_2\"",
  "RelativePosition": "new Vector2Int(0, -180)",
  "IconName": "\"Icons_118\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Dungeon\", \"DungeonItemLoot\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:72`
- `Assets.Source.Player/TechNode.cs:1`
