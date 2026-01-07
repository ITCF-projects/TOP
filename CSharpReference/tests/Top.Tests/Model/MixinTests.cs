using Top.Model;

namespace Top.Tests.Model;

public class MedGiltighetTests
{
    [Fact]
    public void Can_Create_Empty_MedGiltighet()
    {
        var mixin = new MedGiltighet();
        Assert.Null(mixin.Giltighetsperiod);
        Assert.Null(mixin.UtvarderadGiltighet);
    }

    [Fact]
    public void Can_Create_MedGiltighet_With_Period()
    {
        var mixin = new MedGiltighet
        {
            Giltighetsperiod = new Giltighetsperiod
            {
                GiltigFrom = new DateTimeOffset(2024, 1, 1, 0, 0, 0, TimeSpan.Zero)
            }
        };

        Assert.NotNull(mixin.Giltighetsperiod);
    }

    [Fact]
    public void Can_Create_MedGiltighet_With_Status()
    {
        var mixin = new MedGiltighet
        {
            UtvarderadGiltighet = Giltighetsenum.Aktuellt
        };

        Assert.Equal(Giltighetsenum.Aktuellt, mixin.UtvarderadGiltighet);
    }
}

public class MedTaggningTests
{
    [Fact]
    public void Can_Create_Empty_MedTaggning()
    {
        var mixin = new MedTaggning();
        Assert.Null(mixin.Taggar);
        Assert.Null(mixin.GiltighetsbegransadeTaggar);
    }

    [Fact]
    public void Can_Add_Simple_Tags()
    {
        var mixin = new MedTaggning
        {
            Taggar = new List<Tagg>
            {
                new() { Namnrymd = "*", Typnamn = "test", Varde = "value1" },
                new() { Namnrymd = "*", Typnamn = "test", Varde = "value2" }
            }
        };

        Assert.Equal(2, mixin.Taggar.Count);
    }

    [Fact]
    public void Can_Add_Tags_With_Validity()
    {
        var mixin = new MedTaggning
        {
            GiltighetsbegransadeTaggar = new List<MedGiltighetsbegransadTaggning>
            {
                new()
                {
                    Tagg = new Tagg { Namnrymd = "*", Typnamn = "test", Varde = "value" },
                    Giltighet = new MedGiltighet
                    {
                        UtvarderadGiltighet = Giltighetsenum.Aktuellt
                    }
                }
            }
        };

        Assert.Single(mixin.GiltighetsbegransadeTaggar);
    }
}

public class MedObligatoriskIdentifierareTests
{
    [Fact]
    public void Has_Required_Postid()
    {
        var mixin = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare
            {
                Namnrymd = "test.se",
                Typnamn = "id",
                Varde = "123"
            }
        };

        Assert.NotNull(mixin.Postid);
        Assert.Equal("123", mixin.Postid.Varde);
    }

    [Fact]
    public void Can_Have_Correlation_Ids()
    {
        var mixin = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" },
            Korrelationsidn = new List<Identifierare>
            {
                new() { Namnrymd = "*", Typnamn = "personnummer", Varde = "19800101-1234" }
            }
        };

        Assert.Single(mixin.Korrelationsidn);
    }
}

public class MedFrivilligIdentifierareTests
{
    [Fact]
    public void Postid_Is_Optional()
    {
        var mixin = new MedFrivilligIdentifierare();
        Assert.Null(mixin.Postid);
    }

    [Fact]
    public void Can_Set_Postid()
    {
        var mixin = new MedFrivilligIdentifierare
        {
            Postid = new Identifierare
            {
                Namnrymd = "test.se",
                Typnamn = "id",
                Varde = "123"
            }
        };

        Assert.NotNull(mixin.Postid);
    }
}

public class MedSpridningTests
{
    [Fact]
    public void Can_Create_Empty_MedSpridning()
    {
        var mixin = new MedSpridning();
        Assert.Null(mixin.Synligheter);
    }

    [Fact]
    public void Can_Add_Multiple_Synligheter()
    {
        var mixin = new MedSpridning
        {
            Synligheter = new List<Spridning>
            {
                new() { Synlighet = new Tagg { Namnrymd = "*", Typnamn = "synlighet", Varde = "internt" }, Ranking = 1 },
                new() { Synlighet = new Tagg { Namnrymd = "*", Typnamn = "synlighet", Varde = "extranat" }, Ranking = 2 }
            }
        };

        Assert.Equal(2, mixin.Synligheter.Count);
    }
}

public class MedLokalUtokningMixinTests
{
    [Fact]
    public void Can_Create_Empty_MedLokalUtokning()
    {
        var mixin = new MedLokalUtokning();
        Assert.Null(mixin.LokalUtokning);
    }

    [Fact]
    public void Can_Set_LokalUtokning()
    {
        var mixin = new MedLokalUtokning
        {
            LokalUtokning = new LokalUtokning()
        };

        Assert.NotNull(mixin.LokalUtokning);
    }
}

public class MedTyptaggTests
{
    [Fact]
    public void Has_Required_Typ()
    {
        var mixin = new MedTyptagg
        {
            Typ = new Tagg { Namnrymd = "*", Typnamn = "frånvarotyp", Varde = "semester" }
        };

        Assert.Equal("semester", mixin.Typ.Varde);
    }
}
