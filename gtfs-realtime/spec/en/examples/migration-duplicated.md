## Migration Guide - Transition from ADDED to NEW or DUPLICATED trips 

The GTFS-realtime `trip.schedule_relationship` of `NEW` represents a new trip that runs on a schedule unrelated to any existing scheduled trip.

The GTFS-realtime `trip.schedule_relationship` of `DUPLICATED` represents a new trip that is the same as an existing scheduled trip except for service start date and time. 

This migration guide defines how existing producers and consumers that were using the `ADDED` enumeration should transition to either the `NEW` and the `DUPLICATED` enumeration. The goal is to minimize disruption to producers and consumers during the transition. 

*If you are a producer or consumer that has **not** used the `ADDED` enumeration, no action is required - you can produce/consume `NEW` and/or `DUPLICATED` trips without producing/consuming any `ADDED` entities.* 

For a full history of the `NEW` enumeration, see the [`NEW` and `REPLACEMENT` proposal on GitHub](https://github.com/google/transit/pull/504).

For a full history of the `DUPLICATED` enumeration, see the [`DUPLICATED` proposal on GitHub](https://github.com/google/transit/pull/221).

### Which one to migrate to

Both `NEW` and `DUPLICATED` enumeration are used to specify a trip which was not originally scheduled to run in the GTFS static.

Use `NEW` if your trip cannot be described using any scheduled trips as a template. For example, if the trip calls at different stops from the regular trips of the route, or if the extra trip is pickup only at the beginning of the route despite that the regular trips allow both pickup and drop off at all stops.

Use `DUPLICATED` if your trip is a copy of a scheduled trip, which may run at the same, or at different times of the original scheduled trip.

### Using ADDED and NEW entities in the same feed

If you are a producer who has been using the `ADDED` enumeration to specify trips which are unrelated to the schedule, to avoid disruption to existing consumers it is recommended that you continue to produce `ADDED` entitles for these trips but also add `NEW` entitles for the same trip.

However, to prevent consumers from accidentally adding the same trip twice, the entities referencing the same trip **must** be linked using the same `trip_id`, `route_id` and `start_date`.
In addition, the contents of the `stop_time_update` must also be the same as well.

#### Producers

~~~
entity {
  id: "ei0"
  trip_update {
    trip: {
      trip_id: "1" // <-- a trip_id not found in the static GTFS
      route_id: "A"
      schedule_relationship: ADDED
      start_date: "20200821" // <-- New trip date
      start_time: "11:30:00" // <-- New trip time
    }
    stop_time_update {
	... // The full list of the calling points of the trip
    }
  }
}

entity {
  id: "ei10"
  trip_update {
    trip: {
      trip_id: "1" // <-- The same trip_id as the above
      route_id: "A" // <-- The same route_id as the above
      schedule_relationship: NEW
      start_date: "20200821" // <-- The same date as the above
      start_time: "11:30:00" // <-- The same time as the above
    }
    stop_time_update {
	... // <-- The same content as the above
    }
  }
}
~~~

It is suggested that you notify existing consumers (e.g., via a developer mailing list) that the use of `ADDED` is being deprecated by a set deadline and that consumers should start consuming the `NEW` trips instead. The above strategy being used to match `ADDED` and `NEW` trip entities should also be mentioned and a link to this migration guide should be included. After the deadline passes, you can remove the `NEW` entities from your feed and publish only the `NEW` entities for newly-added trips.

#### Consumers

As mentioned above, producers will transition from `ADDED` to `NEW` enumerations by initially publishing two entities for each new trip using the same `trip_id`.

Therefore, when a consumer implements support for `NEW` trips, it is important that consumers ignore any `ADDED` trips that have the same `trip_id` as a `NEW` trip `trip_id`.

### Using ADDED and DUPLICATED entities in same feed

#### Producers

If you are a producer who has been using the `ADDED` enumeration for duplicated trips, to avoid disruption to existing consumers it is recommended that you continue to produce `ADDED` entities for these trips but also add `DUPLICATED` entities for the same trip.  

However, to prevent consumers from accidentally adding the same trip twice, the entities referencing the same trip **must** be linked using the same `trip_id`. You can link the two entities in **one** of two ways:  

 1. `trip.trip_id` of both entities **must** be the same, OR
 2. `trip.trip_id` of the `ADDED` trip **must** be the same as the `DUPLICATED` trip `trip_properties.trip_id`
 
Here's an example of the first option (1) to duplicate GTFS `trip_id 1`, with the `trip.trip_id` matching in the `ADDED` and `DUPLICATED` entities:

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

Here's an example of the second option (2) to duplicate GTFS `trip_id 1`, with the `trip.trip_id` of the `ADDED` trip matching the `DUPLICATED` trip `trip_properties.trip_id`:

~~~
entity {
  id: "ei0"
  trip_update {
    trip: {
      trip_id: "NewTripId987" // <-- New trip_id unique to this trip
      schedule_relationship: ADDED
      start_date: "20200821" // <-- New trip date
      start_time: "11:30:00" // <-- New trip time
    }
    stop_time_update {
	...
    }
  }
}

entity {
  id: "ei10"
  trip_update {
    trip: {
      trip_id: "1" // <-- trip_id from static GTFS to copy
      schedule_relationship: DUPLICATED
    }
    trip_properties {
      trip_id: "NewTripId987" // <-- Matches the ADDED trip.trip_id
      start_date: "20200821"  // <-- New trip date
      start_time: "11:30:00"  // <-- New trip time
    }
    stop_time_update {
	...
    }
  }
}
~~~

It is suggested that you notify existing consumers (e.g., via a developer mailing list) that the use of `ADDED` is being deprecated by a set deadline and that consumers should start consuming the `DUPLICATED` trips instead. The above strategy being used to match `ADDED` and `DUPLICATED` trip entities should also be mentioned and a link to this migration guide should be included. After the deadline passes, you can remove the `ADDED` entities from your feed and publish only the `DUPLICATED` entities for duplicated trips.

#### Consumers

As mentioned above, producers will transition from `ADDED` to `DUPLICATED` enumerations by initially publishing two entities for each duplicated trip, using one of the two above options for matching IDs between the entities. 
 
Therefore, when a consumer implements support for `DUPLICATED` trips, it is important that consumers:
 1. Ignore any `ADDED` trips that have the same `trip.trip_id` as a `DUPLICATED` trip `trip.trip_id`
 1. Ignore any `ADDED` trips that have the same `trip.trip_id` as a `DUPLICATED` trip `trip_properties.trip_id`