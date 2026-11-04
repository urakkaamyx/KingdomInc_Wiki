# Filter

Sorts incoming items by type to disentangle mixed inputs.

## Purpose

Sorts incoming items by type to disentangle mixed inputs.

## Building reference

| Property | Value |
| --- | --- |
| Type | Filter |
| Category | Utility |
| Inheritance | Filter → FlowElement |
| Research required | [Filter](tech-filter.md) |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Filter |
| Category | ElementCategory.Utility |
| Icon Name | Icons 150 |
| Has Craft Button | false |
| Icon | FilterType?.GetIcon() ?? base.Icon |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Filter",
  "Inherited behavior": "Filter → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Filter.cs:9`
