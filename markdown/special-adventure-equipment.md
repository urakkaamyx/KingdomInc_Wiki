# Adventure potions, auras, scrolls, and rescue effects

Consumable thresholds and unusual equipment behavior that raw stat lists do not explain.

## Potions and rations

Healing Potion triggers below 33% health and heals 70 × item quality × the wearer’s healing-done multiplier. Greater Healing Potion uses 180. The wearer’s healing-taken traits then apply. Each consumes the Potion slot. They have hooks in war, quest, arena, and dungeon healing.

Energy Potion triggers below 33% energy, restores 40 × quality, and consumes the Potion slot. Regeneration Potion instead heals 6 × quality on every supported hook and is not consumed by that helper. Rations multiply requested training by 1 + 0.25 × quality.

Lifebearer (Amulet of Healing) multiplies healing received by 1 + 0.2 × quality. Lifebloom heals 2 × quality to eligible rolled recipients: 100% chance for self in arena, 50% per quest party member, 80% per dungeon member. Its war chance uses integer 4 ÷ army count; armies above four therefore receive no Lifebloom healing from that hook.

## Group energy and resistance

Amulet of Energy restores 40 × quality to the party in quest/dungeon hooks when any member is below 30% energy, or when every member is at most 60%. It consumes the wearer’s Amulet. The energy helper’s ordered scan implements these thresholds.

Fire, Shadow, and Poison protection amulets grant their matching group resistance. Triune Shield grants all three only to its wearer. Resistance uses the highest-quality active source.

Fireball Amulet adds 45 × quality × wearer damage multiplier to war PartialProgress on war hooks and dungeon StageProgress on dungeon healing hooks. It does not use a separate attack entity.

## Scrolls

Healing Scroll triggers below 33% health, heals 220 × quality × wearer healing-done multiplier, and consumes Scroll. Group Healing Scroll heals 80 × quality × wearer healing-done multiplier: it triggers when anyone is below 35% health, or everyone is at most 65%. War recipients use integer 4 ÷ army count as their chance, so larger armies can consume it without healing recipients.

Damage Scroll adds 4 × wearer CombatPower on the fifth active combat tick of each boss stage. The hook does not consume it and does not directly multiply this extra hit by item quality or damage-trait multiplier.

Energy Scroll restores 30 × quality using the same 30% / 60% group-energy thresholds. Its helper removes Amulet rather than Scroll. In this installed implementation it can therefore remove an equipped amulet while retaining the scroll.

## Divine protection

Pontiff Ring applies DivineProtection as an aura; Martyr Relic supplies DivineProtection2 on its wearer. When pending damage is at least current health, the protection heals maximum health through normal healing and returns zero incoming damage. Martyr Relic removes Trinket.

The ring branch, in dungeon context, removes Pontiff Rings from party members but asks to remove DivineProtection2 buffs rather than DivineProtection. Stored/aura refresh behavior means it should not be described as a guaranteed clean one-charge effect. Its cleanup branch is also dungeon-specific. These are code-observed exceptions, not promises about intended design.

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:615`
- `Assets.Source.Adventure/AdventurerTrait.cs:627`
- `Assets.Source.Adventure/AdventurerTrait.cs:499`
- `Assets.Source.Adventure/AdventurerTrait.cs:639`
- `Assets.Source.Items.Impl/Tier8.cs:144`
- `Assets.Source.Items.Impl/Tier8.cs:237`
- `Assets.Source.Items.Impl/Tier8.cs:265`
- `Assets.Source.Items.Impl/Tier9.cs:188`
- `Assets.Source.Items.Impl/Tier10.cs:260`
- `Assets.Source.Items.Impl/Tier10.cs:412`
- `Assets.Source.Items.Impl/Tier10.cs:444`
- `Assets.Source.Items.Impl/Tier10.cs:334`
