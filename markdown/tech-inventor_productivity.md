# Inventor · overseers

Inventor · overseers is a tier 11 upgrade slot research node.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | inventor_productivity |
| Type | Upgrade Slot |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |
| [Automaton](tech-inventor_automation.md) |
| [War Effort](tech-war_effort.md) |

<details><summary>Implementation fields</summary>

```json
{
  "GeneratedBy": "TechNodeHelper",
  "Model": "{\"type\": \"UpgradeSlot\", \"source\": \"source/Assets.Source.Player/TechNodeHelper.cs\", \"line\": 143, \"generated\": true, \"building\": \"Inventor\", \"callSource\": \"source/Assets.Source.Player.Tech/T10Inventor.cs\", \"callLine\": 25, \"id\": \"inventor_productivity\", \"previous\": \"inventor_automation\", \"additional\": [\"war_effort\"], \"tier\": 11, \"name\": \"Inventor · overseers\", \"icon\": \"Icons2_76\", \"addon\": \"Overseer\", \"root\": \"inventor\", \"requires\": [\"inventor\", \"inventor_automation\", \"war_effort\"], \"grants\": [], \"resourceGrants\": []}"
}
```

</details>

## Sources

- `Assets.Source.Player/TechNodeHelper.cs:143`
- `Assets.Source.Player/TechNode.cs:1`
- `Assets.Source.Player.Tech/T10Inventor.cs:25`
