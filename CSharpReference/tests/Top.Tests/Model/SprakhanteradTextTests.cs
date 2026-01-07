using Top.Model;

namespace Top.Tests.Model;

public class SprakhanteradTextTests
{
    [Fact]
    public void Can_Create_Empty_SprakhanteradText()
    {
        var text = new SprakhanteradText();
        Assert.Empty(text.Translations);
    }

    [Fact]
    public void Can_Set_And_Get_Swedish_Text()
    {
        var text = new SprakhanteradText { Svenska = "Hej" };
        Assert.Equal("Hej", text.Svenska);
        Assert.Equal("Hej", text["sv"]);
    }

    [Fact]
    public void Can_Set_And_Get_English_Text()
    {
        var text = new SprakhanteradText { Engelska = "Hello" };
        Assert.Equal("Hello", text.Engelska);
        Assert.Equal("Hello", text["en"]);
    }

    [Fact]
    public void Can_Set_Arbitrary_Language()
    {
        var text = new SprakhanteradText();
        text["de"] = "Hallo";
        Assert.Equal("Hallo", text["de"]);
    }

    [Fact]
    public void Can_Initialize_With_Dictionary()
    {
        var text = new SprakhanteradText(new Dictionary<string, string>
        {
            ["sv"] = "Hej",
            ["en"] = "Hello"
        });

        Assert.Equal("Hej", text.Svenska);
        Assert.Equal("Hello", text.Engelska);
    }

    [Fact]
    public void Missing_Language_Returns_Null()
    {
        var text = new SprakhanteradText { Svenska = "Hej" };
        Assert.Null(text.Engelska);
        Assert.Null(text["fr"]);
    }
}
