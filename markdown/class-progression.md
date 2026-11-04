# Adventurer classes and advancement routes

The complete class tree and its equipment conditions.

## First specialization

With Training Grounds specialization research, an Adventurer is checked halfway through training unless the energy payment just exhausted it. The first matching declared advancement wins.

| Class | Requirement |
| --- | --- |
| Fighter | Main weapon’s declared main stat Strength; Heavy armor qualification |
| Rogue | Main weapon’s declared main stat Dexterity; Medium armor qualification |
| Mage | Main weapon’s declared main stat Magic; Light armor qualification |
| Cleric | Main weapon’s declared main stat Wisdom; no armor condition |

## Quest branches

Fighter branches to Guardian or Battlemaster; Rogue to Thief or Ranger; Mage to Elementalist or Warlock; Cleric to Ritualist or Priest. The eight advancement quests change only members whose type exactly matches the required base class. Repeat quest rewards retain the advancement effect.

## Final specializations

Arena advancement checks choose the first eligible declared route after a bout.

| Starting class | Final class | Route |
| --- | --- | --- |
| Guardian | Paladin | Crafting cr_paladin |
| Guardian | Bulwark | Arena with Shield |
| Battlemaster | Berserker | Arena without Heavy armor qualification |
| Battlemaster | Reaver | Arena while dual wielding |
| Thief | Assassin | Crafting cr_assassin |
| Thief | Swashbuckler | Arena while dual wielding |
| Ranger | Beast Master / Survivalist | Crafting cr_beast_master / cr_survivalist |
| Elementalist | Pyromancer / Lithomancer | Crafting cr_pyromancer / cr_lithomancer |
| Warlock | Necrolyte / Demonologist | Crafting cr_necrolyte / cr_demonologist |
| Ritualist | Shaman | Crafting cr_shaman |
| Ritualist | Inquisitor | Arena; equipped main-hand item has positive actual Strength appraiser stat |
| Priest | Evangelist / Lightbringer | Crafting cr_evangelist / cr_lightbringer |

## Armor qualification

Only Head, Chest, and Off Hand participate. At least one of Head or Chest must be present, and at least one must match the requested category. None of the checked pieces may have a category above the requested one. A lighter partner piece is allowed; a completely unarmored character does not qualify.

A weapon’s main stat is the first largest declared BaseStats entry in stat enum order. Inquisitor’s condition is different: it checks the actual equipped weapon’s Strength value.

## Sources

- `Assets.Source.Items.Impl/Adventurers.cs:13`
- `Assets.Source.Items.Impl/Adventurers.cs:205`
- `Assets.Source.Items.Impl/Adventurers.cs:393`
- `Assets.Source.Flow.Elements/TrainingGroundsSlot.cs:68`
- `Assets.Source.Items.Data/HumanItemData.cs:366`
- `Assets.Source.Items.Type/EquipmentItemType.cs:58`
- `Assets.Source.Flow.Elements/Arena.cs:339`
- `Assets.Source.Adventure.Rewards/AdvancementReward.cs:51`
