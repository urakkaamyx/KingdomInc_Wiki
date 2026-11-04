# Warlock

A mage that has specialized in the unseen magics that surround us all.

## In the game

A mage that has specialized in the unseen magics that surround us all.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | warlock |
| Item type | Adventurer |
| Resource Value | 4000 |
| Archetype | Mage |
| Power Stat | Magic |
| Power Multiplier | 1.5 |
| Source Quest | true |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Introduction to Necromancy](recipe-cr_necrolyte.md) | 1 |
| [Demonic Initiation](recipe-cr_demonologist.md) | 1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Necrolyte | Crafting | See advancement implementation |
| Demonologist | Crafting | See advancement implementation |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_106\"",
  "ResourceValue": "4000L",
  "Archetype": "AdventurerArchetype.Mage",
  "PowerStat": "EquipStat.Magic",
  "PowerMultiplier": "1.5f",
  "AdvancementUnlocked": "(GamePlayer ply) => ply.HasTech(\"experimental_summons\")",
  "SourceQuest": "true",
  "ClassTraits": "new List<AdventurerTrait> { AdventurerTrait.ClassWarlock }",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@necrolyte\",\n\t\t\t\t\tDescription = \"@necrolyte_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_131\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@demonologist\",\n\t\t\t\t\tDescription = \"@demonologist_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_133\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:365`
