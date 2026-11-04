# Character, training, recovery, and Arena displays

Inspect equipped humans and interpret training slots, outfitting and fight-state indicators.

## Human details

Character details show the seeded personal name, displayed level (internal Level+1), class/item name, quality, health, energy, combat power, four main stats, equipment, traits and advancement options. Empty equipment slots show a gray slot label/icon and no item tooltip; filled slots show their full item. Armor tooltip calculates damage reduction rather than merely repeating the armor number.

## Advancement visibility

The panel marks available advancement options and shows a locked state until TrainingGrounds.SpecUnlock. Available markers reflect each advancement’s predicate; these small UI components provide descriptions/availability rather than a manual purchase button. Traits and advancement lists rebuild when their source list changes.

## Training and Inn slots

Training slot portraits show progress, current human, and a transformation animation when its icon changes. Inn reuses this widget for five slots, including any current food icon. Right click a human in a slot opens details. Empty slots disable item tooltips; spawn/leave/evolve animations are presentation.

## Outfitter

Manual outfitting button queues an action once; automated mode shows a progress bar instead. Inspect opens the current or last human. After outfitter_timeout, the timeout popup sets seconds in half-second steps (slider/2); zero is labeled None. Releasing the slider commits/closes the popup.

## Arena

Arena displays two combatants, their health and fighting/idle animations. War blocking replaces both slots with blocked artwork. Manual fight button appears only when manual crafting is possible and automation is off. Output Full indicates blocked production. Right click a human slot to inspect it.

## Power and equipment terminology

Weapon slot wording distinguishes two-handed, ambidextrous one-handed, and fixed-slot weapons. Armor/slot/stat extension methods supply localized names. Combatant tooltips show live health, quality above baseline, armor, combat power and description.

## Sources

- `Assets.Behaviour.UI.Human/HumanDetailsPopup.cs:89`
- `Assets.Behaviour.UI.Human/HumanDetailsAdvancement.cs:20`
- `Assets.Behaviour.UI.Human/HumanDetailsArmor.cs:12`
- `Assets.Behaviour.UI.Human/HumanDetailsItemSlot.cs:27`
- `Assets.Behaviour.UI.Human/HumanDetailsPower.cs:19`
- `Assets.Behaviour.Flow.Elements/WorldFlowTrainingGrounds.cs:34`
- `Assets.Behaviour.Flow.Elements/WorldFlowTrainingGroundsSlot.cs:59`
- `Assets.Behaviour.Flow.Elements/WorldFlowInn.cs:21`
- `Assets.Behaviour.Flow.Elements/WorldFlowOutfitter.cs:56`
- `Assets.Behaviour.Flow.Elements/WorldFlowArena.cs:28`
- `Assets.Behaviour.Flow.Elements/WorldFlowArenaSlot.cs:25`
- `Assets.Behaviour.Flow/WorldFlowCombatant.cs:40`
- `Assets.Source.Adventure/AdventurerAdvancement.cs:5`
- `Assets.Source.Adventure/AdventurerArchetypeExtensions.cs:5`
- `Assets.Source.Items.Type/AdventurerItemType.cs:40`
- `Assets.Source.Items.Type/WeaponItemType.cs:21`
- `Assets.Source.Items/ArmorTypeExtensions.cs:5`
- `Assets.Source.Items/EquipmentSlotExtensions.cs:5`
- `Assets.Source.Items/EquipStatExtensions.cs:5`
