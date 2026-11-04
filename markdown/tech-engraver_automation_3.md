# Engraver · third add-on slot

Engraver · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engraver_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Parallel Engraving](tech-engraver_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"Engraver\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Engraver.cs\", \"callLine\": 23, \"id\": \"engraver_automation_3\", \"previous\": \"engraver_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Engraver · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"engraver\", \"requires\": [\"engraver\", \"engraver_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Engraver.cs:23`
