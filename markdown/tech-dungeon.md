# Dungeon

Send a party of five adventurers down into the depths to defeat evil and recover valuable loot.

## Research effect

Send a party of five adventurers down into the depths to defeat evil and recover valuable loot.

## Research data

| Property | Value |
| --- | --- |
| Internal ID | dungeon |
| Type | Flow Element |
| Cost tier | 8 |

## Prerequisites

| Required research |
| --- |
| [Farm](tech-farm.md) |

## Additional condition

Requires war progress: Ruins of Arlingen

## Campaign condition

eastern:2 (campaign ID : completed stage)

## Also grants research

| Unlocked automatically |
| --- |
| [Ruins of Arlingen](tech-dungeon_ruins.md) |

## Leads to

| Research |
| --- |
| [Mine · third add-on slot](tech-mine_automation_3.md) |
| [Forge · third add-on slot](tech-forge_automation_3.md) |
| [Item Shop · third add-on slot](tech-shop_automation_3.md) |
| [Blacksmith · third add-on slot](tech-blacksmith_automation_3.md) |
| [Supply Depot · third add-on slot](tech-supply_depot_automation_3.md) |
| [Requisition Office · third add-on slot](tech-requisition_office_automation_3.md) |
| [Tailor · third add-on slot](tech-tailor_automation_3.md) |
| [Crystalline Staff](tech-ancient_int_staff.md) |
| [Staff of Sages](tech-ancient_wis_staff.md) |
| [Carpenter · third add-on slot](tech-carpenter_automation_3.md) |
| [Leatherworker · third add-on slot](tech-leatherworker_automation_3.md) |
| [Barracks · third add-on slot](tech-barracks_automation_3.md) |
| [Engraver · third add-on slot](tech-engraver_automation_3.md) |
| [Forest · third add-on slot](tech-forest_automation_3.md) |
| [Campfire · third add-on slot](tech-campfire_automation_3.md) |
| [Adventurer's Guild · third add-on slot](tech-adventurers_guild_automation_3.md) |
| [Quest Board · third add-on slot](tech-quest_board_automation_3.md) |
| [Bank "Heist"](tech-bank_heist.md) |
| [Adventure Supplies · third add-on slot](tech-adventure_supplies_automation_3.md) |
| [Elixir of Fire Resistance](tech-supply_fire_resist_potion.md) |
| [Elixir of Shadow Resistance](tech-supply_shadow_resist_potion.md) |
| [Enchanter · third add-on slot](tech-enchanter_automation_3.md) |
| [Annihilate Gemstone](tech-annihilate_gemstone.md) |
| [Disenchanter · third add-on slot](tech-disenchanter_automation_3.md) |
| [Farm · second add-on slot](tech-farm_automation_2.md) |
| [Farm · third add-on slot](tech-farm_automation_3.md) |
| [Kitchen · second add-on slot](tech-kitchen_automation_2.md) |
| [Kitchen · third add-on slot](tech-kitchen_automation_3.md) |
| [Restaurant · second add-on slot](tech-restaurant_automation_2.md) |
| [Restaurant · third add-on slot](tech-restaurant_automation_3.md) |
| [Butcher · second add-on slot](tech-butcher_automation_2.md) |
| [Butcher · third add-on slot](tech-butcher_automation_3.md) |
| [Dungeon Keeper](tech-dungeon_automation.md) |
| [Dungeon · second add-on slot](tech-dungeon_automation_2.md) |
| [Dungeon · third add-on slot](tech-dungeon_automation_3.md) |
| [Ruins of Arlingen](tech-dungeon_ruins.md) |
| [Trash Loot](tech-dungeon_trash_loot.md) |
| [Ancient Treasures](tech-dungeon_coin_loot.md) |
| [Together As One](tech-dungeon_limit_break.md) |
| [Perfectly Preserved](tech-dungeon_item_loot.md) |
| [Unshakable Devotion](tech-dungeon_limit_break_2.md) |
| [Guildhouse](tech-guildhouse.md) |
| [Jeweler](tech-jeweler.md) |
| [Jeweler · second add-on slot](tech-jeweler_automation_2.md) |
| [Jeweler · third add-on slot](tech-jeweler_automation_3.md) |
| [Summoning Circle · second add-on slot](tech-summoning_circle_automation_2.md) |
| [Summoning Circle · third add-on slot](tech-summoning_circle_automation_3.md) |
| [Alchemist · second add-on slot](tech-alchemist_automation_2.md) |
| [Alchemist · third add-on slot](tech-alchemist_automation_3.md) |
| [Arena · second add-on slot](tech-arena_automation_2.md) |
| [Arena · third add-on slot](tech-arena_automation_3.md) |
| [Inventor · second add-on slot](tech-inventor_automation_2.md) |
| [Inventor · third add-on slot](tech-inventor_automation_3.md) |
| [Scribe · second add-on slot](tech-scribe_automation_2.md) |
| [Scribe · third add-on slot](tech-scribe_automation_3.md) |
| [Shrine · second add-on slot](tech-shrine_automation_2.md) |
| [Shrine · third add-on slot](tech-shrine_automation_3.md) |
| [Graveyard · second add-on slot](tech-graveyard_automation_2.md) |
| [Graveyard · third add-on slot](tech-graveyard_automation_3.md) |
| [Necromancer · second add-on slot](tech-necromancer_automation_2.md) |
| [Necromancer · third add-on slot](tech-necromancer_automation_3.md) |

<details><summary>Implementation fields</summary>

```json
{
  "NodeType": "TechNodeType.FlowElement",
  "Previous": "\"farm\"",
  "RelativePosition": "new Vector2Int(0, 450)",
  "IconName": "\"Icons_195\"",
  "ForceRootNode": "true",
  "CostCurrency": "CurrencyCollection.GoldRing",
  "CostTier": "8",
  "CostMultiplier": "5.0",
  "CustomRequirement": "(GamePlayer ply) => ply.HasWarStage(\"eastern\", 2)",
  "CustomRequirementDesc": "\"@dungeon_unlock\"",
  "OnUnlock": "(GamePlayer ply) =>\n\t\t\t{\n\t\t\t\tply.AddTech(\"dungeon_ruins\");\n\t\t\t\tply.UnlockDungeon(\"ruins\");\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Player.Tech/T8Dungeon.cs:10`
- `Assets.Source.Player/TechNode.cs:1`
