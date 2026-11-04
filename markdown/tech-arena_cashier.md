# Fight Purse

Unlocks a new Upgrade for your Arena.

Increases gold income from arena fights by {0}.

## Research effect

Unlocks a new Upgrade for your Arena.

Increases gold income from arena fights by {0}.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arena_cashier |
| Type | Upgrade Slot |
| Cost tier | 9 |

## Prerequisites

| Required research |
| --- |
| [Arena](tech-arena.md) |
| [Fight Announcer](tech-arena_automation.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"arena_automation\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "Description": "Translation.TranslateOnly(\"@arena_cashier_desc\", GameMath.FormatPercentage(0.10000000149011612))",
  "IconName": "\"Icons_119\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Arena\", \"ArenaCashier\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Arena.cs:26`
- `Assets.Source.Player/TechNode.cs:1`
