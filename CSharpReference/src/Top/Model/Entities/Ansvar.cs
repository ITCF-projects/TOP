namespace Top.Model;

/// <summary>
/// Responsibility for a certain organizational unit, either assigned personally or via a role assignment.
/// </summary>
public class Organisationsdelsansvar
{
    public MedGiltighet? Giltighet { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedFrivilligIdentifierare? Identifiering { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Responsibility type(s) (manager, financially responsible, supervisor...).
    /// </summary>
    public Tagg Typ { get; set; } = null!;

    /// <summary>
    /// The organization for which the responsibility applies.
    /// </summary>
    public Organisationsdel? Organisationsdel { get; set; }

    /// <summary>
    /// Role assignment(s) via which the responsibility was assigned.
    /// </summary>
    public List<Rolltilldelning>? ViaRolltilldelningar { get; set; }

    /// <summary>
    /// Individual(s) who have been personally assigned the responsibility.
    /// </summary>
    public List<Person>? DirektUtpekade { get; set; }
}

/// <summary>
/// Responsibility for a person who has a certain role assignment, e.g., being a supervisor for an intern.
/// </summary>
public class Rolltilldelningsansvar
{
    public MedGiltighet? Giltighet { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedFrivilligIdentifierare? Identifiering { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Responsibility type(s) (supervisor, mentor...).
    /// </summary>
    public Tagg Typ { get; set; } = null!;

    /// <summary>
    /// The person who has the responsibility (e.g., the supervisor).
    /// </summary>
    public Person? Ansvarig { get; set; }

    /// <summary>
    /// The role assignment that the responsible person is responsible for.
    /// </summary>
    public Rolltilldelning? Rolltilldelning { get; set; }
}

/// <summary>
/// Calculated responsibility - a pre-calculated relationship saying one person is responsible for another.
/// </summary>
public class BeraknatAnsvar
{
    public MedGiltighet? Giltighet { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Responsibility type (manager, financially responsible, supervisor...).
    /// </summary>
    public Tagg Typ { get; set; } = null!;

    /// <summary>
    /// The person who has the responsibility (e.g., the manager).
    /// </summary>
    public Person? Ansvarig { get; set; }

    /// <summary>
    /// The person the responsibility applies to (e.g., the managed).
    /// </summary>
    public Person? Berord { get; set; }
}
