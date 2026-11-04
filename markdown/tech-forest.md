# Forest

Hunters, loggers and foragers provide a wide variety of supplies to your kingdom.

## Research effect

Hunters, loggers and foragers provide a wide variety of supplies to your kingdom.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | forest |
| Type | Flow Element |
| Cost tier | 4 |

## Prerequisites

| Required research |
| --- |
| [War Effort](tech-war_effort.md) |

## Additional condition

Requires war progress: Byrgenwald

## Campaign condition

forest:1 (campaign ID : completed stage)

## Also grants research

| Unlocked automatically |
| --- |
| [Harvest Wood Log](tech-forest_wood_log.md) |
| [Wolf Hunt](tech-forest_wolf_hide.md) |
| [Harvest Bird Eggs](tech-forest_bird_egg.md) |

## Leads to

| Research |
| --- |
| [Softwood Plank](tech-wood_plank.md) |
| [Rough Leather](tech-rough_leather.md) |
| [Embroider Clothing: Wisdom](tech-engrave_light_armor_wis.md) |
| [Engrave Weapon: Wisdom](tech-engrave_weapon_wis.md) |
| [Cross-country Carriers](tech-forest_automation.md) |
| [Forest · second add-on slot](tech-forest_automation_2.md) |
| [Forest · overseers](tech-forest_productivity.md) |
| [Forest · artisans](tech-forest_quality.md) |
| [Forest · third add-on slot](tech-forest_automation_3.md) |
| [Animated Workforce](tech-forest_workforce.md) |
| [Harvest Wood Log](tech-forest_wood_log.md) |
| [Wolf Hunt](tech-forest_wolf_hide.md) |
| [Harvest Bird Eggs](tech-forest_bird_egg.md) |
| [Harvest Lettuce](tech-forest_lettuce.md) |
| [Boar Hunt](tech-forest_boar_meat.md) |
| [Harvest Resin](tech-forest_resin.md) |
| [Harvest Bone](tech-forest_bone.md) |
| [Harvest Mushrooms](tech-forest_mushroom.md) |
| [Harvest Ancient Wood](tech-forest_ancient_wood.md) |
| [Stalker Hunt](tech-forest_supple_leather.md) |
| [Harvest Wild Onion](tech-forest_wild_onion.md) |
| [Manifold](tech-manifold.md) |
| [Campfire](tech-campfire.md) |
| [Turtle Statue](tech-turtle_statue.md) |
| [Adventurer's Guild](tech-adventurers_guild.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"war_effort\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_65\"",
  "ForceRootNode": "true",
  "CostTier": "4",
  "CostMultiplier": "8.0",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"forest\", 1)",
  "CustomRequirementDesc": "\"@forest_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.ForestSettings = new ForestSettings();\n\t\t\t\tply.ForestSettings.AddWorkerCount(ForestWorker.Unassigned, 3);\n\t\t\t\tply.ForestSettings.AddWorkerCount(ForestWorker.Hunter, 1);\n\t\t\t\tply.ForestSettings.AddWorkerCount(ForestWorker.Logger, 1);\n\t\t\t\tply.ForestSettings.AddWorkerCount(ForestWorker.Forager, 1);\n\t\t\t\tply.AddTech(\"forest_wood_log\");\n\t\t\t\tply.AddTech(\"forest_wolf_hide\");\n\t\t\t\tply.AddTech(\"forest_bird_egg\");\n\t\t\t\tGameUI.Instance.UpdateForestCrewButton();\n\t\t\t\tTutorialUI.Instance?.ShowForestArrow(show: true);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T4Forest.cs:14`
- `Assets.Source.Player/TechNode.cs:1`
