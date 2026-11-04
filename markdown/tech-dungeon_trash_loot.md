# Trash Loot

Unlocks a new Upgrade for your Dungeon.

While walking in a dungeon's intermission stage, adventurers have a small chance to collect additional Ducats.

## Research effect

Unlocks a new Upgrade for your Dungeon.

While walking in a dungeon's intermission stage, adventurers have a small chance to collect additional Ducats.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_trash_loot |
| Type | Upgrade Slot |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Dungeon](tech-dungeon.md) |
| [Dungeon Keeper](tech-dungeon_automation.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"dungeon_automation\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons_197\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Dungeon\", \"DungeonTrashLoot\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:37`
- `Assets.Source.Player/TechNode.cs:1`
