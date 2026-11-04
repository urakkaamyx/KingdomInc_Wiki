# SeedGenerator — source reference

SeedGenerator.cs · 98 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class SeedGenerator |
| 9 | public static readonly ulong FnvPrime64 = 1099511628211uL |
| 11 | public static readonly ulong FnvOffset64 = 14695981039346656037uL |
| 13 | public ulong Hash { get; private set; } |
| 15 | public SeedGenerator() |
| 20 | public SeedGenerator Add(string data) |
| 29 | public SeedGenerator Add(object data) |
| 34 | public SeedGenerator Add(byte[] data) |
| 44 | public SeedGenerator Add(JsonObject data) |
| 74 | public SeedGenerator Add(JsonArray data) |
| 94 | public SeededRandom CreateRandom() |

## Documented by

| Wiki article |
| --- |
| [Character names and random generation](names-and-randomness.md) |

## Sources

- `SeedGenerator.cs:1`
