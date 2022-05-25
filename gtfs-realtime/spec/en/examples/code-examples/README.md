# Code Examples

GTFS-realtime data is encoded and decoded using [Protocol Buffers](https://developers.google.com/protocol-buffers/), a compact binary representation designed for fast and efficient processing. How does one generate or parse this binary data? Read on for code samples to help you get started.

### Language Bindings
To work with GTFS realtime data, a developer would typically use the [gtfs-realtime.proto](../proto) schema to generate classes in the programming language of their choice. These classes can then be used for constructing GTFS realtime data model objects and serializing them as binary data or, in the reverse direction, parsing binary data into data model objects.

Because generating GTFS realtime data model classes from the [gtfs-realtime.proto](../proto)  schema is such a common task, but also one that sometimes causes confusion for first-time developers, we provide pre-generated GTFS realtime language bindings for a number of the most popular programming languages through the open-source [gtfs-realtime-bindings](https://github.com/google/gtfs-realtime-bindings) project.

Read on for language-specific details on parsing GTFS realtime data:

- [.NET](dotnet.md)
- [Java](java.md)
- [JavaScript/Node.js](nodejs.md)
- [PHP](php.md)
- [Python](python.md)
- [Ruby](ruby.md)

### Other Languages
We have tried to provide language bindings for all programming languages where (a) developers want to use GTFS realtime and (b) there is a mechanism for packaging code for easy re-use.

If you feel that your favorite language has been unjustly left off the list, you have two options:

1. Open an issue at the [gtfs-realtime-bindings](https://github.com/google/gtfs-realtime-bindings) project page requesting that the language be added.
2. Generate your own [Protocol Buffer](https://developers.google.com/protocol-buffers/) bindings, possibly using a [Third-Party Add On](https://github.com/google/protobuf/blob/master/docs/third_party.md).