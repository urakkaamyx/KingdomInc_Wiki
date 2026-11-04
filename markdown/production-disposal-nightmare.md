# Incineration and nightmare distillation

Special sinks remove surplus items or advance global nightmare progress.

## Incinerator

Incinerator accepts every item type except HumanItemType. Each update it consumes its waiting item and records it as LastItem. It produces no output or currency.

Combatant is broader than HumanItemType: nonhuman combatants pass its filter. Human remains are item types rather than living human characters, so eligibility follows the concrete type test.

## Nightmare Distiller

The building class is NightmareCollector, but its displayed label is Nightmare Distiller. It accepts the nightmare_collector item and has no craft button.

While global NightmareProgress is below 1, it consumes one collector and adds 1 ÷ floor(square root of NightmareCount) to that global progress. Values above 0.985 but still below 1 are snapped to 1. It does not consume collectors once progress is already at least 1.

The node reads and writes the player's shared progress rather than keeping a separate pool per building. Its formula has no explicit zero-count guard in this class, so the progression system's current NightmareCount is part of interpreting the requirement.

## Sources

- `Assets.Source.Flow.Elements/Incinerator.cs:20`
- `Assets.Source.Flow.Elements/Incinerator.cs:33`
- `Assets.Source.Flow.Elements/NightmareCollector.cs:9`
- `Assets.Source.Flow.Elements/NightmareCollector.cs:19`
- `Assets.Source.Flow.Elements/NightmareCollector.cs:35`
