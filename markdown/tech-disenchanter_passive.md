# Aether Collector

Unlocks a new Upgrade for your Disenchanter.

Passively generates Mana over time.

## Research effect

Unlocks a new Upgrade for your Disenchanter.

Passively generates Mana over time.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | disenchanter_passive |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Disenchanter](tech-disenchanter.md) |
| [Enhanced Collectors](tech-disenchanter_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"disenchanter_automation_2\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "CostCurrency": "CurrencyCollection.GoldMana",
  "IconName": "\"Icons_162\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Disenchanter\", \"ManaPassive\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T6Disenchanter.cs:33`
- `Assets.Source.Player/TechNode.cs:1`
