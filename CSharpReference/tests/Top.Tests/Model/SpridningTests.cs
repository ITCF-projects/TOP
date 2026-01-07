using Top.Model;

namespace Top.Tests.Model;

public class SpridningTests
{
    [Fact]
    public void Can_Create_Spridning_With_Required_Synlighet()
    {
        var spridning = new Spridning
        {
            Synlighet = new Tagg
            {
                Namnrymd = "*",
                Typnamn = "synlighet",
                Varde = "internt"
            }
        };

        Assert.Equal("internt", spridning.Synlighet.Varde);
        Assert.Null(spridning.Ranking);
    }

    [Fact]
    public void Can_Create_Spridning_With_Ranking()
    {
        var spridning = new Spridning
        {
            Synlighet = new Tagg
            {
                Namnrymd = "*",
                Typnamn = "synlighet",
                Varde = "extranat"
            },
            Ranking = 10
        };

        Assert.Equal(10, spridning.Ranking);
    }
}
