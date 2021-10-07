## Migration Guide - Transition from SKIPPED to MODIFIED

The GTFS-realtime `StopTimeUpdate.schedule_relationship` of `SKIPPED`, which is now experimentally deprecated, was used to indicate that a vehicle will not be serving a particular stop that was originally scheduled as a part of `stop_times.txt` in GTFS-static.

The GTFS-static `pickup_type` and `drop_off_type` fields within `stop_times.txt` allow an agency to specify details on what a rider needs to do in order to board/alight at a given stop (e.g. a rider must explicitly request a drop-off at a stop, otherwise the driver will skip the stop).

This migration guide defines how existing producers who use the `SKIPPED` enumeration for indicating that vehicle will not stop at a given stop or as a best approximation of partial service at a stop can provide a more nuanced picture of the level of service through `pickup_type` and `drop_off_type` via `StopTimeProperties` instead. The goal is to minimize disruption to producers and consumers during the transition. 

See the [Add pickup and drop-off types to GTFS-RT proposal on GitHub](https://github.com/google/transit/pull/265).

### Initially providing SKIPPED and pickup_type / drop_off_type in same feed

#### Producers

If you are a producer who uses the `SKIPPED` enumeration for indicating that a vehicle will not stop at a given stop or as a best approximation of partial service at a stop, it is recommended that you continue to produce `SKIPPED` entities for those stop time updates but also add `pickup_type` and `drop_off_type` entities for the same `StopTimeUpdate`, such as a `NO_PICKUP` and `NO_DROP_OFF` for a stop that's will not be made.

Here's an example of indicating to consumers that a vehicle will be "drop-off only": 

~~~
entity {
  id: "ei0"
  trip_update {
    ...
    stop_time_update {
      ...
      schedule_relationship: SKIPPED
      
      stop_time_properties {
        pickup_type: NO_PICKUP
        drop_off_type: MUST_ASK_DRIVER_DROP_OFF
      }
    }
  }
}
~~~

When a stop is not fully skipped and you'd like to provide additional information through `pickup_type` and `drop_off_type`, you may also use `SCHEDULED` in the interim.

It is suggested that you notify existing consumers (e.g., via a developer mailing list) that the use of `SKIPPED` is being deprecated in favor of more nuanced information using `MODIFIED` by a set deadline and that consumers should start consuming the `MODIFIED` enumeration as well as `pickup_type` and `drop_off_type`. You should also provide a link to this migration guide. After the deadline passes, you can stop using `SKIPPED` entities for scenarios where `pickup_type` or `drop_off_type` are included and start using `MODIFIED` instead.

#### Consumers 
In this interim period, when `pickup_type` and `drop_off_type` are set in `StopTimeProperties`, it takes precedence over `schedule_relationship=SKIPPED` or `schedule_relationship=SCHEDULED`, meaning that the definitions of `SKIPPED` and `SCHEDULED` do not apply. Real-time arrival information should still be used to inform passengers rather being potentially ignored when `SKIPPED`. For example, a passenger-facing application could use this additional information to provide additional instructions or notification on how to board/alight, similar to what may happen with those fields being specified statically in `stop_times.txt`.

In the future, instead of `SKIPPED`, as per above, you should expect `MODIFIED` instead, with `pickup_type=NO_PICKUP` and `drop_off_type=NO_DROP_OFF` in scenarios where a vehicle will entirely skip a scheduled stop.
