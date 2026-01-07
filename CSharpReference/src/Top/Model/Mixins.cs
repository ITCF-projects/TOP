namespace Top.Model;

/// <summary>
/// Validity mixin - contains a validity period and/or an evaluated validity status.
/// </summary>
public class MedGiltighet
{
    /// <summary>
    /// Validity period. If omitted, the sender knows neither start nor end date,
    /// only that the object is currently valid.
    /// </summary>
    public Giltighetsperiod? Giltighetsperiod { get; set; }

    /// <summary>
    /// Evaluated validity status (past, current, or future).
    /// </summary>
    public Giltighetsenum? UtvarderadGiltighet { get; set; }
}

/// <summary>
/// A tag with an associated validity period.
/// </summary>
public class MedGiltighetsbegransadTaggning
{
    /// <summary>
    /// The tag that is/was/will be attached during the validity period.
    /// </summary>
    public Tagg Tagg { get; set; } = null!;

    /// <summary>
    /// The validity information for this tag.
    /// </summary>
    public MedGiltighet? Giltighet { get; set; }
}

/// <summary>
/// Tagging mixin - contains lists of simple tags and tags with validity periods.
/// </summary>
public class MedTaggning
{
    /// <summary>
    /// List of tags currently attached to the post, where we don't know any history/future.
    /// </summary>
    public List<Tagg>? Taggar { get; set; }

    /// <summary>
    /// List of tags that have been/are/will be attached to the post, where we know history/future.
    /// </summary>
    public List<MedGiltighetsbegransadTaggning>? GiltighetsbegransadeTaggar { get; set; }
}

/// <summary>
/// Mandatory identifier mixin - has a required Postid and optional correlation/merged IDs.
/// </summary>
public class MedObligatoriskIdentifierare
{
    /// <summary>
    /// Primary ID. Should "never" change, or at least as rarely as possible.
    /// Personnummer is bad (changes often), while a UUID in a local personnel catalog can be fine.
    /// </summary>
    public Identifierare Postid { get; set; } = null!;

    /// <summary>
    /// IDs that can be found in other applications or external systems.
    /// </summary>
    public List<Identifierare>? Korrelationsidn { get; set; }

    /// <summary>
    /// If this post is the result of merging other posts, the IDs of the removed posts are here.
    /// </summary>
    public List<Identifierare>? SammanslagnaIdn { get; set; }

    /// <summary>
    /// If a correlation ID disappears, e.g., when changing personnummer, the previously
    /// used correlation ID is sent here for a period.
    /// </summary>
    public List<Identifierare>? TidigareKorrelationsidn { get; set; }
}

/// <summary>
/// Optional identifier mixin - all fields are optional, including Postid.
/// </summary>
public class MedFrivilligIdentifierare
{
    /// <summary>
    /// Primary ID (if any). Should "never" change, or at least as rarely as possible.
    /// </summary>
    public Identifierare? Postid { get; set; }

    /// <summary>
    /// IDs that can be found in other applications or external systems.
    /// </summary>
    public List<Identifierare>? Korrelationsidn { get; set; }

    /// <summary>
    /// If this post is the result of merging other posts, the IDs of the removed posts are here.
    /// </summary>
    public List<Identifierare>? SammanslagnaIdn { get; set; }

    /// <summary>
    /// If a correlation ID disappears, e.g., when changing personnummer, the previously
    /// used correlation ID is sent here for a period.
    /// </summary>
    public List<Identifierare>? TidigareKorrelationsidn { get; set; }
}

/// <summary>
/// Visibility/distribution mixin - contains a list of visibility configurations.
/// </summary>
public class MedSpridning
{
    /// <summary>
    /// The post's visibilities, with post-local ranking per visibility.
    /// </summary>
    public List<Spridning>? Synligheter { get; set; }
}

/// <summary>
/// Local extension mixin - contains an optional extension container.
/// </summary>
public class MedLokalUtokning
{
    /// <summary>
    /// Place to put all your cool extensions. See LokalUtokning for a description of the content.
    /// </summary>
    public LokalUtokning? LokalUtokning { get; set; }
}

/// <summary>
/// Type tag mixin - contains a single tag representing the object's type.
/// </summary>
public class MedTyptagg
{
    /// <summary>
    /// A single tag representing the object's type.
    /// </summary>
    public Tagg Typ { get; set; } = null!;
}
