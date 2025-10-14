### Revision History

#### September 2025
* Added `cemv_support` field in `agency.txt` and `routes.txt`. See [discussion](https://github.com/google/transit/pull/545).
* Added `stop_access` field in `stops.txt`. See [discussion](https://github.com/google/transit/pull/515).

#### June 2025
* Added cars_allowed field to trips.txt. See [discussion](https://github.com/google/transit/pull/547).

#### April 2025
* Added clarification to allow value 1 for continuous_pickup/continuous_drop_off for DRT services. See [discussion](https://github.com/google/transit/pull/558).

#### February 2025
* Added rider_categories.txt. See [discussion](https://github.com/google/transit/pull/511).

#### January 2025
* Update agency_fare_url to expand its description and include fare information only. See [discussion](https://github.com/google/transit/pull/524).

#### December 2024
* Added `fare_leg_join_rules.txt` and introduced the concept of Effective Fare Leg. See [discussion](https://github.com/google/transit/pull/439).

#### September 2024
* Clarify presence and use of from/to_stop_id & from/to_trip_id fields in transfers.txt. See [discussion](https://github.com/google/transit/pull/455).
* Added validity rules for polygons in GeoJSON files. See [discussion](https://github.com/google/transit/pull/476).

#### August 2024
* Change stops.txt presence because of demand responsive services. See [discussion](https://github.com/google/transit/pull/472).
* Clarify intended use for timepoint in stop_times.txt. See [discussion](https://github.com/google/transit/pull/474).
* Add that headsigns are recommended. See [discussion](https://github.com/google/transit/pull/485).

#### July 2024
* Update requirement for feed_info.txt. See [discussion](https://github.com/google/transit/pull/460).
* Add that shapes should be included. See [discussion](https://github.com/google/transit/pull/470).

#### May 2024
* Added `rule_priority` field in `fare_leg_rules.txt`. See [discussion](https://github.com/google/transit/pull/418).
* Clarify presence of `stops.zone_id`. See [discussion](https://github.com/google/transit/pull/432).

#### April 2024
* Clarify fare product definition. See [discussion](https://github.com/google/transit/pull/426). 

#### March 2024
* Added GTFS Flex. See [discussion](https://github.com/google/transit/pull/433).

#### November 2023
* Best practices: add Dataset Publishing guidelines and Practice Recommendations for all files. See [discussion](https://github.com/google/transit/pull/406).
* Add networks.txt & route_networks.txt. See [discussion](https://github.com/google/transit/pull/405).

#### August 2023
* Add fare_media_type=1. See [discussion](https://github.com/google/transit/pull/385).

#### July 2023
* Forbid subfolders in GTFS files. See [discussion](https://github.com/google/transit/pull/379).
* Added variable fares by time or day. See [discussion](https://github.com/google/transit/pull/357).
* Clarify implied timezone in stop_times.txt. See [discussion](https://github.com/google/transit/pull/378).
* Specify stop times shape_dist_traveled must not exceed the trip shape's maximum distance. See [discussion](https://github.com/google/transit/pull/380).
* Best practices: add recommended presence. See [discussion](https://github.com/google/transit/pull/386).

#### March 14, 2023

* Added fare media. See [discussion](https://github.com/google/transit/pull/355).

#### July 26, 2022

* Added trip-to-trip transfers with in-seat option. See [discussion](https://github.com/google/transit/pull/303).

#### May 17, 2022

* GTFS-Fares v2 base implementation. See [discussion](https://github.com/google/transit/pull/286).

#### Oct 22, 2021

* Added Primary and Foreign ID fields. See [discussion](https://github.com/google/transit/pull/278).

#### Oct 05, 2021

* Added Trip-to-trip and route-to-route transfers. See [discussion](https://github.com/google/transit/pull/284).

#### September 15, 2021

* Allowed fare gates (pathway_mode=6) to be bidirectional. See [discussion](https://github.com/google/transit/pull/276).

#### September 13, 2021

* Updated `stop_name` best practices. See [discussion](https://github.com/google/transit/pull/282).

#### August 27, 2021

* Updated GTFS Schedule to [RFC 2119](https://datatracker.ietf.org/doc/html/rfc2119). See [discussion](https://github.com/google/transit/pull/277).

#### January 4, 2021

* Clarified description of `stop_times.stop_id`. See [discussion](https://github.com/google/transit/pull/258).
* Defined positive and non-zero field signs. See [discussion](https://github.com/google/transit/pull/251).

#### October 2, 2020

* Changed field type of `frequencies.headway_secs` from non-negative to positive integer. See [discussion](https://github.com/google/transit/pull/249).

#### May 25, 2020

* Defined `pathways.txt`, `levels.txt` and `attributions.txt` as translatable tables. Added recommendations for translating multilingual `signposted_as` values. See [discussion](https://github.com/google/transit/pull/220).

#### May 13, 2020

* Added `continuous_pickup` and `continuous_drop_off` to `routes.txt` and `stop_times.txt`. Changed `shape_id` from "Optional" to "Conditionally required". See [discussion](https://github.com/google/transit/pull/208).

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

* Added `pathways.txt` and `levels.txt`. See [discussion](https://github.com/google/transit/pull/143).

#### February 6, 2019

* Editorial and formatting changes for clarity.  See [discussion](https://github.com/google/transit/pull/120).

#### October 2, 2018

* Factorized field types. See [discussion](https://github.com/google/transit/pull/104).

#### September 14, 2018

* Added "Conditionally required" concept. See [discussion](https://github.com/google/transit/pull/100).

#### September 4, 2018

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
