# Pontiff's Ring

Protects the wearer's allies from a single fatal attack.

## Effect

Protects the wearer's allies from a single fatal attack.

## Behavior hooks

This definition changes apply group buffs. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@pontiff_ring\"",
  "Description": "\"@pontiff_ring_trait\"",
  "IconName": "\"Icons3_77\"",
  "ApplyGroupBuffs": "(ActiveTrait trait, CombatantItemData ally, object context) =>\n\t\t{\n\t\t\tally.ApplyBuff(DivineProtection, trait.Quality);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:568`
