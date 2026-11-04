# Decorations, labels, colors, and stickers

Buying and editing layout decorations and their exact base prices.

## Types and costs

| Decoration | Raw Currency.Gold units | Initial size |
| --- | --- | --- |
| Container | 500 = 5 silver | 128×128 |
| Label | 300 = 3 silver | 192×64 |
| Icon sticker | 400 = 4 silver | 128×128 |

## Editing containers and labels

Decoration research exposes containers; deco_label and deco_sticker expose their additional rows. The options popup edits style index, lock state, anchor/parent state, and label text. Style choices select one of the prefab’s background-color sprites; this code does not expose an arbitrary RGB color picker. Labels resize to preferred text width+96 and height+32. Enter ends label editing and closes the popup.

## Stickers

A sticker selects an icon from item, technology, and currency icon names. Search uses a case-insensitive name substring. Size is a slider integer multiplied by 64, keeping a square footprint. Selecting an icon changes it immediately; double clicking an icon also saves/closes. Stickers use alpha hit-testing so transparent pixels are not the full clickable rectangle.

## Persistence and copy

FlowDeco saves position, size, style, optional sticker data, label, lock and parent flags. IconSticker saves IconName and uses the standard sticker cost. CreateCopy copies style/size/label/parent/sticker, but does not copy Locked in this implementation. Sticker factories reconstruct the subtype from its saved Type.

## Sources

- `Assets.Behaviour.UI.Deco/DecoBuyMenu.cs:14`
- `Assets.Behaviour.UI.Deco/DecoBuyMenuRow.cs:23`
- `Assets.Behaviour.UI.Deco/DecoOptionsPopup.cs:35`
- `Assets.Behaviour.UI.Deco/DecoOptionsStyle.cs:19`
- `Assets.Behaviour.UI.Deco/StickerOptionsPopup.cs:40`
- `Assets.Source.Flow/FlowDeco.cs:52`
- `Assets.Source.Flow/DecoSticker.cs:20`
- `Assets.Source.Flow.Stickers/IconSticker.cs:11`
- `Assets.Behaviour.UI.SwapFlow/FlowOptionsIcon.cs:18`
- `SpriteLibrary.cs:21`
