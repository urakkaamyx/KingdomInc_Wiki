# War Effort combat, medals, and defense

How army power becomes territorial progress and why completed fronts still need soldiers.

## Army progress

War updates every two seconds. Combine carried PartialProgress with each soldier’s base damage. A human without a main-hand weapon contributes half. Adventurers additionally multiply contribution by lerp(0.5, 1, energy fraction). This energy weighting is separate from zero-energy human power loss.

Enemy strength is interpolated between the current stage’s StartStrength and EndStrength using progress fraction. While accumulated power is strictly greater than current strength, subtract that strength and gain one progress point, recalculating as stages change. Retain the rounded remainder for future updates.

If the update gains no progress points, it loses one instead. Partial progress is still retained. A new conquered stage begins at 5 progress. Losing below zero falls back one stage with progress set to its maximum minus 5; the first stage floors at zero.

## Defense

After every stage is cleared, the front becomes a defense meter. Required strength uses half the last stage’s EndStrength, except the North keeps full EndStrength. The defense meter can fall back into the final stage if lost. Holding territory is therefore an ongoing supply commitment.

The final defense meter’s base maximum is 100. Nightmare scaling can alter endgame maximum progress. Defense combat uses lower damage-hit and medal chances than active conquest.

## Damage, healing, medals

Each soldier has a 66% chance per conquest update to be hit, or 33% in completed-front defense. The damage basis interpolates from the previous stage’s EnemyDamage to the current one where applicable, then rolls from that value to ×1.6, truncates to an integer, and uses normal armor/traits. Dead soldiers are removed.

A human carrying any WeaponItemType can generate a medal on a 20% conquest chance, or about 6.67% during defense. Its death adds another medal unit when that armed-human condition is met. The total is rounded after multiplying by the front’s MedalsMultiplier.

Full Healers cast once subject to the one-per-five-soldiers rounded limit, clamped 1–10. War trait hooks then run, including potions, passive regeneration, and other special effects.

## Inputs and remains

War Effort accepts combatants; Adventurers require the adventurer-to-war technology. Intake continues while that front’s CanProgress condition allows it. The passive recruitment technology gives a separate 5% chance at one Medal per new soldier.

With a remains output present and empty, a soldier death has a 50% chance to create Human Remains carrying the soldier’s quality. This branch is not restricted to human item types by its code. Barracks has base output rate 0.5 × Speed and quality resource cost multiplier 2.

## All four war fronts

These are base values before active Nightmare scaling. Ironcrag Siege intake is gated by currently holding Siege of Yensburg stage 4. Final defense keeps full last-stage strength in Ironcrag and halves it in other fronts.

| Front | Stage | Enemy strength | Progress amount | Enemy damage basis | Medal multiplier |
| --- | --- | --- | --- | --- | --- |
| Southside Brigands | 1. Byrgenwald | 100 → 400 | 100 | 15 | 1 |
| Southside Brigands | 2. Byrgenwald College | 400 → 800 | 150 | 18 | 1 |
| Southside Brigands | 3. Feral Den | 800 → 1200 | 200 | 21 | 1 |
| Southside Brigands | 4. Yensmouth | 1200 → 1600 | 250 | 24 | 1 |
| Orcish Horde | 1. Arlingen Farmstead | 2000 → 4000 | 100 | 24 | 1.5 |
| Orcish Horde | 2. Ruins of Arlingen | 4000 → 6000 | 150 | 28 | 1.5 |
| Orcish Horde | 3. Terminus Gorge | 6000 → 8000 | 200 | 32 | 1.5 |
| Orcish Horde | 4. Bastion | 8000 → 10000 | 250 | 36 | 1.5 |
| Siege of Yensburg | 1. Artisan Row | 8000 → 10000 | 100 | 36 | 1.5 |
| Siege of Yensburg | 2. Cathedral of Saint Ilonia | 10000 → 12000 | 150 | 42 | 1.5 |
| Siege of Yensburg | 3. Castle District | 12000 → 13000 | 200 | 43 | 1.5 |
| Siege of Yensburg | 4. Throne Room | 13000 → 14000 | 250 | 44 | 1.5 |
| Ironcrag Siege | 1. The Old Guildhouse | 12000 → 14000 | 100 | 42 | 2 |
| Ironcrag Siege | 2. Deadrock Pass | 14000 → 17000 | 150 | 44 | 2 |
| Ironcrag Siege | 3. Ironcrag Summit | 17000 → 19000 | 200 | 46 | 2 |
| Ironcrag Siege | 4. Pinnacle Ruins | 19000 → 21000 | 250 | 47 | 2 |

## Sources

- `Assets.Source.Adventure/WarProgress.cs:61`
- `Assets.Source.Adventure/WarProgress.cs:232`
- `Assets.Source.Player/GamePlayer.cs:154`
- `Assets.Source.Flow.Elements/WarEffort.cs:92`
- `Assets.Source.Flow.Elements/WarEffort.cs:135`
- `Assets.Source.Flow.Elements/Barracks.cs:18`
- `Assets.Source.Adventure.Wars/Forest.cs:5`
- `Assets.Source.Adventure.Wars/East.cs:7`
- `Assets.Source.Adventure.Wars/Yensburg.cs:7`
- `Assets.Source.Adventure.Wars/North.cs:7`
- `Assets.Source.Adventure.Wars/North.cs:17`
