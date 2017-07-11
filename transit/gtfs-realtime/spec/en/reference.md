A GTFS Realtime feed lets transit agencies provide consumers with realtime information about disruptions to their service (stations closed, lines not operating, important delays, etc.) location of their vehicles, and expected arrival times.

Version 1.0 of the feed specification is discussed and documented on this site.

### Term Definitions

*   **required**: Exactly one
*   **repeated**: Zero or more
*   **message**: Complex type
*   **enum**: List of fixed values
*   **experimental**: Experimental field, subject to change. It may be formally adopted in the future.

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
        *   [VehiclePosition](#message-vehicleposition)
            *   [TripDescriptor](#message-tripdescriptor)
                *   [ScheduleRelationship](#enum-schedulerelationship-1)
            *   [VehicleDescriptor](#message-vehicledescriptor)
            *   [Position](#message-position)
            *   [VehicleStopStatus](#enum-vehiclestopstatus)
            *   [CongestionLevel](#enum-congestionlevel)
            *   [OccupancyStatus](#enum-occupancystatus)
        *   [Alert](#message-alert)
            *   [TimeRange](#message-timerange)
            *   [EntitySelector](#message-entityselector)
                *   [TripDescriptor](#message-tripdescriptor)
                    *   [ScheduleRelationship](#enum-schedulerelationship-1)
            *   [Cause](#enum-cause)
            *   [Effect](#enum-effect)
            *   [TranslatedString](#message-translatedstring)
                *   [Translation](#message-translation)

# Elements

## _message_ FeedMessage

The contents of a feed message. Each message in the stream is obtained as a response to an appropriate HTTP GET request. A realtime feed is always defined with relation to an existing GTFS feed. All the entity ids are resolved with respect to the GTFS feed.

#### Fields

|_**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|-----------------|------------|-------------------|-------------------|
|**header** | [FeedHeader](#message-feedheader) | required | Metadata about this feed and feed message. |
|**entity** | [FeedEntity](#message-feedentity) | repeated | Contents of the feed. |

## _message_ FeedHeader

Metadata about a feed, included in feed messages.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **gtfs_realtime_version** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | required | Version of the feed specification. The current version is 1.0. |
| **incrementality** | [Incrementality](#enum-incrementality) | optional |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | This timestamp identifies the moment when the content of this feed has been created (in server time). In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). To avoid time skew between systems producing and consuming realtime information it is strongly advised to derive timestamp from a time server. It is completely acceptable to use Stratum 3 or even lower strata servers since time differences up to a couple of seconds are tolerable. |

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

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | required | Feed-unique identifier for this entity. The ids are used only to provide incrementality support. The actual entities referenced by the feed must be specified by explicit selectors (see EntitySelector below for more info). |
| **is_deleted** | [bool](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Whether this entity is to be deleted. Relevant only for incremental fetches. |
| **trip_update** | [TripUpdate](#message-tripupdate) | optional | Data about the realtime departure delays of a trip. |
| **vehicle** | [VehiclePosition](#message-vehicleposition) | optional | Data about the realtime position of a vehicle. |
| **alert** | [Alert](#message-alert) | optional | Data about the realtime alert. |

## _message_ TripUpdate

Realtime update on the progress of a vehicle along a trip. Please also refer to the general discussion of the [trip updates entities](trip-updates.md).

Depending on the value of ScheduleRelationship, a TripUpdate can specify:

*   A trip that proceeds along the schedule.
*   A trip that proceeds along a route but has no fixed schedule.
*   A trip that has been added or removed with regard to schedule.

The updates can be for future, predicted arrival/departure events, or for past events that already occurred. In most cases information about past events is a measured value thus its uncertainty value is recommended to be 0\. Although there could be cases when this does not hold so it is allowed to have uncertainty value different from 0 for past events. If an update's uncertainty is not 0, either the update is an approximate prediction for a trip that has not completed or the measurement is not precise or the update was a prediction for the past that has not been verified after the event occurred.

Note that the update can describe a trip that has already completed.To this end, it is enough to provide an update for the last stop of the trip. If the time of arrival at the last stop is in the past, the client will conclude that the whole trip is in the past (it is possible, although inconsequential, to also provide updates for preceding stops). This option is most relevant for a trip that has completed ahead of schedule, but according to the schedule, the trip is still proceeding at the current time. Removing the updates for this trip could make the client assume that the trip is still proceeding. Note that the feed provider is allowed, but not required, to purge past updates - this is one case where this would be practically useful.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **trip** | [TripDescriptor](#message-tripdescriptor) | required | The Trip that this message applies to. There can be at most one TripUpdate entity for each actual trip instance. If there is none, that means there is no prediction information available. It does *not* mean that the trip is progressing according to schedule. |
| **vehicle** | [VehicleDescriptor](#message-vehicledescriptor) | optional | Additional information on the vehicle that is serving this trip. |
| **stop_time_update** | [StopTimeUpdate](#message-stoptimeupdate) | repeated | Updates to StopTimes for the trip (both future, i.e., predictions, and in some cases, past ones, i.e., those that already happened). The updates must be sorted by stop_sequence, and apply for all the following stops of the trip up to the next specified one. |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Moment at which the vehicle's real-time progress was measured. In POSIX time (i.e., the number of seconds since January 1st 1970 00:00:00 UTC). |
| **delay** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional |The current schedule deviation for the trip. Delay should only be specified when the prediction is given relative to some existing schedule in GTFS.<br>Delay (in seconds) can be positive (meaning that the vehicle is late) or negative (meaning that the vehicle is ahead of schedule). Delay of 0 means that the vehicle is exactly on time.<br>Delay information in StopTimeUpdates take precedent of trip-level delay information, such that trip-level delay is only propagated until the next stop along the trip with a StopTimeUpdate delay value specified.<br>Feed providers are strongly encouraged to provide a TripUpdate.timestamp value indicating when the delay value was last updated, in order to evaluate the freshness of the data.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.|

## _message_ StopTimeEvent

Timing information for a single predicted event (either arrival or departure). Timing consists of delay and/or estimated time, and uncertainty.

*   delay should be used when the prediction is given relative to some existing schedule in GTFS.
*   time should be given whether there is a predicted schedule or not. If both time and delay are specified, time will take precedence (although normally, time, if given for a scheduled trip, should be equal to scheduled time in GTFS + delay).

Uncertainty applies equally to both time and delay. The uncertainty roughly specifies the expected error in true delay (but note, we don't yet define its precise statistical meaning). It's possible for the uncertainty to be 0, for example for trains that are driven under computer timing control.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **delay** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Delay (in seconds) can be positive (meaning that the vehicle is late) or negative (meaning that the vehicle is ahead of schedule). Delay of 0 means that the vehicle is exactly on time. |
| **time** | [int64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Event as absolute time. In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). |
| **uncertainty** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | If uncertainty is omitted, it is interpreted as unknown. To specify a completely certain prediction, set its uncertainty to 0. |

## _message_ StopTimeUpdate

Realtime update for arrival and/or departure events for a given stop on a trip. Please also refer to the general discussion of stop time updates in the [TripDescriptor](#message-tripdescriptor) and [trip updates entities](trip-updates.md) documentation.

Updates can be supplied for both past and future events. The producer is allowed, although not required, to drop past events.
The update is linked to a specific stop either through stop_sequence or stop_id, so one of these fields must necessarily be set.  If the same stop_id is visited more than once in a trip, then stop_sequence should be provided in all StopTimeUpdates for that stop_id on that trip.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **stop_sequence** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Must be the same as in stop_times.txt in the corresponding GTFS feed. |
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Must be the same as in stops.txt in the corresponding GTFS feed. |
| **arrival** | [StopTimeEvent](#message-stoptimeevent) | optional |
| **departure** | [StopTimeEvent](#message-stoptimeevent) | optional |
| **schedule_relationship** | [ScheduleRelationship](#enum-schedulerelationship) | optional | The default relationship is SCHEDULED. |

## _enum_ ScheduleRelationship

The relation between this StopTime and the static schedule.

#### Values

| _**Value**_ | _**Comment**_ |
|-------------|---------------|
| **SCHEDULED** | The vehicle is proceeding in accordance with its static schedule of stops, although not necessarily according to the times of the schedule. This is the **default** behavior. At least one of arrival and departure must be provided. If the schedule for this stop contains both arrival and departure times then so must this update. |
| **SKIPPED** | The stop is skipped, i.e., the vehicle will not stop at this stop. Arrival and departure are optional. |
| **NO_DATA** | No data is given for this stop. It indicates that there is no realtime information available. When set NO_DATA is propagated through subsequent stops so this is the recommended way of specifying from which stop you do not have realtime information. When NO_DATA is set neither arrival nor departure should be supplied. |

## _message_ VehiclePosition

Realtime positioning information for a given vehicle.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **trip** | [TripDescriptor](#message-tripdescriptor) | optional | The Trip that this vehicle is serving. Can be empty or partial if the vehicle can not be identified with a given trip instance. |
| **vehicle** | [VehicleDescriptor](#message-vehicledescriptor) | optional | Additional information on the vehicle that is serving this trip. Each entry should have a **unique** vehicle id. |
| **position** | [Position](#message-position) | optional | Current position of this vehicle. |
| **current_stop_sequence** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | The stop sequence index of the current stop. The meaning of current_stop_sequence (i.e., the stop that it refers to) is determined by current_status. If current_status is missing IN_TRANSIT_TO is assumed. |
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Identifies the current stop. The value must be the same as in stops.txt in the corresponding GTFS feed. |
| **current_status** | [VehicleStopStatus](#enum-vehiclestopstatus) | optional | The exact status of the vehicle with respect to the current stop. Ignored if current_stop_sequence is missing. |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Moment at which the vehicle's position was measured. In POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). |
| **congestion_level** | [CongestionLevel](#enum-congestionlevel) | optional |
| _**occupancy_status**_ | _[OccupancyStatus](#enum-occupancystatus)_ | _optional_ |The degree of passenger occupancy of the vehicle.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.|

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

The degree of passenger occupancy for the vehicle.

**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.

#### _Values_

| _**Value**_ | _**Comment**_ |
|-------------|---------------|
| _**EMPTY**_ | _The vehicle is considered empty by most measures, and has few or no passengers onboard, but is still accepting passengers._ |
| _**MANY_SEATS_AVAILABLE**_ | _The vehicle has a large percentage of seats available. What percentage of free seats out of the total seats available is to be considered large enough to fall into this category is determined at the discretion of the producer._ |
| _**FEW_SEATS_AVAILABLE**_ | _The vehicle has a small percentage of seats available. What percentage of free seats out of the total seats available is to be considered small enough to fall into this category is determined at the discretion of the producer._ |
| _**STANDING_ROOM_ONLY**_ | _The vehicle can currently accomodate only standing passengers._ |
| _**CRUSHED_STANDING_ROOM_ONLY**_ | _The vehicle can currently accomodate only standing passengers and has limited space for them._ |
| _**FULL**_ | _The vehicle is considered full by most measures, but may still be allowing passengers to board._ |
| _**NOT_ACCEPTING_PASSENGERS**_ | _The vehicle can not accept passengers._ |

## _message_ Alert

An alert, indicating some sort of incident in the public transit network.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **active_period** | [TimeRange](#message-timerange) | repeated | Time when the alert should be shown to the user. If missing, the alert will be shown as long as it appears in the feed. If multiple ranges are given, the alert will be shown during all of them. |
| **informed_entity** | [EntitySelector](#message-entityselector) | repeated | Entities whose users we should notify of this alert. |
| **cause** | [Cause](#enum-cause) | optional |
| **effect** | [Effect](#enum-effect) | optional |
| **url** | [TranslatedString](#message-translatedstring) | optional | The URL which provides additional information about the alert. |
| **header_text** | [TranslatedString](#message-translatedstring) | optional | Header for the alert. This plain-text string will be highlighted, for example in boldface. |
| **description_text** | [TranslatedString](#message-translatedstring) | optional | Description for the alert. This plain-text string will be formatted as the body of the alert (or shown on an explicit "expand" request by the user). The information in the description should add to the information of the header. |

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

## _message_ TimeRange

A time interval. The interval is considered active at time `t` if `t` is greater than or equal to the start time and less than the end time.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **start** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Start time, in POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). If missing, the interval starts at minus infinity. |
| **end** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | End time, in POSIX time (i.e., number of seconds since January 1st 1970 00:00:00 UTC). If missing, the interval ends at plus infinity. |

## _message_ Position

A geographic position of a vehicle.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **latitude** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | required | Degrees North, in the WGS-84 coordinate system. |
| **longitude** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | required | Degrees East, in the WGS-84 coordinate system. |
| **bearing** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Bearing, in degrees, clockwise from True North, i.e., 0 is North and 90 is East. This can be the compass bearing, or the direction towards the next stop or intermediate location. This should not be deduced from the sequence of previous positions, which clients can compute from previous data. |
| **odometer** | [double](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Odometer value, in meters. |
| **speed** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Momentary speed measured by the vehicle, in meters per second. |

## _message_ TripDescriptor

A descriptor that identifies an instance of a GTFS trip, or all instances of a trip along a route. To specify a single trip instance, the trip_id (and if necessary, start_time) is set. If route_id is also set, then it should be same as one that the given trip corresponds to. To specify all the trips along a given route, only the route_id should be set. Note that if the trip_id is not known, then station sequence ids in TripUpdate are not sufficient, and stop_ids must be provided as well. In addition, absolute arrival/departure times must be provided.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **trip_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | The trip_id from the GTFS feed that this selector refers to. For non frequency-based trips, this field is enough to uniquely identify the trip. For frequency-based trip, start_time and start_date might also be necessary. |
| **route_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | The route_id from the GTFS that this selector refers to. |
| **direction_id** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | The direction_id from the GTFS feed trips.txt file, indicating the direction of travel for trips this selector refers to.<br>**Caution:** this field is still **experimental**, and subject to change. It may be formally adopted in the future.<br>|
| **start_time** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | The initially scheduled start time of this trip instance. When the trip_id corresponds to a non-frequency-based trip, this field should either be omitted or be equal to the value in the GTFS feed. When the trip_id correponds to a frequency-based trip, the start_time must be specified for trip updates and vehicle positions. If the trip corresponds to exact_times=1 GTFS record, then start_time must be some multiple (including zero) of headway_secs later than frequencies.txt start_time for the corresponding time period. If the trip corresponds to exact_times=0, then its start_time may be arbitrary, and is initially expected to be the first departure of the trip. Once established, the start_time of this frequency-based trip should be considered immutable, even if the first departure time changes -- that time change may instead be reflected in a StopTimeUpdate. Format and semantics of the field is same as that of GTFS/frequencies.txt/start_time, e.g., 11:15:35 or 25:15:35. |
| **start_date** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | The scheduled start date of this trip instance. This field must be provided to disambiguate trips that are so late as to collide with a scheduled trip on a next day. For example, for a train that departs 8:00 and 20:00 every day, and is 12 hours late, there would be two distinct trips on the same time. This field can be provided but is not mandatory for schedules in which such collisions are impossible - for example, a service running on hourly schedule where a vehicle that is one hour late is not considered to be related to schedule anymore. In YYYYMMDD format. |
| **schedule_relationship** | [ScheduleRelationship](#enum-schedulerelationship-1) | optional |

## _enum_ ScheduleRelationship

The relation between this trip and the static schedule. If a trip is done in accordance with temporary schedule, not reflected in GTFS, then it shouldn't be marked as SCHEDULED, but marked as ADDED.

#### Values

| _**Value**_ | _**Comment**_ |
|-------------|---------------|
| **SCHEDULED** | Trip that is running in accordance with its GTFS schedule, or is close enough to the scheduled trip to be associated with it. |
| **ADDED** | An extra trip that was added in addition to a running schedule, for example, to replace a broken vehicle or to respond to sudden passenger load. |
| **UNSCHEDULED** | A trip that is running with no schedule associated to it, for example, if there is no schedule at all. |
| **CANCELED** | A trip that existed in the schedule but was removed. |

## _message_ VehicleDescriptor

Identification information for the vehicle performing the trip.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | Internal system identification of the vehicle. Should be **unique** per vehicle, and is used for tracking the vehicle as it proceeds through the system. This id should not be made visible to the end-user; for that purpose use the **label** field |
| **label** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | User visible label, i.e., something that must be shown to the passenger to help identify the correct vehicle. |
| **license_plate** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | The license plate of the vehicle. |

## _message_ EntitySelector

A selector for an entity in a GTFS feed. The values of the fields should correspond to the appropriate fields in the GTFS feed. At least one specifier must be given. If several are given, then the matching has to apply to all the given specifiers.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **agency_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional |
| **route_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional |
| **route_type** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional |
| **trip** | [TripDescriptor](#message-tripdescriptor) | optional |
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional |

## _message_ TranslatedString

An internationalized message containing per-language versions of a snippet of text or a URL. One of the strings from a message will be picked up. The resolution proceeds as follows: If the UI language matches the language code of a translation, the first matching translation is picked. If a default UI language (e.g., English) matches the language code of a translation, the first matching translation is picked. If some translation has an unspecified language code, that translation is picked.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **translation** | [Translation](#message-translation) | repeated | At least one translation must be provided. |

## _message_ Translation

A localized string mapped to a language.

#### Fields

| _**Field Name**_ | _**Type**_ | _**Cardinality**_ | _**Description**_ |
|------------------|------------|-------------------|-------------------|
| **text** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | required | A UTF-8 string containing the message. |
| **language** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | optional | BCP-47 language code. Can be omitted if the language is unknown or if no internationalization is done at all for the feed. At most one translation is allowed to have an unspecified language tag. |
