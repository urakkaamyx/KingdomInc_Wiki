# Inns, healing, and food

Five guests can heal automatically, with optional food accelerating their stay.

## Guests and timing

Inn is intrinsically automatic and contains five guest slots. Its human input and output each buffer five items. A stay normally has 20 ticks, and all guests advance on a shared two-second timer.

Each tick restores 0.05 Health01, clamped to full health, and removes one remaining tick. A full stay can therefore restore 100% of maximum health. This class does not use Speed to shorten its two-second timer.

## Food

Inn Add Food enables a second input that accepts Food-slot equipment. A waiting food item is assigned to the first occupied guest slot without food.

With food, each shared tick removes a second remaining tick and restores another 0.05 Health01, halving a complete stay to about ten ticks. It also restores 5 × food Quality energy per tick; an enhanced food item doubles this to 10 × quality.

Without food, InnSlot's actual Tick method restores health but does not restore energy. The class has an EnergyPerTick field, but that field is not used in this implementation.

## Income and output

Admitting a character below 90% health awards 200 Gold. Assigning food awards round(food SellValue × 0.5) Gold. These payments are credited directly as income.

Finished guests wait for output space, with at most one guest moved to output per update. The class contains a manual-action method that attempts an extra tick on each occupied slot with a 50% chance per guest, but its intrinsically automatic state means the generic craft button is hidden.

## Sources

- `Assets.Source.Flow.Elements/Inn.cs:13`
- `Assets.Source.Flow.Elements/Inn.cs:87`
- `Assets.Source.Flow.Elements/Inn.cs:105`
- `Assets.Source.Flow.Elements/InnSlot.cs:20`
- `Assets.Source.Flow.Elements/Inn.cs:55`
