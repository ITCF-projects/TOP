namespace Top.Model;

/// <summary>
/// An access privilege, identified by an ID meaningful to the receiver.
/// </summary>
public class Passerbehorighet
{
    public MedGiltighet? Giltighet { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// The privilege's ID (not the resource the privilege applies to).
    /// </summary>
    public Identifierare Postid { get; set; } = null!;

    /// <summary>
    /// ID of the resource the privilege applies to (not the privilege's own ID if one exists).
    /// </summary>
    public Identifierare ResursId { get; set; } = null!;

    /// <summary>
    /// The person(s) assigned the privilege.
    /// </summary>
    public List<Person> TilldeladPersoner { get; set; } = null!;

    /// <summary>
    /// The access cards assigned the privilege.
    /// </summary>
    public List<Passerkort> TilldeladPasserkort { get; set; } = null!;
}

/// <summary>
/// An access card and the privileges this card should have.
/// </summary>
public class Passerkort
{
    public MedFrivilligIdentifierare? Identifiering { get; set; }
    public MedGiltighet? Giltighet { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Privileges the card should be associated with.
    /// </summary>
    public List<Passerbehorighet>? Passerbehorigheter { get; set; }
}
