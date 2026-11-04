# Venom Injector

Deals Poison damage over time.

## Effect

Deals Poison damage over time.

## Behavior hooks

This definition changes dungeon combat tick. The system guides explain the calculation order; the exact callback expressions are preserved below.

<details><summary>Implementation fields</summary>

```json
{
  "DisplayName": "\"@quest_challenge_inject_poison\"",
  "Description": "\"@quest_challenge_inject_poison_desc_2\"",
  "IconName": "\"Icons3_45\"",
  "DungeonCombatTick": "(ActiveTrait trait, DungeonProgress dungeon) =>\n\t\t{\n\t\t\ttrait.Self.TakeDamage(dungeon.GetDungeonDamage(0.2f), dungeon, ignoreArmor: true);\n\t\t}"
}
```

</details>

## Sources

- `Assets.Source.Adventure/AdventurerTrait.cs:595`
