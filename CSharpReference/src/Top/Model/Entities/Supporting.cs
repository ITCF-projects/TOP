namespace Top.Model;

/// <summary>
/// Organizational home period - says that the organizational home for a certain employment contract
/// during a certain period is at a certain organizational unit.
/// </summary>
public class Hemvistperiod
{
    public MedGiltighet? Giltighet { get; set; }
    public MedTyptagg? Typtagg { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// The organizational unit responsible for the person the employment contract applies to.
    /// </summary>
    public Organisationsdel Organisationsdel { get; set; } = null!;

    /// <summary>
    /// The employment contract that this organizational home details.
    /// </summary>
    public Anknytningsavtal? Anknytningsperiod { get; set; }
}

/// <summary>
/// Work schedule period - an amount of work time the person is expected to perform.
/// </summary>
public class Omfattningsperiod
{
    public MedGiltighet? Giltighet { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedTyptagg? Typtagg { get; set; }
    public MedFrivilligIdentifierare? Identifiering { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Proportion of full-time, as a decimal.
    /// </summary>
    public decimal? Heltidsandel { get; set; }

    /// <summary>
    /// A certain number of hours.
    /// </summary>
    public int? Timmar { get; set; }

    /// <summary>
    /// Distribution of hours across weekdays.
    /// </summary>
    public List<decimal>? TimmarPerDag { get; set; }

    /// <summary>
    /// The role assignment that this work schedule period details.
    /// </summary>
    public Rolltilldelning? Rolltilldelning { get; set; }

    /// <summary>
    /// The employment contract that this work schedule period details.
    /// </summary>
    public Anknytningsavtal? Anknytningsperiod { get; set; }
}

/// <summary>
/// Absence period - expresses vacation, parental leave, sick leave, etc.
/// </summary>
public class Franvaroperiod
{
    public MedGiltighet? Giltighet { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedFrivilligIdentifierare? Identifiering { get; set; }
    public MedTyptagg Typtagg { get; set; } = null!;
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Proportion of full-time, as a decimal.
    /// </summary>
    public decimal? Heltidsandel { get; set; }

    /// <summary>
    /// A certain number of hours.
    /// </summary>
    public int? Timmar { get; set; }

    /// <summary>
    /// Paid or unpaid absence.
    /// </summary>
    public bool? BetaldFranvaro { get; set; }

    /// <summary>
    /// If true, the end date is preliminary.
    /// </summary>
    public bool? SlutdatumArPreliminart { get; set; }

    /// <summary>
    /// The employment contract that this absence period details.
    /// </summary>
    public Anknytningsavtal? Anknytningsperiod { get; set; }
}

/// <summary>
/// Recurring compensation, e.g., salary or supplements.
/// </summary>
public class LopandeErsattning
{
    public MedGiltighet? Giltighet { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Compensation type, e.g., monthly salary or salary supplement.
    /// </summary>
    public Tagg Typ { get; set; } = null!;

    /// <summary>
    /// Monetary value per payment.
    /// </summary>
    public decimal Varde { get; set; }

    /// <summary>
    /// Currency.
    /// </summary>
    public string Valuta { get; set; } = null!;

    /// <summary>
    /// How the sum is divided across different accounts.
    /// </summary>
    public List<Kontering>? Konteringar { get; set; }

    /// <summary>
    /// The role assignment that this compensation details.
    /// </summary>
    public Rolltilldelning? DetaljerarRolltilldelning { get; set; }

    /// <summary>
    /// The employment contract that this compensation details.
    /// </summary>
    public Anknytningsavtal? DetaljerarAnknytningsperiod { get; set; }
}

/// <summary>
/// One-time compensation, e.g., a fee.
/// </summary>
public class Engangsersattning
{
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Type of compensation, e.g., fee.
    /// </summary>
    public Tagg Typ { get; set; } = null!;

    /// <summary>
    /// Payment date.
    /// </summary>
    public DateOnly Utbetalningsdatum { get; set; }

    /// <summary>
    /// Monetary value per payment.
    /// </summary>
    public decimal Varde { get; set; }

    /// <summary>
    /// Currency.
    /// </summary>
    public string Valuta { get; set; } = null!;

    /// <summary>
    /// How the sum is divided across different accounts.
    /// </summary>
    public List<Kontering>? Konteringar { get; set; }

    /// <summary>
    /// The role assignment that this compensation details.
    /// </summary>
    public Rolltilldelning? DetaljerarRolltilldelning { get; set; }

    /// <summary>
    /// The employment contract that this compensation details.
    /// </summary>
    public Anknytningsavtal? DetaljerarAnknytningsperiod { get; set; }
}

/// <summary>
/// Accounting specification.
/// </summary>
public class Kontering
{
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// All relevant IDs for a sufficiently detailed specification (account, cost center, etc.).
    /// </summary>
    public List<Identifierare> Konton { get; set; } = null!;

    /// <summary>
    /// The portion of the value accounted this way.
    /// </summary>
    public decimal Varde { get; set; }
}

/// <summary>
/// Tax information.
/// </summary>
public class Skatt
{
    public MedGiltighet? Giltighet { get; set; }

    public decimal SINK { get; set; }
    public string Tabell { get; set; } = null!;
    public string Kolumn { get; set; } = null!;
    public decimal Procskatt { get; set; }
    public decimal Jamkning { get; set; }
    public bool Ungdomsskatt { get; set; }
}

/// <summary>
/// Side activity/outside work.
/// </summary>
public class Bisyssla
{
    /// <summary>
    /// Company name.
    /// </summary>
    public string Foretag { get; set; } = null!;

    /// <summary>
    /// Organization number.
    /// </summary>
    public string Organisationsnummer { get; set; } = null!;

    /// <summary>
    /// Expected continuation, e.g., "&lt;1 year".
    /// </summary>
    public string ForvantadFortsattning { get; set; } = null!;

    /// <summary>
    /// The person with this side activity.
    /// </summary>
    public Person? Person { get; set; }
}
