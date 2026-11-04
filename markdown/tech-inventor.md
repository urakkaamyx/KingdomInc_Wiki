# Inventor

The kingdom's Chief High Artificer is renowned for creating exciting new technology (side effects not guaranteed).

## Research effect

The kingdom's Chief High Artificer is renowned for creating exciting new technology (side effects not guaranteed).

## Research data

| Property | Value |
| --- | --- |
| Internal ID | inventor |
| Type | Flow Element |
| Cost tier | 10 |

## Prerequisites

| Required research |
| --- |
| [War: Hidden Enemies](tech-war_effort_yensburg.md) |

## Additional condition

Requires war progress: Artisan Row

## Campaign condition

yensburg:1 (campaign ID : completed stage)

## Also grants research

| Unlocked automatically |
| --- |
| [Tinker](tech-tinker.md) |

## Leads to

| Research |
| --- |
| [Tinkersteel Armor](tech-tinkersteel_armor.md) |
| [Tinkersteel Helm](tech-tinkersteel_helm.md) |
| [Tinkersteel Sword](tech-tinkersteel_sword.md) |
| [Tinkersteel Dagger](tech-tinkersteel_dagger.md) |
| [Tinkersteel Rapier](tech-tinkersteel_rapier.md) |
| [Tinkersteel Greatsword](tech-tinkersteel_greatsword.md) |
| [Tinkersteel Battleaxe](tech-tinkersteel_axe.md) |
| [Witch Robe](tech-witch_robe.md) |
| [Witch Hood](tech-witch_hood.md) |
| [Trueshot Bow](tech-trueshot_bow.md) |
| [Petrified Shield](tech-petrified_shield.md) |
| [Archmage's Staff](tech-archmage_staff.md) |
| [Archbishop's Staff](tech-archbishop_staff.md) |
| [Primal String](tech-primal_string.md) |
| [Primal Cover](tech-primal_cover.md) |
| [Primal Mask](tech-primal_mask.md) |
| [Stable Wormhole](tech-portal_cost_reduce_2.md) |
| [Automaton](tech-inventor_automation.md) |
| [Inventor · second add-on slot](tech-inventor_automation_2.md) |
| [Inventor · overseers](tech-inventor_productivity.md) |
| [Inventor · artisans](tech-inventor_quality.md) |
| [Inventor · third add-on slot](tech-inventor_automation_3.md) |
| [Tinker](tech-tinker.md) |
| [Widget](tech-widget.md) |
| [Gizmo](tech-gizmo.md) |
| [Doodad](tech-doodad.md) |
| [Mechanical Experimentation](tech-mechanical_experiment.md) |
| [Alchemical Experimentation](tech-alchemical_experiment.md) |
| [Biological Experimentation](tech-biological_experiment.md) |
| [Tinkersteel](tech-tinkersteel.md) |
| [Witchcloth](tech-witchcloth.md) |
| [Primal Leather](tech-primal_leather.md) |
| [Petrified Wood](tech-petrified_wood.md) |
| [Winged Boots](tech-winged_boots.md) |
| [Golem Gauntlets](tech-golem_gauntlets.md) |
| [Leyline Goggles](tech-mind_goggles.md) |
| [Assassin's Goggles](tech-crit_goggles.md) |
| [Chainsaw](tech-chainsaw.md) |
| [Puppet Shield](tech-shield_arm.md) |
| [Triune Protector](tech-triune_shield.md) |
| [Nightmare Collector](tech-nightmare_collector.md) |
| [Currency Exchange](tech-currency_exchange.md) |
| [Scribe](tech-scribe.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"war_effort_yensburg\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons2_38\"",
  "ForceRootNode": "true",
  "CostTier": "10",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"yensburg\", 1)",
  "CustomRequirementDesc": "\"@inventor_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"tinker\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T10Inventor.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
