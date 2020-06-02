The GTFS Specification is not set in stone. Instead, it is an open specification developed and maintained by the community of transit agencies, developers, and other stakeholders who use GTFS. It is expected that this community of producers and consumers of GTFS data will have proposals for extending the spec to enable new capabilities. To help manage that process, the following procedures and guidelines have been established.

### Specification amendment process
The official specification, reference and documentation are written in English. If a translation to a different language differs from the English original, the latter takes precedence. All communication is performed in English.

1. Create a git branch with update of all relevant parts of protocol definition, specification and documentation files (except for translations).
1. Create pull request on https://github.com/google/transit. Pull request must contain an extended description of the patch. The creator of the pull request becomes the _advocate_.
1. Once pull request is registered, it must be announced by its advocate in the [GTFS Changes mailing list](https://groups.google.com/forum/#!forum/gtfs-changes), including a link to the pull request. Once announced, the pull request is considered a proposal.  The pull request should also be edited to contain a link to the Google Groups announcement so they can easily be cross-referenced.
  	- Since the advocate is a contributor, they must sign the [Contributor License Agreement](../CONTRIBUTING.md) before pull request can be accepted.
1. The discussion of the proposal follows. Pull request comments should be used as the sole discussion forum.
  	- The discussion lasts for as long as the advocate feels necessary, but must be at least 7 calendar days.
  	- The advocate is responsible for timely update of the proposal (i.e. pull request) based on the comments for which they agree to.
  	- At any point in time the advocate can claim proposal abandoned.
1. The advocate can call for a vote on a version of the proposal at any point in time following the initial 7-day interval required for discussion.
  	- Before calling for a vote, at least one GTFS producer and one GTFS consumer should implement the proposed change.  It is expected that the GTFS producer(s) include the change in a public-facing GTFS feed and provide a link to that data within the pull request comments, and that the GTFS consumer(s) provides a link in the pull request comments to an application that is utilizing the change in a non-trivial manner (i.e, it is supporting new or improved functionality).
1. Vote lasts the minimum period sufficient to cover 7 full calendar days and 5 full Swiss business days. Vote ends at 23:59:59 UTC.
  	- The advocate should announce the specific end time at the start of the vote.
  	- During voting period only editorial changes to the proposal are allowed (typos, wording may change as long as it does not change the meaning).
  	- Anyone is allowed to vote yes/no in a form of comment to the pull request, and votes can be changed until the end of the voting period.
    If a voter changes her vote, it is recommended to do it by updating the original vote comment by striking through the vote and writing the new vote.
  	- Votes before the start of the voting period are not considered.
1. The proposal is accepted if there is a unanimous consensus yes with at least 3 votes.
  	- The proposer's vote does not count towards the 3 vote total. For example, if Proposer X creates a pull request and votes yes, and User Y and Z vote yes, this is counted as 2 total yes votes.
  	- Votes against shall be motivated, and ideally provide actionable feedback.
  	- If the vote has failed, then the advocate may choose to continue work on the proposal, or to abandon the proposal.
    Either decision of the advocate must be announced in the mailing list.
  	- If the advocate continues the work on proposal then a new vote can be called for at any point in time but no later than 30 calendar days after the end of the previous vote.
  	- If a vote was not called within 30 calendar days from the original proposal or 30 calendar days since end of the previous vote, then the proposal is abandoned.
1. If the proposal is abandoned, the corresponding pull request is closed.
1. If the proposal is accepted:
  	- Google is committed to merging the voted upon version of the pull request (provided that the contributors have signed the [CLA](../CONTRIBUTING.md)), and performing the pull request within 5 business days.
  	- Translations must not be included into the original pull request.
    Google is responsible for eventually updating relevant translations into supported languages, but pure translation pull requests from the community are welcome and will be accepted as soon as all editorial comments are addressed.
1. The final result of the pull request (accepted or abandoned) should be announced on the same Google Groups thread where the pull request was originally announced.

### Guiding Principles
In order to preserve the original vision of GTFS, a number of guiding principles have been established to take into consideration when extending the spec:

#### Feeds should be easy to create and edit
We chose CSV as the basis for the specification because it's easy to view and edit using spreadsheet programs and text editors, which is helpful for smaller agencies. It's also straightforward to generate from most programming languages and databases, which is good for publishers of larger feeds.

#### Feeds should be easy to parse
Feed readers should be able to extract the information they're looking for with as little work as possible. Changes and additions to the feed should be as broadly useful as possible, to minimize the number of code paths that readers of the feed need to implement. (However, making creation easier should be given precedence, since there will ultimately be more feed publishers than feed readers.)

#### Changes to the spec should be backwards-compatible
When adding features to the specification, we want to avoid making changes that will make existing feeds invalid. We don't want to create more work for existing feed publishers until they want to add capabilities to their feeds. Also, whenever possible, we want existing parsers to be able to continue to read the older parts of newer feeds.

#### Speculative features are discouraged
Every new feature adds complexity to the creation and reading of feeds. Therefore, we want to take care to only add features that we know to be useful. Ideally, any proposal will have been tested by generating data for a real transit system that uses the new feature and writing software to read and display it. Note that the GTFS readily allows for extensions to the format through the addition of extra columns and files that are ignored by the official parsers & validators, so proposals can be easily prototyped and tested on existing feeds.

### Revision History

#### May 28, 2020

* Updated major GTFS changes under "Revision History" in `CHANGES.md`. Last revised in January 2019 with some historical entries missing.

#### May 13, 2020

* Added `continuous_pickup` and `continuous_drop_off` to `routes.txt` and `stop_times.txt`.  See [discussion](https://github.com/google/transit/pull/208).
* Changed `shape_id` from "Optional" to "Conditionally required". See [discussion](https://github.com/google/transit/pull/208).

#### March 24, 2020

* Defined text-to-speech field and added `tts_stop_name` to `stops.txt`. See [discussion](https://github.com/google/transit/pull/49).

#### February 5, 2020

* Added trolleybus and monorail `route_types`. See [discussion](https://github.com/google/transit/pull/174).

#### January 9, 2020

* Added `translations.txt`. See [discussion](https://github.com/google/transit/pull/180).

#### December 26, 2019

* Updated definitions for cable tram and aerial lift in `route_type`. See [discussion](https://github.com/google/transit/pull/186).

#### December 20, 2019

* Added `attributions.txt`. See [discussion](https://github.com/google/transit/pull/192).

#### August 26, 2019

* Specified that `stop_lat` and `stop_lon` be positioned where passengers wait to board the vehicle. See [discussion](https://github.com/google/transit/pull/179).

#### July 9, 2019

* Added arrival and departure time best practices. See [discussion](https://github.com/google/transit/pull/165).
* Added headsign best practices. See [discussion](https://github.com/google/transit/pull/167).
* Added `stop_id` best practices. See [discussion](https://github.com/google/transit/pull/169).

#### June 25, 2019

* Clarified relationship of shape points and stops. See [discussion](https://github.com/google/transit/pull/39).

#### April 4, 2019

* Added `platform_code` field in `stops.txt`. See [discussion](https://github.com/google/transit/pull/146).

#### March 27, 2019

* Added `pathways.txt` and `levels.txt` to GTFS-static. See [discussion](https://github.com/google/transit/pull/143).

#### February 6, 2019

* Editorial and formatting changes for clarity.  See [discussion](https://github.com/google/transit/pull/120).

#### October 2, 2018

* Factorized field types for conciseness.  See [discussion](https://github.com/google/transit/pull/104).

#### September 4, 2018

* Added "Conditionally required" concept. See [discussion](https://github.com/google/transit/pull/100).
* Unified the definitions of `agency_lang` and `feed_lang`. See [discussion](https://github.com/google/transit/pull/98).

#### August 27, 2018

* Updated `CHANGES.md` and last revised date. See [discussion](https://github.com/google/transit/pull/99).

#### August 22, 2018

* Added `feed_contact_email` and `feed_contact_url` fields in the `feed_info.txt` file. See [discussion](https://github.com/google/transit/pull/31).

#### December 11, 2017

* Added `route_sort_order` to `routes.txt`. See [discussion](https://github.com/google/transit/pull/83).

#### March 15, 2017

* Clarified that a proposer's vote does not count towards total. See [discussion](https://github.com/google/transit/pull/50).
* Specified that at before calling a vote, at least one GTFS producer and one GTFS consumer should implement the proposed change. See [discussion](https://github.com/google/transit/pull/46).

#### February 7, 2017

* Clarified relationship of `block_id` and `service_id`. See [discussion](https://github.com/google/transit/pull/44).
* Clarified that frequency-based service begins at vehicle departure. See [discussion](https://github.com/google/transit/pull/42).
* Clarified descriptions of `stop_id` and `stop_code`. See [discussion](https://github.com/google/transit/pull/40).

#### December 11, 2017

* Added `route_sort_order` field in the `routes.txt` file. See [discussion](https://github.com/google/transit/pull/83).

#### November 27, 2016

* Added station entrance as a `stops.location_type`. See [discussion](https://github.com/google/transit/pull/30).

#### September 2, 2016

* Updated documentation to add `agency_id` under `fare_attributes.txt`. See [discussion](https://github.com/google/transit/pull/27).

#### March 16, 2016

* Transition of GTFS documentation to Github at https://github.com/google/transit

#### February 3, 2016

* Added  `agency_email` to `agency.txt` proposal to spec: [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/aezjQsriLYA)

#### February 2, 2015

* Added stop_times.txt 'timepoint' proposal to spec: [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/Ah-J9JP2rJY)

#### February 17, 2014

* Added trips.txt 'bikes_allowed' proposal to spec: [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/rEiSeKNc4cs)

#### October 15, 2012

Added trips.txt 'wheelchair_accessible' proposal to spec: [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/ASxItgsQlh4)

#### June 20, 2012

* Added 'wheelchair_boarding' proposal to spec: [discussion](https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/ASxItgsQlh4)

#### February 2, 2012

* Added 'stop_timezone' proposal to spec: [discussion](https://groups.google.com/forum/#!topic/gtfs-changes/2Il0Q9OXqu4)

#### January 18, 2012

* Migrated documentation from old code.google.com to their new location at developers.google.com.

#### September 26, 2011

* Added 'feed_info' proposal to spec: [discussion](https://groups.google.com/forum/#!topic/gtfs-changes/Sh0e4o9o2Gw)

#### September 6, 2011

* Added 'agency_fare_url' proposal to spec: [discussion](https://groups.google.com/forum/#!topic/gtfs-changes/Zp9rPG07CgE)
* Added 'exact_times' proposal to spec: [discussion](https://groups.google.com/forum/#!topic/gtfs-changes/nZF9lbQ7TQs)

#### March 30, 2009

* A new section on making a transit feed publicly available. This wasn't previously discussed on the group, because it wasn't strictly a change to how the data is interpreted or written. However, some of the folks at Google thought that it would be informative to include discussion of non-Google uses of GTFS, since there are an increasing number of applications that can make use of GTFS-formatted data.
* CSV format clarifications: [discussion](https://groups.google.com/forum/#!topic/gtfs-changes/03qz5aTA2mk).
* Additional guidance on how to pick contrasting colors in the descriptions of the route_color and route_text_color fields.
* trip_short_name, as proposed and tested in these threads: a and b.
* A fix for a minor error in the sample data included at the end of the document (giving stop S7 the parent_station S8).
* Added "agency_lang" information to the sample data at the end of the document, as suggested by Marcy during the comment period: [discussion](https://groups.google.com/forum/#!topic/gtfs-changes/5qP1kDUFqx0).
* Updated the link to OCTA's GTFS feed in the sidebar
* See [original summary](https://groups.google.com/forum/#!topic/gtfs-changes/cL1E4oKKpKw).

#### February 26, 2009

* Removed most of the Google-specific feed submission instructions, since there are many other applications that consume GTFS data at this point.
* Fixed a broken link in the sidebar to Orange County OCTA's public feed.

#### August 7, 2008

* Restored the stop_url field, which was accidentally omitted in the August 6 version
* Added agency_phone to sample data
* Added a mention of the data use agreement when submitting a feed to Google

#### August 6, 2008

* Added transfers.txt file, allowing the feed publishers to provide hints on preferred transfer behavior ([original proposal](https://groups.google.com/forum/#!topic/gtfs-changes/cL1E4oKKpKw))
* Added location_type and parent_station fields to stops.txt, allowing stop points to be grouped into stations ([original proposal](https://groups.google.com/forum/#!topic/gtfs-changes/ScGAyZ9a_yw))
* Added agency_phone field for providing voice telephone number for an agency ([original proposal](https://groups.google.com/forum/#!topic/gtfs-changes/8Itt58ueyqA))
* Added "Testing Your Feeds" section mentioning open-source testing tools
* Added clarifications about CSV format, agency_timezone, agency_lang, route_color, route_text_color, arrival_time, departure_time, calendar.txt vs. calendar_dates.txt, fare tables, and frequencies.txt
* Added link to feed history document, and corrected some public feed links
* Updated example images to depict the current Google Maps UI
* Updated/fixed sample data in document

#### February 29, 2008

* Added the stop_code field in stops.txt to allow for the specification of rider-facing stop codes ([original proposal](https://groups.google.com/forum/#!topic/gtfs-changes/k9A95fYZexc))
* Clarified the descriptions of route_short_name and route_long_name in routes.txt
* Clarified the descriptions of arrival_time and departure_time in stop_times.txt
* Fixed typos in the Sample Data section

#### November 20, 2007

* Clarified block_id description
* Changed language to de-emphasize Google Transit (since non-Google applications are using GTFS, and transit routing is now an integrated feature of Google Maps), and to fix assorted typos
* Updated example screenshots to reflect the presentation of GTFS fields in the current Google Maps UI
* Updated the Google contact email address for transit data providers
* Updated formatting

#### October 5, 2007

* Changed stop_sequence and shape_pt_sequence to allow for any increasing non-negative integers
* Clarified descriptions and fixed typos

#### May 31, 2007

* Updated page style, made HTML cleaner and more accessible
* Added links to public feed examples and other useful sites
* Removed examples from individual field descriptions

#### April 9, 2007

* Added section on [submitting a feed](https://developers.google.com/transit/google-transit#SubmitFeedToGoogle).
* Added the [Example Demo Transit Agency feed](https://developers.google.com/transit/gtfs/examples/gtfs-feed).
* Added note that calendar.txt can be omitted if all the service dates are defined in calendar_dates.txt.
* Made the agency_id field optional in feeds containing only one agency. This allows existing feeds without agency_id to remain valid.
* Added fuller specification of agency_url, stop_url, and route_url, and additional example values for those fields.
* Added 6 (Gondola) and 7 (Funicular) as valid route_type values.

#### March 8, 2007

* Minor edit to move the stop_url field from stop_times.txt, where it was incorrectly specified in the Feb. 28 update, to stops.txt, where it belongs.

#### March 5, 2007

* Minor edit to clarify the description of the route_long_name field.

#### February 28, 2007

* Addition of frequencies.txt for headway-based schedule support.
* Multiple agencies now allowed in the the same feed. Also added new agency_id field in both agencies.txt and routes.txt that lets you specify which route is operated by which agency.
* Addition of per-route and per-stop URLs.
* Addition of direction_id field in trips.txt.
* Support for mid-trip headsign changes with addition of stop_headsign field in stop_times.txt.
* Support for route colors with addition of optional route_color and route_text_color in routes.txt.
* Removed the ability to specify stops using street addresses. The previous version of the spec allowed you to give the location of a transit stop using a street address in the stop_street, stop_city, stop_region, stop_postcode, and stop_country fields. Now stop locations must be given using stop_lat for latitude and stop_lon for longitude, which are more useful for most applications.
* Addition of cable car vehicle type for route_type field in routes.txt.
* See the original [Headway blog post](http://headwayblog.com/2007/03/02/google-feed-spec-update-2007-02/) summary of the changes.

#### November 29, 2006

* Added support for trip shape information via shapes.txt
* Clarified the definition of stop_sequence
* Marked pickup_type and drop_off_type optional

#### October 31, 2006

* Added support for fare information
* Removed dates from individual file names
* Changed the route_type value definitions
* Allowed for multiple feed files to be posted at the same time, as long as their service periods didn't overlap
* Fixed block_id in trips.txt so that it was correctly marked Optional
* Noted that column headers must be included

#### September 29, 2006

* Minor edit to fix a couple errors in the examples.

#### September 25, 2006

* Initial version.
