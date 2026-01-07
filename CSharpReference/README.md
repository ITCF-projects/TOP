# Top C# Reference Library

A C# library for working with the TOP (Transfer of Organizations and Persons) data format - a Swedish sector standard for transferring HR/personnel information between IT systems at Swedish universities.

## Overview

This library provides:
- **POCO classes** representing all TOP domain entities (Person, Organisationsdel, Roll, etc.)
- **JSON serialization/deserialization** that matches the TOP JSON Schema exactly
- **Mixin property flattening** - grouped properties in C# that serialize to flat JSON
- **Strict validation** - rejects unknown properties and detects cycles

## Installation

Add a reference to the `Top` project or build and reference the DLL.

```bash
cd CSharpReference
dotnet build
```

## Quick Start

```csharp
using Top.Model;
using Top.Serialization;

// Create a serializer
var serializer = new TopSerializer();

// Create a person
var person = new Person
{
    Identifiering = new MedObligatoriskIdentifierare
    {
        Postid = new Identifierare
        {
            Namnrymd = "larosate.se",
            Typnamn = "person-id",
            Varde = "12345"
        },
        Korrelationsidn = new List<Identifierare>
        {
            new() { Namnrymd = "*", Typnamn = "personnummer", Varde = "19800101-1234" }
        }
    },
    Fornamn = "Anna",
    Efternamn = "Andersson",
    Giltighet = new MedGiltighet
    {
        UtvarderadGiltighet = Giltighetsenum.Aktuellt
    }
};

// Serialize to JSON
string json = serializer.Serialize(person);

// Deserialize from JSON
Person? loaded = serializer.Deserialize<Person>(json);
```

The resulting JSON:
```json
{
  "postid": {
    "namnrymd": "larosate.se",
    "typnamn": "person-id",
    "varde": "12345"
  },
  "korrelationsidn": [
    {
      "namnrymd": "*",
      "typnamn": "personnummer",
      "varde": "19800101-1234"
    }
  ],
  "utvarderadGiltighet": "AKTUELLT",
  "fornamn": "Anna",
  "efternamn": "Andersson"
}
```

## Working with Messages

The `Meddelande` class is the root container for TOP messages:

```csharp
var message = new Meddelande
{
    // Single entity
    Person = person,

    // Or multiple entities
    Personer = new List<Person> { person1, person2 },

    // Mix different entity types
    Organisationsdelar = new List<Organisationsdel> { org1, org2 },
    Roller = new List<Roll> { roll1 }
};

string json = serializer.Serialize(message);
```

## Language-Handled Text (I18n)

Use `SprakhanteradText` for multilingual strings:

```csharp
var org = new Organisationsdel
{
    Identifiering = new MedObligatoriskIdentifierare
    {
        Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "inst1" }
    },
    Namn = new SprakhanteradText
    {
        Svenska = "Institutionen för datavetenskap",
        Engelska = "Department of Computer Science"
    }
};

// Access by language code
string? german = org.Namn["de"];  // null if not set
org.Namn["de"] = "Institut für Informatik";
```

## Local Extensions

Use `LokalUtokning` for institution-specific data that isn't part of the standard:

```csharp
var person = new Person
{
    Identifiering = new MedObligatoriskIdentifierare { /* ... */ },
    LokalUtokning = new MedLokalUtokning
    {
        LokalUtokning = new LokalUtokning()
    }
};

// Add extension data keyed by your domain
var extensionData = JsonDocument.Parse("""{"customField": "value", "anotherField": 42}""");
person.LokalUtokning.LokalUtokning["chalmers.se"] = extensionData.RootElement;
```

## Error Handling

The library throws specific exceptions for validation errors:

```csharp
try
{
    // Unknown properties are rejected
    var json = """{"postid": {...}, "unknownField": "bad"}""";
    var person = serializer.Deserialize<Person>(json);
}
catch (TopDeserializationException ex)
{
    // "Unknown property 'unknownField' found when deserializing Person..."
}

try
{
    // Cycles/duplicate references are detected
    var person = new Person { /* ... */ };
    person.BeraknadeAnsvar = new List<BeraknatAnsvar>
    {
        new() { Ansvarig = person }  // Self-reference!
    };
    serializer.Serialize(person);
}
catch (TopSerializationException ex)
{
    // "Cycle or duplicate reference detected..."
}
```

