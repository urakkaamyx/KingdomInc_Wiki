# ClassExtensions — source reference

ClassExtensions.cs · 216 lines · 1 linked articles

## Audit classification

Game implementation, UI, data definition or utility. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 9 | public static class ClassExtensions |
| 11 | public delegate T ParseJsonValue<T>(JsonValue data) |
| 13 | public delegate T ParseJsonValueDict<T>(string id, JsonValue data) |
| 15 | public static string ToSnakeCase(this string s) |
| 36 | public static void DestroyChildren(this Transform t) |
| 45 | public static void DestroyActiveChildren(this Transform t) |
| 57 | public static void SetLayerRecursively(this GameObject o, int layer) |
| 66 | public static Transform FindRecursive(this Transform t, string name) |
| 83 | public static JsonArray ToJsonArray<T>(this IEnumerable<T> list) where T : IJsonSource |
| 93 | public static JsonArray ToJsonArray(this IEnumerable<string> list) |
| 103 | public static JsonObject ToJsonObject<T>(this Dictionary<string, T> dict) where T : IJsonSource |
| 113 | public static JsonObject ToJsonObject<E, T>(this Dictionary<E, T> dict) where E : struct, IConvertible where T : IJsonSource |
| 127 | public static void FromJsonArray<T>(this List<T> list, JsonArray data, ParseJsonValue<T> parser) |
| 143 | public static void FromJsonArray<T>(this T[] array, JsonArray data, ParseJsonValue<T> parser) |
| 154 | public static void FromJsonObject<T>(this Dictionary<string, T> dict, JsonObject data, ParseJsonValueDict<T> parser) |
| 170 | public static void FromJsonObject<E, T>(this Dictionary<E, T> dict, JsonObject data, ParseJsonValueDict<T> parser) where E : struct, IConvertible |
| 190 | public static void TL(this TMP_Text t, string s, params object[] values) |
| 195 | public static Vector2Int RoundToInt(this Vector2 v) |
| 200 | public static Vector2Int RoundToInt(this Vector3 v) |
| 205 | public static T GetComponent<T>(this IEnumerable<GameObject> objects) where T : Component |

## Documented by

| Wiki article |
| --- |
| [Data records, serialization, and implementation limits](implementation-data-and-serialization.md) |

## Sources

- `ClassExtensions.cs:1`
