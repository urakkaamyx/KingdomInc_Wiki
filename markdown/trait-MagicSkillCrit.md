# Detect Magic

Magic skill checks are more likely to succeed.

## Effect

Magic skill checks are more likely to succeed.

## Behavior hooks

This definition changes calc skill test. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@magic_skill_crit\"",
  "Description": "\"@magic_skill_crit_desc\"",
  "IconName": "\"Icons3_57\"",
  "CalcSkillTest": "(ActiveTrait trait, EquipStat stat, float chance) => (stat != EquipStat.Magic) ? chance : (chance + 0.4f * trait.Quality)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:552`
