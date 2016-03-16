## Introduction

The GTFS specification is not set in stone. Instead, it is an open specification
developed and maintained by the community of transit agencies, developers, and
other stakeholders who use GTFS. It is expected that this community of producers
and consumers of GTFS data will have proposals for extending the spec to enable
new capabilities. To help manage that process, the following procedures and
guidelines have been established.

## The Change Process

The general outline for changing the spec has a couple of steps:

1.  Propose a change on the [GTFS-changes discussion
    list](https://groups.google.com/group/gtfs-changes).
2.  Receive comments and feedback from the GTFS community and iterate on the
    proposed change.
3.  Find at least one GTFS producer and one consumer to implement and test the
    proposed change.
4.  Submit a final request-for-comments on the proposed change to the discussion
    list. If no outstanding issues are identified after one week’s time, the
    proposal will be officially adopted.

The [discussion group](https://groups.google.com/group/gtfs-changes) will serve
as the primary place for suggesting changes to the spec, such that users of GTFS
can learn about and offer feedback on proposed changes. If the community
generally agrees that the proposal is worthwhile and follows the GTFS guiding
principles outlined below, it will be officially added to the spec. We also
require that any proposed change be implemented by at least one GTFS producer
and one consumer, in order to verify the feasibility of that change in practice.

In addition to the discussion group, note that the [GTFS Changes
Site](https://sites.google.com/site/gtfschanges/) will be used to document
exiting GTFS change proposals in support of of the discussion group.

## Guiding Principles

In order to preserve the original vision of GTFS, a number of guiding principles
have been established to take into consideration when extending the spec:

### Feeds should be easy to create and edit.

We chose CSV as the basis for the specification because it's easy to view and
edit using spreadsheet programs and text editors, which is helpful for smaller
agencies. It's also straightforward to generate from most programming languages
and databases, which is good for publishers of larger feeds.

### Feeds should be easy to parse.

Feed readers should be able to extract the information they're looking for with
as little work as possible. Changes and additions to the feed should be as
broadly useful as possible, to minimize the number of code paths that readers of
the feed need to implement. (However, making creation easier should be given
precedence, since there will ultimately be more feed publishers than feed
readers.)

### Changes to the spec should be backwards-compatible.

When adding features to the specification, we want to avoid making changes that
will make existing feeds invalid. We don't want to create more work for existing
feed publishers until they want to add capabilities to their feeds. Also,
whenever possible, we want existing parsers to be able to continue to read the
older parts of newer feeds.

### Speculative features are discouraged.

Every new feature adds complexity to the creation and reading of feeds.
Therefore, we want to take care to only add features that we know to be useful.
Ideally, any proposal will have been tested by generating data for a real
transit system that uses the new feature and writing software to read and
display it. Note that the GTFS readily allows for extensions to the format
through the addition of extra columns and files that are ignored by the official
parsers & validators, so proposals can be easily prototyped and tested on
existing feeds.

## Revision History

### February 3, 2016

-   Added agency.txt 'agency\_email' proposal to spec:
    [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/aezjQsriLYA)

### February 2, 2015

-   Added stop\_times.txt 'timepoint' proposal to spec:
    [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/Ah-J9JP2rJY)

### February 17, 2014

-   Added trips.txt 'bikes\_allowed' proposal to spec:
    [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/rEiSeKNc4cs)

### October 15, 2012

-   Added trips.txt 'wheelchair\_accessible' proposal to spec:
    [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/xyPh5stQ8o4)

### June 20, 2012

-   Added 'wheelchair\_boarding' proposal to spec:
    [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/ASxItgsQlh4)

### February 2, 2012

-   Added 'stop\_timezone' proposal to spec:
    [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/d8897443d397aaee)

### January 18, 2012

-   Migrated documentation from old [code.google.com](http://code.google.com/)
    to their new location at
    [developers.google.com](http://developers.google.com/).

### September 26, 2011

-   Added 'feed\_info' proposal to spec:
    [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/4a1d1ee28f68d86c)

### September 6, 2011

-   Added 'agency\_fare\_url' proposal to spec:
    [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/669f6b3c6d3b0a01/a20633df56424c5e)
-   Added 'exact\_times' proposal to spec:
    [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/9d917d95b43b4d0b/1298765a30b12edf)

### March 30, 2009

-   A new section on making a transit feed publicly available. This wasn't
    previously discussed on the group, because it wasn't strictly a change to
    how the data is interpreted or written. However, some of the folks at Google
    thought that it would be informative to include discussion of non-Google
    uses of GTFS, since there are an increasing number of applications that can
    make use of GTFS-formatted data.
-   CSV format clarifications:
    [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/d37ab3e5a4c0da69).
-   Additional guidance on how to pick contrasting colors in the descriptions of
    the route\_color and route\_text\_color fields.
-   trip\_short\_name, as proposed and tested in these threads:
    [a](https://groups.google.com/group/gtfs-changes/browse_thread/thread/ab34be2731aa2288)
    and
    [b](https://groups.google.com/group/gtfs-changes/browse_thread/thread/5cf5e5933d108dc).
-   A fix for a minor error in the sample data included at the end of the
    document (giving stop S7 the parent\_station S8).
-   Added "agency\_lang" information to the sample data at the end of the
    document, as suggested by Marcy during the comment period:
    [discussion](https://groups.google.com/group/gtfs-changes/browse_thread/thread/e6a3f5903505ab1d/9c006a18aad87e72).
-   Updated the link to OCTA's GTFS feed in the sidebar
-   See [orignial
    summary](https://groups.google.com/group/gtfs-changes/browse_thread/thread/70bd44e2828aa4ac).

### February 26, 2009

-   Removed most of the Google-specific feed submission instructions, since
    there are many other applications that consume GTFS data at this point.
-   Fixed a broken link in the sidebar to Orange County OCTA's public feed.

### August 7, 2008

-   Restored the stop\_url field, which was accidentally omitted in the August 6
    version
-   Added agency\_phone to sample data
-   Added a mention of the data use agreement when submitting a feed to Google

### August 6, 2008

-   Added transfers.txt file, allowing the feed publishers to provide hints on
    preferred transfer behavior ([original
    proposal](https://groups.google.com/group/gtfs-changes/browse_thread/thread/d2090e9e2f37697b))
-   Added location\_type and parent\_station fields to stops.txt, allowing stop
    points to be grouped into stations ([original
    proposal](https://groups.google.com/group/gtfs-changes/browse_thread/thread/49c180c99f5aff2c/f46db59beec6bdba))
-   Added agency\_phone field for providing voice telephone number for an agency
    ([original
    proposal](https://groups.google.com/group/gtfs-changes/browse_thread/thread/f08b6de7cb9ecaa0))
-   Added "Testing Your Feeds" section mentioning open-source testing tools
-   Added clarifications about CSV format, agency\_timezone, agency\_lang,
    route\_color, route\_text\_color, arrival\_time, departure\_time,
    calendar.txt vs. calendar\_dates.txt, fare tables, and frequencies.txt
-   Added link to feed history document, and corrected some public feed links
-   Updated example images to depict the current Google Maps UI
-   Updated/fixed sample data in document

### February 29, 2008

-   Added the stop\_code field in stops.txt to allow for the specification of
    rider-facing stop codes ([original
    proposal](https://groups.google.com/group/gtfs-changes/browse_thread/thread/93d03de5f6197b17))
-   Clarified the descriptions of route\_short\_name and route\_long\_name in
    routes.txt
-   Clarified the descriptions of arrival\_time and departure\_time in
    stop\_times.txt
-   Fixed typos in the Sample Data section

### November 20, 2007

-   Clarified block\_id description
-   Changed language to de-emphasize Google Transit (since non-Google
    applications are using GTFS, and transit routing is now an integrated
    feature of Google Maps), and to fix assorted typos
-   Updated example screenshots to reflect the presentation of GTFS fields in
    the current Google Maps UI
-   Updated the Google contact email address for transit data providers
-   Updated formatting

### October 5, 2007

-   Changed stop\_sequence and shape\_pt\_sequence to allow for any increasing
    non-negative integers
-   Clarified descriptions and fixed typos

### May 31, 2007

-   Updated page style, made HTML cleaner and more accessible
-   Added links to public feed examples and other useful sites
-   Removed examples from individual field descriptions

### April 9, 2007

-   Added section on [submitting a
    feed](/transit/google-transit#SubmitFeedToGoogle).
-   Added the [Example Demo Transit Agency
    feed](/transit/gtfs/examples/gtfs-feed).
-   Added note that *calendar.txt* can be omitted if all the service dates are
    defined in *calendar\_dates.txt*.
-   Made the *agency\_id* field optional in feeds containing only one agency.
    This allows existing feeds without *agency\_id* to remain valid.
-   Added fuller specification of *agency\_url*, *stop\_url*, and *route\_url*,
    and additional example values for those fields.
-   Added *6* (Gondola) and *7* (Funicular) as valid *route\_type* values.

### March 8, 2007

-   Minor edit to move the *stop\_url* field from *stop\_times.txt*, where it
    was incorrectly specified in the Feb. 28 update, to *stops.txt*, where it
    belongs.

### March 5, 2007

-   Minor edit to clarify the description of the *route\_long\_name* field.

### February 28, 2007

-   Addition of *frequencies.txt* for headway-based schedule support.
-   Multiple agencies now allowed in the the same feed. Also added new
    *agency\_id* field in both *agencies.txt* and *routes.txt* that lets you
    specify which route is operated by which agency.
-   Addition of per-route and per-stop URLs.
-   Addition of *direction\_id* field in *trips.txt*.
-   Support for mid-trip headsign changes with addition of *stop\_headsign*
    field in *stop\_times.txt*.
-   Support for route colors with addition of optional *route\_color* and
    *route\_text\_color* in *routes.txt*.
-   Removed the ability to specify stops using street addresses. The previous
    version of the spec allowed you to give the location of a transit stop using
    a street address in the stop\_street, stop\_city, stop\_region,
    stop\_postcode, and stop\_country fields. Now stop locations must be given
    using *stop\_lat* for latitude and *stop\_lon* for longitude, which are more
    useful for most applications.
-   Addition of cable car vehicle type for *route\_type* field in *routes.txt*.
-   See the original [Headway blog
    post](http://headwayblog.com/2007/03/02/google-feed-spec-update-2007-02/)
    summary of the changes.

### November 29, 2006

-   Added support for trip shape information via *shapes.txt*
-   Clarified the definition of *stop\_sequence*
-   Marked *pickup\_type* and *drop\_off\_type* optional

### October 31, 2006

-   Added support for fare information
-   Removed dates from individual file names
-   Changed the *route\_type* value definitions
-   Allowed for multiple feed files to be posted at the same time, as long as
    their service periods didn't overlap
-   Fixed *block\_id* in *trips.txt* so that it was correctly marked *Optional*
-   Noted that column headers **must** be included

### September 29, 2006

-   Minor edit to fix a couple errors in the examples.

### September 25, 2006

-   Initial version.

