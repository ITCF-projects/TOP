using System.Text.Json;
using Top.Model;
using Top.Serialization;

namespace Top.Tests.Serialization;

public class ValidationTests
{
    private readonly TopSerializer _serializer = new();

    [Fact]
    public void Rejects_Unknown_Properties_On_Decode()
    {
        var json = """
        {
            "postid": {"namnrymd": "test", "typnamn": "id", "varde": "1"},
            "fornamn": "Test",
            "unknownProperty": "should fail"
        }
        """;

        var ex = Assert.Throws<TopDeserializationException>(() => _serializer.Deserialize<Person>(json));
        Assert.Contains("unknownProperty", ex.Message);
    }

    [Fact]
    public void Accepts_Known_Nested_Object_Properties()
    {
        // Nested objects like Identifierare use standard deserialization
        // so extra properties in them get ignored by default.
        // This is acceptable - the main validation is at the entity level.
        var json = """
        {
            "postid": {"namnrymd": "test", "typnamn": "id", "varde": "1"},
            "fornamn": "Test"
        }
        """;

        var person = _serializer.Deserialize<Person>(json);
        Assert.NotNull(person);
        Assert.Equal("1", person.Identifiering?.Postid?.Varde);
    }

    [Fact]
    public void Accepts_Valid_LokalUtokning_Properties()
    {
        // lokalUtokning should accept any properties keyed by domain names
        var json = """
        {
            "postid": {"namnrymd": "test", "typnamn": "id", "varde": "1"},
            "lokalUtokning": {
                "chalmers.se": {"customField": "value"},
                "gu.se": {"otherField": 42}
            }
        }
        """;

        var person = _serializer.Deserialize<Person>(json);

        Assert.NotNull(person?.LokalUtokning?.LokalUtokning);
        Assert.NotNull(person.LokalUtokning.LokalUtokning["chalmers.se"]);
    }
}

public class CycleDetectionTests
{
    private readonly TopSerializer _serializer = new();

    [Fact]
    public void Detects_Direct_Cycle_Person_To_Person()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Fornamn = "Test"
        };

        // Create a cycle through BeraknatAnsvar
        person.BeraknadeAnsvar = new List<BeraknatAnsvar>
        {
            new()
            {
                Typ = new Tagg { Namnrymd = "*", Typnamn = "ansvar", Varde = "chef" },
                Ansvarig = person, // Direct reference back to same person
                Berord = new Person
                {
                    Identifiering = new MedObligatoriskIdentifierare
                    {
                        Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "2" }
                    }
                }
            }
        };

        Assert.Throws<TopSerializationException>(() => _serializer.Serialize(person));
    }

    [Fact]
    public void Detects_Indirect_Cycle_Through_Multiple_Entities()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            }
        };

        var org = new Organisationsdel
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "org1" }
            }
        };

        var rolltilldelning = new Rolltilldelning
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "rt1" }
            },
            Person = person,
            Organisationsdel = org
        };

        // Create cycle: person -> rolltilldelning -> person (through Person property)
        person.Rolltilldelningar = new List<Rolltilldelning> { rolltilldelning };

        Assert.Throws<TopSerializationException>(() => _serializer.Serialize(person));
    }

    [Fact]
    public void Detects_Same_Object_Reference_In_Entity_Tree()
    {
        var sharedOrg = new Organisationsdel
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "org1" }
            },
            Namn = new SprakhanteradText { Svenska = "Delad org" }
        };

        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Rolltilldelningar = new List<Rolltilldelning>
            {
                new()
                {
                    Identifiering = new MedObligatoriskIdentifierare
                    {
                        Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "rt1" }
                    },
                    Organisationsdel = sharedOrg
                },
                new()
                {
                    Identifiering = new MedObligatoriskIdentifierare
                    {
                        Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "rt2" }
                    },
                    Organisationsdel = sharedOrg // Same reference - should be detected as cycle
                }
            }
        };

        // The same object appearing twice in the serialization graph is considered a cycle
        Assert.Throws<TopSerializationException>(() => _serializer.Serialize(person));
    }
}
