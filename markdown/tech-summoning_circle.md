# Summoning Circle

Summons forth extraplanar creatures to fight in your wars and serve as training fodder for your adventurers.

## Research effect

Summons forth extraplanar creatures to fight in your wars and serve as training fodder for your adventurers.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | summoning_circle |
| Type | Flow Element |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Jeweler](tech-jeweler.md) |

## Additional condition

Requires war progress: Terminus Gorge

## Campaign condition

eastern:3 (campaign ID : completed stage)

## Also grants research

| Unlocked automatically |
| --- |
| [Summon Gremlin](tech-summon_gremlin.md) |

## Leads to

| Research |
| --- |
| [Training Dummy](tech-training_grounds_dummy.md) |
| [Experimental Summons](tech-experimental_summons.md) |
| [Metamorphosis](tech-refiner_demon.md) |
| [Mad Hermit](tech-summoning_circle_automation.md) |
| [Summoning Circle · second add-on slot](tech-summoning_circle_automation_2.md) |
| [Summoning Circle · overseers](tech-summoning_circle_productivity.md) |
| [Summoning Circle · artisans](tech-summoning_circle_quality.md) |
| [Summoning Circle · third add-on slot](tech-summoning_circle_automation_3.md) |
| [Summon Gremlin](tech-summon_gremlin.md) |
| [Summon Hellspawn](tech-summon_hellspawn.md) |
| [Summon Watcher](tech-summon_observer.md) |
| [Summon Cherub](tech-summon_cherub.md) |
| [Summon Valkyrie](tech-summon_valkyrie.md) |
| [Summon Arbiter](tech-summon_arbiter.md) |
| [Demonic Initiation](tech-cr_demonologist.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"jeweler\"",
  "RelativePosition": "new Vector2Int(630, 0)",
  "IconName": "\"Icons_199\"",
  "ForceRootNode": "true",
  "CostMultiplier": "4.0",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"eastern\", 3)",
  "CustomRequirementDesc": "\"@summoning_circle_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"summon_gremlin\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8SummoningCircle.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
