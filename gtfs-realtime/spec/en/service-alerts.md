Service alerts allow you to provide updates whenever there is disruption on the network. Delays and cancellations of individual trips should usually be communicated using [Trip updates](trip-updates.md).

You have the option to provide the following:

*   URL - link to your site explaining more about the alert
*   Header text - a summary of the alert
*   Description - a full description of the alert, which will always be shown alongside the header (so should not repeat this information).

## TimeRange

The alert will be displayed where appropriate within the given time range. This range should cover the entire time that the alert is useful for the passenger to see.

If no time is given, we will display the alert for as long as it is in the feed. If multiple ranges are given, we will display during all of them.

## EntitySelector

Entity selector allows you specify exactly which parts of the network this alert affects, so that we can display only the most appropriate alerts to the user. You may include multiple entity selectors for alerts which affect multiple entities.

Entities are selected using their GTFS identifiers, and you can select any of the following:

*   Agency - affects the whole network
*   Route - affects the whole route
*   Route type - affects any route of this type. e.g. all subways.
*   Trip - affects a particular trip
*   Stop - affects a particular stop

You may include more than one of the fields listed above in one `informed_entity`. When multiple fields are included in one `informed_entity`, they should be interpreted as being joined by the `AND` logical operator. In other words, the alert should only be applied in a context that meets all of the fields provided in an `informed_entity`. For example, if `route_id: "1"` and `stop_id: "5"` are both included in one `informed_entity`, then the alert should apply only to route 1 at stop 5.  It should NOT be applied to any other stop on route 1, and it should NOT be applied to any other route at stop 5.

If you would like to represent an alert that affects more than one entity (e.g. an alert for both route 1 and stop 5) , you should add multiple `informed_entity` to your `alert`, with each of them applying to the affected entity (e.g. one `informed_entity` that includes route 1 and another `informed_entity` that includes stop 5).

## Cause

What is the cause of this alert? You may specify one of the following:

*   Unknown cause
*   Other cause (not represented by any of these options)
*   Technical problem
*   Strike
*   Demonstration
*   Accident
*   Holiday
*   Weather
*   Maintenance
*   Construction
*   Police activity
*   Medical emergency

## Effect

What effect does this problem have on the specified entity? You may specify one of the following:

*   No service
*   Reduced service
*   Significant delays (insignificant delays should only be provided through [Trip updates](trip-updates.md)).
*   Detour
*   Additional service
*   Modified service: Operations are different from what the rider would normally expect.  An example is an alert that reminds riders of an upcoming holiday schedule that is different from normal service on that day of the week.
*   Stop moved
*   Other effect (not represented by any of these options)
*   Unknown effect
*   No effect: The alert provides information to riders but does not affect operations.  Examples include advertising public meetings and soliciting feedback via surveys.
*   Accessibility issue: The alert provides information about accessibility issues that affects step-free access. Examples include an out of service elevator or movable ramps.
