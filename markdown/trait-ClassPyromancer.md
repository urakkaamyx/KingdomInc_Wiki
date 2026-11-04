# Pyromancer

Grants Fire Resistance to all party members.

## Effect

Grants Fire Resistance to all party members.

## Behavior hooks

This definition changes apply group buffs. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@pyromancer\"",
  "Description": "\"@pyromancer_trait_desc\"",
  "IconName": "\"Icons2_127\"",
  "ApplyGroupBuffs": "(ActiveTrait trait, CombatantItemData ally, object context) =>\n\t\t{\n\t\t\tally.ApplyBuff(FireResist, trait.Quality);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:319`
