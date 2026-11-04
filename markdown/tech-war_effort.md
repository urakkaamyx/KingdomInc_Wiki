# War Effort

Send soldiers to fight in the various battles that threaten the safety of Yensburg.

## Research effect

Send soldiers to fight in the various battles that threaten the safety of Yensburg.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | war_effort |
| Type | Flow Element |
| Cost tier | 3 |

## Prerequisites

| Required research |
| --- |
| [Barracks](tech-barracks.md) |

## Also grants research

| Unlocked automatically |
| --- |
| [Southside Brigands](tech-war_effort_forest.md) |

## Leads to

| Research |
| --- |
| [Mine · second add-on slot](tech-mine_automation_2.md) |
| [Mine · overseers](tech-mine_productivity.md) |
| [Forge · second add-on slot](tech-forge_automation_2.md) |
| [Forge · overseers](tech-forge_productivity.md) |
| [Item Shop · second add-on slot](tech-shop_automation_2.md) |
| [Item Shop coffers](tech-shop_coffers.md) |
| [Blacksmith · second add-on slot](tech-blacksmith_automation_2.md) |
| [Blacksmith · overseers](tech-blacksmith_productivity.md) |
| [Supply Depot · second add-on slot](tech-supply_depot_automation_2.md) |
| [Supply Depot · overseers](tech-supply_depot_productivity.md) |
| [Requisition Office · second add-on slot](tech-requisition_office_automation_2.md) |
| [Red Tape Specialist](tech-requisition_office_passive.md) |
| [Mass Requisition](tech-requisition_office_contract_2.md) |
| [Tailor · second add-on slot](tech-tailor_automation_2.md) |
| [Tailor · overseers](tech-tailor_productivity.md) |
| [Carpenter · second add-on slot](tech-carpenter_automation_2.md) |
| [Carpenter · overseers](tech-carpenter_productivity.md) |
| [Leatherworker · second add-on slot](tech-leatherworker_automation_2.md) |
| [Leatherworker · overseers](tech-leatherworker_productivity.md) |
| [Barracks · second add-on slot](tech-barracks_automation_2.md) |
| [Barracks · overseers](tech-barracks_productivity.md) |
| [Southside Brigands](tech-war_effort_forest.md) |
| [Participation Trophy](tech-war_effort_passive.md) |
| [Button](tech-single_button.md) |
| [Switch](tech-track_switch.md) |
| [Engraver](tech-engraver.md) |
| [Engraver · second add-on slot](tech-engraver_automation_2.md) |
| [Engraver · overseers](tech-engraver_productivity.md) |
| [Forest](tech-forest.md) |
| [Forest · second add-on slot](tech-forest_automation_2.md) |
| [Forest · overseers](tech-forest_productivity.md) |
| [Campfire · second add-on slot](tech-campfire_automation_2.md) |
| [Campfire · overseers](tech-campfire_productivity.md) |
| [Adventurer's Guild · second add-on slot](tech-adventurers_guild_automation_2.md) |
| [Adventurer's Guild · overseers](tech-adventurers_guild_productivity.md) |
| [Training Grounds · second add-on slot](tech-training_grounds_automation_2.md) |
| [Quest Board · second add-on slot](tech-quest_board_automation_2.md) |
| [Adventure Supplies · second add-on slot](tech-adventure_supplies_automation_2.md) |
| [Adventure Supplies · overseers](tech-adventure_supplies_productivity.md) |
| [Enchanter · second add-on slot](tech-enchanter_automation_2.md) |
| [Enchanter · overseers](tech-enchanter_productivity.md) |
| [Disenchanter · second add-on slot](tech-disenchanter_automation_2.md) |
| [Farm · second add-on slot](tech-farm_automation_2.md) |
| [Farm · overseers](tech-farm_productivity.md) |
| [Kitchen · second add-on slot](tech-kitchen_automation_2.md) |
| [Kitchen · overseers](tech-kitchen_productivity.md) |
| [Restaurant · second add-on slot](tech-restaurant_automation_2.md) |
| [Butcher · second add-on slot](tech-butcher_automation_2.md) |
| [Butcher · overseers](tech-butcher_productivity.md) |
| [Dungeon · second add-on slot](tech-dungeon_automation_2.md) |
| [Jeweler · second add-on slot](tech-jeweler_automation_2.md) |
| [Jeweler · overseers](tech-jeweler_productivity.md) |
| [Summoning Circle · second add-on slot](tech-summoning_circle_automation_2.md) |
| [Summoning Circle · overseers](tech-summoning_circle_productivity.md) |
| [Alchemist · second add-on slot](tech-alchemist_automation_2.md) |
| [Alchemist · overseers](tech-alchemist_productivity.md) |
| [Arena · second add-on slot](tech-arena_automation_2.md) |
| [Inventor · second add-on slot](tech-inventor_automation_2.md) |
| [Inventor · overseers](tech-inventor_productivity.md) |
| [Scribe · second add-on slot](tech-scribe_automation_2.md) |
| [Scribe · overseers](tech-scribe_productivity.md) |
| [Shrine · second add-on slot](tech-shrine_automation_2.md) |
| [Shrine · overseers](tech-shrine_productivity.md) |
| [Graveyard · second add-on slot](tech-graveyard_automation_2.md) |
| [Graveyard · overseers](tech-graveyard_productivity.md) |
| [Necromancer · second add-on slot](tech-necromancer_automation_2.md) |
| [Necromancer · overseers](tech-necromancer_productivity.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"barracks\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_58\"",
  "ForceRootNode": "true",
  "CostCurrency": "CurrencyCollection.GoldRequisition",
  "CostMultiplier": "2.0",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tGamePlayer.Current.UnlockWar(\"forest\");\n\t\t\t\tGamePlayer.Current.AddTech(\"war_effort_forest\");\n\t\t\t\tGameUI.Instance.UpdateWarEffortButton();\n\t\t\t\tTutorialUI.Instance?.ShowWarEffortArrow(show: true);\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T3WarEffort.cs:11`
- `Assets.Source.Player/TechNode.cs:1`
