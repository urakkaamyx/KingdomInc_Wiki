# Guardian

A fighter that has specialized in protecting their party members.

## In the game

A fighter that has specialized in protecting their party members.

## Reference values

| Property | Value |
| --- | --- |
| Item ID | guardian |
| Item type | Adventurer |
| Resource Value | 4000 |
| Archetype | Fighter |
| Power Stat | Strength |
| Power Multiplier | 1.5 |
| Source Quest | true |

## Used in

| Recipe | Units per batch |
| --- | --- |
| [Guardian's Pledge](recipe-cr_paladin.md) | 1 |

## Class advancement

Requirements are evaluated against the individual adventurer. Exact predicates are shown for conditional equipment requirements.

| Result | Where | Requirement |
| --- | --- | --- |
| Paladin | Crafting | See advancement implementation |
| [Bulwark](item-bulwark.md) | Arena | (HumanItemData adv) => adv.HasShield |

<details><summary>Implementation fields</summary>

```json
{
  "IconName": "\"Icons2_96\"",
  "ResourceValue": "4000L",
  "Archetype": "AdventurerArchetype.Fighter",
  "PowerStat": "EquipStat.Strength",
  "PowerMultiplier": "1.5f",
  "AdvancementUnlocked": "(GamePlayer ply) => ply.HasTech(\"shield_innocent\")",
  "SourceQuest": "true",
  "ClassTraits": "new List<AdventurerTrait> { AdventurerTrait.ClassGuardian }",
  "Advancements": "new List<AdventurerAdvancement>\n\t\t\t{\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@paladin\",\n\t\t\t\t\tDescription = \"@paladin_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_111\",\n\t\t\t\t\tSource = AdvancementSource.Crafting\n\t\t\t\t},\n\t\t\t\tnew AdventurerAdvancement\n\t\t\t\t{\n\t\t\t\t\tDisplayName = \"@bulwark\",\n\t\t\t\t\tDescription = \"@bulwark_adv_desc\",\n\t\t\t\t\tIconName = \"Icons2_113\",\n\t\t\t\t\tSource = AdvancementSource.Arena,\n\t\t\t\t\tAvailable = (HumanItemData adv) => adv.HasShield,\n\t\t\t\t\tApply = (HumanItemData adv) =>\n\t\t\t\t\t{\n\t\t\t\t\t\tadv.Item.ChangeItemType(\"bulwark\");\n\t\t\t\t\t}\n\t\t\t\t}\n\t\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:205`
