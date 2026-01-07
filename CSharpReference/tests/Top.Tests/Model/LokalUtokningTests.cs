using System.Text.Json;
using Top.Model;

namespace Top.Tests.Model;

public class LokalUtokningTests
{
    [Fact]
    public void Can_Create_Empty_LokalUtokning()
    {
        var ext = new LokalUtokning();
        Assert.Empty(ext.Extensions);
    }

    [Fact]
    public void Can_Add_Extension_By_Domain()
    {
        var ext = new LokalUtokning();
        var chalmerExt = JsonDocument.Parse("""{"customField": "value"}""").RootElement;

        ext["chalmers.se"] = chalmerExt;

        Assert.True(ext.Extensions.ContainsKey("chalmers.se"));
    }

    [Fact]
    public void Can_Get_Extension_By_Domain()
    {
        var ext = new LokalUtokning();
        var chalmerExt = JsonDocument.Parse("""{"customField": 42}""").RootElement;

        ext["chalmers.se"] = chalmerExt;
        var retrieved = ext["chalmers.se"];

        Assert.NotNull(retrieved);
        Assert.Equal(42, retrieved.Value.GetProperty("customField").GetInt32());
    }

    [Fact]
    public void Missing_Domain_Returns_Null()
    {
        var ext = new LokalUtokning();
        Assert.Null(ext["nonexistent.se"]);
    }
}
