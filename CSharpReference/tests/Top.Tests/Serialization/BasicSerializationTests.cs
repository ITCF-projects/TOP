using System.Text.Json;
using Top.Model;
using Top.Serialization;

namespace Top.Tests.Serialization;

public class BasicSerializationTests
{
    private readonly TopSerializer _serializer = new();

    [Fact]
    public void Can_Serialize_SprakhanteradText()
    {
        var text = new SprakhanteradText
        {
            Svenska = "Hej",
            Engelska = "Hello"
        };

        var json = _serializer.Serialize(text);

        Assert.Contains("\"sv\"", json);
        Assert.Contains("\"en\"", json);
        Assert.Contains("\"Hej\"", json);
        Assert.Contains("\"Hello\"", json);
    }

    [Fact]
    public void Can_Deserialize_SprakhanteradText()
    {
        var json = """{"sv": "Hej", "en": "Hello"}""";

        var text = _serializer.Deserialize<SprakhanteradText>(json);

        Assert.Equal("Hej", text?.Svenska);
        Assert.Equal("Hello", text?.Engelska);
    }

    [Fact]
    public void Can_Serialize_Identifierare()
    {
        var id = new Identifierare
        {
            Namnrymd = "chalmers.se",
            Typnamn = "person-id",
            Varde = "123"
        };

        var json = _serializer.Serialize(id);

        Assert.Contains("\"namnrymd\"", json);
        Assert.Contains("\"typnamn\"", json);
        Assert.Contains("\"varde\"", json);
        Assert.Contains("\"chalmers.se\"", json);
    }

    [Fact]
    public void Can_Deserialize_Identifierare()
    {
        var json = """{"namnrymd": "test.se", "typnamn": "id", "varde": "42"}""";

        var id = _serializer.Deserialize<Identifierare>(json);

        Assert.Equal("test.se", id?.Namnrymd);
        Assert.Equal("id", id?.Typnamn);
        Assert.Equal("42", id?.Varde);
    }

    [Fact]
    public void Can_Serialize_Tagg()
    {
        var tag = new Tagg
        {
            Namnrymd = "*",
            Typnamn = "test",
            Varde = "value",
            Namn = new SprakhanteradText { Svenska = "Test" }
        };

        var json = _serializer.Serialize(tag);

        Assert.Contains("\"namnrymd\"", json);
        Assert.Contains("\"namn\"", json);
    }

    [Fact]
    public void Can_Deserialize_Tagg()
    {
        var json = """{"namnrymd": "*", "typnamn": "test", "varde": "value", "namn": {"sv": "Test"}}""";

        var tag = _serializer.Deserialize<Tagg>(json);

        Assert.Equal("*", tag?.Namnrymd);
        Assert.Equal("Test", tag?.Namn?.Svenska);
    }

    [Fact]
    public void Can_Serialize_Giltighetsperiod()
    {
        var period = new Giltighetsperiod
        {
            GiltigFrom = new DateTimeOffset(2024, 1, 1, 0, 0, 0, TimeSpan.Zero),
            OgiltigFrom = new DateTimeOffset(2024, 12, 31, 23, 59, 59, TimeSpan.Zero)
        };

        var json = _serializer.Serialize(period);

        Assert.Contains("\"giltigFrom\"", json);
        Assert.Contains("\"ogiltigFrom\"", json);
        Assert.Contains("2024-01-01", json);
    }

    [Fact]
    public void Can_Deserialize_Giltighetsperiod()
    {
        var json = """{"giltigFrom": "2024-01-01T00:00:00Z"}""";

        var period = _serializer.Deserialize<Giltighetsperiod>(json);

        Assert.Equal(2024, period?.GiltigFrom.Year);
    }

    [Fact]
    public void Serializes_Enum_As_Uppercase_String()
    {
        var mixin = new MedGiltighet
        {
            UtvarderadGiltighet = Giltighetsenum.Aktuellt
        };

        var json = _serializer.Serialize(mixin);

        Assert.Contains("\"AKTUELLT\"", json);
    }

    [Fact]
    public void Can_Deserialize_Enum_From_Uppercase_String()
    {
        var json = """{"utvarderadGiltighet": "TIDIGARE"}""";

        var mixin = _serializer.Deserialize<MedGiltighet>(json);

        Assert.Equal(Giltighetsenum.Tidigare, mixin?.UtvarderadGiltighet);
    }
}
