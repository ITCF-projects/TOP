namespace Top.Model;

/// <summary>
/// A communication channels object contains up to four lists of addresses/contact information
/// for four different types of contact - email (and other electronic addresses), phone (and fax, etc.),
/// physical visit, and snail mail.
/// </summary>
public class Kommunikation
{
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Phone numbers.
    /// </summary>
    public List<Telefonnummer>? Telefon { get; set; }

    /// <summary>
    /// Postal addresses.
    /// </summary>
    public List<Snigelpost>? Snigelpost { get; set; }

    /// <summary>
    /// Electronic addresses (email, web, etc.).
    /// </summary>
    public List<ElektroniskAdress>? Elektronisk { get; set; }

    /// <summary>
    /// Visit addresses.
    /// </summary>
    public List<Besoksadress>? Besok { get; set; }
}

/// <summary>
/// Phone number.
/// </summary>
public class Telefonnummer
{
    public MedSpridning? Spridning { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Universal phone number including country code, without separators, e.g., +46317721000.
    /// </summary>
    public string Nummer { get; set; } = null!;

    /// <summary>
    /// Phone number in visual format, e.g., +46 (0)31-772 10 00.
    /// </summary>
    public string? Formatterat { get; set; }

    /// <summary>
    /// Can SMS be sent to this phone number? Missing value is interpreted as 'no'.
    /// </summary>
    public bool KanTaEmotSMS { get; set; }
}

/// <summary>
/// Pre-formatted postal address.
/// </summary>
public class Snigelpost
{
    public MedSpridning? Spridning { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Formatted address as written on an envelope mailed from a Swedish mailbox.
    /// </summary>
    public List<string> FormatteradAdress { get; set; } = null!;

    /// <summary>
    /// Copy of the country code from the formatted address.
    /// </summary>
    public string? Landskod { get; set; }

    /// <summary>
    /// Copy of the country name from the formatted address.
    /// </summary>
    public string? Landsnamn { get; set; }

    /// <summary>
    /// Copy of the postal code from the formatted address.
    /// </summary>
    public string? Postnummer { get; set; }

    /// <summary>
    /// Copy of the city from the formatted address.
    /// </summary>
    public string? Postort { get; set; }
}

/// <summary>
/// Electronic address (email, web, etc.).
/// </summary>
public class ElektroniskAdress
{
    public MedSpridning? Spridning { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Media type. The standard defines tags for e.g., web and email.
    /// </summary>
    public Tagg Media { get; set; } = null!;

    /// <summary>
    /// The address. Format depends on media - for email it's an email address, for web a URL.
    /// </summary>
    public string Adress { get; set; } = null!;
}

/// <summary>
/// Visit address, possibly with visiting hours.
/// </summary>
public class Besoksadress
{
    public MedSpridning? Spridning { get; set; }
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Street name and number.
    /// </summary>
    public string Gatuadress { get; set; } = null!;

    /// <summary>
    /// City.
    /// </summary>
    public string Stad { get; set; } = null!;

    /// <summary>
    /// Country (implicit if omitted).
    /// </summary>
    public string? Land { get; set; }

    /// <summary>
    /// Building name.
    /// </summary>
    public SprakhanteradText? Byggnad { get; set; }

    /// <summary>
    /// Instructions for finding the visit location.
    /// </summary>
    public SprakhanteradText? HittaIHuset { get; set; }

    /// <summary>
    /// Visiting hours.
    /// </summary>
    public List<Besokstider> Besokstider { get; set; } = null!;
}

/// <summary>
/// A visiting hours entry.
/// </summary>
public class Besokstider
{
    public MedTaggning? Taggning { get; set; }
    public MedLokalUtokning? LokalUtokning { get; set; }

    /// <summary>
    /// Description of when the hours apply, e.g., 'weekdays' or 'Easter Eve'.
    /// </summary>
    public SprakhanteradText Galler { get; set; } = null!;

    /// <summary>
    /// Time on local clock when visits can begin.
    /// </summary>
    public string? Oppnar { get; set; }

    /// <summary>
    /// Time on local clock when visits can no longer begin.
    /// </summary>
    public string? Stanger { get; set; }

    /// <summary>
    /// Description replacing opens/closes, e.g., "closed".
    /// </summary>
    public SprakhanteradText? Avvikelse { get; set; }
}
