# Farm

Allows you to cultivate your own food, raise animals, and grow powerful reagents directly from the soil.

## Research effect

Allows you to cultivate your own food, raise animals, and grow powerful reagents directly from the soil.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | farm |
| Type | Flow Element |
| Cost tier | 7 |

## Prerequisites

| Required research |
| --- |
| [War: Eastern Front](tech-war_effort_east.md) |

## Additional condition

Requires war progress: Arlingen Farmstead

## Campaign condition

eastern:1 (campaign ID : completed stage)

## Also grants research

| Unlocked automatically |
| --- |
| [Cattle Husbandry](tech-farm_cattle.md) |
| [Wheat Cultivation](tech-farm_wheat.md) |

## Leads to

| Research |
| --- |
| [Farmstead Liberator](tech-farmstead_liberator.md) |
| [Elemental Eradication](tech-elemental_eradication.md) |
| [Farmhand](tech-farm_automation.md) |
| [Farm · second add-on slot](tech-farm_automation_2.md) |
| [Farm · overseers](tech-farm_productivity.md) |
| [Farm · artisans](tech-farm_quality.md) |
| [Farm · third add-on slot](tech-farm_automation_3.md) |
| [Cattle Husbandry](tech-farm_cattle.md) |
| [Wheat Cultivation](tech-farm_wheat.md) |
| [Flax Cultivation](tech-farm_flax.md) |
| [Cotton Cultivation](tech-farm_cotton.md) |
| [Salamander Husbandry](tech-farm_salamander.md) |
| [Onion Cultivation](tech-farm_onion.md) |
| [Stalker Husbandry](tech-farm_stalker.md) |
| [Herb Cultivation](tech-farm_soothing_herbs.md) |
| [Portal](tech-portal.md) |
| [Kitchen](tech-kitchen.md) |
| [Dungeon](tech-dungeon.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"war_effort_east\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_182\"",
  "ForceRootNode": "true",
  "CostTier": "7",
  "CostMultiplier": "8.0",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"eastern\", 1)",
  "CustomRequirementDesc": "\"@farm_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.FarmSettings = new FarmSettings();\n\t\t\t\tply.AddTech(\"farm_cattle\");\n\t\t\t\tply.AddTech(\"farm_wheat\");\n\t\t\t\tGameUI.Instance.UpdateFarmButton();\n\t\t\t\tTutorialUI.Instance?.ShowFarmArrow(show: true);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T7Farm.cs:15`
- `Assets.Source.Player/TechNode.cs:1`
