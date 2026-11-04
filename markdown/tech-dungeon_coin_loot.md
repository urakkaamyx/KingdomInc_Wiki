# Ancient Treasures

Unlocks a new Upgrade for your Dungeon.

Increases currency looted in the Dungeon by 10%.

## Research effect

Unlocks a new Upgrade for your Dungeon.

Increases currency looted in the Dungeon by 10%.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_coin_loot |
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
  "RelativePosition": "new Vector2Int(0, -180)",
  "IconName": "\"Icons_119\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Dungeon\", \"DungeonCoinLoot\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:48`
- `Assets.Source.Player/TechNode.cs:1`
