# JsonParseException — source reference

LightJson.Serialization/JsonParseException.cs · 46 lines · infrastructure

## Audit classification

Bundled infrastructure / metadata. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public sealed class JsonParseException : Exception |
| 7 | public enum ErrorType |
| 15 | public TextPosition Position { get; private set; } |
| 17 | public ErrorType Type { get; private set; } |
| 19 | public JsonParseException() |
| 24 | public JsonParseException(ErrorType type, TextPosition position) |
| 29 | public JsonParseException(string message, ErrorType type, TextPosition position) |

## Sources

- `LightJson.Serialization/JsonParseException.cs:1`
