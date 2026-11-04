# Unshakable Devotion

Unlocks a new Upgrade for your Dungeon.

Adventurers cannot drop below 1 energy. Consumes 5 Faith for each point of energy lost while in this state.

## Research effect

Unlocks a new Upgrade for your Dungeon.

Adventurers cannot drop below 1 energy. Consumes 5 Faith for each point of energy lost while in this state.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon_limit_break_2 |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Dungeon](tech-dungeon.md) |
| [Together As One](tech-dungeon_limit_break.md) |
| [Shrine](tech-shrine.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"dungeon_limit_break\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons2_50\"",
  "CostTier": "11",
  "CostMultiplier": "2.5",
  "AdditionalRequirements": "new List<string> { \"shrine\" }",
  "CostCurrency": "CurrencyCollection.GoldFaith",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Dungeon\", \"DungeonLimitBreak2\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:83`
- `Assets.Source.Player/TechNode.cs:1`
