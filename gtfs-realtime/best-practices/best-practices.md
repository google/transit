# GTFS Realtime Best Practices

## Introduction

These are recommended practices for describing real-time public transportation information in the [GTFS Realtime Reference](https://gtfs.org/realtime/reference/) format. These complement the explicit recommendations outlined in the GTFS Realtime Reference using the terms “recommend” or “should”. Although not mandatory, following these best practices can significantly improve the quality of the data and the overall experience for riders.

These practices have been synthesized from the experience of the [GTFS Best Practices working group](https://gtfs.org/schedule/best-practices/#gtfs-best-practices-working-group) members and [application-specific GTFS practice recommendations](http://www.transitwiki.org/TransitWiki/index.php/Best_practices_for_creating_GTFS). 

For further background, see the [Frequently Asked Questions](https://gtfs.org/schedule/best-practices/#frequently-asked-questions-faq).

### Document Structure

Recommended practices are organized into two primary sections

* __[Practice Recommendations Organized by Message](#practice-recommendations-organized-by-message):__ Recommendations are organized by message and field in the same order described in the official GTFS Realtime reference.
* __[Practice Recommendations Organized by Case](#practice-recommendations-organized-by-case):__ With particular cases, such as frequency-based service (vs. schedule-based service), practices may need to be applied across several messages and fields as well as the corresponding GTFS schedule data. Such recommendations are consolidated in this section.

### Feed Publishing & General Practices

* Feeds should be published at a public, permanent URL
* The URL should be directly accessible without requiring a login to access the feed. If desired, API keys may be used but registration for API keys should be automated and available to all.
* Maintain persistent identifiers (id fields) within a GTFS Realtime feed (e.g., FeedEntity.id, VehicleDescriptor.id, CarriageDetails.id) across feed iterations.
* GTFS Realtime feeds should be refreshed at least once every 30 seconds, or whenever the information represented within the feed (position of a vehicle) changes, whichever is more frequent. VehiclePositions tend to change more frequently than other feed entities and should be updated as frequently as possible. If the content has not changed, the feed should be updated with a new `FeedHeader.timestamp` reflecting that the information is still relevant as of that timestamp.
* Data within a GTFS Realtime feed should not be older than 90 seconds for Trip Updates and Vehicle Positions and not older than 10 minutes for Service Alerts. For example, even if a producer is continuously refreshing the `FeedHeader.timestamp` timestamp every 30 seconds, the age of VehiclePositions within that feed should not be older than 90 seconds.
* The server hosting GTFS Realtime data should be reliable and consistently return validly-formatted protobuf-encoded responses. Fewer than 1% of responses should be invalid (protobuf errors or fetching errors).
* The web-server hosting GTFS Realtime data should be configured to correctly report the file modification date (see HTTP/1.1 - Request for Comments 2616, under Section 14.29) so consumers can leverage the `If-Modified-Since` HTTP header. This saves producers and consumers bandwidth by avoiding transferring feed contents that haven't changed.
* Feeds should provide protocol buffer-encoded feed content by default when queried via an HTTP request at the given URL - consumers should not need to define special HTTP accept headers to receive protocol-buffer encoded content.
* Due to how protocol buffers encode [optional values](https://developers.google.com/protocol-buffers/docs/proto#optional), before reading data from a GTFS Realtime feed consumers should check for the presence of values using the protocol buffer-generated `hasX()` methods before using that value and should only use the value if `hasX()` is true (where `X` is the name of the field). If `hasX()` returns `false`, the default value for that field defined in the `gtfs-realtime.proto` value should be assumed. If the consumer uses the value without checking the `hasX()` method first, it may be reading default data that wasn't intentionally published by the producer.
* Feeds should use HTTPS instead of HTTP (without encryption) to ensure feed integrity.
* Feeds should cover the vast majority of trips included in the companion static GTFS dataset. In particular, it should include data for high-density and high-traffic city areas and busy routes.

## Practice Recommendations Organized by Message

### FeedHeader

| Field Name | Recommendation |
| --- | --- |
| `gtfs_realtime_version` | Current version is "2.0".  All GTFS Realtime feeds should be "2.0" or higher, as early version of GTFS Realtime did not require all fields needed to represent various transit situations adequately. |
| `timestamp` | This timestamp should not decrease between two sequential feed iterations. |
|  | This timestamp value should always change if the feed contents change - the feed contents should not change without updating the header `timestamp`.<br><br>*Common mistakes* - If there are multiple instances of GTFS Realtime feed behind a load balancer, each instance may be pulling information from the realtime data source and publishing it to consumers slightly out of sync. If a GTFS Realtime consumer makes two back-to-back requests, and each request is served by a different GTFS Realtime feed instance, the same feed contents could potentially be returned to the consumer with different timestamps.<br><br>*Possible solution* - Producers should provide a `Last-Modified` HTTP header, and consumers should pass their most recent `If-Modified-Since` HTTP header to avoid receiving stale data.<br><br>*Possible solution* - If HTTP headers cannot be used, options such as sticky sessions can be used to ensure that each consumer is routed to the same producer server. |

### FeedEntity

All entities should only be removed from a GTFS Realtime feed when they are no longer relevant to users. Feeds are considered to be stateless, meaning that each feed reflects the entire real-time state of the transit system. If an entity is provided in one feed instance but dropped in a subsequent feed update, it should be assumed that there is no real-time information for that entity.

| Field Name | Recommendation |
| --- | --- |
| `id` | Should be kept stable over the entire trip duration |

### TripUpdate

General guidelines for trip cancellations:

* When canceling trips over a number of days, producers should provide TripUpdates referencing the given `trip_ids` and `start_dates` as `CANCELED` as well as an Alert with `NO_SERVICE` referencing the same `trip_ids` and `TimeRange` that can be shown to riders explaining the cancellation (e.g., detour).
* If no stops in a trip will be visited, the trip should be `CANCELED` instead of having all `stop_time_updates` being marked as `SKIPPED`.  

| Field Name | Recommendation |
| --- | --- |
| `trip` | Refer to [message TripDescriptor](#TripDescriptor). |
|  | If separate `VehiclePosition` and `TripUpdate` feeds are provided, [TripDescriptor](#TripDescriptor) and [VehicleDescriptor](#VehicleDescriptor) ID values pairing should match between the two feeds.<br><br>For example, a `VehiclePosition` entity has `vehicle_id:A` and `trip_id:4`, then the corresponding `TripUpdate` entity should also have `vehicle_id:A` and `trip_id:4`. If any `TripUpdate` entity has `trip_id:4` and any `vehicle_id` other than 4, this is an error. |
| `vehicle` | Refer to [message VehicleDescriptor](#VehicleDescriptor). |
|  | If separate `VehiclePosition` and `TripUpdate` feeds are provided, [TripDescriptor](#TripDescriptor) and [VehicleDescriptor](#VehicleDescriptor) ID values pairing should match between the two feeds.<br><br>For example, a `VehiclePosition` entity has `vehicle_id:A` and `trip_id:4`, then the corresponding `TripUpdate` entity should also have `vehicle_id:A` and `trip_id:4`. If any `TripUpdate` entity has `trip_id:4` and any `vehicle_id` other than 4, this is an error. |
| `stop_time_update` | `stop_time_updates` for a given `trip_id` should be strictly ordered by increasing `stop_sequence` and no `stop_sequence` should be repeated. |
|  | While the trip is in progress, all `TripUpdates` should include at least one `stop_time_update` with a predicted arrival or departure time in the future. Note that the [GTFS Realtime spec](https://github.com/google/transit/blob/master/gtfs-realtime/spec/en/trip-updates.md#stop-time-updates) says that producers should not drop a past `StopTimeUpdate` if it refers to a stop with a scheduled arrival time in the future for the given trip (i.e. the vehicle has passed the stop ahead of schedule), as otherwise it will be concluded that there is no update for this stop. |
| `timestamp` | Should reflect the time this prediction for this trip was updated. |
| `delay` | `TripUpdate.delay` should represent schedule deviation, i.e., the observed past value for how ahead/behind schedule the vehicle is. Predictions for future stops should be provided through `StopTimeEvent.delay` or `StopTimeEvent.time`. |

### TripDescriptor

If separate `VehiclePosition` and `TripUpdate` feeds are provided, [TripDescriptor](#TripDescriptor) and [VehicleDescriptor](#VehicleDescriptor) ID values pairing should match between the two feeds.

For example, a `VehiclePosition` entity has `vehicle_id:A` and `trip_id:4`, then the corresponding `TripUpdate` entity should also have `vehicle_id:A` and `trip_id:4`.

| Field Name | Recommendation |
| --- | --- |
| `schedule_relationship` | The behavior of `ADDED` trips are unspecified and the use of this enumeration is not recommended. |

### VehicleDescriptor

If separate `VehiclePosition` and `TripUpdate` feeds are provided, [TripDescriptor](#TripDescriptor) and [VehicleDescriptor](#VehicleDescriptor) ID values pairing should match between the two feeds.

For example, a `VehiclePosition` entity has `vehicle_id:A` and `trip_id:4`, then the corresponding `TripUpdate` entity should also have `vehicle_id:A` and `trip_id:4`.

| Field Name | Recommendation |
| --- | --- |
| `id` | Should uniquely and stably identify a vehicle over the entire trip duration |

### StopTimeUpdate

| Field Name | Recommendation |
| --- | --- |
| `stop_sequence` | Provide `stop_sequence` whenever possible, as it unambiguously resolves to a GTFS stop time in `stop_times.txt` unlike `stop_id`, which can occur more than once in a trip (e.g., loop route). |
| `arrival` | Arrival times between sequential stops should increase - they should not be the same or decrease. | 
|         | Arrival `time` (specified in [StopTimeEvent](#StopTimeEvent)) should be before the departure `time` for the same stop if a layover or dwell time is expected - otherwise, arrival `time` should be be the same as departure `time`. |
| `departure` | Departure times between sequential stops should increase - they should not be the same or decrease. |
|           | Departure `time` (specified in [StopTimeEvent](#StopTimeEvent)) should be the same as the arrival `time` for the same stop if no layover or dwell time is expected - otherwise, departure `time` should be after arrival `time` . |

### StopTimeEvent

| Field Name | Recommendation |
| --- | --- |
| `delay` | If only `delay` is provided in a `stop_time_update` `arrival` or `departure` (and not `time`), then the GTFS [`stop_times.txt`](https://gtfs.org/reference/static#stopstxt) should contain `arrival_times` and/or `departure_times` for these corresponding stops. A `delay` value in the realtime feed is meaningless unless you have a clock time to add it to in the GTFS `stop_times.txt` file. |

### VehiclePosition

Following are the recommended fields that should be included for a VehiclePostions feed to provide consumers with high-quality data (e.g., for generating predictions)

| Field name | Notes |
| --- | --- |
| `entity.id` | Should be kept stable over the entire trip duration
| `vehicle.timestamp` | Providing the timestamp at which vehicle position was measured is strongly recommended. Otherwise, consumers must use the message timestamp, which can have misleading results for riders when the last message was updated more frequently than the individual position.
| `vehicle.vehicle.id` | Should uniquely and stably identify a vehicle over the entire trip duration |

### Position

The vehicle position should be within 200 meters of the GTFS `shapes.txt` data for the current trip unless there is an alert with the effect of `DETOUR` for this `trip_id`.

### Alert

General guidelines for alerts:

* When `trip_id` and `start_time` are within `exact_time=1` interval, `start_time` should be later than the beginning of the interval by an exact multiple of `headway_secs`. 
* When canceling trips over a number of days, producers should provide TripUpdates referencing the given `trip_ids` and `start_dates` as `CANCELED` as well as an Alert with `NO_SERVICE` referencing the same `trip_ids` and `TimeRange` that can be shown to riders explaining the cancellation (e.g., detour).
* If an alert affects all stops on a line, use a line-based alert instead of a stop-based alert. Do not apply the alert to every stop of the line.
* While there is no character limit for service alerts, transit riders will often be viewing alerts on mobile devices. Please be concise.

| Field Name | Recommendation |
| --- | --- |
| `description_text` | Use line breaks to make your service alert easier to read. |


## Practice Recommendations Organized by Use Case

### Frequency-based trips

A frequency-based trip does not follow a fixed schedule but attempts to maintain predetermined headways. These trips are denoted in [GTFS frequency.txt](https://gtfs.org/reference/static/#frequenciestxt) by setting `exact_times=0` or omitting the `exact_times` field (note that `exact_times=1` trips are *NOT* frequency-based trips - `frequencies.txt` with `exact_times=1` is simply used as a convenience method for storing schedule-based trips in a more compact manner). There are several best practices to keep in mind when constructing GTFS Realtime feeds for frequency-based trips.

* In [TripUpdate.StopTimeUpdate](#StopTimeUpdate), the [StopTimeEvent](#StopTimeEvent) for `arrival` and `departure` should not contain `delay` because frequency-based trips do not follow a fixed schedule. Instead, `time` should be provided to indicate arrival/departure predictions.

* As required by the spec, when describing `trip` in [TripUpdate](#TripUpdate) or [VehiclePosition](#VehiclePosition) by using [TripDescriptor](#TripDescriptor), all of `trip_id`, `start_time`, and `start_date` must be provided. Additionally, `schedule_relationship` should be `UNSCHEDULED`.
 (e.g., re-enforcement trips).

 ## About This Document

### Objectives

The objectives of these GTFS Best Practices are:

* Support greater interoperability of transit data
* Improve end-user customer experience in public transportation apps
* Make it easier for software developers to deploy and scale applications, products, and services
* Facilitate the use of GTFS in various application categories (beyond its original focus on trip planning)

### Contributing
New Best Practices are now being added directly into the [spec](https://gtfs.org/schedule/reference/) in order to gradually consolidate both documents. 
If you'd like to suggest a new best practice, please go to the [GTFS Reference GitHub repository](https://github.com/google/transit/), [open an issue](https://github.com/google/transit/issues/new/choose) or create a Pull Request, or contact [specifications@mobilitydata.org](mailto:specifications@mobilitydata.org).

### Linking to This Document

Please link here in order to provide feed producers with guidance for correct formation of GTFS Realtime data. Each individual recommendation has an anchor link. Click the recommendation to get the URL for the in-page anchor link.

If a GTFS Realtime-consuming application makes requirements or recommendations for GTFS Realtime data practices that are not described here, it is recommended to publish a document with those requirements or recommendations to supplement these common best practices.

