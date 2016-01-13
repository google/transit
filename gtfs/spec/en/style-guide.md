## GTFS Style Guide

The GTFS specification provides a lot of flexibility in how a physical transit system is modeled. What is the best approach? In general, it is a good idea to keep the following guidelines in mind when developing a feed.

### Route Organization

The entries in [routes.txt](reference.md#routes.txt) should typically have the same organization as the physical routes communicated to riders by an agency. As an example, an agency will often first group their timetables by route when presenting them on a website or in a printed booklet. The entries in routes.txt should generally have a one-to-one correspondence to the timetable routes. It can be tempting for an agency to break a physical route into multiple entries in routes.txt in order to represent different route variations, such as direction of travel, but the preferred approach is to instead use features of [trips.txt](reference.md#trips.txt) to model those variations. Multiple entries in routes.txt with the same route short name or route long name are often an indication that routes have been needlessly subdivided.

Do:

~~~
**routes.txt**
route_id,route_short_name,route_long_name,route_type
R10,10,Airport - Downtown,3
~~~

~~~
**trips.txt**
route_id,trip_id,trip_headsign,direction_id
R10,T-10-1,Airport,0
R10,T-10-2,Downtown,1
~~~

Don't:

~~~
**routes.txt**
route_id,route_short_name,route_long_name,route_type
R10-in,10,To Downtown,3
R10-out,10,To Airport,3
R20-in,20,To Downtown,3
R20-out,20,To University,3
~~~