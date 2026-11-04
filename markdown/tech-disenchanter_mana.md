# Annihilation

Unlocks a new Upgrade for your Disenchanter.

Increases Mana gained from disenchanting items by {0}.

## Research effect

Unlocks a new Upgrade for your Disenchanter.

Increases Mana gained from disenchanting items by {0}.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | disenchanter_mana |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Disenchanter](tech-disenchanter.md) |
| [Mana Vacuum](tech-disenchanter_automation.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"disenchanter_automation\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "Description": "Translation.TranslateOnly(\"@disenchanter_mana_desc\", GameMath.FormatPercentage(0.10000000149011612))",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "IconName": "\"Icons2_168\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Disenchanter\", \"ManaCashier\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Disenchanter.cs:19`
- `Assets.Source.Player/TechNode.cs:1`
