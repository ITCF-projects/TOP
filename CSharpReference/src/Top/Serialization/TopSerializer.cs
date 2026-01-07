using System.Text.Json;
using System.Text.Json.Serialization;
using Top.Model;

namespace Top.Serialization;

/// <summary>
/// Serializer for TOP format JSON messages.
/// </summary>
public class TopSerializer
{
    private readonly JsonSerializerOptions _options;

    public TopSerializer()
    {
        _options = new JsonSerializerOptions
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
            DefaultIgnoreCondition = JsonIgnoreCondition.WhenWritingNull,
            WriteIndented = true,
            Converters =
            {
                new JsonStringEnumConverter(new UpperCaseNamingPolicy()),
                new SprakhanteradTextConverter(),
                new LokalUtokningConverter(),
                // Entity converters with mixin flattening
                new FlatteningConverter<Person>(),
                new FlatteningConverter<Organisationsdel>(),
                new FlatteningConverter<Roll>(),
                new FlatteningConverter<Rolltilldelning>(),
                new FlatteningConverter<Anknytningsavtal>(),
                new FlatteningConverter<Hemvistperiod>(),
                new FlatteningConverter<Omfattningsperiod>(),
                new FlatteningConverter<Franvaroperiod>(),
                new FlatteningConverter<LopandeErsattning>(),
                new FlatteningConverter<Engangsersattning>(),
                new FlatteningConverter<Organisationsdelsansvar>(),
                new FlatteningConverter<Rolltilldelningsansvar>(),
                new FlatteningConverter<BeraknatAnsvar>(),
                new FlatteningConverter<OrganisatoriskRelation>(),
                new FlatteningConverter<Servicefunktion>(),
                new FlatteningConverter<Kommunikation>(),
                new FlatteningConverter<Telefonnummer>(),
                new FlatteningConverter<Snigelpost>(),
                new FlatteningConverter<ElektroniskAdress>(),
                new FlatteningConverter<Besoksadress>(),
                new FlatteningConverter<Besokstider>(),
                new FlatteningConverter<Passerbehorighet>(),
                new FlatteningConverter<Passerkort>(),
                new FlatteningConverter<Skatt>(),
                new FlatteningConverter<Kontering>(),
            }
        };
    }

    /// <summary>
    /// Serializes an object to JSON.
    /// </summary>
    public string Serialize<T>(T value)
    {
        return JsonSerializer.Serialize(value, _options);
    }

    /// <summary>
    /// Deserializes JSON to an object.
    /// </summary>
    public T? Deserialize<T>(string json)
    {
        return JsonSerializer.Deserialize<T>(json, _options);
    }

    /// <summary>
    /// Gets the configured JsonSerializerOptions for advanced usage.
    /// </summary>
    public JsonSerializerOptions Options => _options;
}

/// <summary>
/// Naming policy that converts enum values to uppercase.
/// </summary>
internal class UpperCaseNamingPolicy : JsonNamingPolicy
{
    public override string ConvertName(string name) => name.ToUpperInvariant();
}

/// <summary>
/// JSON converter for SprakhanteradText (language-keyed dictionary).
/// </summary>
internal class SprakhanteradTextConverter : JsonConverter<SprakhanteradText>
{
    public override SprakhanteradText? Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType == JsonTokenType.Null)
            return null;

        var dict = JsonSerializer.Deserialize<Dictionary<string, string>>(ref reader, options);
        return dict == null ? null : new SprakhanteradText(dict);
    }

    public override void Write(Utf8JsonWriter writer, SprakhanteradText value, JsonSerializerOptions options)
    {
        writer.WriteStartObject();
        foreach (var kvp in value.Translations)
        {
            writer.WriteString(kvp.Key, kvp.Value);
        }
        writer.WriteEndObject();
    }
}

/// <summary>
/// JSON converter for LokalUtokning (domain-keyed extension dictionary).
/// </summary>
internal class LokalUtokningConverter : JsonConverter<LokalUtokning>
{
    public override LokalUtokning? Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType == JsonTokenType.Null)
            return null;

        var result = new LokalUtokning();
        using var doc = JsonDocument.ParseValue(ref reader);

        foreach (var prop in doc.RootElement.EnumerateObject())
        {
            result[prop.Name] = prop.Value.Clone();
        }

        return result;
    }

    public override void Write(Utf8JsonWriter writer, LokalUtokning value, JsonSerializerOptions options)
    {
        writer.WriteStartObject();
        foreach (var kvp in value.Extensions)
        {
            writer.WritePropertyName(kvp.Key);
            kvp.Value.WriteTo(writer);
        }
        writer.WriteEndObject();
    }
}
