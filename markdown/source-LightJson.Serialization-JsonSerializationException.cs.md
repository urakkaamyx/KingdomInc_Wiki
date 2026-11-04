# JsonSerializationException — source reference

LightJson.Serialization/JsonSerializationException.cs · 43 lines · infrastructure

## Audit classification

Bundled infrastructure / metadata. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public sealed class JsonSerializationException : Exception |
| 7 | public enum ErrorType |
| 15 | public ErrorType Type { get; private set; } |
| 17 | public JsonSerializationException() |
| 22 | public JsonSerializationException(ErrorType type) |
| 27 | public JsonSerializationException(string message, ErrorType type) |

## Sources

- `LightJson.Serialization/JsonSerializationException.cs:1`
