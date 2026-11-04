# Fight To The Death

Unlocks the Blood Sport upgrade: Combatants fight until only one is left standing. Training received is increased massively, especially in human-versus-human fights, and spectators pay more for a bloody finale.

## Research effect

Unlocks the Blood Sport upgrade: Combatants fight until only one is left standing. Training received is increased massively, especially in human-versus-human fights, and spectators pay more for a bloody finale.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | arena_blood_sport |
| Type | Upgrade Slot |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Arena](tech-arena.md) |
| [Hypogeum](tech-arena_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.UpgradeSlot",
  "Previous": "\"arena_automation_2\"",
  "RelativePosition": "new Vector2Int(0, 180)",
  "IconName": "\"Icons2_56\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddAvailableFlowUpgrade(\"Arena\", \"ArenaBloodSport\");\n\t\t\t\tWorldFlowManager.Instance.UpdateFlowElements(\"Arena\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T9Arena.cs:38`
- `Assets.Source.Player/TechNode.cs:1`
