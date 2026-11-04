# Engraver

Enhances the equipment created by your workers by inscribing them with magical runes.

## Research effect

Enhances the equipment created by your workers by inscribing them with magical runes.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | engraver |
| Type | Flow Element |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [War Effort](tech-war_effort.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Gold Wire](tech-gold_wire.md) |
| [Silver Thread](tech-silver_thread.md) |

## Leads to

| Research |
| --- |
| [Mine Gold Ore](tech-mine_gold_ore.md) |
| [Mine Silver Ore](tech-mine_silver_ore.md) |
| [Runic Apprentice](tech-engraver_automation.md) |
| [Engraver · second add-on slot](tech-engraver_automation_2.md) |
| [Engraver · overseers](tech-engraver_productivity.md) |
| [Engraver · artisans](tech-engraver_quality.md) |
| [Engraver · third add-on slot](tech-engraver_automation_3.md) |
| [Gold Wire](tech-gold_wire.md) |
| [Silver Thread](tech-silver_thread.md) |
| [Engrave Heavy Armor: Health](tech-engrave_heavy_armor_health.md) |
| [Embroider Clothing: Health](tech-engrave_light_armor_health.md) |
| [Engrave Heavy Armor: Defense](tech-engrave_heavy_armor_armor.md) |
| [Embroider Clothing: Defense](tech-engrave_light_armor_armor.md) |
| [Embroider Clothing: Dexterity](tech-engrave_light_armor_dex.md) |
| [Embroider Clothing: Magic](tech-engrave_light_armor_mag.md) |
| [Embroider Clothing: Wisdom](tech-engrave_light_armor_wis.md) |
| [Engrave Weapon: Strength](tech-engrave_weapon_str.md) |
| [Engrave Weapon: Dexterity](tech-engrave_weapon_dex.md) |
| [Engrave Weapon: Magic](tech-engrave_weapon_mag.md) |
| [Engrave Weapon: Wisdom](tech-engrave_weapon_wis.md) |
| [Embroidered Cotton](tech-embroidered_cotton.md) |
| [Embossed Leather](tech-embossed_leather.md) |
| [Engraved Jewelry](tech-engrave_jewelry_quality.md) |
| [Gilded Coffin](tech-gilded_coffin.md) |
| [Timer](tech-timer_node.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"war_effort\"",
  "RelativePosition": "new Vector2Int(-630, 0)",
  "IconName": "\"Icons_84\"",
  "ForceRootNode": "true",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"gold_wire\");\n\t\t\t\tply.AddTech(\"silver_thread\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3Engraver.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
