# Data records, serialization, and implementation limits

Support code that stores game state and presents names, stats, rewards, and assets.

## Items and stats

ItemData links to its InventoryItem and serializes Type plus subtype fields; reconstruction uses the saved type string then loads subtype data. CraftingInput stores lists of consumed inputs per reagent slot and serializes them as arrays. StatSet uses an enum-indexed integer array, yields only nonzero values, and saves nonzero entries by stat name. GameConstants derives stat/enhancement/equipment counts from their enums.

## Resource and enhancement metadata

ResourceItemType holds quota defaults (1 amount, 1.2 cost multiplier, base cost 1950 raw Gold units), optional harvest costs and a resource tag. Positive available quota can make it unlocked independently of normal recipe unlocks. Forest/Farm types defer visibility to their settings. ItemEnhancement finds its default recipe, derives its base value from recipe result count, scales described stats by quality, and serializes itself as its identifier.

## Quest, dungeon and war records

QuestMetadata saves a quest ID and completed count. DungeonMetadata saves per-stage completed and wipe arrays and loads older records with a missing wipe array. QuestReward defines both quest and dungeon reward entry points; CustomReward invokes the configured action in either context. WarStage stores descriptions/rewards, combat requirements and completion callback; WarType registers four campaigns and exposes a two-second TickDelay.

## Names and localization records

AdventurerName combines given/family names and culture fields. AdventurerIdentity optionally adds a title after a comma, but the shown human-details name uses HumanNameGenerator directly. CultureProfile, SurnamePattern and WeightedOption contain the syllable pools, patterns and positive weights explained in Character names. Armor, equipment slot, stat, category and worker extension methods supply @translation keys.

## Registers, helpers and assets

Register stores named boolean flags, integer counters and string data on the player, with defaults for missing keys and JSON objects for each collection. ClassExtensions provides serialization helpers, enum-key conversion, snake_case identifiers, translated TMP text, integer-vector conversion and recursive UI cleanup/lookups. Materials supplies normal and grayscale materials. SpriteLibrary loads Icons, Icons2, Icons3 and AnimationFrames resource sheets and builds icon choices from items, nondeveloper research and currencies.

## Version and completeness caveats

GameVersion parses a trailing major.minor.patch and compares components for old-save patches. The inspected C# defines behavior and references serialized scenes/prefabs, fonts, sprites, audio and localized text; it cannot by itself prove every inspector-assigned event, slider bound, visual asset or Steam backend rule. This article documents support code without treating record fields or dormant helper methods as secret playable systems.

## Sources

- `Assets.Source.Items/ItemData.cs:9`
- `Assets.Source.Items/CraftingInput.cs:27`
- `Assets.Source.Items/StatSet.cs:13`
- `Assets.Source.Util/GameConstants.cs:6`
- `Assets.Source.Items/ResourceItemType.cs:45`
- `Assets.Source.Items/ItemEnhancement.cs:89`
- `Assets.Source.Adventure/QuestMetadata.cs:11`
- `Assets.Source.Adventure/QuestReward.cs:19`
- `Assets.Source.Adventure.Rewards/CustomReward.cs:20`
- `Assets.Source.Name/AdventurerIdentity.cs:6`
- `Assets.Source.Name/AdventurerName.cs:18`
- `Assets.Source.Name/CultureProfile.cs:6`
- `Assets.Source.Name/SurnamePattern.cs:19`
- `Assets.Source.Name/WeightedOption.cs:13`
- `Assets.Source.Flow/ElementCategoryExtensions.cs:5`
- `Register.cs:13`
- `ClassExtensions.cs:15`
- `Assets.Source.Util/GameVersion.cs:15`
- `Materials.cs:27`
- `SpriteLibrary.cs:21`
