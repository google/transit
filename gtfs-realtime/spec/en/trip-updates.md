Trip updates represent fluctuations in the timetable. We would expect to receive trip updates for all trips you have scheduled that are realtime-capable. These updates would give a predicted arrival or departure time for stops along the route. Trip updates can also provide for more complex scenarios where trips are canceled or added to the schedule, or even re-routed.

**Reminder:** In [GTFS](https://developers.google.com/transit/gtfs/), a trip is a sequence of two of more stops occurring at a specific time.

There should be **at most** one trip update for each scheduled trip. In case there is no trip update for a scheduled trip, it will be concluded that no realtime data is available for the trip. The data consumer should **not** assume that the trip is running on time.

If a vehicle is serving multiple trips within the same block (for more information about trips and blocks, please refer to [GTFS trips.txt](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md#tripstxt)):
* the feed should include a TripUpdate for the trip currently being served by the vehicle. Producers are encouraged to include TripUpdates for one or more trips after the current trip in this vehicle's block if the producer is confident in the quality of the predictions for these future trip(s). Including multiple TripUpdates for the same vehicle avoids prediction "pop-in" for riders as the vehicle transitions from one trip to another and also gives riders advance notice of delays that impact downstream trips (e.g., when the known delay exceeds planned layover times between trips).
* the respective TripUpdate entities are not required to be added to the feed in the same order that they are scheduled in the block. For example, if there are trips with `trip_ids` 1, 2, and 3 that all belong to one block, and the vehicle travels trip 1, then trip 2, and then trip 3, the `trip_update` entities may appear in any order - for example, adding trip 2, then trip 1, and then trip 3 is allowed.

## Stop Time Updates

A trip update consists of one or more updates to vehicle stop times, which are referred to as [StopTimeUpdates](reference.md#StopTimeUpdate). These can be supplied for past and future stop times. You are allowed, but not required, to drop past stop times.  Producers should not drop a past `StopTimeUpdate` if it refers to a stop with a scheduled arrival time in the future for the given trip (i.e. the vehicle has passed the stop ahead of schedule), as otherwise it will be concluded that there is no update for this stop.

For example, if the following data appears in the GTFS-rt feed:

* Stop 4 – Predicted at 10:18am (scheduled at 10:20am – 2 min early)
* Stop 5 – Predicted at 10:30am (scheduled at 10:30am – on time)

...the prediction for Stop 4 cannot be dropped from the feed until 10:21am, even if the bus actually passes the stop at 10:18am. If the `StopTimeUpdate` for Stop 4 was dropped from the feed at 10:18am or 10:19am, and the scheduled arrival time is 10:20am, then the consumer should assume that no real-time information exists for Stop 4 at that time, and schedule data from GTFS should be used.

Each [StopTimeUpdate](reference.md#StopTimeUpdate) is linked to a stop. Ordinarily this can be done using either a GTFS stop_sequence or a GTFS stop_id. However, in the case you are providing an update for a trip without a GTFS trip_id, you must specify stop_id as stop_sequence has no value. The stop_id must still reference a stop_id in GTFS. If the same stop_id is visited more than once in a trip, then stop_sequence should be provided in all StopTimeUpdates for that stop_id on that trip.

The update can provide a exact timing for **arrival** and/or **departure** at a stop in [StopTimeUpdates](reference.md#StopTimeUpdate) using [StopTimeEvent](reference.md#StopTimeEvent). This should contain either an absolute **time** or a **delay** (i.e. an offset from the scheduled time in seconds). Delay can only be used in case the trip update refers to a scheduled GTFS trip, as opposed to a frequency-based trip. In this case, time should be equal to scheduled time + delay. You may also specify **uncertainty** of the prediction along with [StopTimeEvent](reference.md#StopTimeEvent), which is discussed in more detail in section [Uncertainty](#uncertainty) further down the page.

For each [StopTimeUpdate](reference.md#StopTimeUpdate), the default schedule relationship is **scheduled**. (Note that this is different from the schedule relationship for the trip). You may change this to **skipped** if the stop will not be stopped at, or **no data** if you only have realtime data for some of the trip.

**Updates should be sorted by stop_sequence** (or stop_ids in the order they occur in the trip).

If one or more stops are missing along the trip the `delay` from the update (or, if only `time` is provided in the update, a delay computed by comparing the `time` against the GTFS schedule time) is propagated to all subsequent stops. This means that updating a stop time for a certain stop will change all subsequent stops in the absence of any other information. Note that updates with a schedule relationship of `SKIPPED` will not stop delay propagation, but updates with schedule relationships of `SCHEDULED` (also the default value if schedule relationship is not provided) or `NO_DATA` will.

**Example 1**

For a trip with 20 stops, a [StopTimeUpdate](reference.md#StopTimeUpdate) with arrival delay and departure delay of 0 ([StopTimeEvents](reference.md#StopTimeEvent)) for stop_sequence of the current stop means that the trip is exactly on time.

**Example 2**

For the same trip instance, three [StopTimeUpdates](reference.md#StopTimeUpdate) are provided:

*   delay of 300 seconds for stop_sequence 3
*   delay of 60 seconds for stop_sequence 8
*   [ScheduleRelationship](/gtfs-realtime/spec/en/reference.md/#enum-schedulerelationship) of `NO_DATA` for stop_sequence 10

This will be interpreted as:

*   stop_sequences 1,2 have unknown delay.
*   stop_sequences 3,4,5,6,7 have delay of 300 seconds.
*   stop_sequences 8,9 have delay of 60 seconds.
*   stop_sequences 10,..,20 have unknown delay.

### Trip Descriptor

The information provided by the trip descriptor depends on the schedule relationship of trip you are updating. There are a number of options for you to set:

|_**Value**_|_**Comment**_|
|-----------|-------------|
| **Scheduled** | This trip is running according to a GTFS schedule, or is close enough to still be associated with it. |
| **Added** | This trip was not scheduled and has been added. For example, to cope with demand, or replace a broken down vehicle. |
| **Unscheduled** | This trip is running and is never associated with a schedule. For example, if there is no schedule and the buses run on a shuttle service. |
| **Canceled** | This trip was scheduled, but is now removed. |
| **Duplicated** | This new trip is a copy of an existing trip in static GTFS except for the service start date and time. The new trip will run at the service date and time specified in TripProperties. |

In most cases, you should provide the trip_id of the scheduled trip in GTFS that this update relates to.

#### Systems with repeated trip_ids

For systems using repeated trip_ids, for example trips modeled using frequencies.txt, that is frequency-based trips, the trip_id is not in itself a unique identifier of a single journey, as it lacks a
specific time component. In order to uniquely identify such trips within a
TripDescriptor, a triple of identifiers must be provided:

*    __trip_id__
*    __start_time__
*    __start_date__

start_time should be first published, and any subsequent feed updates should use
that same start_time when referring to the same journey. StopTimeUpdates
should be used to indicate adjustments; start_time does not have to be precisely
the departure time from the first station, although it should be pretty close to
that time.

For example, let’s say we decide at 10:00, May, 25th 2015, that a trip with
trip_id=T will start at start_time=10:10:00, and provide this information via
realtime feed at 10:01. By 10:05 we suddenly know that the trip will start not
at 10:10 but at 10:13. In our new realtime feed we can still identify this trip
as (T, 2015-05-25, 10:10:00) but provide a StopTimeUpdate with departure from
first stop at 10:13:00.

#### Alternative trip matching

Trips which are not frequency based may also be uniquely identified by a
TripDescriptor including the combination of:

*    __route_id__
*    __direction_id__
*    __start_time__
*    __start_date__

where start_time is the scheduled start time as defined in the static schedule, as long as the combination of ids provided resolves to a unique trip.


## Uncertainty

Uncertainty applies to both the time and the delay value of a [StopTimeUpdate](reference.md#StopTimeUpdate). The uncertainty roughly specifies the expected error in true delay as an integer in seconds (but note, the precise statistical meaning is not defined yet). It's possible for the uncertainty to be 0, for example for trains that are driven under computer timing control.

As an example a long-distance bus that has an estimated delay of 15 minutes arriving to its next stop within a 4 minute window of error (that is +2 / -2 minutes) will have an Uncertainty value of 240.
