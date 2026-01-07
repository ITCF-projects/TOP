namespace Top.Model;

/// <summary>
/// Identifier with type and value. Two identifiers are identical only if namespace, type name, value,
/// and value scope (if specified) are identical.
/// </summary>
public class Identifierare
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
    /// Often in the form "larosate.se/applikationsinstans".
    /// </summary>
    public string? Varderymd { get; set; }
}
