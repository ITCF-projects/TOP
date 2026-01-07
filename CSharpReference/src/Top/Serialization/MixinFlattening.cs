using System.Reflection;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Text.Json.Serialization.Metadata;
using Top.Model;

namespace Top.Serialization;

/// <summary>
/// Provides mixin flattening support for TOP entities.
/// </summary>
public static class MixinFlattening
{
    /// <summary>
    /// Known mixin types that should be flattened.
    /// </summary>
    private static readonly HashSet<Type> MixinTypes = new()
    {
        typeof(MedObligatoriskIdentifierare),
        typeof(MedFrivilligIdentifierare),
        typeof(MedGiltighet),
        typeof(MedTaggning),
        typeof(MedSpridning),
        typeof(MedLokalUtokning),
        typeof(MedTyptagg)
    };

    /// <summary>
    /// Property names that indicate a mixin property that should be flattened.
    /// </summary>
    private static readonly HashSet<string> MixinPropertyNames = new()
    {
        "Identifiering",
        "Giltighet",
        "Taggning",
        "Spridning",
        "LokalUtokning",
        "Typtagg"
    };

    /// <summary>
    /// Checks if a type is a TOP entity that uses mixins.
    /// </summary>
    public static bool IsMixinContainingType(Type type)
    {
        return type.GetProperties().Any(p => MixinPropertyNames.Contains(p.Name) && IsMixinType(p.PropertyType));
    }

    /// <summary>
    /// Checks if a type is a mixin type.
    /// </summary>
    public static bool IsMixinType(Type type) => MixinTypes.Contains(type);

    /// <summary>
    /// Gets all valid JSON property names for a type, including flattened mixin properties.
    /// </summary>
    public static HashSet<string> GetValidPropertyNames(Type type, JsonNamingPolicy? namingPolicy)
    {
        var names = new HashSet<string>();
        var properties = type.GetProperties(BindingFlags.Public | BindingFlags.Instance);

        foreach (var prop in properties)
        {
            if (IsMixinType(prop.PropertyType))
            {
                // Add mixin's flattened property names
                foreach (var mixinProp in prop.PropertyType.GetProperties(BindingFlags.Public | BindingFlags.Instance))
                {
                    var jsonName = namingPolicy?.ConvertName(mixinProp.Name) ?? mixinProp.Name;
                    names.Add(jsonName);
                }
            }
            else
            {
                var jsonName = namingPolicy?.ConvertName(prop.Name) ?? prop.Name;
                names.Add(jsonName);
            }
        }

        return names;
    }
}

/// <summary>
/// Shared context for cycle detection during serialization.
/// Detects both true cycles AND duplicate references, since TOP uses inline serialization
/// and duplicates would result in the same object being serialized multiple times.
/// </summary>
internal static class SerializationContext
{
    [ThreadStatic]
    private static HashSet<object>? _visitedObjects;

    [ThreadStatic]
    private static int _depth;

    /// <summary>
    /// Attempts to add an object to the visited set.
    /// Returns false if the object has already been visited (cycle or duplicate reference).
    /// </summary>
    public static bool TryAdd(object obj)
    {
        _visitedObjects ??= new HashSet<object>(ReferenceEqualityComparer.Instance);
        return _visitedObjects.Add(obj);
    }

    /// <summary>
    /// Enter a serialization scope. Call this at the start of serialization.
    /// </summary>
    public static void EnterScope()
    {
        _depth++;
        if (_depth == 1)
        {
            _visitedObjects = new HashSet<object>(ReferenceEqualityComparer.Instance);
        }
    }

    /// <summary>
    /// Exit a serialization scope. Call this at the end of serialization.
    /// </summary>
    public static void ExitScope()
    {
        _depth--;
        if (_depth == 0)
        {
            _visitedObjects = null;
        }
    }
}

