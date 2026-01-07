namespace Top.Model;

/// <summary>
/// A tag - a property expressed as a boolean variable with a true value. These are usually defined by
/// the university itself to express properties like 'employment-like relationship' on a person or
/// 'line organization' on an organizational part.
///
/// The structure is essentially identical to Identifierare, with the addition that you can include
/// a language-handled text to display the tag to humans.
/// </summary>
public class Tagg
{
    /// <summary>
    /// Namespace for the type, essentially the entity that defined the type name.
    /// This allows, for example, both Chalmers and GU to have types called "person-id".
    /// Should be '*' if TOP defines the type, otherwise something URL-like with at least
    /// a domain name for the entity that defined the semantics for the type.
    /// </summary>
    public string Namnrymd { get; set; } = null!;

    /// <summary>
    /// The combination of (namnrymd, typnamn) is a uniquely defined type of identifier,
    /// with semantics according to what namnrymd has determined.
    /// </summary>
    public string Typnamn { get; set; } = null!;

    /// <summary>
    /// Value
    /// </summary>
    public string Varde { get; set; } = null!;

    /// <summary>
    /// Domain name or similar identifier that provides a context for the combination
    /// (namnrymd, typnamn, varde) if the same type+value exists in different contexts
    /// (e.g., different instances of the same application). Only needs to be used when
    /// there is a risk that such values meet in the same receiver.
    /// Often in the form "larosate.se" or "larosate.se/applikationsinstans".
    /// </summary>
    public string? Varderymd { get; set; }

    /// <summary>
    /// Description of the tag intended for human consumption. Not value-bearing - each sender
    /// can essentially put whatever they want here. The receiver should NOT act on .Namn,
    /// only on the combination namnrymd/typnamn/varde/varderymd.
    /// </summary>
    public SprakhanteradText? Namn { get; set; }
}
