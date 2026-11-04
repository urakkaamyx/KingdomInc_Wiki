# ItemEnhancement — source reference

Assets.Source.Items/ItemEnhancement.cs · 138 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public class ItemEnhancement : IJsonSource |
| 14 | public readonly string Identifier |
| 16 | public string DisplayName |
| 18 | public EnhancementType Type |
| 20 | public string IconName |
| 22 | public StatSet Stats |
| 24 | public float AddQuality |
| 26 | public AdventurerTrait EquipTrait |
| 28 | public string OverrideRecipe |
| 34 | public string TextLine { private get; set; } |
| 36 | public Sprite Icon => SpriteLibrary.Get(IconName) |
| 38 | public CraftingRecipe DefaultRecipe |
| 64 | public virtual long BaseValue |
| 89 | public ItemEnhancement(string id) |
| 96 | public string GetTextLine(float quality) |
| 114 | public int GetStat(EquipStat stat) |
| 119 | public JsonValue ToJson() |
| 124 | public static void Add(ItemEnhancement it) |
| 129 | public static ItemEnhancement Get(string id) |
| 134 | public static implicit operator ItemEnhancement(string id) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Assets.Source.Items/ItemEnhancement.cs:1`
