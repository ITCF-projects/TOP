namespace Top.Model;

/// <summary>
/// A role assignment says that a person is expected to act in a certain role for a certain part
/// of the organization during a certain time. Hopefully the person has also been given the ability
/// to fulfill the responsibilities that the role entails - or the role assignment is used as a basis
/// for automatically granting such permissions.
/// </summary>
public class Rolltilldelning
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

    // Rolltilldelning-specific properties

    /// <summary>
    /// The employment contract that this role assignment details.
    /// </summary>
    public Anknytningsavtal? Anknytningsavtal { get; set; }

    /// <summary>
    /// The person who has been assigned the role.
    /// </summary>
    public Person? Person { get; set; }

    /// <summary>
    /// The part of the organization where the person has been assigned the role.
    /// </summary>
    public Organisationsdel? Organisationsdel { get; set; }

    /// <summary>
    /// Communication channels to the person in the context of this role assignment.
    /// </summary>
    public Kommunikation? Kommunikationsvagar { get; set; }

    /// <summary>
    /// The role that the person is assigned.
    /// </summary>
    public Roll? Roll { get; set; }

    /// <summary>
    /// Work schedule(s) for this role assignment.
    /// </summary>
    public List<Omfattningsperiod>? Omfattningsperioder { get; set; }

    /// <summary>
    /// Salary supplements or other extra compensation the person receives for this role assignment.
    /// </summary>
    public List<LopandeErsattning>? LopandeErsattningsperioder { get; set; }

    /// <summary>
    /// One-time compensation for this role assignment.
    /// </summary>
    public List<Engangsersattning>? Engangsersattningar { get; set; }

    /// <summary>
    /// The responsibilities that this role assignment entails.
    /// </summary>
    public List<Organisationsdelsansvar>? Ansvarsperioder { get; set; }

    /// <summary>
    /// Personal responsibilities assigned to someone else for this role assignment.
    /// </summary>
    public List<Rolltilldelningsansvar>? AnsvarsperioderForTilldelningen { get; set; }

    /// <summary>
    /// The service functions (if any) that are staffed via this role assignment.
    /// </summary>
    public List<Servicefunktion>? BemannarServicefunktioner { get; set; }
}
