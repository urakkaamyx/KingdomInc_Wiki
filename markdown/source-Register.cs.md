# Register — source reference

Register.cs · 134 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public class Register |
| 13 | public Register() |
| 20 | public static bool FlagExists(string name) |
| 25 | public static bool HasFlag(string name, bool defaultValue = false) |
| 34 | public static void SetFlag(string name, bool value = true) |
| 39 | public static bool CounterExists(string name) |
| 44 | public static int GetCounter(string name, int defaultValue = 0) |
| 53 | public static void SetCounter(string name, int value) |
| 58 | public static int AddCounter(string name, int add = 1, int defaultValue = 0) |
| 69 | public static bool DataExists(string name) |
| 74 | public static string GetData(string name, string defaultValue = null) |
| 83 | public static void SetData(string name, string value) |
| 88 | public JsonObject ToJson() |
| 113 | public static Register FromJson(JsonObject data) |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `Register.cs:1`
