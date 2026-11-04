# JsonArray — source reference

LightJson/JsonArray.cs · 147 lines · infrastructure

## Audit classification

Bundled infrastructure / metadata. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 11 | public sealed class JsonArray : IEnumerable<JsonValue>, IEnumerable |
| 18 | public JsonValue[] Items |
| 31 | public JsonArrayDebugView(JsonArray jsonArray) |
| 39 | public int Count => items.Count |
| 41 | public JsonValue this[int index] |
| 57 | public JsonArray() |
| 62 | public JsonArray(params JsonValue[] values) |
| 75 | public JsonArray Add(JsonValue value) |
| 81 | public JsonArray AddIfNotNull(JsonValue value) |
| 90 | public JsonArray Insert(int index, JsonValue value) |
| 96 | public JsonArray InsertIfNotNull(int index, JsonValue value) |
| 105 | public JsonArray Remove(int index) |
| 111 | public JsonArray Clear() |
| 117 | public bool Contains(JsonValue item) |
| 122 | public int IndexOf(JsonValue item) |
| 127 | public IEnumerator<JsonValue> GetEnumerator() |
| 137 | public override string ToString() |
| 142 | public string ToString(bool pretty) |

## Sources

- `LightJson/JsonArray.cs:1`
