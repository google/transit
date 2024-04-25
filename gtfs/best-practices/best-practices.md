# GTFS Schedule Best Practices

These are recommended practices for describing public transportation services in the [GTFS Schedule Reference](https://gtfs.org/schedule/reference/) format. These complement the explicit recommendations outlined in the GTFS Schedule Reference using the terms “recommend” or “should”. Although not mandatory, following these best practices can significantly improve the quality of the data and the overall experience for riders.

These practices have been synthesized from the experience of the [GTFS Best Practices working group](#gtfs-best-practices-working-group) members and [application-specific GTFS practice recommendations](http://www.transitwiki.org/TransitWiki/index.php/Best_practices_for_creating_GTFS). 

For further background, see the [Frequently Asked Questions](#frequently-asked-questions-faq).

## Document Structure

Practices are organized into two primary sections:

* __[Practice Recommendations Organized by File](#practice-recommendations-organized-by-file):__ Recommendations are organized by file and field in the GTFS to facilitate mapping practices back to the official GTFS reference.
* __[Practice Recommendations Organized by Case](#practice-recommendations-organized-by-case):__ With particular cases, such as loop routes, practices may need to be applied across several files and fields. Such recommendations are consolidated in this section.

## Practice Recommendations Organized by File

This section shows practices organized by file and field, aligning with the [GTFS reference](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md).

### agency.txt

| Field Name | Recommendation |
| --- | --- |
| `agency_phone` | Should be included unless no such customer service phone exists. |
| `agency_email` | Should be included unless no such customer service email exists. |
| `agency_fare_url` | Should be included unless the agency is fully fare-free. |

__Examples:__

- Bus services are run by several small bus agencies. But there is one big agency that is responsible for scheduling and ticketing and from a user’s perspective responsible for the bus services.The one big agency should be defined as agency within the feed. Even if the data is split internally by different small bus operators there should only be one agency defined in the feed.
  
- The feed provider runs the ticketing portal, but there are different agencies that actually operate the services and are known by users to be responsible. The agencies actually operating the services should be defined as agencies within the feed.

### stops.txt

| Field Name | Recommendation |
| --- | --- |
| `stop_name` | When there is not a published stop name, follow consistent stop naming conventions throughout the feed.  | |
| | By default, `stop_name` should not contain generic or redundant words like “Station” or “Stop”, but some edge cases are allowed.<ul><li>When it is actually part of the name (Union Station, Central Station<li>When the `stop_name` is too generic (such as if it is the name of the city). “Station”, “Terminal”, or other words make the meaning clear.</ul> |
| `stop_lat` & `stop_lon` | Stop locations should be as accurate possible. Stop locations should have an error of __no more__ than four meters when compared to the actual stop position. |
| | Stop locations should be placed very near to the pedestrian right of way where a passenger will board (i.e. correct side of the street). |
| | If a stop location is shared across separate data feeds (i.e. two agencies use exactly the same stop / boarding facility), indicate the stop is shared by using the exact same `stop_lat` and `stop_lon` for both stops. |
| `parent_station` & `location_type` | Many stations or terminals have multiple boarding facilities (depending on mode, they might be called a bus bay, platform, wharf, gate, or another term). In such cases, feed producers should describe stations, boarding facilities (also called child stops), and their relation. <ul><li>The station or terminal should be defined as a record in `stops.txt` with `location_type = 1`.</li><li>Each boarding facility should be defined as a stop with `location_type = 0`. The `parent_station` field should reference the `stop_id` of the station the boarding facility is in.</li></ul> |
| | When naming the station and child stops, set names that are well-recognized by riders, and can help riders to identify the station and boarding facility (bus bay, platform, wharf, gate, etc.).<table class='example'><thead><tr><th>Parent Station Name</th><th>Child Stop Name</th></tr></thead><tbody><tr><td>Chicago Union Station</td><td>Chicago Union Station Platform 19</td></tr><tr><td>San Francisco Ferry Building Terminal</td><td>San Francisco Ferry Building Terminal Gate E</td></tr><tr><td>Downtown Transit Center</td><td>Downtown Transit Center Bay B</td></tr></tbody></table> |

### routes.txt

| Field Name | Recommendation |
| --- | --- |
| `route_long_name` | The definition from Specification reference: <q>This name is generally more descriptive than the <code>route_short_name</code> and will often include the route's destination or stop. At least one of <code>route_short_name</code> or <code>route_long_name</code> must be specified, or potentially both if appropriate. If the route does not have a long name, please specify a <code>route_short_name</code> and use an empty string as the value for this field.</q><br>Examples of types of long names are below:<table class='example'><thead><tr><th colspan='3'>Primary Travel Path or Corridor</th></tr><tr><th>Route Name</th><th>Form</th><th>Agency</th></tr></thead><tbody><tr><td><a href='https://www.sfmta.com/getting-around/transit/routes-stops/n-judah'>“N”/“Judah”</a></td><td><code>route_short_name</code>/<br><code>route_long_name</code></td><td><a href='https://www.sfmta.com/'>Muni</a>, in San Francisco</td></tr><tr><td><a href='https://trimet.org/schedules/r006.htm'>“6“/“ML King Jr Blvd“</a></td><td><code>route_short_name</code>/<br><code>route_long_name</code></td><td><a href='https://trimet.org/'>TriMet</a>, in Portland, Or.</td></tr><tr><td><a href='http://www.ratp.fr/informer/pdf/orienter/f_plan.php?nompdf=m6'>“6”/“Nation - Étoile”</a></td><td><code>route_short_name</code>/<br><code>route_long_name</code></td><td><a href='http://www.ratp.fr/'>RATP</a>, in Paris France.</td></tr><tr><td><a href='http://www.bvg.de/images/content/linienverlaeufe/LinienverlaufU2.pdf'>“U2”-“Pankow – Ruhleben”</a></td><td><code>route_short_name</code>-<br><code>route_long_name</code></td><td><a href='http://www.bvg.de/'>BVG</a>, in Berlin, Germany</td></tr></tbody></table><table class='example'><thead><tr><th>Description of the Service</th></tr></thead><tbody><tr><td><a href='https://128bc.org/schedules/rev-bus-hartwell-area/'>“Hartwell Area Shuttle“</a></td></tr></tbody></table>        
| | `route_long_name` should not contain the `route_short_name`. |
| | Include the full designation including a service identity when populating `route_long_name`. Examples:<table class='example'><thead><tr><th>Service Identity</th><th>Recommendation</th><th>Examples</th></tr></thead><tbody><tr><td>"MAX Light Rail"<br>TriMet, in Portland, Oregon</td><td>The <code>route_long_name</code> should include the brand (MAX) and the specific route designation</td><td>"MAX Red Line" "MAX Blue Line"</td></tr><tr><td>"Rapid Ride"<br>ABQ Ride, in Albuquerque, New Mexico</td><td>The <code>route_long_name</code> should include the brand (Rapid Ride) and the specific route designation</td><td>"Rapid Ride Red Line"<br>"Rapid Ride Blue Line"</td></tr></tbody></table>
| `route_id` | All trips on a given named route should reference the same `route_id`. <li>Different directions of a route should not be separated into different `route_id` values.</li><li>Different spans of operation of a route should not be separated into different `route_id` values. i.e. do not create different records in `routes.txt` for “Downtown AM” and “Downtown PM” services).</li> |
| | If a route group includes distinctly named branches (e.g. 1A and 1B), follow recommendations in the route [branches](#branches) case to determine `route_short_name` and `route_long_name`. |
| `route_color` & `route_text_color` | Should be consistent with signage and printed and online customer information (and thus not included if they do not exist in other places). |

### trips.txt

* __See special case for loop routes:__ Loop routes are cases where trips start and end at the same stop, as opposed to linear routes, which have two distinct termini. Loop routes must be described following specific practices. [See Loop route case.](#loop-routes)
* __See special case for lasso routes:__ Lasso routes are a hybrid of linear and loop geometries, in which vehicles travel on a loop for only a portion of the route. Lasso routes must be described following specific practices. [See Lasso route case.](#lasso-routes)

| Field Name | Recommendation |
| --- | --- |
| `trip_headsign` | Do not provide route names (matching `route_short_name` and `route_long_name`) in the `trip_headsign` or `stop_headsign` fields. |
| | Should contain destination, direction, and/or other trip designation text shown on the headsign of the vehicle which may be used to distinguish amongst trips in a route. Consistency with direction information shown on the vehicle is the primary and overriding goal for determining headsigns supplied in GTFS datasets. Other information should be included only if it does not compromise this primary goal. If headsigns change during a trip, override `trip_headsign` with `stop_times.stop_headsign`. Below are recommendations for some possible cases: |
| | <table class="example"><thead><tr><th>Route Description</th><th>Recommendation</th></tr></thead><tbody><tr><td>2A. Destination-only</td><td>Provide the terminus destination. e.g. "Transit Center", “Portland City Center”, or “Jantzen Beach”> </td></tr><tr><td>2B. Destinations with waypoints</td><td>&lt;destination&gt; via &lt;waypoint&gt; “Highgate via Charing Cross”. If waypoint(s) are removed from the headsign show to passengers after the vehicle passes those waypoints, use <code>stop_times.stop_headsign</code> to set an updated headsign.> </td></tr><tr><td>2C. Regional placename with local stops</td><td>If there will be multiple stops inside the city or borough of destination, use <code>stop_times.stop_headsign</code> once reaching the destination city.> </td></tr><tr><td>2D. Direction-only</td><td>Indicate using terms such as “Northbound”, “Inbound”, “Clockwise,” or similar directions.></td></tr><tr><td>2E. Direction with destination</td><td>&lt;direction&gt; to &lt;terminus name&gt; e.g. “Southbound to San Jose”></td></tr><tr><td>2F. Direction with destination and waypoints</td><td>&lt;direction&gt; via &lt;waypoint&gt; to &lt;destination&gt; (“Northbound via Charing Cross to Highgate”).></td></tr></tbody></table> |
| | Do not begin a headsign with the words “To” or “Towards”. |
| `direction_id` | Use values 0 and 1 consistently throughout the dataset. i.e.<ul><li>If 1 = Outbound on the Red route, then 1 = Outbound on the Green route</li><li>If 1 = Northbound on Route X, then 1 = Northbound on Route Y</li><li>If 1 = clockwise on Route X then 1 = clockwise on Route Y</li></ul> |
| `bikes_allowed` | For ferry trips, be explicit about bikes being allowed (or not), as avoiding ferry trips due to missing data usually leads to big detours. |

### stop_times.txt

Loop routes: Loop routes require special `stop_times` considerations. (See: [Loop route case](#loop-routes))

| Field Name | Recommendation |
| --- | --- |
| `pickup_type` & `drop_off_type` | Non-revenue (deadhead) trips that do not provide passenger service should be marked with `pickup_type` and `drop_off_type` value of `1` for all `stop_times` rows.
| | On revenue trips, internal “timing points” for monitoring operational performance and other places such as garages that a passenger cannot board should be marked with `pickup_type = 1` (no pickup available) and `drop_off_type = 1` (no drop off available).  |
| `arrival_time` & `departure_time` | `arrival_time` and `departure_time` fields should specify time values whenever possible, including non-binding estimated or interpolated times between timepoints.  |
| `stop_headsign` | In general, headsign values should also correspond to signs in the stations.<br><br>In the cases below, “Southbound” would mislead customers because it is not used in the station signs.
| | <table class="example"><thead><tr><th colspan="2">In NYC, for the 2 going Southbound:</th></tr><tr><th>For <code>stop_times.txt</code> rows:</th><th>Use <code>stop_headsign</code> value:</th></tr></thead><tbody><tr><td>Until Manhattan is Reached</td><td><code>Manhattan & Brooklyn</code></td></tr><tr><td>Until Downtown is Reached</td><td><code>Downtown & Brooklyn</code></td></tr><tr><td>Until Brooklyn is Reached</td><td><code>Brooklyn</code></td></tr><tr><td>Once Brooklyn is Reached</td><td><code>Brooklyn (New Lots Av)</code></td></tr></tbody></table> |
| | <table class="example"><thead><tr><th colspan="2">In Boston, for the Red Line going Southbound, for the Braintree branch:</th></tr><tr><th>For <code>stop_times.txt</code> rows:</th><th>Use <code>stop_headsign</code> value:</th></tr></thead><tbody><tr><td>Until Downtown is Reached</td><td><code>Inbound to Braintree</code></td></tr><tr><td>Once Downtown is Reached</td><td><code>Braintree</code></td></tr><tr><td>After Downtown</td><td><code>Outbound to Braintree</code></td>  </tr></tbody></table> |

### calendar.txt

| Field Name | Recommendation |
| --- | --- |
| All Fields | Including a `calendar.service_name` field can also increase the human readability of GTFS, although this is not adopted in the spec. |

### calendar_dates.txt

| Field Name | Recommendation |
| --- | --- |
| All Fields | Including a `calendar.service_name` field can also increase the human readability of GTFS, although this is not adopted in the spec.|

### fare_attributes.txt

| Field Name | Recommendation |
| --- | --- |
| | If a fare system cannot be accurately modeled, avoid further confusion and leave it blank. |
| | Include fares (`fare_attributes.txt` and `fare_rules.txt`) and model them as accurately as possible. In edge cases where fares cannot be accurately modeled, the fare should be represented as more expensive rather than less expensive so customers will not attempt to board with insufficient fare. If the vast majority of fares cannot be modeled correctly, do not include fare information in the feed. |

### fare_rules.txt

| Field Name | Recommendation |
| --- | --- |
| All Fields | If a fare system cannot be accurately modeled, avoid further confusion and leave it blank. |
| | Include fares (`fare_attributes.txt` and `fare_rules.txt`) and model them as accurately as possible. In edge cases where fares cannot be accurately modeled, the fare should be represented as more expensive rather than less expensive so customers will not attempt to board with insufficient fare. If the vast majority of fares cannot be modeled correctly, do not include fare information in the feed. |

### shapes.txt

| Field Name | Recommendation |
| --- | --- |
| All Fields | Ideally, for alignments that are shared (i.e. in a case where Routes 1 and 2 operate on the same segment of roadway or track) then the shared portion of alignment should match exactly. This helps to facilitate high-quality transit cartography. <!-- (77) -->
| | Alignments should follow the centerline of the right of way on which the vehicle travels. This could be either the centerline of the street if there are no designated lanes, or the centerline of the side of the roadway that travels in the direction the vehicle moves. <br><br>Alignments should not “jag” to a curb stop, platform, or boarding location. |
| `shape_dist_traveled` | The `shape_dist_traveled` field allows the agency to specify exactly how the stops in the `stop_times.txt` file fit into their respective shape. A common value to use for the `shape_dist_traveled` field is the distance from the beginning of the shape as traveled by the vehicle (think something like an odometer reading). <li>Route alignments (in `shapes.txt`) should be within 100 meters of stop locations which a trip serves.</li><li>Simplify alignments so that <code>shapes.txt</code> does not contain extraneous points (i.e. remove extra points on straight-line segments; see discussion of line simplification problem).</li>

### frequencies.txt

| Field Name | Recommendation |
| --- | --- |
| All Fields | Actual stop times are ignored for trips referenced by `frequencies.txt`; only travel time intervals between stops are significant for frequency-based trips. For clarity/human readability, it is recommended that the first stop time of a trip referenced in `frequencies.txt` should begin at 00:00:00 (first `arrival_time` value of 00:00:00). |
| `block_id` | Can be provided for frequency-based trips. |

### transfers.txt

`transfers.transfer_type` can be one of four values [defined in the GTFS](https://github.com/google/transit/blob/master/gtfs/spec/en/reference.md/#transferstxt). These `transfer_type` definitions are quoted from the GTFS Specification below, _in italics_, with additional practice recommendations.

| Field Name | Recommendation |
| --- | --- |
| `transfer_type` | <q>0 or (empty): This is a recommended transfer point between routes.</q><br>If there are multiple transfer opportunities that include a superior option (i.e. a transit center with additional amenities or a station with adjacent or connected boarding facilities/platforms), specify a recommended transfer point. |
| | <q>1: This is a timed transfer point between two routes. The departing vehicle is expected to wait for the arriving one, with sufficient time for a passenger to transfer between routes.</q><br>This transfer type overrides a required interval to reliably make transfers.  As an example, Google Maps assumes that passengers need 3 minutes to safely make a transfer. Other applications may assume other defaults. |
| | <q>2: This transfer requires a minimum amount of time between arrival and departure to ensure a connection. The time required to transfer is specified by <code>min_transfer_time</code>.</q><br>Specify minimum transfer time if there are obstructions or other factors which increase the time to travel between stops. |
| | <q>3: Transfers are not possible between routes at this location.</q><br>Specify this value if transfers are not possible because of physical barriers, or if they are made unsafe or complicated by difficult road crossings or gaps in the pedestrian network. |
| | If in-seat (block) transfers are allowed between trips, then the last stop of the arriving trip must be the same as the first stop of the departing trip. |


## Practice Recommendations Organized by Case

This section covers particular cases with implications across files and fields.

### Loop Routes

On loop routes, vehicles’ trips begin and end at the same location (sometimes a transit or transfer center). Vehicles usually operate continuously and allow passengers to stay onboard as the vehicle continues its loop.

<img src="https://raw.githubusercontent.com/MobilityData/GTFS_Schedule_Best-Practices/master/en/loop-route.svg" width=200px style="display: block; margin-left: auto; margin-right: auto;">

Headsigns recommendations should therefore be applied in order to show riders the direction in which the vehicle is going.

To indicate the changing direction of travel, provide `stop_headsigns` in the `stop_times.txt` file. The `stop_headsign` describes the direction for trips departing from the stop for which it's defined. Adding `stop_headsigns` to each stop of a trip allows you to change the headsign information along a trip.

Don’t define one single circular trip in the stop_times.txt file for a route that operates between two endpoints (such as when the same bus goes back and forth). Instead, split the trip into two separate trip directions.
  
__Examples of circular trip modeling:__

- Circular trip with changing headsign for each stop

| trip_id | arrival_time | departure_time | stop_id | stop_sequence | stop_headsign |
|---------|--------------|----------------|---------|---------------|---------------|
| trip_1  | 06:10:00     | 06:10:00       | stop_A  | 1             | "B"           |
| trip_1  | 06:15:00     | 06:15:00       | stop_B  | 2             | "C"           |
| trip_1  | 06:20:00     | 06:20:00       | stop_C  | 3             | "D"           |
| trip_1  | 06:25:00     | 06:25:00       | stop_D  | 4             | "E"           |
| trip_1  | 06:30:00     | 06:30:00       | stop_E  | 5             | "A"           |
| trip_1  | 06:35:00     | 06:35:00       | stop_A  | 6             | ""            |
 
- Circular trip with two headsigns

| trip_id | arrival_time | departure_time | stop_id | stop_sequence | stop_headsign |
|---------|--------------|----------------|---------|---------------|---------------|
| trip_1  | 06:10:00     | 06:10:00       | stop_A  | 1             | "outbound"    |
| trip_1  | 06:15:00     | 06:15:00       | stop_B  | 2             | "outbound"    |
| trip_1  | 06:20:00     | 06:20:00       | stop_C  | 3             | "outbound"    |
| trip_1  | 06:25:00     | 06:25:00       | stop_D  | 4             | "inbound"     |
| trip_1  | 06:30:00     | 06:30:00       | stop_E  | 5             | "inbound"     |
| trip_1  | 06:35:00     | 06:35:00       | stop_F  | 6             | "inbound"     |
| trip_1  | 06:40:00     | 06:40:00       | stop_A  | 7             | ""            |

| Field Name | Recommendation |
| --- | --- |
| `trips.trip_id `| Model the complete round-trip for the loop with a single trip. |
| `stop_times.stop_id` | Include the first/last stop twice in `stop_times.txt` for the trip that is a loop. Example below. Often, a loop route may include first and last trips that do not travel the entire loop. Include these trips as well. <table class="example"><thead><tr><th><code>trip_id</code></th><th><code>stop_id</code></th><th><code>stop_sequence</code></th></tr></thead><tbody><tr><td>9000</td><td>101</td><td>1</td></tr><tr><td>9000</td><td>102</td><td>2</td></tr><tr><td>9000</td><td>103</td><td>3</td></tr><tr><td>9000</td><td>101</td><td>4</td></tr></tbody></table> |
| `trips.direction_id` | If loop operates in opposite directions (i.e. clockwise and counterclockwise), then designate `direction_id` as `0` or `1`. |
| `trips.block_id` | Indicate continuous loop trips with the same `block_id`. |

### Lasso Routes

Lasso routes combine aspects of a loop route and directional route.

<img src="https://raw.githubusercontent.com/MobilityData/GTFS_Schedule_Best-Practices/master/en/lasso-route.svg" width=140px style="display: block; margin-left: auto; margin-right: auto;">

| Examples: |
| -------- |
| Subway Routes ([Chicago](https://www.transitchicago.com/assets/1/6/ctamap_Lsystem.pdf)) |
| Bus Suburb to Downtown Routes ([St. Albert](https://stalbert.ca/uploads/PDF-infosheets/RideGuide-201-207_Revised_Oct_2017.pdf) or [Edmonton](http://webdocs.edmonton.ca/transit/route_schedules_and_maps/future/RT039.pdf)) |
| CTA Brown Line ([CTA Website](http://www.transitchicago.com/brownline/) and [TransitFeeds](https://transitfeeds.com/p/chicago-transit-authority/165/latest/route/Brn)) |

| Field Name | Recommendation |
| --- | --- |
| `trips.trip_id` | The full extent of a “vehicle round-trip” (see illustration [above](#lasso-route-fig)) consists of travel from A to B to B and back to A. An entire vehicle round-trip may be expressed by: <li>A __single__ `trip_id` value/record in `trips.txt`</li><li>__Multiple__ `trip_id` values/records in `trips.txt`, with continuous travel indicated by `block_id`.</li> |
| `stop_times.stop_headsign` | The stops along the A-B section will be passed through in both directions. `stop_headsign` facilitates distinguishing travel direction. Therefore, providing `stop_headsign` is recommended for these trips.example_table: <table class="example"><thead>  <tr><th>Examples:</th></tr></thead><tbody><tr><td>"A via B"</td></tr><tr><td>"A"</td></tr></tbody></table><table class="example"><thead><tr><th>Chicago Transit Authority's <a href="http://www.transitchicago.com/purpleline/">Purple Line</a></th></tr></thead><tbody><tr><td>"Southbound to Loop"</td></tr><tr><td>"Northbound via Loop"</td></tr><tr><td>"Northbound to Linden"</td></tr></tbody></table><table class="example"><thead><tr><th>Edmonton Transit Service Bus Lines, here <a href="http://webdocs.edmonton.ca/transit/route_schedules_and_maps/future/RT039.pdf">the 39</a></th></tr></thead><tbody><tr><td>"Rutherford"</td></tr><tr><td>"Century Park"</td></tr></tbody></table>
| `trip.trip_headsign` | The trip headsign should be a global description of the trip, like displayed in the schedules. Could be “Linden to Linden via Loop” (Chicago example), or “A to A via B” (generic example). |

### Branches

Some routes may include branches. Alignment and stops are shared amongst these branches, but each also serves distinct stops and alignment sections. The relationship among branches may be indicated by route name(s), headsigns, and trip short name using the further guidelines below.

<img src="https://raw.githubusercontent.com/MobilityData/GTFS_Schedule_Best-Practices/master/en/branching.svg" width=250px style="display: block; margin-left: auto; margin-right: auto;">

| Field Name | Recommendation |
| --- | --- |
| All Fields | In naming branch routes, it is recommended to follow other passenger information materials. Below are descriptions and examples of two cases: |
| | If timetables and on-street signage represent two distinctly named routes (e.g. 1A and 1B), then present this as such in the GTFS, using the `route_short_name` and/or `route_long_name` fields. Example: GoDurham Transit [routes 2, 2A, and 2B](https://gotriangle.org/sites/default/files/brochure/godurham-route2-2a-2b_1.pdf) share a common alignment throughout the majority of the route, but they vary in several different aspects. <ul><li>Route 2 is core service, running most hours.</li><li>Route 2 includes a deviation on Main Street nights, Sundays, and holidays.</li><li>Routes 2A and 2B operate daytime hours Monday through Saturday.</li><li>Route 2B serves additional stops in a deviation of the shared alignment path.</li></ul> |
| | If agency-provided information describes branches as the same named route, then utilize the `trips.trip_headsign`, `stop_times.stop_headsign`, and/or `trips.trip_short_name` fields. Example: GoTriangle [route 300](https://gotriangle.org/sites/default/files/route_300_v.1.19.pdf) travels to different locations depending on the time of day. During peak commuter hours extra legs are added onto the standard route to accommodate workers entering and leaving the city. |

## Frequently Asked Questions (FAQ)

### Why are these GTFS Best Practices important?

The objectives of GTFS Best Practices are:

* To improve end-user customer experience in public transportation apps
* Support broad data interoperability to make it easier for software developers to deploy and scale applications, products, and services
* Facilitate the use of GTFS in various application categories (beyond its original focus on trip planning)

Without coordinated GTFS Best Practices, various GTFS-consuming applications may establish requirements and expectations in an uncoordinated way, which leads to diverging requirements and application-specific datasets and less interoperability. Prior to the release of the Best Practices, there was greater ambiguity and disagreement in what constitutes correctly-formed GTFS data.

### How were they developed? Who developed them?

These Best Practices were developed by a working group of 17 organizations involved in GTFS, including app providers & data consumers, transit providers, and consultants with extensive involvement in GTFS. The working group was convened and facilitated by [Rocky Mountain Institute](http://www.rmi.org/mobility).

Working Group members voted on each Best Practice. Most Best Practices were approved by a unanimous vote. In a minority of cases, Best Practices were approved a large majority of organizations.

Some GTFS Best Practices have been merged into the spec and have been removed from this document.

### Why not change the GTFS Reference directly?

Good question! 
The process of examining the Specification, data usage and needs did indeed trigger some changes to the Specification. 
The Best Practices were created to bring everyone's understanding of the spec into harmony with the intention for some to be added into the spec and undergo the larger governance process, and others to be moved into a "how-to" guide. 
Since then, some Best Practices have been added into the spec based on their level of adoption and community consensus. 
To contribute to this effort, please go to the [GTFS Reference GitHub repository](https://github.com/google/transit/), or contact [specifications@mobilitydata.org](mailto:specifications@mobilitydata.org).

### How to check for conformance with these Best Practices?

The Canonical GTFS Schedule Validator checks for compliance against the GTFS Best Practices that can be automatically verified. Each [warning](https://gtfs-validator.mobilitydata.org/rules.html#WARNING-table) corresponds to recommendations that are either explicitly suggested by the GTFS Schedule Reference, using the term “recommend” or “should,” or mentioned in this document.
You can find more about this validation tool on the [validate page](https://gtfs.org/schedule/validate/).

### I represent a transit agency. What steps can I take so that our software service providers and vendors follow these Best Practices?

Refer your vendor or software service provider to these Best Practices. We recommend referencing the GTFS Best Practices URL, as well as core Spec Reference in procurement for GTFS-producing software.

### What should I do if I notice a GTFS data feed does not conform to the GTFS Best Practices?

Identify the contact for the feed, using the `feed_contact_email` or `feed_contact_url` fields in [feed_info.txt](https://gtfs.org/schedule/reference/#feed_infotxt) if they are provided, or looking up contact information on the transit agency or feed producer website. When communicating the issue to the feed producer, link to the specific GTFS Best Practice that isn't being followed using this document (See ["Linking to this Document"](#linking-to-this-document)) or [the appropriate warning](https://gtfs-validator.mobilitydata.org/rules.html#WARNING-table) in the Canonical GTFS Schedule Validator if available.

### How to propose or amend published GTFS Best Practices
New Best Practices are now being added directly into the [spec](https://gtfs.org/schedule/reference/) in order to gradually consolidate both documents. 
If you'd like to suggest a new best practice, please go to the [GTFS Reference GitHub repository](https://github.com/google/transit/), [open an issue](https://github.com/google/transit/issues/new/choose) or create a Pull Request, or contact [specifications@mobilitydata.org](mailto:specifications@mobilitydata.org).

## About This Document

### Objectives

The objectives of maintaining GTFS Best Practices is to:

* Support greater interoperability of transit data
* Improve end-user customer experience in public transportation apps
* Make it easier for software developers to deploy and scale applications, products, and services
* Facilitate the use of GTFS in various application categories (beyond its original focus on trip planning)

### Linking to This Document

Please link here in order to provide feed producers with guidance for correct formation of GTFS data. Each individual recommendation has an anchor link. Click the recommendation to get the URL for the in-page anchor link.

If a GTFS-consuming application makes requirements or recommendations for GTFS data practices that are not described here, it is recommended to publish a document with those requirements or recommendations to supplement these common best practices.

### GTFS Best Practices Working Group

The GTFS Best Practices Working Group was convened by [Rocky Mountain Institute](http://rmi.org/) in 2016-17, consisting of public transportation providers, developers of GTFS-consuming applications, consultants, and academic organizations to define common practices and expectations for GTFS data. 
Members of this working group included:

* [Cambridge Systematics](https://www.camsys.com/)
* [Capital Metro](https://www.capmetro.org/)
* [Center for Urban Transportation Research at University of South Florida](https://www.cutr.usf.edu/)
* [Conveyal](http://conveyal.com/)
* [Google](https://www.google.com/)
* [IBI Group](http://www.ibigroup.com/)
* [Mapzen](https://mapzen.com/)
* [Microsoft](https://www.microsoft.com/)
* [Moovel](https://www.moovel.com/)
* [Oregon Department of Transportation](http://www.oregon.gov/odot/)
* [Swiftly](https://goswift.ly/)
* [Transit](https://transitapp.com/)
* [Trillium](http://trilliumtransit.com/)
* [TriMet](https://trimet.org/)
* [World Bank](http://www.worldbank.org/)

Today, this document is maintained by [MobilityData](http://mobilitydata.org/).
