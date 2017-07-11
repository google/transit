# What is GTFS?

The General Transit Feed Specification (GTFS) defines a common format for public transportation schedules and associated geographic information. GTFS "feeds" allow public transit agencies to publish their transit data and developers to write applications that consume that data in an interoperable way.

## How do I start?

1.  Continue reading the overview below.
1.  Take a look at the [example feeds](examples/).
1.  Create your own feeds using the [reference](reference.md) as a guide.
1.  Test your feed using [validation tools](tools.md).
1.  Publish your feed.

## Overview of a GTFS feed

A GTFS feed is composed of a series of text files collected in a ZIP file. Each file models a particular aspect of transit information: stops, routes, trips, and other schedule data. The details of each file are defined in the [GTFS reference](reference.md). An example feed can be found in the [GTFS examples](examples/). A transit agency can produce a GTFS feed to share their public transit information with developers, who write tools that consume GTFS feeds to incorporate public transit information into their applications. GTFS can be used to power trip planners, time table publishers, and a variety of applications, too diverse to list here, that use public transit information in some way.

## Making a Transit Feed Publicly Available

Many applications are compatible with data in the GTFS format. The simplest way to make a feed public is to host it on a web server and publish an announcement that makes it available for use.

Here are a few ways that interested software developers learn about public feeds:

* A list of transit agencies who provide public feeds is available on the [TransitWiki.org "Publicly-accessible public transportation data" page](http://www.transitwiki.org/TransitWiki/index.php?title=Publicly-accessible_public_transportation_data).
* Several websites allows developers to subscribe to announcements about new and updated feeds, and serve as a registry of feeds:
  * [Gtfs Data Exchange.com](http://www.gtfs-data-exchange.com/)
  * [TransitFeeds.com](http://transitfeeds.com/)
  * [Transit.land](https://transit.land/feed-registry/)

## Submitting a Transit Feed to Google

If you're at a public agency that oversees public transportation for your city, you can use the GTFS specification to provide schedules and geographic information to Google Maps and other Google applications that show transit information. For full details, please refer to the [Google Transit Partners Program website](http://maps.google.com/help/maps/mapcontent/transit/participate.html).

## Getting Help

To participate in discussions around GTFS and suggest changes and additions to the specification, join the [GTFS changes mailing list](http://groups.google.com/group/gtfs-changes).

*Except as otherwise noted, the content of this page is licensed under the Creative Commons Attribution 3.0 License.*