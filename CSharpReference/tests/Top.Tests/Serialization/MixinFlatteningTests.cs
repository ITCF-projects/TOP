using System.Text.Json;
using Top.Model;
using Top.Serialization;

namespace Top.Tests.Serialization;

public class MixinFlatteningTests
{
    private readonly TopSerializer _serializer = new();

    [Fact]
    public void Person_Serializes_With_Flattened_Identifiering()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "123" }
            },
            Fornamn = "Test"
        };

        var json = _serializer.Serialize(person);

        // The mixin properties should be flattened to top level
        Assert.Contains("\"postid\"", json);
        Assert.Contains("\"fornamn\"", json);
        // The wrapper "identifiering" should NOT appear
        Assert.DoesNotContain("\"identifiering\"", json);
    }

    [Fact]
    public void Person_Serializes_With_Flattened_Giltighet()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Giltighet = new MedGiltighet
            {
                UtvarderadGiltighet = Giltighetsenum.Aktuellt,
                Giltighetsperiod = new Giltighetsperiod
                {
                    GiltigFrom = new DateTimeOffset(2024, 1, 1, 0, 0, 0, TimeSpan.Zero)
                }
            }
        };

        var json = _serializer.Serialize(person);

        // Flattened mixin properties
        Assert.Contains("\"utvarderadGiltighet\"", json);
        Assert.Contains("\"giltighetsperiod\"", json);
        // Wrapper should not appear
        Assert.DoesNotContain("\"giltighet\"", json.ToLower().Replace("utvarderadgiltighet", ""));
    }

    [Fact]
    public void Person_Serializes_With_Flattened_Taggning()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Taggning = new MedTaggning
            {
                Taggar = new List<Tagg>
                {
                    new() { Namnrymd = "*", Typnamn = "test", Varde = "value" }
                }
            }
        };

        var json = _serializer.Serialize(person);

        Assert.Contains("\"taggar\"", json);
        Assert.DoesNotContain("\"taggning\"", json);
    }

    [Fact]
    public void Person_Deserializes_From_Flattened_Json()
    {
        var json = """
        {
            "postid": {"namnrymd": "test", "typnamn": "id", "varde": "123"},
            "korrelationsidn": [{"namnrymd": "*", "typnamn": "pnr", "varde": "19800101-1234"}],
            "utvarderadGiltighet": "AKTUELLT",
            "taggar": [{"namnrymd": "*", "typnamn": "test", "varde": "value"}],
            "fornamn": "Test",
            "efternamn": "Testsson"
        }
        """;

        var person = _serializer.Deserialize<Person>(json);

        Assert.NotNull(person);
        Assert.Equal("123", person.Identifiering?.Postid?.Varde);
        Assert.Single(person.Identifiering?.Korrelationsidn ?? new List<Identifierare>());
        Assert.Equal(Giltighetsenum.Aktuellt, person.Giltighet?.UtvarderadGiltighet);
        Assert.Single(person.Taggning?.Taggar ?? new List<Tagg>());
        Assert.Equal("Test", person.Fornamn);
        Assert.Equal("Testsson", person.Efternamn);
    }

    [Fact]
    public void Null_Mixin_Properties_Are_Omitted()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            }
            // All other mixins are null
        };

        var json = _serializer.Serialize(person);

        Assert.DoesNotContain("\"taggar\"", json);
        Assert.DoesNotContain("\"giltighetsperiod\"", json);
        Assert.DoesNotContain("\"utvarderadGiltighet\"", json);
    }

    [Fact]
    public void Organisationsdel_Serializes_With_Flattened_Mixins()
    {
        var org = new Organisationsdel
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "org1" }
            },
            Namn = new SprakhanteradText { Svenska = "Testavdelningen", Engelska = "Test Department" }
        };

        var json = _serializer.Serialize(org);

        Assert.Contains("\"postid\"", json);
        Assert.Contains("\"namn\"", json);
        Assert.DoesNotContain("\"identifiering\"", json);
    }
}
