# Portal

Enables instantaneous transport of items over long distances and between workspaces. Consumes a small amount of Mana.

## Purpose

Enables instantaneous transport of items over long distances and between workspaces. Consumes a small amount of Mana.

## Building reference

| Property | Value |
| --- | --- |
| Type | Portal |
| Category | Utility |
| Inheritance | Portal → FlowElement |
| Research required | [Portal](tech-portal.md) |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Portal |
| Category | ElementCategory.Utility |
| Icon Name | Icons 183 |
| Has Craft Button | false |
| Icon | LastItem?.Icon ?? base.Icon |
| Portal List | GamePlayer.Current.GetPortalList(Channel, ChannelIndex) |
| Channel Color | ArmoryContents.ChannelColor[Channel] |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Portal",
  "Inherited behavior": "Portal → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Portal.cs:11`
