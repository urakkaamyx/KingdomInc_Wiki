# Necrolyte

Summons an undead minion while in a dungeon.

## Effect

Summons an undead minion while in a dungeon.

## Behavior hooks

This definition changes calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Companion Sprite | AnimationFrames_100 |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@necrolyte\"",
  "Description": "\"@necrolyte_trait_desc\"",
  "IconName": "\"Icons2_131\"",
  "CompanionSprite": "\"AnimationFrames_100\"",
  "CalcDamageDone": "(ActiveTrait trait, float current, object context) => (context is DungeonProgress) ? (current + 0.15f * trait.Quality) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:349`
