using Top.Model;

namespace Top.Tests.Model;

public class TaggTests
{
    [Fact]
    public void Can_Create_Tagg_With_Required_Properties()
    {
        var tag = new Tagg
        {
            Namnrymd = "*",
            Typnamn = "anstallningsform",
            Varde = "fastanstalld"
        };

        Assert.Equal("*", tag.Namnrymd);
        Assert.Equal("anstallningsform", tag.Typnamn);
        Assert.Equal("fastanstalld", tag.Varde);
        Assert.Null(tag.Varderymd);
        Assert.Null(tag.Namn);
    }

    [Fact]
    public void Can_Create_Tagg_With_Human_Readable_Name()
    {
        var tag = new Tagg
        {
            Namnrymd = "*",
            Typnamn = "remuneration_type",
            Varde = "monthly_salary",
            Namn = new SprakhanteradText
            {
                Svenska = "Manadslön",
                Engelska = "Monthly salary"
            }
        };

        Assert.Equal("Manadslön", tag.Namn.Svenska);
        Assert.Equal("Monthly salary", tag.Namn.Engelska);
    }

    [Fact]
    public void Can_Create_Larosate_Specific_Tagg_With_Varderymd()
    {
        var tag = new Tagg
        {
            Namnrymd = "*",
            Typnamn = "anstallningsform",
            Varde = "chalmers_special",
            Varderymd = "chalmers.se"
        };

        Assert.Equal("chalmers.se", tag.Varderymd);
    }
}
