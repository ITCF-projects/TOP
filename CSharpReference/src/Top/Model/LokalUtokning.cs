using System.Text.Json;

namespace Top.Model;

/// <summary>
/// Local extension container. Extensions are keyed by a URI (typically a domain name) identifying
/// the entity that defines the extension. Each extension value is an arbitrary JSON object.
/// </summary>
public class LokalUtokning
{
    private readonly Dictionary<string, JsonElement> _extensions = new();

    /// <summary>
    /// The underlying extensions dictionary.
    /// </summary>
    public IReadOnlyDictionary<string, JsonElement> Extensions => _extensions;

    /// <summary>
    /// Gets or sets an extension by domain/URI key.
    /// </summary>
    public JsonElement? this[string key]
    {
        get => _extensions.TryGetValue(key, out var value) ? value : null;
        set
        {
            if (value is null)
            {
                _extensions.Remove(key);
            }
            else
            {
                _extensions[key] = value.Value;
            }
        }
    }
}
