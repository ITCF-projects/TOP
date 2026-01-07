namespace Top.Model;

/// <summary>
/// An employment contract says that a person has been connected to the university and how,
/// but doesn't say what the person does (that's in Rolltilldelning). The most common form
/// of employment contract is an employment agreement.
/// </summary>
public class Anknytningsavtal
{
    // Mixin properties

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

    // Anknytningsavtal-specific properties

    /// <summary>
    /// The person this employment contract applies to.
    /// </summary>
    public Person? Person { get; set; }

    /// <summary>
    /// Type of employment contract, e.g., "employment", "delegation", or "verbal agreement".
    /// </summary>
    public Tagg Typ { get; set; } = null!;

    /// <summary>
    /// The organizational part that is the counterpart in the contract.
    /// </summary>
    public Organisationsdel? OrganisationellAvtalspart { get; set; }

    /// <summary>
    /// Organizational home(s) - on which organizational part this contract currently places the person.
    /// </summary>
    public List<Hemvistperiod>? Hemvistperioder { get; set; }

    /// <summary>
    /// Work schedules for this employment contract.
    /// </summary>
    public List<Omfattningsperiod>? Omfattningsperioder { get; set; }

    /// <summary>
    /// Role assignments in the context of this contract.
    /// </summary>
    public List<Rolltilldelning>? Rolltilldelningar { get; set; }

    /// <summary>
    /// Absence periods - all circumstances that reduce the work schedule during some period.
    /// </summary>
    public List<Franvaroperiod>? Franvaroperioder { get; set; }

    /// <summary>
    /// Recurring compensation such as salary or supplements.
    /// </summary>
    public List<LopandeErsattning>? LopandeErsattningar { get; set; }

    /// <summary>
    /// One-time compensation for this employment contract.
    /// </summary>
    public List<Engangsersattning>? Engangsersattningar { get; set; }

    /// <summary>
    /// Limitation code explaining why someone doesn't have permanent employment.
    /// </summary>
    public string? Begransningskod { get; set; }

    /// <summary>
    /// If true, this is the main contract if the system can only handle one per person.
    /// </summary>
    public bool? ArHuvudavtal { get; set; }

    /// <summary>
    /// This contract is subordinate to another (e.g., a delegation may be subordinate to an employment).
    /// </summary>
    public Anknytningsavtal? Underordnat { get; set; }

    /// <summary>
    /// Other contracts that are subordinate to this one.
    /// </summary>
    public List<Anknytningsavtal>? Underordnade { get; set; }

    /// <summary>
    /// Reason for contract termination.
    /// </summary>
    public string? Avslutsorsak { get; set; }

    /// <summary>
    /// Formal termination codes to pension authority (S1-S9).
    /// </summary>
    public List<Tagg>? Avslutsorsakskoder { get; set; }

    /// <summary>
    /// Employment number used in reports to tax authority.
    /// </summary>
    public int? Anstallningsnummer { get; set; }

    /// <summary>
    /// Position name (salary-related, almost but not quite matching the role).
    /// </summary>
    public string? Befattningsnamn { get; set; }

    /// <summary>
    /// Position category.
    /// </summary>
    public string? Befattningskategori { get; set; }

    /// <summary>
    /// SCB position code.
    /// </summary>
    public string? BefattningskodSCB { get; set; }

    /// <summary>
    /// BESTA code (9 characters).
    /// </summary>
    public string? BESTA { get; set; }

    /// <summary>
    /// Tax information.
    /// </summary>
    public Skatt? Skatt { get; set; }
}
