# Assassin

Assassin is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, apply group buffs. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@assassin\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@assassin_trait_desc\", GameMath.FormatPercentage(0.03f * trait.Quality))",
  "IconName": "\"Icons2_119\"",
  "ApplyGroupBuffs": "(ActiveTrait trait, CombatantItemData ally, object context) =>\n\t\t{\n\t\t\tif (context is DungeonProgress)\n\t\t\t{\n\t\t\t\tally.ApplyBuff(ClassAssassinBuff, trait.Quality);\n\t\t\t}\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:255`
