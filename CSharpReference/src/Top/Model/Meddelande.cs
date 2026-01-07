namespace Top.Model;

/// <summary>
/// Top-level message object with singular and list-valued references to all value objects.
/// Good foundation for messages, also e.g., a great top-Query for a GraphQL interface.
/// </summary>
public class Meddelande
{
    // Person

    /// <summary>
    /// A single person.
    /// </summary>
    public Person? Person { get; set; }

    /// <summary>
    /// Multiple persons.
    /// </summary>
    public List<Person>? Personer { get; set; }

    // Organisationsdel

    /// <summary>
    /// A single organizational unit.
    /// </summary>
    public Organisationsdel? Organisationsdel { get; set; }

    /// <summary>
    /// Multiple organizational units.
    /// </summary>
    public List<Organisationsdel>? Organisationsdelar { get; set; }

    // Roll

    /// <summary>
    /// A single role.
    /// </summary>
    public Roll? Roll { get; set; }

    /// <summary>
    /// Multiple roles.
    /// </summary>
    public List<Roll>? Roller { get; set; }

    // Rolltilldelning

    /// <summary>
    /// A single role assignment.
    /// </summary>
    public Rolltilldelning? Rolltilldelning { get; set; }

    /// <summary>
    /// Multiple role assignments.
    /// </summary>
    public List<Rolltilldelning>? Rolltilldelningar { get; set; }

    // Anknytningsavtal (called anknytningsperiod in schema for historical reasons)

    /// <summary>
    /// A single employment contract.
    /// </summary>
    public Anknytningsavtal? Anknytningsperiod { get; set; }

    /// <summary>
    /// Multiple employment contracts.
    /// </summary>
    public List<Anknytningsavtal>? Anknytningsperioder { get; set; }

    // Passerkort

    /// <summary>
    /// A single access card.
    /// </summary>
    public Passerkort? Passerkort { get; set; }

    /// <summary>
    /// Multiple access cards.
    /// </summary>
    public List<Passerkort>? Passerkortslista { get; set; }

    // Passerbehorighet

    /// <summary>
    /// A single access privilege.
    /// </summary>
    public Passerbehorighet? Passerbehorighet { get; set; }

    /// <summary>
    /// Multiple access privileges.
    /// </summary>
    public List<Passerbehorighet>? Passerbehorigheter { get; set; }
}
