namespace Top.Model;

/// <summary>
/// Represents some form of grouping that is important for how the university organizes
/// a certain aspect of its work. No limits are set for what is or isn't an organizational unit;
/// each university decides based on needs and capabilities.
/// </summary>
public class Organisationsdel
{
    // Mixin properties

    /// <summary>
    /// Identifier information including primary ID and correlation IDs.
    /// </summary>
    public MedObligatoriskIdentifierare Identifiering { get; set; } = null!;

    /// <summary>
    /// Validity information.
    /// </summary>
    public MedGiltighet? Giltighet { get; set; }

    /// <summary>
    /// Tagging information.
    /// </summary>
    public MedTaggning? Taggning { get; set; }

    /// <summary>
    /// Local extension data.
    /// </summary>
    public MedLokalUtokning? LokalUtokning { get; set; }

    // Organisationsdel-specific properties

    /// <summary>
    /// The organizational unit's name.
    /// </summary>
    public SprakhanteradText? Namn { get; set; }

    /// <summary>
    /// The organizational unit's type(s). Other tags that cannot be said to be its type
    /// are placed in the regular tagging attributes instead.
    /// </summary>
    public List<Tagg>? Typer { get; set; }

    /// <summary>
    /// Communication channels to the organizational unit as an abstract entity.
    /// </summary>
    public Kommunikation? Kommunikationsvagar { get; set; }

    /// <summary>
    /// Role assignments that connect persons to the organizational unit.
    /// </summary>
    public List<Rolltilldelning>? Rolltilldelningar { get; set; }

    /// <summary>
    /// Service functions (e.g., offices) that offer services for this organizational unit.
    /// </summary>
    public List<Servicefunktion>? Servicefunktioner { get; set; }

    /// <summary>
    /// Employment contracts for which this organizational unit is the counterpart.
    /// </summary>
    public List<Hemvistperiod>? MotpartForAnknytningsavtal { get; set; }

    /// <summary>
    /// Persons with certain responsibilities for this organizational unit.
    /// </summary>
    public List<Organisationsdelsansvar>? Ansvarshallare { get; set; }

    /// <summary>
    /// Relations defining this organizational unit's parent(s).
    /// </summary>
    public List<OrganisatoriskRelation>? Foralderrelationer { get; set; }

    /// <summary>
    /// Relations defining this organizational unit's children.
    /// </summary>
    public List<OrganisatoriskRelation>? Barnrelationer { get; set; }

    /// <summary>
    /// Organizational units relevant for filtering, divided by relation type.
    /// </summary>
    public List<KontextualiseradOrganisationsdelsrelation>? Filterrelationer { get; set; }
}
