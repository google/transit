GTFS Realtime is a feed specification that allows public transportation agencies to provide realtime updates about their fleet to application developers. It is an extension to [GTFS](https://developers.google.com/transit/gtfs/reference) (General Transit Feed Specification), an open data format for public transportation schedules and associated geographic information. GTFS Realtime was designed around ease of implementation, good GTFS interoperability and a focus on passenger information.

The specification was designed through a partnership of the initial [Live Transit Updates](https://developers.google.com/transit/google-transit#LiveTransitUpdates) partner agencies, a number of transit developers and Google. The specification is published under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0.html).

## How do I start?

1.  Continue reading the overview below.
2.  Decide which [feed entities](feed-entities.md) you will be providing.
3.  Take a look at [example feeds](examples/).
4.  Create your own feeds using the [reference](reference.md).
5.  Publish your feed.

## Overview of GTFS Realtime feeds

The specification currently supports the following types of information:

*   **Trip updates** - delays, cancellations, changed routes
*   **Service alerts** - stop moved, unforeseen events affecting a station, route or the entire network
*   **Vehicle positions** - information about the vehicles including location and congestion level

A feed may, although not required to, combine entities of different types. Feeds are served via HTTP and updated frequently. The file itself is a regular binary file, so any type of webserver can host and serve the file (other transfer protocols might be used as well). Alternatively, web application servers could also be used which as a response to a valid HTTP GET request will return the feed. There are no constraints on how frequently nor on the exact method of how the feed should be updated or retrieved.

Because GTFS Realtime allows you to present the _actual_ status of your fleet, the feed needs to be updated regularly - preferably whenever new data comes in from your Automatic Vehicle Location system.

[More about feed entities...](feed-entities.md)

## Data format

The GTFS Realtime data exchange format is based on [Protocol Buffers](https://developers.google.com/protocol-buffers/)

Protocol buffers are a language- and platform-neutral mechanism for serializing structured data (think XML, but smaller, faster, and simpler). The data structure is defined in a [gtfs-realtime.proto](../../proto/gtfs-realtime.proto) file, which then is used to generate source code to easily read and write your structured data from and to a variety of data streams, using a variety of languages – e.g. Java, C++ or Python.

[More about Protocol Buffers...](https://developers.google.com/protocol-buffers/).

## Data structure

The hierarchy of elements and their type definitions are specified in the [gtfs-realtime.proto](../../proto/gtfs-realtime.proto) file.

This text file is used to generate the necessary libraries in your choice of programming language. These libraries provide the classes and functions needed for generating valid GTFS Realtime feeds. The libraries not only make feed creation easier but also ensure that only valid feeds are produced.

[More about the data structure...](reference.md)

## Getting Help

To participate in discussions around GTFS Realtime and suggest changes and additions to the specification, join the [GTFS Realtime mailing list](http://groups.google.com/group/gtfs-realtime).

## Google Maps and Live Transit Updates

One of the possible applications that uses GTFS Realtime is [Live Transit Updates](https://developers.google.com/transit/google-transit#LiveTransitUpdates), a feature within Google Maps that provides users with realtime transit information. If you are working for a public transportation agency that is interested in providing realtime updates to Google Maps, please visit the [Google Transit Partner Page](http://maps.google.com/help/maps/transit/partners/live-updates.html).
