# SeededRandom — source reference

SeededRandom.cs · 181 lines · 4 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 6 | public class SeededRandom |
| 19 | public static SeededRandom Global = new SeedGenerator().Add(DateTime.Now.Ticks).CreateRandom() |
| 23 | public SeededRandom(ulong seed) |
| 28 | public ulong RandomLong() |
| 36 | public uint RandomInt() |
| 41 | public int RandomRange(int lo, int hi) |
| 50 | public float RandomRange(float lo, float hi) |
| 59 | public float RandomFloat() |
| 65 | public float RandomGaussian(float mean, float stdDev) |
| 73 | public float RandomScatter(float baseVal, float scatter = 0.2f) |
| 78 | public bool RandomBool(float chanceOfTrue = 0.5f) |
| 91 | public bool RandomBool(double chanceOfTrue) |
| 96 | public string RandomString(int length) |
| 106 | public string RandomItemSeed() |
| 111 | public T Choose<T>(IReadOnlyList<T> list) |
| 124 | public T ChooseAndRemove<T>(List<T> list) |
| 131 | public T ChooseEnum<T>() |
| 145 | public T Choose<T>(Dictionary<T, float> values) |
| 171 | public void Shuffle<T>(IList<T> list) |

## Documented by

| Wiki article |
| --- |
| [Equipment slots, hands, and armor affinity](equipment-slots-and-hands.md) |
| [Character names and random generation](names-and-randomness.md) |
| [Item quality and critical crafting](production-quality.md) |
| [Skill tests and elemental resistances](skill-tests-and-resistances.md) |

## Sources

- `SeededRandom.cs:1`
