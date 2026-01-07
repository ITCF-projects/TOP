namespace Top.Model;

/// <summary>
/// Language-handled text. Keys are language codes according to RFC4646/RFC4647 (e.g., 'en' or 'sv'),
/// values are the text in that language.
/// </summary>
public class SprakhanteradText
{
    private readonly Dictionary<string, string> _translations = new();

    public SprakhanteradText()
    {
    }

    public SprakhanteradText(Dictionary<string, string> translations)
    {
        foreach (var kvp in translations)
        {
            _translations[kvp.Key] = kvp.Value;
        }
    }

    /// <summary>
    /// The underlying translations dictionary.
    /// </summary>
    public IReadOnlyDictionary<string, string> Translations => _translations;

    /// <summary>
    /// Gets or sets the Swedish text.
    /// </summary>
    public string? Svenska
    {
        get => this["sv"];
        set => this["sv"] = value;
    }

    /// <summary>
    /// Gets or sets the English text.
    /// </summary>
    public string? Engelska
    {
        get => this["en"];
        set => this["en"] = value;
    }

    /// <summary>
    /// Gets or sets the text for a specific language code.
    /// </summary>
    public string? this[string languageCode]
    {
        get => _translations.TryGetValue(languageCode, out var value) ? value : null;
        set
        {
            if (value is null)
            {
                _translations.Remove(languageCode);
            }
            else
            {
                _translations[languageCode] = value;
            }
        }
    }
}
