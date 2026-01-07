namespace Top.Model;

/// <summary>
/// A time period within which an associated value is valid.
/// </summary>
public class Giltighetsperiod
{
    /// <summary>
    /// The date/time from which the value is valid.
    /// </summary>
    public DateTimeOffset GiltigFrom { get; set; }

    /// <summary>
    /// The date/time from which the value is no longer valid.
    /// If null, the validity has no known end date.
    /// </summary>
    public DateTimeOffset? OgiltigFrom { get; set; }
}

/// <summary>
/// Evaluated validity status.
/// </summary>
public enum Giltighetsenum
{
    /// <summary>
    /// Past - the validity period has ended.
    /// </summary>
    Tidigare,

    /// <summary>
    /// Current - the value is currently valid.
    /// </summary>
    Aktuellt,

    /// <summary>
    /// Future - the validity period has not yet started.
    /// </summary>
    Framtida
}
