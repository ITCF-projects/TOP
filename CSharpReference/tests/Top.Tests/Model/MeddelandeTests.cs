using Top.Model;

namespace Top.Tests.Model;

public class MeddelandeTests
{
    [Fact]
    public void Can_Create_Empty_Meddelande()
    {
        var msg = new Meddelande();

        Assert.Null(msg.Person);
        Assert.Null(msg.Personer);
        Assert.Null(msg.Organisationsdel);
        Assert.Null(msg.Organisationsdelar);
    }

    [Fact]
    public void Can_Set_Single_Person()
    {
        var person = CreateMinimalPerson("1");
        var msg = new Meddelande { Person = person };

        Assert.NotNull(msg.Person);
        Assert.Equal("1", msg.Person.Identifiering.Postid.Varde);
    }

    [Fact]
    public void Can_Set_Multiple_Persons()
    {
        var msg = new Meddelande
        {
            Personer = new List<Person>
            {
                CreateMinimalPerson("1"),
                CreateMinimalPerson("2")
            }
        };

        Assert.Equal(2, msg.Personer!.Count);
    }

    [Fact]
    public void Can_Set_Single_Organisationsdel()
    {
        var org = CreateMinimalOrganisationsdel("org1");
        var msg = new Meddelande { Organisationsdel = org };

        Assert.NotNull(msg.Organisationsdel);
    }

    [Fact]
    public void Can_Set_Multiple_Organisationsdelar()
    {
        var msg = new Meddelande
        {
            Organisationsdelar = new List<Organisationsdel>
            {
                CreateMinimalOrganisationsdel("org1"),
                CreateMinimalOrganisationsdel("org2")
            }
        };

        Assert.Equal(2, msg.Organisationsdelar!.Count);
    }

    [Fact]
    public void Can_Set_Roll_And_Roller()
    {
        var msg = new Meddelande
        {
            Roll = CreateMinimalRoll("role1"),
            Roller = new List<Roll>
            {
                CreateMinimalRoll("role2"),
                CreateMinimalRoll("role3")
            }
        };

        Assert.NotNull(msg.Roll);
        Assert.Equal(2, msg.Roller!.Count);
    }

    [Fact]
    public void Can_Set_Rolltilldelning_And_Rolltilldelningar()
    {
        var msg = new Meddelande
        {
            Rolltilldelning = CreateMinimalRolltilldelning("rt1"),
            Rolltilldelningar = new List<Rolltilldelning>
            {
                CreateMinimalRolltilldelning("rt2")
            }
        };

        Assert.NotNull(msg.Rolltilldelning);
        Assert.Single(msg.Rolltilldelningar!);
    }

    [Fact]
    public void Can_Set_Anknytningsperiod_And_Anknytningsperioder()
    {
        var msg = new Meddelande
        {
            Anknytningsperiod = CreateMinimalAnknytningsavtal("ak1"),
            Anknytningsperioder = new List<Anknytningsavtal>
            {
                CreateMinimalAnknytningsavtal("ak2")
            }
        };

        Assert.NotNull(msg.Anknytningsperiod);
        Assert.Single(msg.Anknytningsperioder!);
    }

    private static Person CreateMinimalPerson(string id) => new()
    {
        Identifiering = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = id }
        }
    };

    private static Organisationsdel CreateMinimalOrganisationsdel(string id) => new()
    {
        Identifiering = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = id }
        }
    };

    private static Roll CreateMinimalRoll(string id) => new()
    {
        Identifiering = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = id }
        }
    };

    private static Rolltilldelning CreateMinimalRolltilldelning(string id) => new()
    {
        Identifiering = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = id }
        }
    };

    private static Anknytningsavtal CreateMinimalAnknytningsavtal(string id) => new()
    {
        Identifiering = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = id }
        },
        Typ = new Tagg { Namnrymd = "*", Typnamn = "anknytningstyp", Varde = "anstallning" }
    };
}
