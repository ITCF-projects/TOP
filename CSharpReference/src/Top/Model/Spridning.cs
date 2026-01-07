namespace Top.Model;

/// <summary>
/// Visibility/distribution configuration for an object.
/// </summary>
public class Spridning
{
    /// <summary>
    /// A tag describing how the post may be distributed (e.g., internal, intranet, extranet...).
    /// </summary>
    public Tagg Synlighet { get; set; } = null!;

    /// <summary>
    /// If multiple posts of the same type meet in the above medium (e.g., multiple role assignments
    /// for the same person are visible on a person page on the intranet), they are sorted by
    /// ranking value. Lowest value wins. If multiple objects have the same ranking, the receiver
    /// chooses arbitrarily.
    /// </summary>
    public int? Ranking { get; set; }
}
