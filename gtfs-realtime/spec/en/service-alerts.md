Service alerts allow you to provide updates whenever there is disruption on the network. Delays and cancellations of individual trips should usually be communicated using [Trip updates](trip-updates.md).

You have the option to provide the following:

*   URL - link to your site explaining more about the alert
*   Header text - a summary of the alert
*   Description - a full description of the alert, which will always be shown alongside the header (so should not repeat this information).

### Time Range

The alert will be displayed where appropriate within the given time range. This range should cover the entire time that the alert is useful for the passenger to see.

If no time is given, we will display the alert for as long as it is in the feed. If multiple ranges are given, we will display during all of them.

### Entity Selector

Entity selector allows you specify exactly which parts of the network this alert affects, so that we can display only the most appropriate alerts to the user. You may include multiple entity selectors for alerts which affect multiple entities.

Entities are selected using their GTFS identifiers, and you can select any of the following:

*   Agency - affects the whole network
*   Route - affects the whole route
*   Route type - affects any route of this type. e.g. all subways.
*   Trip - affects a particular trip
*   Stop - affects a particular stop

### Cause

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

### Effect

What effect does this problem have on the specified entity? You may specify one of the following:

*   No service
*   Reduced service
*   Significant delays (insignificant delays should only be provided through [Trip updates](trip-updates.md)).
*   Detour
*   Additional service
*   Modified service
*   Stop moved
*   Other effect (not represented by any of these options)
*   Unknown effect
