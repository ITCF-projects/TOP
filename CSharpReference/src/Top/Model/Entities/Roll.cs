namespace Top.Model;

/// <summary>
/// A role - a set of work tasks and responsibilities, e.g., 'Study counselor' or 'Rector'.
/// Persons can act in a role (i.e., perform the work tasks the role describes),
/// but the role itself cannot perform anything.
/// </summary>
public class Roll
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
    /// Local extension data.
    /// </summary>
    public MedLokalUtokning? LokalUtokning { get; set; }

    // Roll-specific properties

    /// <summary>
    /// The role's name, e.g., {'sv': 'Studievägledare', 'en': 'Study counsellor'}.
    /// </summary>
    public SprakhanteradText? Namn { get; set; }

    /// <summary>
    /// Description of the role, e.g., what work tasks and responsibilities are included.
    /// </summary>
    public SprakhanteradText? Beskrivning { get; set; }

    /// <summary>
    /// Role assignments for this role.
    /// </summary>
    public List<Rolltilldelning>? Rolltilldelningar { get; set; }
}
