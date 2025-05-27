### Revision History

#### May 2025

* Added schedule_relationship `ADDED` and `REPLACEMENT` to be used instead of `NEW`. See [discussion](https://github.com/google/transit/pull/504).
* Further clarifications to trip modifications. See [discussion](https://github.com/google/transit/pull/542).

#### December 2024

* Added new string field that matches feed_info.feed_version from the GTFS Schedule feed that the realtime data is based on. See [discussion](https://github.com/google/transit/pull/434).

#### October 2024

* Clarification and small changes for Trip Modifications. See [discussion](https://github.com/google/transit/pull/497).

#### March 2024

* Adopted Trip-Modifications. See [discussion](https://github.com/google/transit/pull/403).

#### November 2022

* Added support for DELETED trips. See [discussion](https://github.com/google/transit/pull/352).

#### July 2022

* Add cause_detail and effect_detail. See [discussion](https://github.com/google/transit/pull/332)
* Added ability to specify a wheelchair_accessible value in a TripUpdate.VehicleDescriptor. See [discussion](https://github.com/google/transit/pull/340).

#### September 2021

* Feature/image in alerts. See [discussion](https://github.com/google/transit/pull/283).

#### August 2021

* Add GTFS-NewShapes as experimental. See [discussion](https://github.com/google/transit/pull/272).

#### April 2021

* Add departure_occupancy_status to TripUpdate. See [discussion](https://github.com/google/transit/pull/260).

#### February 2021

* Clarification of GTFS Realtime occupancy descriptions. See [discussion](https://github.com/google/transit/pull/259).

#### September 2020 

* Support multi-car crowding. See [discussion](https://github.com/google/transit/pull/237).

#### April 2020

* Support stop assignments. See [discussion](https://github.com/google/transit/pull/219).

#### July 2020

* Support DUPLICATED trips. See [discussion](https://github.com/google/transit/pull/221).
* Alert tts_header_text, tts_description_text no longer experimental. See [discussion](https://github.com/google/transit/pull/229).
* Label GTFS-RT ADDED trips as not fully specified. See [discussion](https://github.com/google/transit/pull/230).

#### April 2020

* Mark SeverityLevel as final. See [discussion](https://github.com/google/transit/pull/214).
* Add occupancy_percentage. See [discussion](https://github.com/google/transit/pull/213).

#### March 12, 2020

* Recommend providing TripUpdate predictions for the next trip in block. See [discussion](https://github.com/google/transit/pull/206).

#### August 2019

* Document that trip_updates are not required to occur in feed in block-order. See [discussion](https://github.com/google/transit/pull/176).
* Add StopTimeUpdate.ScheduleRelationship UNSCHEDULED value. See [discussion](https://github.com/google/transit/pull/173).

#### May 2019

* Add accessibility issue alert effect. See [discussion](https://github.com/google/transit/pull/164).

#### February 2019

* Add NO_EFFECT effect option for GTFS-realtime service alert. See [discussion](https://github.com/google/transit/pull/137).
* Add new optional field SeverityLevel to Service Alerts feed. See [discussion](https://github.com/google/transit/pull/136).
* Add new optional fields for Text-to-Speech functionality in Service Alerts feed. See [discussion](https://github.com/google/transit/pull/135).

#### April 2018

* Remove requirement for stop_time_update arrival AND departure for SCHEDULED trips. See [discussion](https://github.com/google/transit/pull/165).

#### August 2017

* Define semantic cardinality for GTFS-realtime fields. See [discussion](https://github.com/google/transit/pull/64).

#### January 30, 2015

* Added Protocol Buffer extension namespace to all remaining GTFS-realtime messages that didn't already have one (such as `FeedMessage` and `FeedEntity`).

#### January 28, 2015

* Added experimental field `delay` to `TripUpdate` ([discussion](https://groups.google.com/forum/#!topic/gtfs-realtime/NsTIRQdMNN8)).

#### January 16, 2015

* Update description of `TripDescriptor.start_time`.

#### January 8, 2015

* Defined experimental enum `OccupancyStatus`.
* Added experimental field `occupancy_status` to `VehiclePosition` ([discussion](https://groups.google.com/forum/#!topic/gtfs-realtime/_HtNTGp5LxM)).

#### May 22, 2014

* Updated description of `ScheduleRelationship` enum in `StopTimeUpdate` message ([discussion](https://groups.google.com/forum/#!topic/gtfs-realtime/77c3WZrGBnI)).
* Removed REPLACEMENT from `ScheduleRelationship` enum values in `TripDescriptor` message ([discussion](https://groups.google.com/forum/#!topic/gtfs-realtime/77c3WZrGBnI)).

#### Oct 12, 2012

* Added timestamp field to `TripUpdate` message.

#### May 30, 2012

* Added specific details about Extensions to the specification.

#### November 30, 2011

* Added Protocol Buffer extension namespace to key GTFS-realtime messages to facilitate writing extensions to the spec.

#### October 25, 2011

* Updated documentation to clarify that `alert`, `header_text` and `description_text` are both plain-text values.

#### August 20, 2011

* Updated documentation to clarify semantics of the `TimeRange` message.

#### August 22, 2011

* Initial version.
