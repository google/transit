GTFS Realtime supports three distinct types of realtime data, that can be
combined witin a single realtime feed. Summaries are given below, with full
documentation given in the relevant section.

## Trip Updates

#### "Bus X is delayed by 5 minutes"

Trip updates represent fluctuations in the timetable. We would expect to receive
trip updates for all trips you have scheduled that are realtime-capable. These
updates would give a predicted arrival or departure for stops along the route.
Trip updates can also provide for more complex scenarios where trips are
canceled, added to the schedule, or even re-routed.

Producers MUST ensure that Trip Updates are up-to-date and accurate in relation to the real-time situation in the transit network.

[More about Trip Updates...](trip-updates.md)

## Service Alerts

#### "Station Y is closed due to construction"

Service alerts represent higher level problems with a particular entity and are
generally in the form of a textual description of the disruption.

They could represent problems with:

*   Stations
*   Lines
*   The whole network
*   etc.

A service alert will usually consist of some text which will describe the
problem, and we also allow for URLs for more information as well as more
structured information to help us understand who this service alert affects.

#### Usage of Trip Updates and Service Alerts

If producers provide both Trip Updates and Service Alerts, producers SHOULD be able update their service alerts independently from their TripUpdates. These two feeds should not fully depend on each other.  

Producers MUST also ensure that there is no conflict between their Trip Updates and Service Alerts feeds.  

Examples of conflicts include:

* A service alert informing of a stop closure while the trip updates for that stop are not set to `SKIPPED`.  
* A service alert informing of a route closure while the trip updates for the cancelled trips are not set to `CANCELED`.  
* A route is closed for the whole day. The trip updates feed cancels all trips on this route for the next 90 minutes. However, no alert was set up to inform that the route closure continues beyond those 90 minutes.

Data consumers MUST use both Trip Updates and Service Alerts to make routing decisions, such as cancelling a trip or closing a stop. When using Service Alerts to make routing decisions, Consumers MUST only use alerts whose effect is set to `NO_SERVICE`.

Since alerts with `NO_SERVICE` are used to make routing decisions, producers need to make sure to specify the most granular informed entities possible. This is done to avoid closing more transit services than are affected.

[More about Service Alerts...](service-alerts.md)

## Vehicle Positions

#### "This bus is at position X at time Y"

Vehicle position represents a few basic pieces of information about a particular
vehicle on the network.

Most important are the latitude and longitude the vehicle is at, but we can also
use data on current speed and odometer readings from the vehicle.

[More about Vehicle Position updates...](vehicle-positions.md)

## Trip Modifications

#### "These trips are affected by a detour on certain days"

Trip modifications are used to describe detours which affect a set of trips. 

A trip modification can cancel certain stops, adjust the timing for trips, 
provide a new shape that trips will take and provide the location of temporary
stops along the way.

[More about Trip Modifications...](trip-modifications.md)

## Historical remark on feed types

Early versions of GTFS Realtime Specification required each feed to only contain
single type of entities. An example tool to convert from merged to the
feed-per-type schema is located in the Bliksem Labs [gtfsrt-examples](https://github.com/bliksemlabs/gtfsrt-examples/blob/master/split_by_entitytype.py) GitHub repository.
