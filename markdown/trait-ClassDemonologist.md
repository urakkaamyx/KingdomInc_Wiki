# Demonologist

Summons a subjugated demon while in a dungeon.

## Effect

Summons a subjugated demon while in a dungeon.

## Behavior hooks

This definition changes calc damage done. The system guides explain the calculation order; the exact callback expressions are preserved below.

## Properties

| Property | Value |
| --- | --- |
| Companion Sprite | AnimationFrames_101 |

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@demonologist\"",
  "Description": "\"@demonologist_trait_desc\"",
  "IconName": "\"Icons2_133\"",
  "CompanionSprite": "\"AnimationFrames_101\"",
  "CalcDamageDone": "(ActiveTrait trait, float current, object context) => (context is DungeonProgress) ? (current + 0.15f * trait.Quality) : current"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:358`
