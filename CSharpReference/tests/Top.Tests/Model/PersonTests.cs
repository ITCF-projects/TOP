using Top.Model;

namespace Top.Tests.Model;

public class PersonTests
{
    [Fact]
    public void Can_Create_Minimal_Person()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare
                {
                    Namnrymd = "larosate.se",
                    Typnamn = "person-id",
                    Varde = "12345"
                }
            }
        };

        Assert.Equal("12345", person.Identifiering.Postid.Varde);
    }

    [Fact]
    public void Can_Set_Person_Name_Properties()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Fornamn = "Patrik",
            Tilltalsnamn = "Putte",
            Efternamn = "Socrates",
            FormatteratNamn = "Patrik \"Putte\" Socrates"
        };

        Assert.Equal("Patrik", person.Fornamn);
        Assert.Equal("Putte", person.Tilltalsnamn);
        Assert.Equal("Socrates", person.Efternamn);
        Assert.Equal("Patrik \"Putte\" Socrates", person.FormatteratNamn);
    }

    [Fact]
    public void Can_Set_Person_Validity()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Giltighet = new MedGiltighet
            {
                UtvarderadGiltighet = Giltighetsenum.Aktuellt
            }
        };

        Assert.Equal(Giltighetsenum.Aktuellt, person.Giltighet?.UtvarderadGiltighet);
    }

    [Fact]
    public void Can_Add_Taggning_To_Person()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Taggning = new MedTaggning
            {
                Taggar = new List<Tagg>
                {
                    new() { Namnrymd = "*", Typnamn = "anstallningsliknande", Varde = "ja" }
                }
            }
        };

        Assert.Single(person.Taggning!.Taggar!);
    }

    [Fact]
    public void Can_Add_Correlation_Ids()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" },
                Korrelationsidn = new List<Identifierare>
                {
                    new() { Namnrymd = "*", Typnamn = "personnummer", Varde = "19800101-1234" },
                    new() { Namnrymd = "orcid.org", Typnamn = "orcid", Varde = "0000-0001-2345-6789" }
                }
            }
        };

        Assert.Equal(2, person.Identifiering.Korrelationsidn!.Count);
    }

    [Fact]
    public void Person_Has_All_Expected_Mixin_Properties()
    {
        var person = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Taggning = new MedTaggning(),
            Giltighet = new MedGiltighet(),
            LokalUtokning = new MedLokalUtokning()
        };

        Assert.NotNull(person.Identifiering);
        Assert.NotNull(person.Taggning);
        Assert.NotNull(person.Giltighet);
        Assert.NotNull(person.LokalUtokning);
    }
}
