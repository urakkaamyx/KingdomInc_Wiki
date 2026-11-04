# Shrine

Serves as a place of worship for your Clerics. Their devotion can be converted into powerful blessings.

## Research effect

Serves as a place of worship for your Clerics. Their devotion can be converted into powerful blessings.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | shrine |
| Type | Flow Element |
| Cost tier | 11 |

## Prerequisites

| Required research |
| --- |
| [Scribe](tech-scribe.md) |

## Additional condition

Requires war progress: Cathedral of Saint Ilonia

## Campaign condition

yensburg:2 (campaign ID : completed stage)

## Also grants research

| Unlocked automatically |
| --- |
| [Simple Prayer](tech-prayer_1.md) |

## Leads to

| Research |
| --- |
| [Unshakable Devotion](tech-dungeon_limit_break_2.md) |
| [Prayer Beads](tech-prayer_beads.md) |
| [Summon Cherub](tech-summon_cherub.md) |
| [Summon Valkyrie](tech-summon_valkyrie.md) |
| [Summon Arbiter](tech-summon_arbiter.md) |
| [Prayer Wheel](tech-shrine_automation.md) |
| [Shrine · second add-on slot](tech-shrine_automation_2.md) |
| [Shrine · overseers](tech-shrine_productivity.md) |
| [Shrine · artisans](tech-shrine_quality.md) |
| [Shrine · third add-on slot](tech-shrine_automation_3.md) |
| [Simple Prayer](tech-prayer_1.md) |
| [Blessed Prayer Beads](tech-blessed_prayer_beads.md) |
| [Ritual Prayer](tech-prayer_2.md) |
| [Indulgence](tech-indulgence.md) |
| [Blessed Armaments](tech-blessed_arms.md) |
| [Sanctified Equipment](tech-blessed_equipment.md) |
| [Pontiff's Ring](tech-pontiff_ring.md) |
| [Relic of the Martyr](tech-martyr_relic.md) |
| [Guardian's Pledge](tech-cr_paladin.md) |
| [Commune with Nature](tech-cr_shaman.md) |
| [Preaching to the Choir](tech-cr_evangelist.md) |
| [Prayer of Light](tech-cr_lightbringer.md) |
| [Purified Mago-tech](tech-purified_tech.md) |
| [Vanquisher's Sword](tech-vanquisher_sword.md) |
| [Blighted Dagger](tech-blighted_dagger.md) |
| [Ethereal Rapier](tech-blink_rapier.md) |
| [Flenser's Sword](tech-flenser_greatsword.md) |
| [Cyclopean Battleaxe](tech-unblinking_axe.md) |
| [Deadeye Bow](tech-deadeye_bow.md) |
| [Splintered Staff](tech-fragment_staff.md) |
| [Unlife Staff](tech-unlife_staff.md) |
| [Cleansed Nightmare](tech-cleansed_nightmare.md) |
| [Yensburg Catacombs](tech-dungeon_catacombs.md) |
| [War: Ironcrag Siege](tech-war_effort_north.md) |
| [Graveyard](tech-graveyard.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"scribe\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons2_44\"",
  "ForceRootNode": "true",
  "CostTier": "11",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"yensburg\", 2)",
  "CustomRequirementDesc": "\"@shrine_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"prayer_1\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T11Shrine.cs:11`
- `Assets.Source.Player/TechNode.cs:1`
