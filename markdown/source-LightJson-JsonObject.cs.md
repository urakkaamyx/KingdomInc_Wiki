# JsonObject — source reference

LightJson/JsonObject.cs · 110 lines · infrastructure

## Audit classification

Bundled infrastructure / metadata. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 7 | public sealed class JsonObject : IEnumerable<KeyValuePair<string, JsonValue>>, IEnumerable, IEnumerable<JsonValue> |
| 11 | public int Count => properties.Count |
| 13 | public JsonValue this[string key] |
| 29 | public JsonObject() |
| 34 | public JsonObject Add(string key) |
| 39 | public JsonObject Add(string key, JsonValue value) |
| 45 | public JsonObject AddIfNotNull(string key, JsonValue value) |
| 54 | public bool Remove(string key) |
| 59 | public JsonObject Clear() |
| 65 | public JsonObject Rename(string oldKey, string newKey) |
| 75 | public bool ContainsKey(string key) |
| 80 | public bool Contains(JsonValue value) |
| 85 | public IEnumerator<KeyValuePair<string, JsonValue>> GetEnumerator() |
| 100 | public override string ToString() |
| 105 | public string ToString(bool pretty) |

## Sources

- `LightJson/JsonObject.cs:1`
