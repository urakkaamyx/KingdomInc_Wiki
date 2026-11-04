# TextScanner — source reference

LightJson.Serialization/TextScanner.cs · 79 lines · infrastructure

## Audit classification

Bundled infrastructure / metadata. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 5 | public sealed class TextScanner |
| 11 | public TextPosition Position => position |
| 13 | public bool CanRead => reader.Peek() != -1 |
| 15 | public TextScanner(TextReader reader) |
| 20 | public char Peek() |
| 30 | public char Read() |
| 54 | public void SkipWhitespace() |
| 62 | public void Assert(char next) |
| 72 | public void Assert(string next) |

## Sources

- `LightJson.Serialization/TextScanner.cs:1`
