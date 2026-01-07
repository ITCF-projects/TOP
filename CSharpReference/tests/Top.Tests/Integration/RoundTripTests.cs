using System.Text.Json;
using Top.Model;
using Top.Serialization;

namespace Top.Tests.Integration;

/// <summary>
/// Integration tests verifying complete round-trip serialization/deserialization
/// of realistic TOP messages.
/// </summary>
public class RoundTripTests
{
    private readonly TopSerializer _serializer = new();

    [Fact]
    public void Person_With_All_Mixins_RoundTrips_Correctly()
    {
        var original = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare
                {
                    Namnrymd = "larosate.se/idp",
                    Typnamn = "person-uuid",
                    Varde = "550e8400-e29b-41d4-a716-446655440000"
                },
                Korrelationsidn = new List<Identifierare>
                {
                    new() { Namnrymd = "*", Typnamn = "personnummer", Varde = "19850315-1234" },
                    new() { Namnrymd = "orcid.org", Typnamn = "orcid", Varde = "0000-0001-2345-6789" }
                }
            },
            Giltighet = new MedGiltighet
            {
                Giltighetsperiod = new Giltighetsperiod
                {
                    GiltigFrom = new DateTimeOffset(2020, 1, 1, 0, 0, 0, TimeSpan.Zero),
                    OgiltigFrom = new DateTimeOffset(2025, 12, 31, 23, 59, 59, TimeSpan.Zero)
                },
                UtvarderadGiltighet = Giltighetsenum.Aktuellt
            },
            Taggning = new MedTaggning
            {
                Taggar = new List<Tagg>
                {
                    new()
                    {
                        Namnrymd = "*",
                        Typnamn = "anstallningsliknande",
                        Varde = "ja",
                        Namn = new SprakhanteradText { Svenska = "Anställningsliknande", Engelska = "Employment-like" }
                    }
                }
            },
            Fornamn = "Anna Maria",
            Tilltalsnamn = "Anna",
            Efternamn = "Andersson",
            FormatteratNamn = "Anna Maria Andersson",
            Avliden = false,
            StatligAnstallningFrom = new DateOnly(2015, 8, 1)
        };

        // Round-trip
        var json = _serializer.Serialize(original);
        var restored = _serializer.Deserialize<Person>(json);

        // Verify
        Assert.NotNull(restored);
        Assert.Equal(original.Identifiering.Postid.Varde, restored.Identifiering.Postid.Varde);
        Assert.Equal(2, restored.Identifiering.Korrelationsidn?.Count);
        Assert.Equal(original.Giltighet?.UtvarderadGiltighet, restored.Giltighet?.UtvarderadGiltighet);
        Assert.Equal(original.Giltighet?.Giltighetsperiod?.GiltigFrom, restored.Giltighet?.Giltighetsperiod?.GiltigFrom);
        Assert.Single(restored.Taggning?.Taggar ?? new List<Tagg>());
        Assert.Equal("Anställningsliknande", restored.Taggning?.Taggar?[0].Namn?.Svenska);
        Assert.Equal(original.Fornamn, restored.Fornamn);
        Assert.Equal(original.Tilltalsnamn, restored.Tilltalsnamn);
        Assert.Equal(original.Efternamn, restored.Efternamn);
        Assert.Equal(original.Avliden, restored.Avliden);
        Assert.Equal(original.StatligAnstallningFrom, restored.StatligAnstallningFrom);
    }

    [Fact]
    public void Complete_Organisationsdel_With_Relations_RoundTrips_Correctly()
    {
        var original = new Organisationsdel
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare
                {
                    Namnrymd = "larosate.se",
                    Typnamn = "org-id",
                    Varde = "CSE"
                }
            },
            Giltighet = new MedGiltighet
            {
                UtvarderadGiltighet = Giltighetsenum.Aktuellt
            },
            Namn = new SprakhanteradText
            {
                Svenska = "Institutionen för data- och informationsteknik",
                Engelska = "Department of Computer Science and Engineering"
            },
            Typer = new List<Tagg>
            {
                new() { Namnrymd = "*", Typnamn = "orgtyp", Varde = "institution" }
            },
            Kommunikationsvagar = new Kommunikation
            {
                Elektronisk = new List<ElektroniskAdress>
                {
                    new()
                    {
                        Media = new Tagg { Namnrymd = "*", Typnamn = "media", Varde = "email" },
                        Adress = "info@cse.larosate.se"
                    }
                },
                Telefon = new List<Telefonnummer>
                {
                    new()
                    {
                        Nummer = "+46317721000",
                        Formatterat = "+46 (0)31-772 10 00",
                        KanTaEmotSMS = false
                    }
                }
            }
        };

        var json = _serializer.Serialize(original);
        var restored = _serializer.Deserialize<Organisationsdel>(json);

        Assert.NotNull(restored);
        Assert.Equal("CSE", restored.Identifiering.Postid.Varde);
        Assert.Equal("Institutionen för data- och informationsteknik", restored.Namn?.Svenska);
        Assert.Equal("Department of Computer Science and Engineering", restored.Namn?.Engelska);
        Assert.Single(restored.Typer ?? new List<Tagg>());
        Assert.Equal("info@cse.larosate.se", restored.Kommunikationsvagar?.Elektronisk?[0].Adress);
        Assert.Equal("+46317721000", restored.Kommunikationsvagar?.Telefon?[0].Nummer);
    }

    [Fact]
    public void Anknytningsavtal_With_Nested_Entities_RoundTrips_Correctly()
    {
        var original = new Anknytningsavtal
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "larosate.se", Typnamn = "avtal-id", Varde = "A001" }
            },
            Typ = new Tagg
            {
                Namnrymd = "*",
                Typnamn = "anknytningstyp",
                Varde = "anstallning",
                Namn = new SprakhanteradText { Svenska = "Anställning", Engelska = "Employment" }
            },
            Giltighet = new MedGiltighet
            {
                Giltighetsperiod = new Giltighetsperiod
                {
                    GiltigFrom = new DateTimeOffset(2020, 1, 1, 0, 0, 0, TimeSpan.Zero)
                },
                UtvarderadGiltighet = Giltighetsenum.Aktuellt
            },
            ArHuvudavtal = true,
            Anstallningsnummer = 12345,
            Befattningsnamn = "Universitetslektor",
            BESTA = "A1234567X",
            LopandeErsattningar = new List<LopandeErsattning>
            {
                new()
                {
                    Typ = new Tagg { Namnrymd = "*", Typnamn = "ersattningstyp", Varde = "manadslön" },
                    Varde = 45000m,
                    Valuta = "SEK",
                    Giltighet = new MedGiltighet
                    {
                        Giltighetsperiod = new Giltighetsperiod
                        {
                            GiltigFrom = new DateTimeOffset(2023, 1, 1, 0, 0, 0, TimeSpan.Zero)
                        }
                    }
                }
            },
            Omfattningsperioder = new List<Omfattningsperiod>
            {
                new()
                {
                    Heltidsandel = 1.0m,
                    Giltighet = new MedGiltighet { UtvarderadGiltighet = Giltighetsenum.Aktuellt }
                }
            }
        };

        var json = _serializer.Serialize(original);
        var restored = _serializer.Deserialize<Anknytningsavtal>(json);

        Assert.NotNull(restored);
        Assert.Equal("A001", restored.Identifiering.Postid.Varde);
        Assert.Equal("anstallning", restored.Typ.Varde);
        Assert.True(restored.ArHuvudavtal);
        Assert.Equal(12345, restored.Anstallningsnummer);
        Assert.Equal("Universitetslektor", restored.Befattningsnamn);
        Assert.Equal("A1234567X", restored.BESTA);
        Assert.Single(restored.LopandeErsattningar ?? new List<LopandeErsattning>());
        Assert.Equal(45000m, restored.LopandeErsattningar?[0].Varde);
        Assert.Equal("SEK", restored.LopandeErsattningar?[0].Valuta);
        Assert.Single(restored.Omfattningsperioder ?? new List<Omfattningsperiod>());
        Assert.Equal(1.0m, restored.Omfattningsperioder?[0].Heltidsandel);
    }

    [Fact]
    public void Complete_Meddelande_With_Multiple_Entities_RoundTrips_Correctly()
    {
        var person1 = CreateTestPerson("P001", "Anna", "Andersson");
        var person2 = CreateTestPerson("P002", "Bertil", "Bengtsson");
        var org = CreateTestOrganisationsdel("ORG001", "Testavdelningen");
        var roll = CreateTestRoll("R001", "Studievägledare");

        var original = new Meddelande
        {
            Personer = new List<Person> { person1, person2 },
            Organisationsdel = org,
            Roll = roll
        };

        var json = _serializer.Serialize(original);
        var restored = _serializer.Deserialize<Meddelande>(json);

        Assert.NotNull(restored);
        Assert.Equal(2, restored.Personer?.Count);
        Assert.Equal("Anna", restored.Personer?[0].Fornamn);
        Assert.Equal("Bertil", restored.Personer?[1].Fornamn);
        Assert.Equal("ORG001", restored.Organisationsdel?.Identifiering.Postid.Varde);
        Assert.Equal("R001", restored.Roll?.Identifiering.Postid.Varde);
    }

    [Fact]
    public void LokalUtokning_Preserves_Arbitrary_Json_Structure()
    {
        var extensionJson = JsonDocument.Parse("""
        {
            "customField": "custom value",
            "nestedObject": {
                "innerField": 42,
                "innerArray": [1, 2, 3]
            },
            "booleanField": true
        }
        """);

        var original = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            LokalUtokning = new MedLokalUtokning
            {
                LokalUtokning = new LokalUtokning()
            }
        };
        original.LokalUtokning.LokalUtokning["chalmers.se"] = extensionJson.RootElement;

        var json = _serializer.Serialize(original);
        var restored = _serializer.Deserialize<Person>(json);

        Assert.NotNull(restored?.LokalUtokning?.LokalUtokning);
        var ext = restored.LokalUtokning.LokalUtokning["chalmers.se"];
        Assert.NotNull(ext);
        Assert.Equal("custom value", ext.Value.GetProperty("customField").GetString());
        Assert.Equal(42, ext.Value.GetProperty("nestedObject").GetProperty("innerField").GetInt32());
        Assert.True(ext.Value.GetProperty("booleanField").GetBoolean());
    }

    [Fact]
    public void SprakhanteradText_With_Multiple_Languages_RoundTrips_Correctly()
    {
        var original = new Roll
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "R1" }
            },
            Namn = new SprakhanteradText
            {
                Svenska = "Prefekt",
                Engelska = "Head of Department"
            },
            Beskrivning = new SprakhanteradText
            {
                Svenska = "Ansvarar för institutionens verksamhet",
                Engelska = "Responsible for department operations"
            }
        };
        original.Namn["de"] = "Abteilungsleiter";
        original.Namn["fr"] = "Chef de département";

        var json = _serializer.Serialize(original);
        var restored = _serializer.Deserialize<Roll>(json);

        Assert.NotNull(restored?.Namn);
        Assert.Equal("Prefekt", restored.Namn.Svenska);
        Assert.Equal("Head of Department", restored.Namn.Engelska);
        Assert.Equal("Abteilungsleiter", restored.Namn["de"]);
        Assert.Equal("Chef de département", restored.Namn["fr"]);
        Assert.Equal("Ansvarar för institutionens verksamhet", restored.Beskrivning?.Svenska);
    }

    [Fact]
    public void Giltighetsbegransade_Taggar_RoundTrips_Correctly()
    {
        var original = new Person
        {
            Identifiering = new MedObligatoriskIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "1" }
            },
            Taggning = new MedTaggning
            {
                Taggar = new List<Tagg>
                {
                    new() { Namnrymd = "*", Typnamn = "current", Varde = "now" }
                },
                GiltighetsbegransadeTaggar = new List<MedGiltighetsbegransadTaggning>
                {
                    new()
                    {
                        Tagg = new Tagg { Namnrymd = "*", Typnamn = "historisk", Varde = "tidigare-roll" },
                        Giltighet = new MedGiltighet
                        {
                            Giltighetsperiod = new Giltighetsperiod
                            {
                                GiltigFrom = new DateTimeOffset(2020, 1, 1, 0, 0, 0, TimeSpan.Zero),
                                OgiltigFrom = new DateTimeOffset(2022, 12, 31, 0, 0, 0, TimeSpan.Zero)
                            },
                            UtvarderadGiltighet = Giltighetsenum.Tidigare
                        }
                    },
                    new()
                    {
                        Tagg = new Tagg { Namnrymd = "*", Typnamn = "framtida", Varde = "kommande-roll" },
                        Giltighet = new MedGiltighet
                        {
                            Giltighetsperiod = new Giltighetsperiod
                            {
                                GiltigFrom = new DateTimeOffset(2025, 1, 1, 0, 0, 0, TimeSpan.Zero)
                            },
                            UtvarderadGiltighet = Giltighetsenum.Framtida
                        }
                    }
                }
            }
        };

        var json = _serializer.Serialize(original);
        var restored = _serializer.Deserialize<Person>(json);

        Assert.NotNull(restored?.Taggning);
        Assert.Single(restored.Taggning.Taggar ?? new List<Tagg>());
        Assert.Equal(2, restored.Taggning.GiltighetsbegransadeTaggar?.Count);

        var historisk = restored.Taggning.GiltighetsbegransadeTaggar?[0];
        Assert.Equal("tidigare-roll", historisk?.Tagg.Varde);
        Assert.Equal(Giltighetsenum.Tidigare, historisk?.Giltighet?.UtvarderadGiltighet);

        var framtida = restored.Taggning.GiltighetsbegransadeTaggar?[1];
        Assert.Equal("kommande-roll", framtida?.Tagg.Varde);
        Assert.Equal(Giltighetsenum.Framtida, framtida?.Giltighet?.UtvarderadGiltighet);
    }

    [Fact]
    public void Kommunikation_With_All_Channel_Types_RoundTrips_Correctly()
    {
        var original = new Servicefunktion
        {
            Identifiering = new MedFrivilligIdentifierare
            {
                Postid = new Identifierare { Namnrymd = "test", Typnamn = "id", Varde = "EXP1" }
            },
            Namn = new SprakhanteradText { Svenska = "Studentexpeditionen" },
            Kommunikationsvagar = new Kommunikation
            {
                Telefon = new List<Telefonnummer>
                {
                    new()
                    {
                        Nummer = "+46317721234",
                        Formatterat = "+46 31-772 12 34",
                        KanTaEmotSMS = true,
                        Spridning = new MedSpridning
                        {
                            Synligheter = new List<Spridning>
                            {
                                new()
                                {
                                    Synlighet = new Tagg { Namnrymd = "*", Typnamn = "synlighet", Varde = "extern" },
                                    Ranking = 1
                                }
                            }
                        }
                    }
                },
                Elektronisk = new List<ElektroniskAdress>
                {
                    new()
                    {
                        Media = new Tagg { Namnrymd = "*", Typnamn = "media", Varde = "email" },
                        Adress = "expedition@larosate.se"
                    },
                    new()
                    {
                        Media = new Tagg { Namnrymd = "*", Typnamn = "media", Varde = "web" },
                        Adress = "https://www.larosate.se/expedition"
                    }
                },
                Besok = new List<Besoksadress>
                {
                    new()
                    {
                        Gatuadress = "Universitetsgatan 1",
                        Stad = "Göteborg",
                        Land = "Sverige",
                        Byggnad = new SprakhanteradText { Svenska = "Huvudbyggnaden" },
                        HittaIHuset = new SprakhanteradText { Svenska = "Rum 1234, plan 2" },
                        Besokstider = new List<Besokstider>
                        {
                            new()
                            {
                                Galler = new SprakhanteradText { Svenska = "Vardagar" },
                                Oppnar = "09:00",
                                Stanger = "16:00"
                            }
                        }
                    }
                },
                Snigelpost = new List<Snigelpost>
                {
                    new()
                    {
                        FormatteradAdress = new List<string>
                        {
                            "Studentexpeditionen",
                            "Lärosätet",
                            "Box 123",
                            "405 30 Göteborg",
                            "SWEDEN"
                        },
                        Postnummer = "405 30",
                        Postort = "Göteborg",
                        Landskod = "SE"
                    }
                }
            }
        };

        var json = _serializer.Serialize(original);
        var restored = _serializer.Deserialize<Servicefunktion>(json);

        Assert.NotNull(restored?.Kommunikationsvagar);

        // Telefon
        Assert.Single(restored.Kommunikationsvagar.Telefon ?? new List<Telefonnummer>());
        Assert.Equal("+46317721234", restored.Kommunikationsvagar.Telefon?[0].Nummer);
        Assert.True(restored.Kommunikationsvagar.Telefon?[0].KanTaEmotSMS);

        // Elektronisk
        Assert.Equal(2, restored.Kommunikationsvagar.Elektronisk?.Count);
        Assert.Equal("expedition@larosate.se", restored.Kommunikationsvagar.Elektronisk?[0].Adress);

        // Besök
        Assert.Single(restored.Kommunikationsvagar.Besok ?? new List<Besoksadress>());
        Assert.Equal("Universitetsgatan 1", restored.Kommunikationsvagar.Besok?[0].Gatuadress);
        Assert.Equal("09:00", restored.Kommunikationsvagar.Besok?[0].Besokstider[0].Oppnar);

        // Snigelpost
        Assert.Single(restored.Kommunikationsvagar.Snigelpost ?? new List<Snigelpost>());
        Assert.Equal(5, restored.Kommunikationsvagar.Snigelpost?[0].FormatteradAdress.Count);
        Assert.Equal("405 30", restored.Kommunikationsvagar.Snigelpost?[0].Postnummer);
    }

    // Helper methods
    private static Person CreateTestPerson(string id, string fornamn, string efternamn) => new()
    {
        Identifiering = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "person-id", Varde = id }
        },
        Fornamn = fornamn,
        Efternamn = efternamn,
        Giltighet = new MedGiltighet { UtvarderadGiltighet = Giltighetsenum.Aktuellt }
    };

    private static Organisationsdel CreateTestOrganisationsdel(string id, string namn) => new()
    {
        Identifiering = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "org-id", Varde = id }
        },
        Namn = new SprakhanteradText { Svenska = namn },
        Giltighet = new MedGiltighet { UtvarderadGiltighet = Giltighetsenum.Aktuellt }
    };

    private static Roll CreateTestRoll(string id, string namn) => new()
    {
        Identifiering = new MedObligatoriskIdentifierare
        {
            Postid = new Identifierare { Namnrymd = "test", Typnamn = "roll-id", Varde = id }
        },
        Namn = new SprakhanteradText { Svenska = namn }
    };
}
