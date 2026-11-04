# JsonWriter — source reference

LightJson.Serialization/JsonWriter.cs · 278 lines · infrastructure

## Audit classification

Bundled infrastructure / metadata. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 8 | public sealed class JsonWriter : IDisposable |
| 18 | public string IndentString { get; set; } |
| 20 | public string SpacingString { get; set; } |
| 22 | public string NewLineString { get; set; } |
| 24 | public bool SortObjects { get; set; } |
| 26 | public JsonWriter() |
| 31 | public JsonWriter(bool pretty) |
| 255 | public string Serialize(JsonValue jsonValue) |
| 262 | public void Dispose() |

## Sources

- `LightJson.Serialization/JsonWriter.cs:1`