---

# Design Decisions

## 1. Swedish Property Names

**Decision:** All C# property names match the Swedish JSON schema exactly.

**Motivation:**
- TOP is a Swedish sector standard; Swedish terminology is canonical
- Direct mapping between C# and JSON eliminates translation errors
- Developers working with TOP will already be familiar with Swedish terms
- The schema generator (`schemagen`) produces Swedish output; consistency is key

**Example:**
```csharp
public class Person
{
    public string? Fornamn { get; set; }      // Not "FirstName"
    public string? Efternamn { get; set; }    // Not "LastName"
    public MedGiltighet? Giltighet { get; set; }  // Not "Validity"
}
```

## 2. Mixin Properties Grouped in Sub-Objects

**Decision:** Mixin properties (like `MedGiltighet`, `MedTaggning`) are grouped in named sub-objects rather than being inlined as individual properties.

**Motivation:**
- C# doesn't support multiple inheritance, so mixins can't be inherited directly
- Grouping enables users to write generic filters/handlers for validity, tagging, etc.
- Makes it clear which properties "belong together" conceptually
- The JSON still serializes flat (matching the schema) via custom converters

**Example:**
```csharp
// C# - grouped for clarity and filterability
person.Giltighet?.UtvarderadGiltighet
person.Giltighet?.Giltighetsperiod?.GiltigFrom
person.Taggning?.Taggar

// JSON - flat as per TOP schema
{
  "utvarderadGiltighet": "AKTUELLT",
  "giltighetsperiod": { "giltigFrom": "..." },
  "taggar": [...]
}
```

**Alternative considered:** Inlining all mixin properties directly on each entity. Rejected because it would make filtering harder and obscure the conceptual grouping.

## 3. POCO Classes with Public Get/Set

**Decision:** Use traditional mutable classes rather than records or immutable types.

**Motivation:**
- POCOs are easier to construct incrementally (common when building messages)
- Many properties are optional; positional records would be awkward
- Familiar pattern for most C# developers
- Serialization/deserialization is simpler with mutable types
- Future versions could add builders if immutability becomes important

**Example:**
```csharp
var person = new Person();
person.Identifiering = new MedObligatoriskIdentifierare { /* ... */ };
person.Fornamn = "Anna";  // Can set properties after construction
```

## 4. `List<T>` for Collections

**Decision:** Use `List<T>` rather than arrays or interfaces.

**Motivation:**
- Mutable and easy to work with when building messages
- System.Text.Json handles `List<T>` efficiently
- Consistent with the "easy to construct" philosophy
- Users can convert to immutable collections if needed

## 5. Strict Unknown Property Rejection

**Decision:** Deserializing JSON with unknown properties throws `TopDeserializationException`.

**Motivation:**
- TOP standard explicitly forbids unknown properties (except in `lokalUtokning`)
- Fail-fast prevents silent data loss from typos or version mismatches
- Encourages proper use of `lokalUtokning` for extensions
- Makes schema violations immediately visible

**Example:**
```csharp
// This throws - "customField" is not in the TOP schema
var json = """{"postid": {...}, "customField": "value"}""";
serializer.Deserialize<Person>(json);  // TopDeserializationException

// This is the correct approach for custom data
var json = """{"postid": {...}, "lokalUtokning": {"myorg.se": {"customField": "value"}}}""";
```

## 6. Cycle/Duplicate Reference Detection

**Decision:** Serialization throws `TopSerializationException` if the same object instance appears multiple times in the graph.

**Motivation:**
- TOP uses inline serialization (no `$ref` mechanism)
- The same object serialized twice would produce duplicate data
- Circular references would cause infinite loops without detection
- Catches common programming errors (accidental shared references)

