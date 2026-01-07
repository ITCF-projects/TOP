namespace Top.Model;

/// <summary>
/// A person of flesh and blood. The data is as normalized as the sender can manage - in the normal case,
/// each physical person corresponds to at most one data record. No sender should, for example, send
/// multiple person records with different IDs when a person has multiple parallel employments.
/// </summary>
public class Person
{
    // Mixin properties (grouped)

    /// <summary>
    /// Identifier information including primary ID and correlation IDs.
    /// </summary>
    public MedObligatoriskIdentifierare Identifiering { get; set; } = null!;

    /// <summary>
    /// Tagging information.
    /// </summary>
    public MedTaggning? Taggning { get; set; }

    /// <summary>
    /// Validity information.
    /// </summary>
    public MedGiltighet? Giltighet { get; set; }

    /// <summary>
    /// Local extension data.
    /// </summary>
    public MedLokalUtokning? LokalUtokning { get; set; }

    // Person-specific properties

    /// <summary>
    /// First name(s) (all of them).
    /// </summary>
    public string? Fornamn { get; set; }

    /// <summary>
    /// Preferred name. If we have all names, they are all sent in Fornamn, and the preferred name here.
    /// May be a nickname.
    /// </summary>
    public string? Tilltalsnamn { get; set; }

    /// <summary>
    /// Last name (including any middle names).
    /// </summary>
    public string? Efternamn { get; set; }

    /// <summary>
    /// Pre-formatted name, with proper capitalization.
    /// </summary>
    public string? FormatteratNamn { get; set; }

    /// <summary>
    /// Communication channels to the person as an individual.
    /// </summary>
    public Kommunikation? Kommunikationsvagar { get; set; }

    /// <summary>
    /// Access privileges the person should have, regardless of which access card they use.
    /// </summary>
    public List<Passerbehorighet>? Passerbehorigheter { get; set; }

    /// <summary>
    /// Access cards including any privileges for the card itself rather than the person.
    /// </summary>
    public List<Passerkort>? Passerkort { get; set; }

    /// <summary>
    /// Employment contracts for this person.
    /// </summary>
    public List<Anknytningsavtal>? Anknytningsavtal { get; set; }

    /// <summary>
    /// Role assignments for this person.
    /// </summary>
    public List<Rolltilldelning>? Rolltilldelningar { get; set; }

    /// <summary>
    /// Whether the person is deceased.
    /// </summary>
    public bool? Avliden { get; set; }

    /// <summary>
    /// Education level achieved (e.g., at recruitment).
    /// </summary>
    public Tagg? Utbildningsniva { get; set; }

    /// <summary>
    /// The university where the person achieved docent status.
    /// </summary>
    public string? DocentLarosate { get; set; }

    /// <summary>
    /// The subject area for docent status.
    /// </summary>
    public string? DocentAmne { get; set; }

    /// <summary>
    /// Start date of state employment (continues when changing universities).
    /// </summary>
    public DateOnly? StatligAnstallningFrom { get; set; }

    /// <summary>
    /// Research subject for reporting.
    /// </summary>
    public string? Forskningsamne { get; set; }

    /// <summary>
    /// SCB research subject code.
    /// </summary>
    public string? ForskningsamneSCB { get; set; }

    /// <summary>
    /// Workplace ID from/to SCB.
    /// </summary>
    public int? ArbetsstalleID { get; set; }

    /// <summary>
    /// Workplace address for tax authority reporting.
    /// </summary>
    public string? ArbetsplatsAdress { get; set; }

    /// <summary>
    /// Personally assigned responsibilities.
    /// </summary>
    public List<Organisationsdelsansvar>? PersonligaAnsvar { get; set; }

    /// <summary>
    /// All responsibilities this person can be calculated to have for other persons.
    /// </summary>
    public List<BeraknatAnsvar>? BeraknadeAnsvar { get; set; }

    /// <summary>
    /// All responsibilities other persons can be calculated to have over this person.
    /// </summary>
    public List<BeraknatAnsvar>? OmfattasAvAnsvar { get; set; }

    /// <summary>
    /// Registered side activities/outside work.
    /// </summary>
    public List<Bisyssla>? Bisysslor { get; set; }
}
