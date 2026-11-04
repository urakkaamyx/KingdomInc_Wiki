# JsonValue — source reference

LightJson/JsonValue.cs · 550 lines · infrastructure

## Audit classification

Bundled infrastructure / metadata. Symbol inventory was generated from this complete source file. Source references are static inspection, not runtime tests.

## Public and protected symbols

| Line | Declaration |
| --- | --- |
| 10 | public struct JsonValue |
| 17 | public JsonObject ObjectView |
| 30 | public JsonArray ArrayView |
| 42 | public JsonValueType Type => jsonValue.Type |
| 44 | public object Value |
| 60 | public JsonValueDebugView(JsonValue jsonValue) |
| 72 | public static readonly JsonValue Null = new JsonValue(JsonValueType.Null, 0.0, null) |
| 74 | public JsonValueType Type => type |
| 76 | public bool IsNull => Type == JsonValueType.Null |
| 78 | public bool IsBoolean => Type == JsonValueType.Boolean |
| 80 | public bool IsInteger |
| 97 | public bool IsNumber => Type == JsonValueType.Number |
| 99 | public bool IsString => Type == JsonValueType.String |
| 101 | public bool IsJsonObject => Type == JsonValueType.Object |
| 103 | public bool IsJsonArray => Type == JsonValueType.Array |
| 105 | public bool IsDateTime => AsDateTime.HasValue |
| 107 | public bool AsBoolean |
| 128 | public int AsInteger |
| 145 | public double AsNumber |
| 168 | public string AsString |
| 190 | public JsonObject AsJsonObject |
| 202 | public JsonArray AsJsonArray |
| 214 | public DateTime? AsDateTime |
| 226 | public object AsObject |
| 245 | public JsonValue this[string key] |
| 266 | public JsonValue this[int index] |
| 294 | public JsonValue(bool? value) |
| 308 | public JsonValue(double? value) |
| 322 | public JsonValue(string value) |
| 336 | public JsonValue(JsonObject value) |
| 350 | public JsonValue(JsonArray value) |
| 364 | public static implicit operator JsonValue(bool? value) |
| 369 | public static implicit operator JsonValue(double? value) |
| 374 | public static implicit operator JsonValue(string value) |
| 379 | public static implicit operator JsonValue(JsonObject value) |
| 384 | public static implicit operator JsonValue(JsonArray value) |
| 389 | public static implicit operator JsonValue(DateTime? value) |
| 398 | public static implicit operator int(JsonValue jsonValue) |
| 407 | public static implicit operator int?(JsonValue jsonValue) |
| 416 | public static implicit operator bool(JsonValue jsonValue) |
| 425 | public static implicit operator bool?(JsonValue jsonValue) |
| 434 | public static implicit operator double(JsonValue jsonValue) |
| 443 | public static implicit operator double?(JsonValue jsonValue) |
| 452 | public static implicit operator string(JsonValue jsonValue) |
| 461 | public static implicit operator JsonObject(JsonValue jsonValue) |
| 470 | public static implicit operator JsonArray(JsonValue jsonValue) |
| 479 | public static implicit operator DateTime(JsonValue jsonValue) |
| 489 | public static implicit operator DateTime?(JsonValue jsonValue) |
| 498 | public static bool operator ==(JsonValue a, JsonValue b) |
| 507 | public static bool operator !=(JsonValue a, JsonValue b) |
| 512 | public static JsonValue Parse(string text) |
| 517 | public override bool Equals(object obj) |
| 531 | public override int GetHashCode() |
| 540 | public override string ToString() |
| 545 | public string ToString(bool pretty) |

## Sources

- `LightJson/JsonValue.cs:1`
