namespace Top.Model;

/// <summary>
/// An organizational relation represents a directed relationship in some tree
/// that places one organizational unit "under" another during a certain period.
/// </summary>
public class OrganisatoriskRelation
{
    public MedObligatoriskIdentifierare Identifiering { get; set; } = null!;
    public MedGiltighet? Giltighet { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// The structure(s)/tree(s)/perspective(s) that this relation applies to.
    /// </summary>
    public List<Tagg> Typer { get; set; } = null!;

    /// <summary>
    /// The organizational unit that is the parent/above in this relation.
    /// </summary>
    public Organisationsdel? Foralder { get; set; }

    /// <summary>
    /// The organizational unit that is the child/below in this relation.
    /// </summary>
    public Organisationsdel? Barn { get; set; }
}

/// <summary>
/// A contextualized relation with an organizational unit, used for filtering.
/// </summary>
public class KontextualiseradOrganisationsdelsrelation
{
    /// <summary>
    /// The structure where the relation applies.
    /// </summary>
    public Tagg Type { get; set; } = null!;

    /// <summary>
    /// The organizational parts pointed out by the relation in this structure.
    /// </summary>
    public List<Organisationsdel> Organisationsdelar { get; set; } = null!;
}

/// <summary>
/// A service function, e.g., an office, handler group, or other way of performing work
/// that doesn't directly relate to a specific role assignment.
/// </summary>
public class Servicefunktion
{
    public MedFrivilligIdentifierare? Identifiering { get; set; }
    public MedGiltighet? Giltighet { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// The service function's name.
    /// </summary>
    public SprakhanteradText Namn { get; set; } = null!;

    /// <summary>
    /// A description.
    /// </summary>
    public SprakhanteradText? Beskrivning { get; set; }

    /// <summary>
    /// Communication channels to the service function.
    /// </summary>
    public Kommunikation? Kommunikationsvagar { get; set; }

    /// <summary>
    /// The role assignment(s) via which the service function is staffed.
    /// </summary>
    public List<Rolltilldelning>? BemannadViaRolltilldelningar { get; set; }

    /// <summary>
    /// The organizational parts for which this service function provides services.
    /// </summary>
    public List<Organisationsdel>? Organisationsdelar { get; set; }
}
