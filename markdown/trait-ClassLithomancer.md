# Lithomancer

Lithomancer is a trait definition used by the game simulation.

## Behavior hooks

This definition changes get description, apply group buffs. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@lithomancer\"",
  "GetDescription": "(ActiveTrait trait) => Translation.TranslateOnly(\"@lithomancer_trait_desc\", 50f * trait.Quality)",
  "IconName": "\"Icons2_129\"",
  "ApplyGroupBuffs": "(ActiveTrait trait, CombatantItemData ally, object context) =>\n\t\t{\n\t\t\tally.ApplyBuff(ClassLithomancerBuff, trait.Quality);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:330`
