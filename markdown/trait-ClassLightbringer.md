# Lightbringer

Lightbringer is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, apply group buffs. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@lightbringer\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@lightbringer_trait_desc\", GameMath.FormatPercentage(0.1f * trait.Quality))",
  "IconName": "\"Icons2_141\"",
  "ApplyGroupBuffs": "(ActiveTrait trait, CombatantItemData ally, object context) =>\n\t\t{\n\t\t\tif (context is DungeonProgress && ally.HasTrait(Tank))\n\t\t\t{\n\t\t\t\tally.ApplyBuff(ClassLightbringerBuff, trait.Quality);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:402`
