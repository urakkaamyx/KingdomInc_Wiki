# Adventurer's Guild

Allows you to recruit rookie adventurers, ready for training and questing.

## Research effect

Allows you to recruit rookie adventurers, ready for training and questing.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | adventurers_guild |
| Type | Flow Element |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Forest](tech-forest.md) |

## Additional condition

Requires war progress: Yensmouth

## Campaign condition

forest:4 (campaign ID : completed stage)

## Also grants research

| Unlocked automatically |
| --- |
| [Recruit Adventurers](tech-recruit_adventurer.md) |

## Resource quota granted

| Resource | Amount |
| --- | --- |
| [Adventurer](item-adventurer.md) | 0.20000000298023224 |

## Leads to

| Research |
| --- |
| [Overseas Export](tech-requisition_office_contract_3.md) |
| [Recruit Adventurers](tech-recruit_adventurer.md) |
| [Tech List View](tech-global_tech_upgrade.md) |
| [Reception Desk](tech-adventurers_guild_automation.md) |
| [Adventurer's Guild · second add-on slot](tech-adventurers_guild_automation_2.md) |
| [Adventurer's Guild · overseers](tech-adventurers_guild_productivity.md) |
| [Adventurer's Guild · artisans](tech-adventurers_guild_quality.md) |
| [Adventurer's Guild · third add-on slot](tech-adventurers_guild_automation_3.md) |
| [Training Grounds](tech-training_grounds.md) |
| [Quest Board](tech-quest_board.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"forest\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_67\"",
  "ForceRootNode": "true",
  "CostTier": "5",
  "CostCurrency": "CurrencyCollection.GoldMedal",
  "CostMultiplier": "2.0",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"forest\", 4)",
  "CustomRequirementDesc": "\"@adventurers_guild_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddResource(\"adventurer\", 0.20000000298023224);\n\t\t\t\tply.AddTech(\"recruit_adventurer\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5AdventurersGuild.cs:24`
- `Assets.Source.Player/TechNode.cs:1`
