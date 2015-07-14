Trip updates represent fluctuations in the timetable. We would expect to receive trip updates for all trips you have scheduled that are realtime-capable. These updates would give a predicted arrival or departure time for stops along the route. Trip updates can also provide for more complex scenarios where trips are canceled or added to the schedule, or even re-routed.

**Reminder:** In [GTFS](https://developers.google.com/transit/gtfs/), a trip is a sequence of two of more stops occurring at a specific time.

There should be **at most** one trip update for each scheduled trip. In case there is no trip update for a scheduled trip, it will be concluded that no realtime data is available for the trip. The data consumer should **not** assume that the trip is running on time.

## Stop Time Updates

A trip update consists of one or more updates to vehicle stop times, which are referred to as [StopTimeUpdates](reference.md#StopTimeUpdate). These can be supplied for past and future stop times. You are allowed, but not required, to drop past stop times. When doing this, be aware that you shouldn't drop a past update if it refers to a trip that isn't yet scheduled to have finished (i.e. it finished ahead of schedule) as otherwise it will be concluded that there is no update on this trip.

Each [StopTimeUpdate](reference.md#StopTimeUpdate) is linked to a stop. Ordinarily this can be done using either a GTFS stop_sequence or a GTFS stop_id. However, in the case you are providing an update for a trip without a GTFS trip_id, you must specify stop_id as stop_sequence has no value. The stop_id must still reference a stop_id in GTFS.

The update can provide a exact timing for **arrival** and/or **departure** at a stop in [StopTimeUpdates](reference.md#StopTimeUpdate) using [StopTimeEvent](reference.md#StopTimeEvent). This should contain either an absolute **time** or a **delay** (i.e. an offset from the scheduled time in seconds). Delay can only be used in case the trip update refers to a scheduled GTFS trip, as opposed to a frequency-based trip. In this case, time should be equal to scheduled time + delay. You may also specify **uncertainty** of the prediction along with [StopTimeEvent](reference.md#StopTimeEvent), which is discussed in more detail in section [Uncertainty](#uncertainty) further down the page.

For each [StopTimeUpdate](reference.md#StopTimeUpdate), the default schedule relationship is **scheduled**. (Note that this is different from the schedule relationship for the trip). You may change this to **skipped** if the stop will not be stopped at, or **no data** if you only have realtime data for some of the trip.

**Updates should be sorted by stop_sequence** (or stop_ids in the order they occur in the trip).

If one or more stops are missing along the trip the update is propagated to all subsequent stops. This means that updating a stop time for a certain stop will change all subsequent stops in the absence of any other information.

**Example 1**

For a trip with 20 stops, a [StopTimeUpdate](reference.md#StopTimeUpdate) with arrival delay and departure delay of 0 ([StopTimeEvents](reference.md#StopTimeEvent)) for stop_sequence of the current stop means that the trip is exactly on time.

**Example 2**

For the same trip instance, three [StopTimeUpdates](reference.md#StopTimeUpdate) are provided:

*   delay of 300 seconds for stop_sequence 3
*   delay of 60 seconds for stop_sequence 8
*   delay of unspecified duration for stop_sequence 10

This will be interpreted as:

*   stop_sequences 3,4,5,6,7 have delay of 300 seconds.
*   stop_sequences 8,9 have delay of 60 seconds.
*   stop_sequences 10,..,20 have unknown delay.

### Trip Descriptor

The information provided by the trip descriptor depends on the schedule relationship of trip you are updating. There are a number of options for you to set:

| **Scheduled** | This trip is running according to a GTFS schedule, or is close enough to still be associated with it. |
| **Added** | This trip was not scheduled and has been added. For example, to cope with demand, or replace a broken down vehicle. |
| **Unscheduled** | This trip is running and is never associated with a schedule. For example, if there is no schedule and the buses run on a shuttle service. |
| **Canceled** | This trip was scheduled, but is now removed. |

In most cases, you should provide the trip_id of the scheduled trip in GTFS that this update relates to. In case you are not able to link this update to a trip in GTFS, you can instead provide a GTFS route_id and a start time and date for the trip. This is normally the case for added, unscheduled or some types of replacement trips.

## Uncertainty

Uncertainty applies to both the time and the delay value of a [StopTimeUpdate](reference.md#StopTimeUpdate). The uncertainty roughly specifies the expected error in true delay as an integer in seconds (but note, the precise statistical meaning is not defined yet). It's possible for the uncertainty to be 0, for example for trains that are driven under computer timing control.

As an example a long-distance bus that has an estimated delay of 15 minutes arriving to its next stop within a 4 minute window of error (that is +2 / -2 minutes) will have an Uncertainty value of 240.