/// <summary>
/// Generic converter that handles mixin flattening for a specific entity type.
/// </summary>
public class FlatteningConverter<T> : JsonConverter<T> where T : class, new()
{
    public override T? Read(ref Utf8JsonReader reader, Type typeToConvert, JsonSerializerOptions options)
    {
        if (reader.TokenType == JsonTokenType.Null)
            return null;

        using var doc = JsonDocument.ParseValue(ref reader);
        var root = doc.RootElement;

        // Validate no unknown properties
        ValidateNoUnknownProperties(root, typeof(T), options);

        var result = new T();
        var properties = typeof(T).GetProperties(BindingFlags.Public | BindingFlags.Instance);

        foreach (var prop in properties)
        {
            if (MixinFlattening.IsMixinType(prop.PropertyType))
            {
                // Read flattened mixin properties
                var mixinValue = ReadMixin(root, prop.PropertyType, options);
                if (mixinValue != null)
                {
                    prop.SetValue(result, mixinValue);
                }
            }
            else
            {
                // Read regular property
                var jsonName = options.PropertyNamingPolicy?.ConvertName(prop.Name) ?? prop.Name;
                if (root.TryGetProperty(jsonName, out var element))
                {
                    var value = element.Deserialize(prop.PropertyType, options);
                    prop.SetValue(result, value);
                }
            }
        }

        return result;
    }

    public override void Write(Utf8JsonWriter writer, T value, JsonSerializerOptions options)
    {
        SerializationContext.EnterScope();

        try
        {
            // Check for cycles/duplicates - TOP uses inline serialization so duplicate references are not allowed
            if (!SerializationContext.TryAdd(value))
            {
                throw new TopSerializationException(
                    $"Cycle or duplicate reference detected: object of type {typeof(T).Name} has already been serialized in the current graph. " +
                    "TOP uses inline serialization and does not support the same object being referenced from multiple places.");
            }

            writer.WriteStartObject();

            var properties = typeof(T).GetProperties(BindingFlags.Public | BindingFlags.Instance);

            foreach (var prop in properties)
            {
                var propValue = prop.GetValue(value);
                if (propValue == null)
                    continue;

                if (MixinFlattening.IsMixinType(prop.PropertyType))
                {
                    // Write flattened mixin properties
                    WriteMixin(writer, propValue, options);
                }
                else
                {
                    // Write regular property
                    var jsonName = options.PropertyNamingPolicy?.ConvertName(prop.Name) ?? prop.Name;
                    writer.WritePropertyName(jsonName);
                    JsonSerializer.Serialize(writer, propValue, prop.PropertyType, options);
                }
            }

            writer.WriteEndObject();
        }
        finally
        {
            SerializationContext.ExitScope();
        }
    }

    private static void ValidateNoUnknownProperties(JsonElement root, Type type, JsonSerializerOptions options)
    {
        var validNames = MixinFlattening.GetValidPropertyNames(type, options.PropertyNamingPolicy);

        foreach (var prop in root.EnumerateObject())
        {
            if (!validNames.Contains(prop.Name))
            {
                throw new TopDeserializationException(
                    $"Unknown property '{prop.Name}' found when deserializing {type.Name}. " +
                    "TOP standard does not allow unknown properties outside of lokalUtokning.");
            }
        }
    }

    private static object? ReadMixin(JsonElement root, Type mixinType, JsonSerializerOptions options)
    {
        var mixinProps = mixinType.GetProperties(BindingFlags.Public | BindingFlags.Instance);
        bool hasAnyValue = false;

        var mixin = Activator.CreateInstance(mixinType);

        foreach (var prop in mixinProps)
        {
            var jsonName = options.PropertyNamingPolicy?.ConvertName(prop.Name) ?? prop.Name;
            if (root.TryGetProperty(jsonName, out var element))
            {
                var value = element.Deserialize(prop.PropertyType, options);
                prop.SetValue(mixin, value);
                hasAnyValue = true;
            }
        }

        return hasAnyValue ? mixin : null;
    }

    private static void WriteMixin(Utf8JsonWriter writer, object mixin, JsonSerializerOptions options)
    {
        var mixinProps = mixin.GetType().GetProperties(BindingFlags.Public | BindingFlags.Instance);

        foreach (var prop in mixinProps)
        {
            var propValue = prop.GetValue(mixin);
            if (propValue == null)
                continue;

            var jsonName = options.PropertyNamingPolicy?.ConvertName(prop.Name) ?? prop.Name;
            writer.WritePropertyName(jsonName);
            JsonSerializer.Serialize(writer, propValue, prop.PropertyType, options);
        }
    }
}
