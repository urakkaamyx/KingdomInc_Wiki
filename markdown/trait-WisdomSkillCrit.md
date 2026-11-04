# Intuition

Wisdom skill checks are more likely to succeed.

## Effect

Wisdom skill checks are more likely to succeed.

## Behavior hooks

This definition changes calc skill test. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@wisdom_skill_crit\"",
  "Description": "\"@wisdom_skill_crit_desc\"",
  "IconName": "\"Icons3_58\"",
  "CalcSkillTest": "(ActiveTrait trait, EquipStat stat, float chance) => (stat != EquipStat.Wisdom) ? chance : (chance + 0.4f * trait.Quality)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:560`
