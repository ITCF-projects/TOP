using Top.Model;

namespace Top.Tests.Model;

public class GiltighetsperiodTests
{
    [Fact]
    public void Can_Create_Giltighetsperiod_With_Only_Start()
    {
        var period = new Giltighetsperiod
        {
            GiltigFrom = new DateTimeOffset(2024, 1, 1, 0, 0, 0, TimeSpan.Zero)
        };

        Assert.Equal(new DateTimeOffset(2024, 1, 1, 0, 0, 0, TimeSpan.Zero), period.GiltigFrom);
        Assert.Null(period.OgiltigFrom);
    }

    [Fact]
    public void Can_Create_Giltighetsperiod_With_Start_And_End()
    {
        var period = new Giltighetsperiod
        {
            GiltigFrom = new DateTimeOffset(2024, 1, 1, 0, 0, 0, TimeSpan.Zero),
            OgiltigFrom = new DateTimeOffset(2024, 12, 31, 23, 59, 59, TimeSpan.Zero)
        };

        Assert.Equal(new DateTimeOffset(2024, 1, 1, 0, 0, 0, TimeSpan.Zero), period.GiltigFrom);
        Assert.Equal(new DateTimeOffset(2024, 12, 31, 23, 59, 59, TimeSpan.Zero), period.OgiltigFrom);
    }
}

public class GiltighetsenumTests
{
    [Fact]
    public void Giltighetsenum_Has_Expected_Values()
    {
        Assert.Equal("TIDIGARE", Giltighetsenum.Tidigare.ToString().ToUpper());
        Assert.Equal("AKTUELLT", Giltighetsenum.Aktuellt.ToString().ToUpper());
        Assert.Equal("FRAMTIDA", Giltighetsenum.Framtida.ToString().ToUpper());
    }
}
