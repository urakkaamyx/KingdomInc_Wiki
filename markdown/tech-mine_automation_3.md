# Mine · third add-on slot

Mine · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | mine_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Mine](tech-mine.md) |
| [Motivated Workers](tech-mine_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"Mine\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Mine.cs\", \"callLine\": 73, \"id\": \"mine_automation_3\", \"previous\": \"mine_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Mine · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"mine\", \"requires\": [\"mine\", \"mine_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Mine.cs:73`
