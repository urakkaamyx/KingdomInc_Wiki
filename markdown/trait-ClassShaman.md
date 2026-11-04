# Shaman

Summons an elemental minion while in a dungeon.

## Effect

Summons an elemental minion while in a dungeon.

## Behavior hooks

This definition changes calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Companion Sprite | AnimationFrames_99 |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@shaman\"",
  "Description": "\"@shaman_trait_desc\"",
  "IconName": "\"Icons2_135\"",
  "CompanionSprite": "\"AnimationFrames_99\"",
  "CalcDamageDone": "(ActiveTrait trait, float current, object context) => (context is DungeonProgress) ? (current + 0.15f * trait.Quality) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:367`
