# Quest Board

Offers a wide variety of Quests for your adventurers to undertake and earn rewards.

## Research effect

Offers a wide variety of Quests for your adventurers to undertake and earn rewards.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | quest_board |
| Type | Flow Element |
| Cost tier | 5 |

## Prerequisites

| Required research |
| --- |
| [Adventurer's Guild](tech-adventurers_guild.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Patrol the Market](tech-patrol_market.md) |

## Leads to

| Research |
| --- |
| [New Hotness](tech-outfitter_skip_replace.md) |
| [Forest · second add-on slot](tech-forest_automation_2.md) |
| [Campfire · second add-on slot](tech-campfire_automation_2.md) |
| [Adventurer's Guild · second add-on slot](tech-adventurers_guild_automation_2.md) |
| [Training Grounds · second add-on slot](tech-training_grounds_automation_2.md) |
| [Quest Receptionist](tech-quest_board_automation.md) |
| [Negotiator](tech-quest_board_coins.md) |
| [Quest Board · second add-on slot](tech-quest_board_automation_2.md) |
| [Explorer](tech-quest_board_quality.md) |
| [Quest Board · third add-on slot](tech-quest_board_automation_3.md) |
| [Autodidact](tech-quest_board_training.md) |
| [Additional Workspace](tech-add_diagrams.md) |
| [Patrol the Market](tech-patrol_market.md) |
| [Exterminate Rats!](tech-exterminate_rats.md) |
| [Mine Sweep](tech-clear_mines.md) |
| [Wilderness Evangelism](tech-forest_evangelism.md) |
| [Decursing the Library](tech-dispel_library.md) |
| [Mercurial Reagents](tech-mercurial_reagents.md) |
| [Shield of the Innocent](tech-shield_innocent.md) |
| [Farmstead Liberator](tech-farmstead_liberator.md) |
| [Bank "Heist"](tech-bank_heist.md) |
| [Byrgenwald Expedition](tech-byrgenwald_expedition.md) |
| [Elemental Eradication](tech-elemental_eradication.md) |
| [Experimental Summons](tech-experimental_summons.md) |
| [Extinguish the Ritual](tech-extinguish_ritual.md) |
| [Aiding the Refugees](tech-aid_refugees.md) |
| [Adventure Supplies](tech-adventure_supplies.md) |
| [Adventure Supplies · second add-on slot](tech-adventure_supplies_automation_2.md) |
| [Inn](tech-inn.md) |
| [Enchanter · second add-on slot](tech-enchanter_automation_2.md) |
| [Disenchanter · second add-on slot](tech-disenchanter_automation_2.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"adventurers_guild\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_136\"",
  "ForceRootNode": "true",
  "CostMultiplier": "1.0",
  "CostCurrency": "CurrencyCollection.GoldMedal",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"patrol_market\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T5QuestBoard.cs:13`
- `Assets.Source.Player/TechNode.cs:1`
