# Nightmare Distiller

Allows you collect more Distilled Nightmare prestige currency. Requires a steady supply of Nightmare Collectors.

## Purpose

Allows you collect more Distilled Nightmare prestige currency. Requires a steady supply of Nightmare Collectors.

## Building reference

| Property | Value |
| --- | --- |
| Type | NightmareCollector |
| Category | Consumption |
| Inheritance | NightmareCollector → FlowElement |
| Research required | [Nightmare Distiller](tech-nightmare_distiller.md) |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Nightmare Distiller |
| Icon Name | Icons3 92 |
| Music Track | Icicles LOOP BPM110 |
| Category | ElementCategory.Consumption |
| Has Craft Button | false |
| Progress Per Collector | 1f / Mathf.Floor(Mathf.Sqrt(GamePlayer.Current.NightmareCount)) |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "NightmareCollector",
  "Inherited behavior": "NightmareCollector → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/NightmareCollector.cs:7`
