# Blacksmith

Crafts a variety of items made primarily of metal.

## Research effect

Crafts a variety of items made primarily of metal.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | blacksmith |
| Type | Flow Element |
| Cost tier | 1 |

## Prerequisites

| Required research |
| --- |
| [Forge](tech-forge.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Iron Armor](tech-iron_armor.md) |

## Leads to

| Research |
| --- |
| [Apprenticeship](tech-blacksmith_automation.md) |
| [Blacksmith · second add-on slot](tech-blacksmith_automation_2.md) |
| [Blacksmith · overseers](tech-blacksmith_productivity.md) |
| [Blacksmith · artisans](tech-blacksmith_quality.md) |
| [Blacksmith · third add-on slot](tech-blacksmith_automation_3.md) |
| [Iron Armor](tech-iron_armor.md) |
| [Iron Helm](tech-iron_helm.md) |
| [Iron Sword](tech-iron_sword.md) |
| [Iron Dagger](tech-iron_dagger.md) |
| [Iron Greatsword](tech-iron_greatsword.md) |
| [Iron Battleaxe](tech-iron_battleaxe.md) |
| [Ceremonial Sword](tech-gold_sword.md) |
| [Parade Armor](tech-gold_armor.md) |
| [Sapphire Crown](tech-gold_crown.md) |
| [Iron Rapier](tech-iron_rapier.md) |
| [Ancient Woodcutter](tech-ancient_woodcutter.md) |
| [Arcanite Chestguard](tech-arcanium_armor.md) |
| [Arcanite Casque](tech-arcanium_helm.md) |
| [Arcanite Blade](tech-arcanium_sword.md) |
| [Arcanite Backstabber](tech-arcanium_dagger.md) |
| [Arcanite Claymore](tech-arcanium_greatsword.md) |
| [Arcanite Cleaver](tech-arcanium_battleaxe.md) |
| [Tinkersteel Armor](tech-tinkersteel_armor.md) |
| [Tinkersteel Helm](tech-tinkersteel_helm.md) |
| [Tinkersteel Sword](tech-tinkersteel_sword.md) |
| [Tinkersteel Dagger](tech-tinkersteel_dagger.md) |
| [Tinkersteel Rapier](tech-tinkersteel_rapier.md) |
| [Tinkersteel Greatsword](tech-tinkersteel_greatsword.md) |
| [Tinkersteel Battleaxe](tech-tinkersteel_axe.md) |
| [Nightmare Casing](tech-nightmare_casing.md) |
| [Node Duplication](tech-unlock_picker.md) |
| [Supply Depot](tech-supply_depot.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"forge\"",
  "RelativePosition": "new Vector2Int(630, 0)",
  "IconName": "\"Icons_2\"",
  "CostMultiplier": "0.5",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"iron_armor\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T1Blacksmith.cs:11`
- `Assets.Source.Player/TechNode.cs:1`
