## Migration Guide - Transition from ADDED to DUPLICATED trips 

The GTFS-realtime `trip.schedule_relationship` of `DUPLICATED` represents a new trip that is the same as an existing scheduled trip except for service start date and time. 

This migration guide defines how existing producers and consumers that were using the `ADDED` enumeration to represent duplicated trips should transition to the `DUPLICATED` enumeration. The goal is to minimize disruption to producers and consumers during the transition. If you are a producer or consumer that has not used the `ADDED` enumeration to describe duplicated trips, no action is required. 

For a full history of the `DUPLICATED` enumeration, see the [`DUPLICATED` proposal on GitHub](https://github.com/google/transit/pull/221).

### Using ADDED and DUPLICATED entities in same feed

#### Producers

If you are a producer who has been using the `ADDED` enumeration for duplicated trips, to avoid disruption to existing consumers it is recommended that you continue to produce `ADDED` entities for these trips but also add `DUPLICATED` entities for the same trip - so a duplicated trip will have both an `ADDED` entity as well as a `DUPLICATED` entity in your feed for the same `trip_id`.  

However, note that the `trip.trip_id` of both entities **must** be the same so consumers don't process the trip twice. While past implementations of duplicated trips using `ADDED` have varied, it is important that producers standardize on this behavior so it is predictable to consumers during the transition period.

Here's how the `ADDED` entity looks to duplicate `trip_id 1` from static GTFS:

~~~
entity {
  id: "ei0"
  trip_update {
    trip: {
      trip_id: "1" // <-- trip_id from static GTFS to copy
      schedule_relationship: ADDED
      start_date: "20200821" // <-- New trip date
      start_time: "11:30:00" // <-- New trip time
    }
    stop_time_update {
	...
    }
  }
}
~~~

...and here's how the `DUPLICATED` entity looks:

~~~
entity {
  id: "ei10"
  trip_update {
    trip: {
      trip_id: "1" // <-- trip_id from static GTFS to copy
      schedule_relationship: DUPLICATED
    }
    trip_properties {
      trip_id: "NewTripId987" // <-- New trip_id unique to this trip
      start_date: "20200821"  // <-- New trip date
      start_time: "11:30:00"  // <-- New trip time
    }
    stop_time_update {
	...
    }
  }
}
~~~

It is suggested that you notify existing consumers (e.g., via a developer mailing list) that the use of `ADDED` for duplicated trips is being deprecated by a set deadline and that consumers should start consuming the `DUPLICATED` trips instead. After the deadline passes, you can remove the `ADDED` entities from your feed and publish only the `DUPLICATED` entities for duplicated trips.

#### Consumers

As mentioned above, producers will transition from `ADDED` to `DUPLICATED` enumerations by initially publishing two entities for each duplicated trip with the same `trip.trip_id` - one with the `ADDED` enum and one with the `DUPLICATED` enum. 

Therefore, when a consumer implements support for `DUPLICATED` trips, it is important that consumers ignore any `ADDED` trips that have the same `trip.trip_id` as a `DUPLICATED` trip.