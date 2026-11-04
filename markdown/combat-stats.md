# Combat stats and power

How rolled stats, equipment, quality, class multipliers, and damage traits combine.

## Eight stats

Health is damage capacity, Armor reduces ordinary incoming damage, Strength/Dexterity/Magic/Wisdom supply class power and skill checks, Energy limits adventurer activity, and Combat Power is a separate bonus added to a human’s main combat stat.

An unclassed human uses the highest of Strength, Dexterity, and Magic; ties favor Strength, then Dexterity. A class with an assigned PowerStat uses that instead, including Wisdom for cleric classes.

Human power = round((main stat + Combat Power bonus) × class multiplier × exhaustion multiplier). At zero energy, a human with an energy pool uses an exhaustion multiplier of 0.75. A nonhuman combatant instead uses round(Combat Power stat × its type multiplier). Base damage = round(power × active damage-trait multiplier). Activities then apply their own damage scaling and random rolls.

## Rolls and quality

Initial combatant stats range from floor(0.75 × declared base) through ceil(1.333 × base), using rounded interpolation. Energy has a fixed declared base. The basic Adventurer has base 100 Health, 100 Energy, and 40 Strength, Dexterity, Magic, and Wisdom.

For human stats, add stored base and all equipment contributions, apply active stat traits, then multiply by human quality and round. Energy is rounded without human-quality multiplication. A human with zero stored base Energy remains without an energy pool even if equipment supplies Energy. Health also receives the Human Health prestige multiplier before quality.

Equipment has independent quality and rolls. Its final stats are added before the wearer-quality multiplier, so both can compound. Health and energy are stored as fractions; changing the maximum retains the fraction.

## Class power multipliers

These declared values precede damage traits.

| Class family | Main stat | Power multiplier |
| --- | --- | --- |
| Fighter / Rogue / Mage | Strength / Dexterity / Magic | 1.25 |
| Guardian, Battlemaster / Thief, Ranger / Elementalist, Warlock | Archetype stat | 1.5 |
| Final Fighter, Rogue, Mage specializations | Archetype stat | 2.0 |
| Cleric | Wisdom | 0.75 |
| Ritualist / Priest | Wisdom | 1.15 |
| Shaman / Inquisitor / Evangelist / Lightbringer | Wisdom | 1.3 |

## Critical damage

Critical Hit rolls a 5% × active trait quality chance whenever its damage multiplier is evaluated. A success doubles the current damage multiplier. Multiple sources of this same trait keep only the highest-quality active source. The weapon critical enchantment supplies this trait.

## Sources

- `Assets.Source.Items.Data/CombatantItemData.cs:75`
- `Assets.Source.Items.Data/CombatantItemData.cs:223`
- `Assets.Source.Items.Data/HumanItemData.cs:209`
- `Assets.Source.Items.Data/HumanItemData.cs:244`
- `Assets.Source.Items.Data/HumanItemData.cs:254`
- `Assets.Source.Items.Impl/Adventurers.cs:13`
- `Assets.Source.Adventure/AdventurerTrait.cs:528`
