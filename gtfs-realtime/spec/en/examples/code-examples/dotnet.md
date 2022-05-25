# .NET
To use the `gtfs-realtime-bindings` .NET classes in your own project, you need to first install the module from the [NuGet repository](https://www.nuget.org/packages/GtfsRealtimeBindings/).

```
Install-Package GtfsRealtimeBindings
```

The following code snippet demonstrates downloading a GTFS realtime data feed from a particular URL, parsing it as a `FeedMessage` (the root type of the GTFS realtime schema), and iterating over the results.

```vb
using System.Net;
using ProtoBuf;
using transit_realtime;

WebRequest req = HttpWebRequest.Create("URL OF YOUR GTFS-REALTIME SOURCE GOES HERE");
FeedMessage feed = Serializer.Deserialize<FeedMessage>(req.GetResponse().GetResponseStream());

foreach (FeedEntity entity in feed.entity) {
  ...
}
```

For more details, see the [.NET project page](https://github.com/google/gtfs-realtime-bindings/tree/master/dotnet).