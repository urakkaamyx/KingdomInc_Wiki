# Armory

A storage space for weapons and armor for a small fee. All armories are linked and contents can be accessed from anywhere.

## Purpose

A storage space for weapons and armor for a small fee. All armories are linked and contents can be accessed from anywhere.

## Building reference

| Property | Value |
| --- | --- |
| Type | Armory |
| Category | Utility |
| Inheritance | Armory → FlowElement |
| Research required | [Armory](tech-armory.md) |

## Declared behavior values

| Property | Definition |
| --- | --- |
| Label | Armory |
| Category | ElementCategory.Utility |
| Icon | ArmoryType?.GetIcon() ?? base.Icon |
| Icon Name | Icons 138 |
| Has Craft Button | false |
| Base Input Cost | 100 |
| Max Items | 10 |
| Armory List | GamePlayer.Current.GetArmoryList(Channel, ArmoryType) |
| Channel Color | ArmoryContents.ChannelColor[Channel] |
| Cost Tech | _costTech |
| Channel Tech | _channelTech |
| Tooltip Description | Input equipment here to add them to the global storage. |

<details><summary>Implementation fields</summary>

```json
{
  "Source class": "Armory",
  "Inherited behavior": "Armory → FlowElement"
}
```

</details>

## Sources

- `Assets.Source.Flow.Elements/Armory.cs:12`
