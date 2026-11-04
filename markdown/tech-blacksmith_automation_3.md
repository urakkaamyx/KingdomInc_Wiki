# Blacksmith · third add-on slot

Blacksmith · third add-on slot is a tier 7 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blacksmith_automation_3 |
| Type | Upgrade Slot |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [Blacksmith](tech-blacksmith.md) |
| [Attentive Workers](tech-blacksmith_automation_2.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 73, \"generated\": true, \"building\": \"Blacksmith\", \"callSource\": \"source/Assets.Source.Player.Tech/T1Blacksmith.cs\", \"callLine\": 23, \"id\": \"blacksmith_automation_3\", \"previous\": \"blacksmith_automation_2\", \"additional\": [\"dungeon\"], \"tier\": 7, \"name\": \"Blacksmith · third add-on slot\", \"icon\": \"Icons2_77\", \"slotCount\": 3, \"root\": \"blacksmith\", \"requires\": [\"blacksmith\", \"blacksmith_automation_2\", \"dungeon\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:73`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T1Blacksmith.cs:23`
