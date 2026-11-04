# Survivalist

Grants Poison Resistance to all party members.

## Effect

Grants Poison Resistance to all party members.

## Behavior hooks

This definition changes apply group buffs. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@survivalist\"",
  "Description": "\"@survivalist_trait_desc\"",
  "IconName": "\"Icons2_125\"",
  "ApplyGroupBuffs": "(ActiveTrait trait, CombatantItemData ally, object context) =>\n\t\t{\n\t\t\tally.ApplyBuff(PoisonResist, trait.Quality);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:308`