**Example:**
```csharp
var sharedOrg = new Organisationsdel { /* ... */ };

// This throws - sharedOrg would be serialized twice
var person = new Person
{
    Rolltilldelningar = new List<Rolltilldelning>
    {
        new() { Organisationsdel = sharedOrg },
        new() { Organisationsdel = sharedOrg }  // Same instance!
    }
};
serializer.Serialize(person);  // TopSerializationException
```

**Solution:** Create separate instances or restructure your data model.

## 7. `SprakhanteradText` as Dictionary Wrapper

**Decision:** `SprakhanteradText` wraps a dictionary but provides `Svenska` and `Engelska` convenience properties.

**Motivation:**
- Swedish and English are by far the most common languages in Swedish universities
- Convenience properties reduce boilerplate for common cases
- Full dictionary access remains available for other languages
- Maintains flexibility while optimizing for typical usage

**Example:**
```csharp
var text = new SprakhanteradText
{
    Svenska = "Hej",      // Convenience
    Engelska = "Hello"    // Convenience
};
text["de"] = "Hallo";     // Full flexibility for other languages
```

## 8. `LokalUtokning` as `Dictionary<string, JsonElement>`

**Decision:** Extension data uses `JsonElement` rather than `object` or a custom type.

**Motivation:**
- Extension schemas are not known at compile time
- `JsonElement` preserves the exact JSON structure
- Users can deserialize to specific types when needed
- Avoids the complexity of dynamic typing or `ExpandoObject`

## 9. Custom Exceptions

**Decision:** Dedicated exception types `TopSerializationException` and `TopDeserializationException`.

**Motivation:**
- Enables precise error handling
- Distinguishes TOP-specific errors from general JSON errors
- Exception messages include context about what went wrong
- Follows .NET exception best practices

## 10. Thread-Safe Cycle Detection

**Decision:** Cycle detection uses thread-local storage with depth counting.

**Motivation:**
- Serialization must be thread-safe (multiple threads can serialize concurrently)
- Depth counting ensures the context is properly cleaned up
- No locking required - each thread has its own context
- Works correctly with nested serialization calls

---

# API Reference

## TopSerializer

Main serialization class.

```csharp
var serializer = new TopSerializer();

// Serialize to JSON string
string json = serializer.Serialize<T>(value);

// Deserialize from JSON string
T? value = serializer.Deserialize<T>(json);

// Access underlying options for advanced scenarios
JsonSerializerOptions options = serializer.Options;
```

## Core Types

| Type | Description |
|------|-------------|
| `Identifierare` | Identifier with namespace, type, value, and optional value scope |
| `Tagg` | Tag (like identifier but with human-readable name) |
| `SprakhanteradText` | Multilingual text dictionary |
| `Giltighetsperiod` | Validity period with start/end dates |
| `Giltighetsenum` | Validity status: `Tidigare`, `Aktuellt`, `Framtida` |
| `LokalUtokning` | Extension data container |

## Mixin Types

| Type | Properties |
|------|------------|
| `MedObligatoriskIdentifierare` | `Postid` (required), `Korrelationsidn`, `SammanslagnaIdn`, `TidigareKorrelationsidn` |
| `MedFrivilligIdentifierare` | Same as above but `Postid` is optional |
| `MedGiltighet` | `Giltighetsperiod`, `UtvarderadGiltighet` |
| `MedTaggning` | `Taggar`, `GiltighetsbegransadeTaggar` |
| `MedSpridning` | `Synligheter` |
| `MedLokalUtokning` | `LokalUtokning` |
| `MedTyptagg` | `Typ` |

## Main Entities

| Entity | Description |
|--------|-------------|
| `Person` | A person with identity, contact info, employment contracts, role assignments |
| `Organisationsdel` | An organizational unit (department, project, etc.) |
| `Roll` | A role definition (e.g., "Professor", "Study Counselor") |
| `Rolltilldelning` | Assignment of a person to a role at an organizational unit |
| `Anknytningsavtal` | Employment contract linking a person to the university |
| `Meddelande` | Root message container with singular and plural properties for all entities |

---

# License

This reference implementation is part of the TOP standard documentation.
