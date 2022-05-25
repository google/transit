# Java

To use the `gtfs-realtime-bindings` Java classes in your own project, you need to add an appropriate dependency. We publish our module to the [Maven Central Repository](https://search.maven.org/) so that it can be easily referenced by Java build tools like Maven, Ivy, and Gradle.

In the dependency snippets below, replace version string `X.Y.Z` with the latest version available in the [Maven Central Repository](https://search.maven.org/#search%7Cga%7C1%7Ca%3A%22gtfs-realtime-bindings%22).

For [Maven](https://maven.apache.org/), add the following to your `pom.xml` dependencies section:

```xml
<dependency>
  <groupId>com.google.transit</groupId>
  <artifactId>gtfs-realtime-bindings</artifactId>
  <version>X.Y.Z</version>
</dependency>
```

For [Gradle](https://www.gradle.org/), add the following to your `build.gradle` dependencies section:

```java
compile group: 'org.google.transit', name: 'gtfs-realtime-bindings', version: 'X.Y.Z'
```

The following code snippet demonstrates downloading a GTFS realtime data feed from a particular URL, parsing it as a `FeedMessage` (the root type of the GTFS realtime schema), and iterating over the results.

```java
import java.net.URL;

import com.google.transit.realtime.GtfsRealtime.FeedEntity;
import com.google.transit.realtime.GtfsRealtime.FeedMessage;

public class GtfsRealtimeExample {
  public static void main(String[] args) throws Exception {
    URL url = new URL("URL OF YOUR GTFS-REALTIME SOURCE GOES HERE");
    FeedMessage feed = FeedMessage.parseFrom(url.openStream());
    for (FeedEntity entity : feed.getEntityList()) {
      if (entity.hasTripUpdate()) {
        System.out.println(entity.getTripUpdate());
      }
    }
  }
}
```

For more details, see the [Java project page](https://github.com/google/gtfs-realtime-bindings/tree/master/java).