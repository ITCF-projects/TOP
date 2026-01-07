using Top.Model;

namespace Top.Tests.Model;

public class IdentifierareTests
{
    [Fact]
    public void Can_Create_Identifierare_With_Required_Properties()
    {
        var id = new Identifierare
        {
            Namnrymd = "chalmers.se",
            Typnamn = "person-id",
            Varde = "12345"
        };

        Assert.Equal("chalmers.se", id.Namnrymd);
        Assert.Equal("person-id", id.Typnamn);
        Assert.Equal("12345", id.Varde);
        Assert.Null(id.Varderymd);
    }

    [Fact]
    public void Can_Create_Identifierare_With_Varderymd()
    {
        var id = new Identifierare
        {
            Namnrymd = "evry.se/primula",
            Typnamn = "aperson_id",
            Varde = "42",
            Varderymd = "chalmers.se/skarp"
        };

        Assert.Equal("evry.se/primula", id.Namnrymd);
        Assert.Equal("aperson_id", id.Typnamn);
        Assert.Equal("42", id.Varde);
        Assert.Equal("chalmers.se/skarp", id.Varderymd);
    }

    [Fact]
    public void Standard_Defined_Identifierare_Uses_Asterisk_Namnrymd()
    {
        var id = new Identifierare
        {
            Namnrymd = "*",
            Typnamn = "personnummer",
            Varde = "19800101-1234"
        };

        Assert.Equal("*", id.Namnrymd);
    }
}
