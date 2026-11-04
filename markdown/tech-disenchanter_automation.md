# Mana Vacuum

Unlocks the first Upgrade slot for your Disenchanter.

Unlocks the Worker upgrade to automatically collect mana.

## Research effect

Unlocks the first Upgrade slot for your Disenchanter.

Unlocks the Worker upgrade to automatically collect mana.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | disenchanter_automation |
| Type | Upgrade Slot |
| Cost tier | 6 |

## Prerequisites

| Required research |
| --- |
| [Disenchanter](tech-disenchanter.md) |

## Leads to

| Research |
| --- |
| [Annihilation](tech-disenchanter_mana.md) |
| [Disenchanter · second add-on slot](tech-disenchanter_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 10, \"generated\": true, \"building\": \"Disenchanter\", \"callSource\": \"source/Assets.Source.Player.Tech/T6Disenchanter.cs\", \"callLine\": 18, \"id\": \"disenchanter_automation\", \"root\": \"disenchanter\", \"tier\": 6, \"name\": \"Mana Vacuum\", \"icon\": \"Icons_17\", \"slotCount\": 1, \"addon\": \"Worker\", \"requires\": [\"disenchanter\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T6Disenchanter.cs:18`
