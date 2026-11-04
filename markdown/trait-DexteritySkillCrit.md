# Alacrity

Dexterity skill checks are more likely to succeed.

## Effect

Dexterity skill checks are more likely to succeed.

## Behavior hooks

This definition changes calc skill test. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@dexterity_skill_crit\"",
  "Description": "\"@dexterity_skill_crit_desc\"",
  "IconName": "\"Icons2_220\"",
  "CalcSkillTest": "(ActiveTrait trait, EquipStat stat, float chance) => (stat != EquipStat.Dexterity) ? chance : (chance + 0.4f * trait.Quality)"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:544`
