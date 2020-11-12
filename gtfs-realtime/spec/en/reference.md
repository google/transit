A GTFS Realtime feed lets transit agencies provide consumers with realtime information about disruptions to their service (stations closed, lines not operating, important delays, etc.) location of their vehicles, and expected arrival times.

Version 2.0 of the feed specification is discussed and documented on this site. Valid versions are "2.0", "1.0".

### Term Definitions

#### Required

In GTFS-realtime v2.0 and higher, the *Required* column describes what fields must be provided by a producer in order for the transit data to be valid and make sense to a consuming application.

The following values are used in the *Required* field:

*   **Required**: This field must be provided by a GTFS-realtime feed producer.
*   **Conditionally required**: This field is required under certain conditions, which are outlined in the field *Description*. Outside of these conditions, the field is optional.
*   **Optional**: This field is optional and is not required to be implemented by producers. However, if the data is available in the underlying automatic vehicle location systems (e.g., VehiclePosition `timestamp`) it is recommended that producers provide these optional fields when possible.

*Note that semantic requirements were not defined in GTFS-realtime version 1.0, and therefore feeds with `gtfs_realtime_version` of `1` may not meet these requirements (see [the proposal for semantic requirements](https://github.com/google/transit/pull/64) for details).*

#### Cardinality

*Cardinality* represents the number of elements that may be provided for a particular field, with the following values:

* **One** - A single one element may be provided for this field. This maps to the [Protocol Buffer *required* and *optional* cardinalities](https://developers.google.com/protocol-buffers/docs/proto#simple).
* **Many** - Many elements (0, 1, or more) may be provided for this field. This maps to the [Protocol Buffer *repeated* cardinality](https://developers.google.com/protocol-buffers/docs/proto#simple).

Always reference the *Required* and *Description* fields to see when a field is required, conditionally required, or optional. Please reference [`gtfs-realtime.proto`](https://github.com/google/transit/blob/master/gtfs-realtime/proto/gtfs-realtime.proto) for Protocol Buffer cardinality.

#### Protocol Buffer data types

The following protocol buffer data types are used to describe feed elements:

*   **message**: Complex type
*   **enum**: List of fixed values

#### Experimental fields

Fields labeled as **experimental** are subject to change and not yet formally adopted into the specification. An **experimental** field may be formally adopted in the future.

## Element Index

*   [FeedMessage](#message-feedmessage)
    *   [FeedHeader](#message-feedheader)
        *   [Incrementality](#enum-incrementality)
    *   [FeedEntity](#message-feedentity)
        *   [TripUpdate](#message-tripupdate)
            *   [TripDescriptor](#message-tripdescriptor)
                *   [ScheduleRelationship](#enum-schedulerelationship-1)
            *   [VehicleDescriptor](#message-vehicledescriptor)
            *   [StopTimeUpdate](#message-stoptimeupdate)
                *   [StopTimeEvent](#message-stoptimeevent)
                *   [ScheduleRelationship](#enum-schedulerelationship)
                *   [StopTimeProperties](#message-stoptimeproperties)
            *   [TripProperties](#message-tripproperties)
        *   [VehiclePosition](#message-vehicleposition)
            *   [TripDescriptor](#message-tripdescriptor)
                *   [ScheduleRelationship](#enum-schedulerelationship-1)
            *   [VehicleDescriptor](#message-vehicledescriptor)
            *   [Position](#message-position)
            *   [VehicleStopStatus](#enum-vehiclestopstatus)
            *   [CongestionLevel](#enum-congestionlevel)
            *   [OccupancyStatus](#enum-occupancystatus)
            *   [CarriageDetails](#message-CarriageDetails)
        *   [Alert](#message-alert)
            *   [TimeRange](#message-timerange)
            *   [EntitySelector](#message-entityselector)
                *   [TripDescriptor](#message-tripdescriptor)
                    *   [ScheduleRelationship](#enum-schedulerelationship-1)
            *   [Cause](#enum-cause)
            *   [Effect](#enum-effect)
            *   [TranslatedString](#message-translatedstring)
                *   [Translation](#message-translation)
            *   [SeverityLevel](#enum-severitylevel)

# Elements

## _message_ FeedMessage

The contents of a feed message. Each message in the stream is obtained as a response to an appropriate HTTP GET request. A realtime feed is always defined with relation to an existing GTFS feed. All the entity ids are resolved with respect to the GTFS feed.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
|**header** | [FeedHeader](#message-feedheader) | Required | One | Metadata about this feed and feed message. |
|**entity** | [FeedEntity](#message-feedentity) | Conditionally required | Many | Contents of the feed.  If there is real-time information available for the transit system, this field must be provided.  If this field is empty, consumers should assume there is no real-time information available for the system. |

## _message_ FeedHeader

Metadata about a feed, included in feed messages.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **gtfs_realtime_version** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Required | One | Version of the feed specification. The current version is 2.0. |
| **incrementality** | [Incrementality](#enum-incrementality) | Required | One |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Required | One | This timestamp identifies the moment when the content of this feed has been created (in server time). In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). To avoid time skew between systems producing and consuming realtime information it is strongly advised to derive timestamp from a time server. It is completely acceptable to use Stratum 3 or even lower strata servers since time differences up to a couple of seconds are tolerable. |

## _enum_ Incrementality

Determines whether the current fetch is incremental.

*   **FULL_DATASET**: this feed update will overwrite all preceding realtime information for the feed. Thus this update is expected to provide a full snapshot of all known realtime information.
*   **DIFFERENTIAL**: currently, this mode is **unsupported** and behavior is **unspecified** for feeds that use this mode. There are discussions on the [GTFS Realtime mailing list](http://groups.google.com/group/gtfs-realtime) around fully specifying the behavior of DIFFERENTIAL mode and the documentation will be updated when those discussions are finalized.

#### Values

| _**Value**_ |
|-------------|
| **FULL_DATASET** |
| **DIFFERENTIAL** |

## _message_ FeedEntity

A definition (or update) of an entity in the transit feed. If the entity is not being deleted, exactly one of 'trip_update', 'vehicle' and 'alert' fields should be populated.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Required | One | Feed-unique identifier for this entity. The ids are used only to provide incrementality support. The actual entities referenced by the feed must be specified by explicit selectors (see EntitySelector below for more info). |
| **is_deleted** | [bool](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Whether this entity is to be deleted. Should be provided only for feeds with Incrementality of DIFFERENTIAL - this field should NOT be provided for feeds with Incrementality of FULL_DATASET. |
| **trip_update** | [TripUpdate](#message-tripupdate) | Conditionally required | One | Data about the realtime departure delays of a trip.  At least one of the fields trip_update, vehicle, or alert must be provided - all these fields cannot be empty. |
| **vehicle** | [VehiclePosition](#message-vehicleposition) | Conditionally required | One | Data about the realtime position of a vehicle. At least one of the fields trip_update, vehicle, or alert must be provided - all these fields cannot be empty. |
| **alert** | [Alert](#message-alert) | Conditionally required | One | Data about the realtime alert. At least one of the fields trip_update, vehicle, or alert must be provided - all these fields cannot be empty. |

## _message_ TripUpdate

Realtime update on the progress of a vehicle along a trip. Please also refer to the general discussion of the [trip updates entities](trip-updates.md).

Depending on the value of ScheduleRelationship, a TripUpdate can specify:

*   A trip that proceeds along the schedule.
*   A trip that proceeds along a route but has no fixed schedule.
*   A trip that has been added or removed with regard to schedule.
*   A new trip that is a copy of an existing trip in static GTFS. It will run at the service date and time specified in TripProperties.

The updates can be for future, predicted arrival/departure events, or for past events that already occurred. In most cases information about past events is a measured value thus its uncertainty value is recommended to be 0\. Although there could be cases when this does not hold so it is allowed to have uncertainty value different from 0 for past events. If an update's uncertainty is not 0, either the update is an approximate prediction for a trip that has not completed or the measurement is not precise or the update was a prediction for the past that has not been verified after the event occurred.

If a vehicle is serving multiple trips within the same block (for more information about trips and blocks, please refer to [GTFS trips.txt](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt)):
* the feed should include a TripUpdate for the trip currently being served by the vehicle. Producers are encouraged to include TripUpdates for one or more trips after the current trip in this vehicle's block if the producer is confident in the quality of the predictions for these future trip(s). Including multiple TripUpdates for the same vehicle avoids prediction "pop-in" for riders as the vehicle transitions from one trip to another and also gives riders advance notice of delays that impact downstream trips (e.g., when the known delay exceeds planned layover times between trips).
* the respective TripUpdate entities are not required to be added to the feed in the same order that they are scheduled in the block. For example, if there are trips with `trip_ids` 1, 2, and 3 that all belong to one block, and the vehicle travels trip 1, then trip 2, and then trip 3, the `trip_update` entities may appear in any order - for example, adding trip 2, then trip 1, and then trip 3 is allowed.

Note that the update can describe a trip that has already completed.To this end, it is enough to provide an update for the last stop of the trip. If the time of arrival at the last stop is in the past, the client will conclude that the whole trip is in the past (it is possible, although inconsequential, to also provide updates for preceding stops). This option is most relevant for a trip that has completed ahead of schedule, but according to the schedule, the trip is still proceeding at the current time. Removing the updates for this trip could make the client assume that the trip is still proceeding. Note that the feed provider is allowed, but not required, to purge past updates - this is one case where this would be practically useful.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **trip** | [TripDescriptor](#message-tripdescriptor) | Required | One | The Trip that this message applies to. There can be at most one TripUpdate entity for each actual trip instance. If there is none, that means there is no prediction information available. It does *not* mean that the trip is progressing according to schedule. |
| **vehicle** | [VehicleDescriptor](#message-vehicledescriptor) | Optional | One | Additional information on the vehicle that is serving this trip. |
| **stop_time_update** | [StopTimeUpdate](#message-stoptimeupdate) | Conditionally required | Many | Updates to StopTimes for the trip (both future, i.e., predictions, and in some cases, past ones, i.e., those that already happened). The updates must be sorted by stop_sequence, and apply for all the following stops of the trip up to the next specified stop_time_update.  At least one stop_time_update must be provided for the trip unless the trip.schedule_relationship is CANCELED or DUPLICATED - if the trip is canceled, no stop_time_updates need to be provided. If the trip is duplicated, stop_time_updates may be provided to indicate real-time information for the new trip. |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Moment at which the vehicle's real-time progress was measured. In POSIX time (i.e., the number of seconds since January 1st 1970 00:00:00 UTC). |
| **delay** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | The current schedule deviation for the trip. Delay should only be specified when the prediction is given relative to some existing schedule in GTFS.<br>Delay (in seconds) can be positive (meaning that the vehicle is late) or negative (meaning that the vehicle is ahead of schedule). Delay of 0 means that the vehicle is exactly on time.<br>Delay information in StopTimeUpdates take precedent of trip-level delay information, such that trip-level delay is only propagated until the next stop along the trip with a StopTimeUpdate delay value specified.<br>Feed providers are strongly encouraged to provide a TripUpdate.timestamp value indicating when the delay value was last updated, in order to evaluate the freshness of the data.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.|
| **trip_properties** | [TripProperties](#message-tripproperties) | Optional | One | Provides the updated properties for the trip. <br>**Caution:** this message is still **experimental**, and subject to change. It may be formally adopted in the future. |

## _message_ StopTimeEvent

Timing information for a single predicted event (either arrival or departure). Timing consists of delay and/or estimated time, and uncertainty.

*   delay should be used when the prediction is given relative to some existing schedule in GTFS.
*   time should be given whether there is a predicted schedule or not. If both time and delay are specified, time will take precedence (although normally, time, if given for a scheduled trip, should be equal to scheduled time in GTFS + delay).

Uncertainty applies equally to both time and delay. The uncertainty roughly specifies the expected error in true delay (but note, we don't yet define its precise statistical meaning). It's possible for the uncertainty to be 0, for example for trains that are driven under computer timing control.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **delay** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | Delay (in seconds) can be positive (meaning that the vehicle is late) or negative (meaning that the vehicle is ahead of schedule). Delay of 0 means that the vehicle is exactly on time.  Either delay or time must be provided within a StopTimeEvent - both fields cannot be empty. |
| **time** | [int64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | Event as absolute time. In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). Either delay or time must be provided within a StopTimeEvent - both fields cannot be empty. |
| **uncertainty** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0. |

## _message_ StopTimeUpdate

Realtime update for arrival and/or departure events for a given stop on a trip. Please also refer to the general discussion of stop time updates in the [TripDescriptor](#message-tripdescriptor) and [trip updates entities](trip-updates.md) documentation.

Updates can be supplied for both past and future events. The producer is allowed, although not required, to drop past events.
The update is linked to a specific stop either through stop_sequence or stop_id, so one of these fields must necessarily be set.  If the same stop_id is visited more than once in a trip, then stop_sequence should be provided in all StopTimeUpdates for that stop_id on that trip.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **stop_sequence** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | Must be the same as in stop_times.txt in the corresponding GTFS feed.  Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty.  stop_sequence is required for trips that visit the same stop_id more than once (e.g., a loop) to disambiguate which stop the prediction is for. If `StopTimeProperties.assigned_stop_id` is populated, then `stop_sequence` must be populated. |
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | Must be the same as in stops.txt in the corresponding GTFS feed. Either stop_sequence or stop_id must be provided within a StopTimeUpdate - both fields cannot be empty. If `StopTimeProperties.assigned_stop_id` is populated, it is preferred to omit `stop_id` and use only `stop_sequence`. If `StopTimeProperties.assigned_stop_id` and `stop_id` are populated, `stop_id` must match `assigned_stop_id`. |
| **arrival** | [StopTimeEvent](#message-stoptimeevent) | Conditionally required | One | If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED.  If schedule_relationship is NO_DATA, arrival and departure must be empty. |
| **departure** | [StopTimeEvent](#message-stoptimeevent) | Conditionally required | One | If schedule_relationship is empty or SCHEDULED, either arrival or departure must be provided within a StopTimeUpdate - both fields cannot be empty. arrival and departure may both be empty when schedule_relationship is SKIPPED.  If schedule_relationship is NO_DATA, arrival and departure must be empty. |
| **schedule_relationship** | [ScheduleRelationship](#enum-schedulerelationship) | Optional | One | The default relationship is SCHEDULED. |
| **stop_time_properties** | [StopTimeProperties](#message-stoptimeproperties) | Optional | One | Realtime updates for certain properties defined within GTFS stop_times.txt <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.<br>. |

## _enum_ ScheduleRelationship

The relation between this StopTime and the static schedule.

#### Values

| _**Value**_ | _**Comment**_ |
|-------------|---------------|
| **SCHEDULED** | The vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the **default** behavior. At least one of arrival and departure must be provided. Frequency-based trips (GTFS frequencies.txt with exact_times = 0) should not have a SCHEDULED value and should use UNSCHEDULED instead. |
| **SKIPPED** | The stop is skipped, i.e., the vehicle will not stop at this stop. Arrival and departure are optional. When set `SKIPPED` is not propagated to subsequent stops in the same trip (i.e., the vehicle will stop at subsequent stops in the trip unless those stops also have a `stop_time_update` with `schedule_relationship: SKIPPED`). Delay from a previous stop in the trip *does* propagate over the `SKIPPED` stop. In other words, if a `stop_time_update` with an `arrival` or `departure` prediction is not set for a stop after the `SKIPPED` stop, the prediction upstream of the `SKIPPED` stop will be propagated to the stop after the `SKIPPED` stop and subsequent stops in the trip until a `stop_time_update` for a subsequent stop is provided.  |
| **NO_DATA** | No data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied. |
| **UNSCHEDULED** | The vehicle is operating a frequency-based trip (GTFS frequencies.txt with exact_times = 0). This value should not be used for trips that are not defined in GTFS frequencies.txt, or trips in GTFS frequencies.txt with exact_times = 1. Trips containing `stop_time_updates` with `schedule_relationship: UNSCHEDULED` must also set the TripDescriptor `schedule_relationship: UNSCHEDULED` <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.<br>.

## _message_ StopTimeProperties

Realtime update for certain properties defined within GTFS stop_times.txt.

**Caution:** this message is still **experimental**, and subject to change. It may be formally adopted in the future.<br> 

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **assigned_stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Supports real-time stop assignments. Refers to a `stop_id` defined in the GTFS `stops.txt`. <br> The new `assigned_stop_id` should not result in a significantly different trip experience for the end user than the `stop_id` defined in GTFS `stop_times.txt`. In other words, the end user should not view this new `stop_id` as an "unusual change" if the new stop was presented within an app without any additional context. For example, this field is intended to be used for platform assignments by using a `stop_id` that belongs to the same station as the stop originally defined in GTFS `stop_times.txt`. <br> To assign a stop without providing any real-time arrival or departure predictions, populate this field and set `StopTimeUpdate.schedule_relationship = NO_DATA`. <br> If this field is populated, `StopTimeUpdate.stop_sequence` must be populated and `StopTimeUpdate.stop_id` should not be populated. Stop assignments should be reflected in other GTFS-realtime fields as well (e.g., `VehiclePosition.stop_id`). <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.<br>. |

## _message_ TripProperties

Defines updated properties of the trip

**Caution:** this message is still **experimental**, and subject to change. It may be formally adopted in the future.<br>.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **trip_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One |  Defines the identifier of a new trip that is a duplicate of an existing trip defined in (CSV) GTFS trips.txt but will start at a different service date and/or time (defined using `TripProperties.start_date` and `TripProperties.start_time`). See definition of `trips.trip_id` in (CSV) GTFS. Its value must be different than the ones used in the (CSV) GTFS. This field is required if `schedule_relationship` is `DUPLICATED`, otherwise this field must not be populated and will be ignored by consumers. <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |
| **start_date** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | Service date on which the duplicated trip will be run. Must be provided in YYYYMMDD format. This field is required if `schedule_relationship` is `DUPLICATED`, otherwise this field must not be populated and will be ignored by consumers. <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |
| **start_time** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | Defines the departure start time of the trip when it’s duplicated. See definition of `stop_times.departure_time` in (CSV) GTFS. Scheduled arrival and departure times for the duplicated trip are calculated based on the offset between the original trip `departure_time` and this field. For example, if a GTFS trip has stop A with a `departure_time` of `10:00:00` and stop B with `departure_time` of `10:01:00`, and this field is populated with the value of `10:30:00`, stop B on the duplicated trip will have a scheduled `departure_time` of `10:31:00`. Real-time prediction `delay` values are applied to this calculated schedule time to determine the predicted time. For example, if a departure `delay` of `30` is provided for stop B, then the predicted departure time is `10:31:30`. Real-time prediction `time` values do not have any offset applied to them and indicate the predicted time as provided.  For example, if a departure `time` representing 10:31:30 is provided for stop B, then the predicted departure time is `10:31:30`.This field is required if `schedule_relationship` is `DUPLICATED`, otherwise this field must not be populated and will be ignored by consumers. <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |

## _message_ VehiclePosition

Realtime positioning information for a given vehicle.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **trip** | [TripDescriptor](#message-tripdescriptor) | Optional | One | The Trip that this vehicle is serving. Can be empty or partial if the vehicle can not be identified with a given trip instance. |
| **vehicle** | [VehicleDescriptor](#message-vehicledescriptor) | Optional | One | Additional information on the vehicle that is serving this trip. Each entry should have a **unique** vehicle id. |
| **position** | [Position](#message-position) | Optional | One | Current position of this vehicle. |
| **current_stop_sequence** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | The stop sequence index of the current stop. The meaning of current_stop_sequence (i.e., the stop that it refers to) is determined by current_status. If current_status is missing IN_TRANSIT_TO is assumed. |
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Identifies the current stop. The value must be the same as in stops.txt in the corresponding GTFS feed. If `StopTimeProperties.assigned_stop_id` is used to assign a `stop_id`, this field should also reflect the change in `stop_id`. |
| **current_status** | [VehicleStopStatus](#enum-vehiclestopstatus) | Optional | One | The exact status of the vehicle with respect to the current stop. Ignored if current_stop_sequence is missing. |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Moment at which the vehicle's position was measured. In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). |
| **congestion_level** | [CongestionLevel](#enum-congestionlevel) | Optional | One |
| **occupancy_status** | [OccupancyStatus](#enum-occupancystatus) | _Optional_ | One | The degree of passenger occupancy of the vehicle or carriage. If multi_carriage_details is populated with per-carriage OccupancyStatus, then this field should describe the entire vehicle with all carriages accepting passengers considered.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.|
| **occupancy_percentage** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | A percentage value representing the degree of passenger occupancy of the vehicle. The value 100 should represent total the maximum occupancy the vehicle was designed for, including both seating and standing capacity, and current operating regulations allow. It's not impossible that the value goes over 100 if there are currently more passenger than the vehicle was designed for. The precision of occupancy_percentage should be low enough that you can't track a single person boarding and alighting for privacy reasons. If multi_carriage_details is populated with per-carriage occupancy_percentage, then this field should describe the entire vehicle with all carriages accepting passengers considered.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |
| **multi_carriage_details** | [CarriageDetails](#message-CarriageDetails) | Optional | Many | Details of the multiple carriages of this given vehicle. The first occurrence represents the first carriage of the vehicle, **given the current direction of travel**. The number of occurrences of the multi_carriage_details field represents the number of carriages of the vehicle. It also includes non boardable carriages, like engines, maintenance carriages, etc… as they provide valuable information to passengers about where to stand on a platform.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |


## _enum_ VehicleStopStatus

#### Values

| _**Value**_ | _**Comment**_ |
|-------------|---------------|
| **INCOMING_AT** | The vehicle is just about to arrive at the stop (on a stop display, the vehicle symbol typically flashes). |
| **STOPPED_AT** | The vehicle is standing at the stop. |
| **IN_TRANSIT_TO** | The vehicle has departed the previous stop and is in transit. |

## _enum_ CongestionLevel

Congestion level that is affecting this vehicle.

#### Values

| _**Value**_ |
|-------------|
| **UNKNOWN_CONGESTION_LEVEL** |
| **RUNNING_SMOOTHLY** |
| **STOP_AND_GO** |
| **CONGESTION** |
| **SEVERE_CONGESTION** |

## _enum OccupancyStatus_

The degree of passenger occupancy for the vehicle or carriage.

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.

#### _Values_

| _**Value**_ | _**Comment**_ |
|-------------|---------------|
| _**EMPTY**_ | _The vehicle is considered empty by most measures, and has few or no passengers onboard, but is still accepting passengers._ |
| _**MANY_SEATS_AVAILABLE**_ | _The vehicle or carriage has a large percentage of seats available. What percentage of free seats out of the total seats available is to be considered large enough to fall into this category is determined at the discretion of the producer._ |
| _**FEW_SEATS_AVAILABLE**_ | _The vehicle or carriage has a small percentage of seats available. What percentage of free seats out of the total seats available is to be considered small enough to fall into this category is determined at the discretion of the producer._ |
| _**STANDING_ROOM_ONLY**_ | _The vehicle or carriage can currently accommodate only standing passengers._ |
| _**CRUSHED_STANDING_ROOM_ONLY**_ | _The vehicle or carriage can currently accommodate only standing passengers and has limited space for them._ |
| _**FULL**_ | _The vehicle is considered full by most measures, but may still be allowing passengers to board._ |
| _**NOT_ACCEPTING_PASSENGERS**_ | _The vehicle or carriage is not accepting passengers. The vehicle or carriage usually accepts passengers for boarding._ |
| _**NO_DATA_AVAILABLE**_ | _The vehicle or carriage doesn't have any occupancy data available at that time._ |
| _**NOT_BOARDABLE**_ | _The vehicle or carriage is not boardable and never accepts passengers. Useful for special vehicles or carriages (engine, maintenance carriage, etc…)._ |


## _message_ CarriageDetails

Carriage specific details, used for vehicles composed of several carriages

**Caution:** this message is still **experimental**, and subject to change. It may be formally adopted in the future.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Identification of the carriage. Should be unique per vehicle. <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |
| **label** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | User visible label that may be shown to the passenger to help identify the carriage. Example: "7712", "Car ABC-32", etc... <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |
| **occupancy_status** | [OccupancyStatus](#enum-occupancystatus) | Optional | One | Occupancy status for this given carriage, in this vehicle. Default is set to `NO_DATA_AVAILABLE`.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.|
| **occupancy_percentage** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Occupancy percentage for this given carriage, in this vehicle. Follows the same rules as "VehiclePosition.occupancy_percentage". Use -1 in case data is not available for this given carriage.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |
| **carriage_sequence** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Required | One | Identifies the order of this carriage with respect to the other carriages in the vehicle's list of CarriageStatus. The first carriage in the direction of travel must have a value of 1. The second value corresponds to the second carriage in the direction of travel and must have a value of 2, and so forth. For example, the first carriage in the direction of travel has a value of 1. If the second carriage in the direction of travel has a value of 3, consumers will discard data for all carriages (i.e., the multi_carriage_details field). Carriages without data must be represented with a valid carriage_sequence number and the fields without data should be omitted (alternately, those fields could also be included and set to the "no data" values). <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future. |

## _message_ Alert

An alert, indicating some sort of incident in the public transit network.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **active_period** | [TimeRange](#message-timerange) | Optional | Many | Time when the alert should be shown to the user. If missing, the alert will be shown as long as it appears in the feed. If multiple ranges are given, the alert will be shown during all of them. |
| **informed_entity** | [EntitySelector](#message-entityselector) | Required | Many | Entities whose users we should notify of this alert.  At least one informed_entity must be provided. |
| **cause** | [Cause](#enum-cause) | Optional | One |
| **effect** | [Effect](#enum-effect) | Optional | One |
| **url** | [TranslatedString](#message-translatedstring) | Optional | One | The URL which provides additional information about the alert. |
| **header_text** | [TranslatedString](#message-translatedstring) | Required | One | Header for the alert. This plain-text string will be highlighted, for example in boldface. |
| **description_text** | [TranslatedString](#message-translatedstring) | Required | One | Description for the alert. This plain-text string will be formatted as the body of the alert (or shown on an explicit "expand" request by the user). The information in the description should add to the information of the header. |
| **tts_header_text** | [TranslatedString](#message-translatedstring) | Optional | One | Text containing the alert's header to be used for text-to-speech implementations. This field is the text-to-speech version of header_text. It should contain the same information as header_text but formatted such that it can read as text-to-speech (for example, abbreviations removed, numbers spelled out, etc.) |
| **tts_description_text** | [TranslatedString](#message-translatedstring) | Optional | One | Text containing a description for the alert to be used for text-to-speech implementations. This field is the text-to-speech version of description_text. It should contain the same information as description_text but formatted such that it can be read as text-to-speech (for example, abbreviations removed, numbers spelled out, etc.) |
| **severity_level** | [SeverityLevel](#enum-severitylevel) | Optional | One | Severity of the alert. |

## _enum_ Cause

Cause of this alert.

#### Values

| _**Value**_ |
|-------------|
| **UNKNOWN_CAUSE** |
| **OTHER_CAUSE** |
| **TECHNICAL_PROBLEM** |
| **STRIKE** |
| **DEMONSTRATION** |
| **ACCIDENT** |
| **HOLIDAY** |
| **WEATHER** |
| **MAINTENANCE** |
| **CONSTRUCTION** |
| **POLICE_ACTIVITY** |
| **MEDICAL_EMERGENCY** |

## _enum_ Effect

The effect of this problem on the affected entity.

#### Values

| _**Value**_ |
|-------------|
| **NO_SERVICE** |
| **REDUCED_SERVICE** |
| **SIGNIFICANT_DELAYS** |
| **DETOUR** |
| **ADDITIONAL_SERVICE** |
| **MODIFIED_SERVICE** |
| **OTHER_EFFECT** |
| **UNKNOWN_EFFECT** |
| **STOP_MOVED** |
| **NO_EFFECT** |
| **ACCESSIBILITY_ISSUE** |

## _enum_ SeverityLevel

The severity of the alert.

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.

#### Values
| _**Value**_ |
|-------------|
| **UNKNOWN_SEVERITY** |
| **INFO** |
| **WARNING** |
| **SEVERE** |

## _message_ TimeRange

A time interval. The interval is considered active at time `t` if `t` is greater than or equal to the start time and less than the end time.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **start** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | Start time, in POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). If missing, the interval starts at minus infinity.  If a TimeRange is provided, either start or end must be provided - both fields cannot be empty. |
| **end** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | End time, in POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). If missing, the interval ends at plus infinity. If a TimeRange is provided, either start or end must be provided - both fields cannot be empty. |

## _message_ Position

A geographic position of a vehicle.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **latitude** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Required | One | Degrees North, in the WGS-84 coordinate system. |
| **longitude** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Required | One | Degrees East, in the WGS-84 coordinate system. |
| **bearing** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data. |
| **odometer** | [double](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Odometer value, in meters. |
| **speed** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Momentary speed measured by the vehicle, in meters per second. |

## _message_ TripDescriptor

A descriptor that identifies a single instance of a GTFS trip.

To specify a single trip instance, in many cases a `trip_id` by itself is sufficient. However, the following cases require additional information to resolve to a single trip instance:
* For trips defined in frequencies.txt, `start_date` and `start_time` are required in addition to `trip_id`
* If the trip lasts for more than 24 hours, or is delayed such that it would collide with a scheduled trip on the following day, then `start_date` is required in addition to `trip_id`
* If the `trip_id` field can't be provided, then `route_id`, `direction_id`, `start_date`, and `start_time` must all be provided

In all cases, if `route_id` is provided in addition to `trip_id`, then the `route_id` must be the same `route_id` as assigned to the given trip in GTFS trips.txt.

The `trip_id` field cannot, by itself or in combination with other TripDescriptor fields, be used to identify multiple trip instances. For example, a TripDescriptor should never specify trip_id by itself for GTFS frequencies.txt exact_times=0 trips because start_time is also required to resolve to a single trip instance starting at a specific time of the day. If the TripDescriptor does not resolve to a single trip instance (i.e., it resolves to zero or multiple trip instances), it is considered an error and the entity containing the erroneous TripDescriptor may be discarded by consumers.

Note that if the trip_id is not known, then station sequence ids in TripUpdate are not sufficient, and stop_ids must be provided as well. In addition, absolute arrival/departure times must be provided.

TripDescriptor.route_id cannot be used within an Alert EntitySelector to specify a route-wide alert that affects all trips for a route - use EntitySelector.route_id instead.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **trip_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The trip_id from the GTFS feed that this selector refers to. For non frequency-based trips (trips not defined in GTFS frequencies.txt), this field is enough to uniquely identify the trip. For frequency-based trips defined in GTFS frequencies.txt, trip_id, start_time, and start_date are all required. For scheduled-based trips (trips not defined in GTFS frequencies.txt), trip_id can only be omitted if the trip can be uniquely identified by a combination of route_id, direction_id, start_time, and start_date, and all those fields are provided. When schedule_relationship is DUPLICATED within a TripUpdate, the trip_id identifies the trip from static GTFS to be duplicated. When schedule_relationship is DUPLICATED within a VehiclePosition, the trip_id identifies the new duplicate trip and must contain the value for the corresponding TripUpdate.TripProperties.trip_id. |
| **route_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The route_id from the GTFS that this selector refers to. If trip_id is omitted, route_id, direction_id, start_time, and schedule_relationship=SCHEDULED must all be set to identify a trip instance. TripDescriptor.route_id should not be used within an Alert EntitySelector to specify a route-wide alert that affects all trips for a route - use EntitySelector.route_id instead. |
| **direction_id** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The direction_id from the GTFS feed trips.txt file, indicating the direction of travel for trips this selector refers to. If trip_id is omitted, direction_id must be provided. <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.<br>|
| **start_time** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The initially scheduled start time of this trip instance. When the trip_id corresponds to a non-frequency-based trip, this field should either be omitted or be equal to the value in the GTFS feed. When the trip_id correponds to a frequency-based trip defined in GTFS frequencies.txt, start_time is required and must be specified for trip updates and vehicle positions. If the trip corresponds to exact_times=1 GTFS record, then start_time must be some multiple (including zero) of headway_secs later than frequencies.txt start_time for the corresponding time period. If the trip corresponds to exact_times=0, then its start_time may be arbitrary, and is initially expected to be the first departure of the trip. Once established, the start_time of this frequency-based exact_times=0 trip should be considered immutable, even if the first departure time changes -- that time change may instead be reflected in a StopTimeUpdate. If trip_id is omitted, start_time must be provided. Format and semantics of the field is same as that of GTFS/frequencies.txt/start_time, e.g., 11:15:35 or 25:15:35. |
| **start_date** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The start date of this trip instance in YYYYMMDD format. For scheduled trips (trips not defined in GTFS frequencies.txt), this field must be provided to disambiguate trips that are so late as to collide with a scheduled trip on a next day. For example, for a train that departs 8:00 and 20:00 every day, and is 12 hours late, there would be two distinct trips on the same time. This field can be provided but is not mandatory for schedules in which such collisions are impossible - for example, a service running on hourly schedule where a vehicle that is one hour late is not considered to be related to schedule anymore. This field is required for frequency-based trips defined in GTFS frequencies.txt. If trip_id is omitted, start_date must be provided. |
| **schedule_relationship** | [ScheduleRelationship](#enum-schedulerelationship-1) | Optional | One | The relation between this trip and the static schedule. If TripDescriptor is provided in an Alert `EntitySelector`, the `schedule_relationship` field is ignored by consumers when identifying the matching trip instance.

## _enum_ ScheduleRelationship

The relation between this trip and the static schedule. If a trip is done in accordance with temporary schedule, not reflected in GTFS, then it shouldn't be marked as SCHEDULED, but marked as ADDED.

#### Values

| _**Value**_ | _**Comment**_ |
|-------------|---------------|
| **SCHEDULED** | Trip that is running in accordance with its GTFS schedule, or is close enough to the scheduled trip to be associated with it. |
| **ADDED** | An extra trip that was added in addition to a running schedule, for example, to replace a broken vehicle or to respond to sudden passenger load. *NOTE: Currently, behavior is unspecified for feeds that use this mode. There are discussions on the GTFS GitHub [(1)](https://github.com/google/transit/issues/106) [(2)](https://github.com/google/transit/pull/221) [(3)](https://github.com/google/transit/pull/219) around fully specifying or deprecating ADDED trips and the documentation will be updated when those discussions are finalized.* |
| **UNSCHEDULED** | A trip that is running with no schedule associated to it - this value is used to identify trips defined in GTFS frequencies.txt with exact_times = 0. It should not be used to describe trips not defined in GTFS frequencies.txt, or trips in GTFS frequencies.txt with exact_times = 1. Trips with `schedule_relationship: UNSCHEDULED` must also set all StopTimeUpdates `schedule_relationship: UNSCHEDULED`|
| **CANCELED** | A trip that existed in the schedule but was removed. |
| **DUPLICATED** | A new trip that is the same as an existing scheduled trip except for service start date and time. Used with `TripUpdate.TripProperties.trip_id`, `TripUpdate.TripProperties.start_date`, and `TripUpdate.TripProperties.start_time` to copy an existing trip from static GTFS but start at a different service date and/or time. Duplicating a trip is allowed if the service related to the original trip in (CSV) GTFS (in `calendar.txt` or `calendar_dates.txt`) is operating within the next 30 days. The trip to be duplicated is identified via `TripUpdate.TripDescriptor.trip_id`. <br><br> This enumeration does not modify the existing trip referenced by `TripUpdate.TripDescriptor.trip_id` - if a producer wants to cancel the original trip, it must publish a separate `TripUpdate` with the value of CANCELED. Trips defined in GTFS `frequencies.txt` with `exact_times` that is empty or equal to `0` cannot be duplicated. The `VehiclePosition.TripDescriptor.trip_id` for the new trip must contain the matching value from `TripUpdate.TripProperties.trip_id` and `VehiclePosition.TripDescriptor.ScheduleRelationship` must also be set to `DUPLICATED`.  <br><br>*Existing producers and consumers that were using the ADDED enumeration to represent duplicated trips must follow the [migration guide](/gtfs-realtime/spec/en/examples/migration-duplicated.md) to transition to the DUPLICATED enumeration.* |

## _message_ VehicleDescriptor

Identification information for the vehicle performing the trip.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | Internal system identification of the vehicle. Should be **unique** per vehicle, and is used for tracking the vehicle as it proceeds through the system. This id should not be made visible to the end-user; for that purpose use the **label** field |
| **label** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. |
| **license_plate** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Optional | One | The license plate of the vehicle. |

## _message_ EntitySelector

A selector for an entity in a GTFS feed. The values of the fields should correspond to the appropriate fields in the GTFS feed. At least one specifier must be given. If several are given, they should be interpreted as being joined by the logical `AND` operator.  Additionally, the combination of specifiers must match the corresponding information in the GTFS feed.  In other words, in order for an alert to apply to an entity in GTFS it must match all of the provided EntitySelector fields.  For example, an EntitySelector that includes the fields `route_id: "5"` and `route_type: "3"` applies only to the `route_id: "5"` bus - it does not apply to any other routes of `route_type: "3"`.  If a producer wants an alert to apply to `route_id: "5"` as well as `route_type: "3"`, it should provide two separate EntitySelectors, one referencing `route_id: "5"` and another referencing `route_type: "3"`.

At least one specifier must be given - all fields in an EntitySelector cannot be empty.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **agency_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The agency_id from the GTFS feed that this selector refers to.
| **route_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The route_id from the GTFS that this selector refers to. If direction_id is provided, route_id must also be provided.
| **route_type** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The route_type from the GTFS that this selector refers to.
| **direction_id** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The direction_id from the GTFS feed trips.txt file, used to select all trips in one direction for a route, specified by route_id. If direction_id is provided, route_id must also be provided. <br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.<br>|
| **trip** | [TripDescriptor](#message-tripdescriptor) | Conditionally required | One | The trip instance from the GTFS that this selector refers to. This TripDescriptor must resolve to a single trip instance in the GTFS data (e.g., a producer cannot provide only a trip_id for exact_times=0 trips). If the ScheduleRelationship field is populated within this TripDescriptor it will be ignored by consumers when attempting to identify the GTFS trip.
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | The stop_id from the GTFS feed that this selector refers to.

## _message_ TranslatedString

An internationalized message containing per-language versions of a snippet of text or a URL. One of the strings from a message will be picked up. The resolution proceeds as follows: If the UI language matches the language code of a translation, the first matching translation is picked. If a default UI language (e.g., English) matches the language code of a translation, the first matching translation is picked. If some translation has an unspecified language code, that translation is picked.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **translation** | [Translation](#message-translation) | Required | Many | At least one translation must be provided. |

## _message_ Translation

A localized string mapped to a language.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Required**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|----------------|-------------------|-------------------|
| **text** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Required | One | A UTF-8 string containing the message. |
| **language** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | Conditionally required | One | BCP-47 language code. Can be omitted if the language is unknown or if no internationalization is done at all for the feed. At most one translation is allowed to have an unspecified language tag - if there is more than one translation, the language must be provided. |
