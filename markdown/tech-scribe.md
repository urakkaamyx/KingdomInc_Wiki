# Scribe

Writes a variety of books and scrolls imbued with magical energy or spiritual significance.

## Research effect

Writes a variety of books and scrolls imbued with magical energy or spiritual significance.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | scribe |
| Type | Flow Element |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [Inventor](tech-inventor.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Blank Vellum](tech-blank_vellum.md) |
| [Blank Tome](tech-blank_tome.md) |

## Leads to

| Research |
| --- |
| [Feeding the Wildlife](tech-cr_beast_master.md) |
| [Enchanted Ink](tech-enchanted_ink.md) |
| [Anatomy Lesson](tech-cr_assassin.md) |
| [Demonic Initiation](tech-cr_demonologist.md) |
| [Enchanted Quill](tech-scribe_automation.md) |
| [Scribe · second add-on slot](tech-scribe_automation_2.md) |
| [Scribe · overseers](tech-scribe_productivity.md) |
| [Scribe · artisans](tech-scribe_quality.md) |
| [Scribe · third add-on slot](tech-scribe_automation_3.md) |
| [Blank Vellum](tech-blank_vellum.md) |
| [Blank Tome](tech-blank_tome.md) |
| [Mad Scribblings](tech-mad_scribblings.md) |
| [Scroll of Healing](tech-scroll_of_healing.md) |
| [Scroll of Radiance](tech-scroll_of_aoe_healing.md) |
| [Scroll of Disintegration](tech-scroll_of_damage.md) |
| [Scroll of Second Wind](tech-scroll_of_energy.md) |
| [Apothecary's Tome](tech-tome_of_health.md) |
| [Manual of Self-Improvement](tech-tome_of_stats.md) |
| [Libram of Awakening](tech-tome_of_energy.md) |
| [Study on Phytotoxins](tech-cr_survivalist.md) |
| [Pyromancy and You: An Introduction](tech-cr_pyromancer.md) |
| [Rock Carving for Dummies](tech-cr_lithomancer.md) |
| [Decoded Writings](tech-decoded_writings.md) |
| [Demonsteel Helm](tech-demonsteel_helm.md) |
| [Demonsteel Armor](tech-demonsteel_armor.md) |
| [Possessed Shield](tech-infected_shield.md) |
| [Malignant Mask](tech-hellish_mask.md) |
| [Malignant Cover](tech-hellish_cover.md) |
| [Archmage's Hat](tech-archmage_hat.md) |
| [Archmage's Robe](tech-archmage_robe.md) |
| [Dark Prophet's Hood](tech-prophet_hood.md) |
| [Dark Prophet's Robe](tech-prophet_robe.md) |
| [Library](tech-library.md) |
| [Shrine](tech-shrine.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"inventor\"",
  "RelativePosition": "new Vector2Int(630, 0)",
  "IconName": "\"Icons2_39\"",
  "ForceRootNode": "true",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"blank_vellum\");\n\t\t\t\tply.AddTech(\"blank_tome\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Scribe.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
