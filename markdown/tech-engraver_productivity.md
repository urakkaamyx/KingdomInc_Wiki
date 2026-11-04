# Engraver · overseers

Engraver · overseers is a tier 4 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engraver_productivity |
| Type | Upgrade Slot |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [Engraver](tech-engraver.md) |
| [Runic Apprentice](tech-engraver_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Engraver\", \"callSource\": \"source/Assets.Source.Player.Tech/T3Engraver.cs\", \"callLine\": 23, \"id\": \"engraver_productivity\", \"previous\": \"engraver_automation\", \"additional\": [\"war_effort\"], \"tier\": 4, \"name\": \"Engraver · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"engraver\", \"requires\": [\"engraver\", \"engraver_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T3Engraver.cs:23`
