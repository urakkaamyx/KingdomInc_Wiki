# Dungeon challenge reference

Every dungeon hazard’s trigger chance, target, check, and effect.

## How to read the table

All probabilities are independent per active combat tick when the hazard is listed on the current stage. D means one fresh GetDungeonDamage(1) roll with that stage’s current difficulty and boss escalation. A ×multiplier requests a roll at that multiplier; final armor and traits are applied afterward unless marked armor-ignoring.

Individual difficulty = integer stage difficulty ÷ 4; group difficulty = integer stage difficulty ÷ 3. A group check stops at the first successful member. A random target is selected from current party members.

## Physical and skill hazards

These use ordinary armor processing.

| Hazard | Chance | Effect |
| --- | --- | --- |
| Acid Rain | 15% | One 0.2D roll dealt to every combatant |
| Clear Rubble | 15% | Any member passes Strength versus individual difficulty, or every party member loses one stage EnergyCost |
| Arcane Traps | 15% | Any member passes Magic group test, or a random target takes 1.5D |
| Reaping Strike | 25% | Tank, or random target without Tank, takes 1.5D |
| Soul Reave | 25% | Any member passes Wisdom group test, or random target loses 2 × stage EnergyCost |
| Caltrops | 15% | Each member failing Dexterity individual test takes 0.8D |
| Flailing Strike | 25% | Random target takes D |
| Reckless Charge | 25% | Any member passes Strength group test, or random target takes 2D |
| Scatter Beam | 15% | Each member failing Dexterity individual test takes 0.5D |
| Chilling Howl | 25% | Any member passes Wisdom group test, or everyone loses stage EnergyCost |
| Tremors | 15% | Each member failing Dexterity individual test takes 0.4D |
| Extract Vigor | 25% | Random target loses half stage EnergyCost |
| Brutal Slam | 25% | Tank, or random without Tank, takes 1.5D |
| Barreling Charge | 25% | Random target passes Dexterity individual test or takes 1.5D |
| Muscle Magic | 25% | Each member failing Strength individual test takes 0.8D |
| Animated Books | 15% | Any member passes Magic group test, or all party members each take 0.5D |
| Animated Guardians | 50% | Random target takes 0.5D |
| Reap Soul | 25% | Random target passes Wisdom individual test or loses fixed 30 Energy |
| Exhausting | 100% | Everyone loses stage EnergyCost ÷ 20; normally 0.5 Energy |

## Elemental hazards

These ignore armor and its unarmored penalty. Resistance is applied only as specified.

| Hazard | Chance | Effect |
| --- | --- | --- |
| Tank Fire Damage | 25% | Tank or random takes 2D × (1 − Fire resistance) |
| Tank Shadow Damage | 25% | Tank or random takes 2D; Shadow resistance is calculated for UI but omitted from applied damage |
| Dilute Poison | 25% | Each failed Dexterity individual test takes 0.6D × (1 − Poison resistance) |
| Major Poison | 15% | First party member takes 0.6D × (1 − Poison resistance); implementation does not iterate over everyone |
| Inject Poison | 25% | Tank or random takes 2D × (1 − Poison resistance); without any reduction, gains Inject Poison debuff |
| Desert Sun | 25% | Shared 0.3D roll hits every combatant, modified by each Fire resistance |
| Venom Barb | 25% | Tank or random takes 3D × (1 − Poison resistance) |
| Consuming Shadows | 15% | Each failed Wisdom individual test takes 0.8D × (1 − Shadow resistance) |
| Mana Poison | 25% | Any member passes Magic group test, or random target takes 1.5D × (1 − Poison resistance) |
| Pyroclasm | 25% | Each failed Dexterity individual test takes 0.8D × (1 − Fire resistance) |
| Waking Nightmare | 25% | Everyone loses fixed 10 Energy × (1 − Shadow resistance), and takes 0.5D × same factor |

## Injected poison

The Inject Poison debuff itself deals 0.2D armor-ignoring damage on each dungeon combat hook. Its tick does not ask for another Poison resistance value. The initial injection avoids adding the debuff whenever the target already has any positive poison reduction. Multiple identical debuffs keep the highest trait quality rather than stacking duplicate active traits.

## Sources

- `Assets.Source.Adventure/QuestChallenge.cs:128`
- `Assets.Source.Adventure/QuestChallenge.cs:145`
- `Assets.Source.Adventure/QuestChallenge.cs:180`
- `Assets.Source.Adventure/QuestChallenge.cs:365`
- `Assets.Source.Adventure/QuestChallenge.cs:430`
- `Assets.Source.Adventure/QuestChallenge.cs:622`
- `Assets.Source.Adventure/QuestChallenge.cs:662`
- `Assets.Source.Adventure/QuestChallenge.cs:681`
- `Assets.Source.Adventure/AdventurerTrait.cs:595`
- `Assets.Source.Adventure/DungeonProgress.cs:324`
