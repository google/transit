## General Transit Feed Specification Reference

**Revised August 4, 2016. See [Revision History](../../CHANGES.md) for more details.**

This document explains the types of files that comprise a GTFS transit feed and defines the fields used in all of those files.

## Table of Contents

1.  [Term Definitions](#term-definitions)
2.  [Feed Files](#feed-files)
3.  [File Requirements](#file-requirements)
4.  [Field Definitions](#field-definitions)
    -   [agency.txt](#agencytxt)
    -   [stops.txt](#stopstxt)
    -   [routes.txt](#routestxt)
    -   [trips.txt](#tripstxt)
    -   [stop\_times.txt](#stop_timestxt)
    -   [calendar.txt](#calendartxt)
    -   [calendar\_dates.txt](#calendar_datestxt)
    -   [fare\_attributes.txt](#fare_attributestxt)
    -   [fare\_rules.txt](#fare_rulestxt)
    -   [shapes.txt](#shapestxt)
    -   [frequencies.txt](#frequenciestxt)
    -   [transfers.txt](#transferstxt)
    -   [feed\_info.txt](#feed_infotxt)

## Term Definitions

This section defines terms that are used throughout this document.

* **Field required** - The field column must be included in your feed, and a value must be provided for each record. Some required fields permit an empty string as a value. To enter an empty string, just omit any text between the commas for that field. Note that 0 is interpreted as "a string of value 0", and is not an empty string. Please see the field definition for details.
* **Field optional** - The field column may be omitted from your feed. If you choose to include an optional column, each record in your feed must have a value for that column. You may include an empty string as a value for records that do not have values for the column. Some optional fields permit an empty string as a value. To enter an empty string, just omit any text between the commas for that field. Note that 0 is interpreted as "a string of value 0", and is not an empty string.
* **Dataset unique** - The field contains a value that maps to a single distinct entity within the column. For example, if a route is assigned the ID **1A**, then no other route may use that route ID. However, you may assign the ID **1A** to a location because locations are a different type of entity than routes.

## Feed Files

This specification defines the following files along with their associated content:

|  Filename | Required | Defines |
|  ------ | ------ | ------ |
|  [agency.txt](#agencytxt) | **Required** | One or more transit agencies that provide the data in this feed. |
|  [stops.txt](#stopstxt) | **Required** | Individual locations where vehicles pick up or drop off passengers. |
|  [routes.txt](#routestxt) | **Required** | Transit routes. A route is a group of trips that are displayed to riders as a single service. |
|  [trips.txt](#tripstxt)  | **Required** | Trips for each route. A trip is a sequence of two or more stops that occurs at specific time. |
|  [stop_times.txt](#stop_timestxt)  | **Required** | Times that a vehicle arrives at and departs from individual stops for each trip. |
|  [calendar.txt](#calendartxt)  | **Required** | Dates for service IDs using a weekly schedule. Specify when service starts and ends, as well as days of the week where service is available. |
|  [calendar_dates.txt](#calendar_datestxt)  | Optional | Exceptions for the service IDs defined in the [calendar.txt](#calendartxt) file. If [calendar.txt](#calendartxt) includes ALL dates of service, this file may be specified instead of [calendar.txt](#calendartxt). |
|  [fare_attributes.txt](#fare_attributestxt)  | Optional | Fare information for a transit organization's routes. |
|  [fare_rules.txt](#fare_rulestxt)  | Optional | Rules for applying fare information for a transit organization's routes. |
|  [shapes.txt](#shapestxt)  | Optional | Rules for drawing lines on a map to represent a transit organization's routes. |
|  [frequencies.txt](#frequenciestxt)  | Optional | Headway (time between trips) for routes with variable frequency of service. |
|  [transfers.txt](#transferstxt)  | Optional | Rules for making connections at transfer points between routes. |
|  [feed_info.txt](#feed_infotxt)  | Optional | Additional information about the feed itself, including publisher, version, and expiration information. |

## File Requirements

The following requirements apply to the format and contents of your files:

* All files in a General Transit Feed Spec (GTFS) feed must be saved as comma-delimited text.
* The first line of each file must contain field names. Each subsection of the [Field Definitions](#Field-Definitions) section corresponds to one of the files in a transit feed and lists the field names you may use in that file.
* All field names are case-sensitive.
* Field values may not contain tabs, carriage returns or new lines.
* Field values that contain quotation marks or commas must be enclosed within quotation marks. In addition, each quotation mark in the field value must be preceded with a quotation mark. This is consistent with the manner in which Microsoft Excel outputs comma-delimited (CSV) files. For more information on the CSV file format, see http://tools.ietf.org/html/rfc4180.
The following example demonstrates how a field value would appear in a comma-delimited file:
  * **Original field value:** `Contains "quotes", commas and text`
  * **Field value in CSV file:** `"Contains ""quotes"", commas and text"`
* Field values must not contain HTML tags, comments or escape sequences.
* Remove any extra spaces between fields or field names. Many parsers consider the spaces to be part of the value, which may cause errors.
* Each line must end with a CRLF or LF linebreak character.
* Files should be encoded in UTF-8 to support all Unicode characters. Files that include the Unicode byte-order mark (BOM) character are acceptable. Please see the [Unicode FAQ](http://unicode.org/faq/utf_bom.html#BOM) for more information on the BOM character and UTF-8.
* Zip the files in your feed.

## Field Definitions

### agency.txt

File: **Required**

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  agency_id | Optional | The **agency_id** field is an ID that uniquely identifies a transit agency. A transit feed may represent data from more than one agency. The **agency_id** is dataset unique. This field is optional for transit feeds that only contain data for a single agency. |
|  agency_name | Required | The **agency_name** field contains the full name of the transit agency. Google Maps will display this name. |
|  agency_url | Required | The **agency_url** field contains the URL of the transit agency. The value must be a fully qualified URL that includes **http**:// or **https**://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values. |
|  agency_timezone | Required | The **agency_timezone** field contains the timezone where the transit agency is located. Timezone names never contain the space character but may contain an underscore. Please refer to http://en.wikipedia.org/wiki/List_of_tz_zones for a list of valid values. If multiple agencies are specified in the feed, each must have the same agency_timezone. |
|  agency_lang | Optional | The **agency_lang field** contains a two-letter ISO 639-1 code for the primary language used by this transit agency. The language code is case-insensitive (both en and EN are accepted). This setting defines capitalization rules and other language-specific settings for all text contained in this transit agency's feed. Please refer to http://www.loc.gov/standards/iso639-2/php/code_list.php for a list of valid values. |
|  agency_phone | Optional | The **agency_phone field** contains a single voice telephone number for the specified agency. This field is a string value that presents the telephone number as typical for the agency's service area. It can and should contain punctuation marks to group the digits of the number. Dialable text (for example, TriMet's "503-238-RIDE") is permitted, but the field must not contain any other descriptive text. |
|  agency_fare_url | Optional | The **agency_fare_url** specifies the URL of a web page that allows a rider to purchase tickets or other fare instruments for that agency online. The value must be a fully qualified URL that includes **http**:// or **https**://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values. |
|  agency_email | Optional | Contains a single valid email address actively monitored by the agency’s customer service department. This email address will be considered a direct contact point where transit riders can reach a customer service representative at the agency. |

### stops.txt

File: **Required**

|  Field Name | Required | Details |  |  |
|  ------ | ------ | ------ | ------ | ------ |
|  stop_id | **Required** | The **stop_id** field contains an ID that uniquely identifies a stop, station, or station entrance. Multiple routes may use the same stop. The **stop_id** is dataset unique. |  |  |
|  stop_code | Optional | The **stop_code** field contains short text or a number that uniquely identifies the stop for passengers. Stop codes are often used in phone-based transit information systems or printed on stop signage to make it easier for riders to get a stop schedule or real-time arrival information for a particular stop.  The stop_code field contains short text or a number that uniquely identifies the stop for passengers.  For internal codes, use **stop_id**. This field should be left blank for stops without a code. |  |  |
|  stop_name | **Required** | The **stop_name** field contains the name of a stop, station, or station entrance. Please use a name that people will understand in the local and tourist vernacular. |  |  |
|  stop_desc | Optional | The **stop_desc** field contains a description of a stop. Please provide useful, quality information. Do not simply duplicate the name of the stop. |  |  |
|  stop_lat | **Required** | The **stop_lat** field contains the latitude of a stop, station, or station entrance. The field value must be a valid WGS 84 latitude. |  |  |
|  stop_lon | **Required** | The **stop_lon** field contains the longitude of a stop, station, or station entrance. The field value must be a valid WGS 84 longitude value from -180 to 180. |  |  |
|  zone_id | Optional | The **zone_id** field defines the fare zone for a stop ID. Zone IDs are required if you want to provide fare information using [fare_rules.txt](#fare_rulestxt). If this stop ID represents a station, the zone ID is ignored. |  |  |
|  stop_url | Optional | The **stop_url** field contains the URL of a web page about a particular stop. This should be different from the agency_url and the route_url fields.  The value must be a fully qualified URL that includes **http**:// or **https**://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values. |  |  |
|  location_type | Optional | The **location_type** field identifies whether this stop ID represents a stop, station, or station entrance. If no location type is specified, or the location_type is blank, stop IDs are treated as stops. Stations may have different properties from stops when they are represented on a map or used in trip planning.  The location type field can have the following values: |  |  |
|   |  | * **0** or blank - Stop. A location where passengers board or disembark from a transit vehicle. |  |  |
|   |  | * **1** - Station. A physical structure or area that contains one or more stop. |  |  |
|   |  | * **2** - Station Entrance/Exit. A location where passengers can enter or exit a station from the street. The stop entry must also specify a parent_station value referencing the stop ID of the parent station for the entrance. |  |  |
|  parent_station | Optional | For stops that are physically located inside stations, the **parent_station** field identifies the station associated with the stop. To use this field, stops.txt must also contain a row where this stop ID is assigned location type=1. |  |  |
|   |  | **This stop ID represents...** | **This entry's location type...** | **This entry's parent_station field contains...** |
|   |  | A stop located inside a station. | 0 or blank | The stop ID of the station where this stop is located. The stop referenced by parent_station must have location_type=1. |
|   |  | A stop located outside a station. | 0 or blank | A blank value. The parent_station field doesn't apply to this stop. |
|   |  | A station. | 1 | A blank value. Stations can't contain other stations. |
|  stop_timezone | Optional | The **stop_timezone** field contains the timezone in which this stop, station, or station entrance is located. Please refer to [Wikipedia List of Timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for a list of valid values. If omitted, the stop should be assumed to be located in the timezone specified by **agency_timezone** in [agency.txt](#agencytxt).   When a stop has a parent station, the stop is considered to be in the timezone specified by the parent station's **stop_timezone** value. If the parent has no stop_timezone value, the stops that belong to that station are assumed to be in the timezone specified by **agency_timezone**, even if the stops have their own **stop_timezone** values. In other words, if a given stop has a **parent_station** value, any **stop_timezone** value specified for that stop must be ignored.  Even if **stop_timezone** values are provided in stops.txt, the times in [stop_times.txt](#stop_timestxt) should continue to be specified as time since midnight in the timezone specified by **agency_timezone** in agency.txt. This ensures that the time values in a trip always increase over the course of a trip, regardless of which timezones the trip crosses. |  |  |
|  wheelchair_boarding | Optional | The **wheelchair_boarding field** identifies whether wheelchair boardings are possible from the specified stop, station, or station entrance. The field can have the following values: |  |  |
|   |  | * **0** (or empty) - indicates that there is no accessibility information for the stop |  |  |
|   |  | * **1** - indicates that at least some vehicles at this stop can be boarded by a rider in a wheelchair |  |  |
|   |  | * **2** - wheelchair boarding is not possible at this stop |  |  |
|   |  | When a stop is part of a larger station complex, as indicated by a stop with a **parent_station** value, the stop's **wheelchair_boarding** field has the following additional semantics: |  |  |
|   |  | * **0** (or empty) - the stop will inherit its **wheelchair_boarding** value from the parent station, if specified in the parent |  |  |
|   |  | * **1** - there exists some accessible path from outside the station to the specific stop / platform |  |  |
|   |  | * **2** - there exists no accessible path from outside the station to the specific stop / platform |  |  |
|   |  | For station entrances, the **wheelchair_boarding** field has the following additional semantics: |  |  |
|   |  | * **0** (or empty) - the station entrance will inherit its **wheelchair_boarding** value from the parent station, if specified in the parent |  |  |
|   |  | * **1** - the station entrance is wheelchair accessible (e.g. an elevator is available to platforms if they are not at-grade)  |  |  |
|   |  | * **2** - there exists no accessible path from the entrance to station platforms |  |  |

### routes.txt

File: **Required**

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  route_id | **Required** | The **route_id** field contains an ID that uniquely identifies a route. The route_id is dataset unique. |
|  agency_id | Optional | The **agency_id** field defines an agency for the specified route. This value is referenced from the [agency.txt](#agencytxt) file. Use this field when you are providing data for routes from more than one agency. |
|  route_short_name | **Required** | The **route_short_name** contains the short name of a route. This will often be a short, abstract identifier like "32", "100X", or "Green" that riders use to identify a route, but which doesn't give any indication of what places the route serves. At least one of *route_short_name* or *route_long_name* must be specified, or potentially both if appropriate. If the route does not have a short name, please specify a *route_long_name* and use an empty string as the value for this field. |
|  route_long_name | **Required** | The **route_long_name** contains the full name of a route. This name is generally more descriptive than the *route_short_name* and will often include the route's destination or stop. At least one of *route_short_name* or *route_long_name* must be specified, or potentially both if appropriate. If the route does not have a long name, please specify a *route_short_nam*e and use an empty string as the value for this field. |
|  route_desc | Optional | The **route_desc** field contains a description of a route. Please provide useful, quality information. Do not simply duplicate the name of the route. For example, "**A** trains operate between Inwood-207 St, Manhattan and Far Rockaway-Mott Avenue, Queens at all times. Also from about 6AM until about midnight, additional **A** trains operate between Inwood-207 St and Lefferts Boulevard (trains typically alternate between Lefferts Blvd and Far Rockaway)." |
|  route_type | **Required** | The **route_type** field describes the type of transportation used on a route. Valid values for this field are: |
|   |  | * **0** - Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area. |
|   |  | * **1** - Subway, Metro. Any underground rail system within a metropolitan area. |
|   |  | * **2** - Rail. Used for intercity or long-distance travel. |
|   |  | * **3** - Bus. Used for short- and long-distance bus routes. |
|   |  | * **4** - Ferry. Used for short- and long-distance boat service. |
|   |  | * **5** - Cable car. Used for street-level cable cars where the cable runs beneath the car. |
|   |  | * **6** - Gondola, Suspended cable car. Typically used for aerial cable cars where the car is suspended from the cable. |
|   |  | * **7** - Funicular. Any rail system designed for steep inclines. |
|  route_url | Optional | The **route_url** field contains the URL of a web page about that particular route. This should be different from the agency_url.  The value must be a fully qualified URL that includes **http**:// or **https**://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values. |
|  route_color | Optional | In systems that have colors assigned to routes, the **route_color** field defines a color that corresponds to a route. The color must be provided as a six-character hexadecimal number, for example, 00FFFF. If no color is specified, the default route color is white (FFFFFF).  The color difference between **route_color** and **route_text_color** should provide sufficient contrast when viewed on a black and white screen. The [W3C Techniques for Accessibility Evaluation And Repair Tools document](https://www.w3.org/TR/AERT#color-contrast) offers a useful algorithm for evaluating color contrast. There are also helpful online tools for choosing contrasting colors, including the [snook.ca Color Contrast Check application](http://snook.ca/technical/colour_contrast/colour.html#fg=33FF33,bg=333333). |
|  route_text_color | Optional | The route_text_color field can be used to specify a legible color to use for text drawn against a background of route_color. The color must be provided as a six-character hexadecimal number, for example, FFD700. If no color is specified, the default text color is black (000000).  The color difference between **route_color** and **route_text_color** should provide sufficient contrast when viewed on a black and white screen. |

### trips.txt

File: **Required**

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  route_id | **Required** | The **route_id** field contains an ID that uniquely identifies a route. This value is referenced from the [routes.txt](#routestxt) file. |
|  service_id | **Required** | The **service_id** contains an ID that uniquely identifies a set of dates when service is available for one or more routes. This value is referenced from the [calendar.txt](#calendartxt) or [calendar_dates.txt](#calendar_datestxt) file. |
|  trip_id | **Required** | The **trip_id** field contains an ID that identifies a trip. The **trip_id** is dataset unique. |
|  trip_headsign | Optional | The **trip_headsign** field contains the text that appears on a sign that identifies the trip's destination to passengers. Use this field to distinguish between different patterns of service in the same route. If the headsign changes during a trip, you can override the **trip_headsign** by specifying values for the the **stop_headsign** field in [stop_times.txt](#stop_timestxt). |
|  trip_short_name | Optional | The **trip_short_name** field contains the text that appears in schedules and sign boards to identify the trip to passengers, for example, to identify train numbers for commuter rail trips. If riders do not commonly rely on trip names, please leave this field blank.  A **trip_short_name** value, if provided, should uniquely identify a trip within a service day; it should not be used for destination names or limited/express designations. |
|  direction_id | Optional | The **direction_id** field contains a binary value that indicates the direction of travel for a trip. Use this field to distinguish between bi-directional trips with the same **route_id**. This field is not used in routing; it provides a way to separate trips by direction when publishing time tables. You can specify names for each direction with the **trip_headsign** field. |
|   |  | * 0 - travel in one direction (e.g. outbound travel) |
|   |  | * 1 - travel in the opposite direction (e.g. inbound travel) |
|   |  | For example, you could use the *trip_headsign* and *direction_id* fields together to assign a name to travel in each direction for a set of trips. A [trips.txt](#tripstxt) file could contain these rows for use in time tables: |
|   |  | * `trip_id,...,trip_headsign,direction_id` |
|   |  | * `1234,...,to Airport,0` |
|   |  | * `1505,...,to Downtown,1` |
|  block_id | Optional | The **block_id** field identifies the block to which the trip belongs. A block consists of two or more sequential trips made using the same vehicle, where a passenger can transfer from one trip to the next just by staying in the vehicle. The **block_id** must be referenced by two or more trips in trips.txt. |
|  shape_id | Optional | The **shape_id** field contains an ID that defines a shape for the trip. This value is referenced from the [shapes.txt](#shapestxt) file. The shapes.txt file allows you to define how a line should be drawn on the map to represent a trip. |
|  wheelchair_accessible | Optional | * **0** (or empty) - indicates that there is no accessibility information for the trip |
|   |  | * **1** - indicates that the vehicle being used on this particular trip can accommodate at least one rider in a wheelchair |
|   |  | * **2** - indicates that no riders in wheelchairs can be accommodated on this trip |
|  bikes_allowed | Optional | 0 (or empty) - indicates that there is no bike information for the trip |
|   |  | * **1** - indicates that the vehicle being used on this particular trip can accommodate at least one bicycle |
|   |  | * **2** - indicates that no bicycles are allowed on this trip |

### stop_times.txt

File: **Required**

|  Field Name | Required | Details |  |
|  ------ | ------ | ------ | ------ |
|  trip_id | **Required** | The **trip_id** field contains an ID that identifies a trip. This value is referenced from the [trips.txt](#tripstxt) file. |  |
|  arrival_time | **Required** | The **arrival_time** specifies the arrival time at a specific stop for a specific trip on a route. The time is measured from "noon minus 12h" (effectively midnight, except for days on which daylight savings time changes occur) at the beginning of the service date. For times occurring after midnight on the service date, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins. If you don't have separate times for arrival and departure at a stop, enter the same value for **arrival_time** and **departure_time**.<br/><br/>Scheduled stops where the vehicle strictly adheres to the specified arrival and departure times are timepoints. For example, if a transit vehicle arrives at a stop before the scheduled departure time, it will hold until the departure time. If this stop is not a timepoint, use either an empty string value for the **arrival_time** field or provide an interpolated time. Further, indicate that interpolated times are provided via the **timepoint** field with a value of zero. If interpolated times are indicated with **timepoint**=0, then time points must be indicated with a value of 1 for the **timepoint** field. Provide arrival times for all stops that are time points.<br/><br/>An arrival time must be specified for the first and the last stop in a trip. Times must be eight digits in HH:MM:SS format (H:MM:SS is also accepted, if the hour begins with 0). Do not pad times with spaces. The following columns list stop times for a trip and the proper way to express those times in the **arrival_time** field: |  |
|   |  | **Time** | **arrival_time value** |
|   |  | 08:10:00 A.M. | 08:10:00 or 8:10:00 |
|   |  | 01:05:00 P.M. | 13:05:00 |
|   |  | 07:40:00 P.M. | 19:40:00 |
|   |  | 01:55:00 A.M. | 25:55:00 |
|   |  | **Note:** Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. |  |
|  departure_time | **Required** | The **departure_time** specifies the departure time from a specific stop for a specific trip on a route. The time is measured from "noon minus 12h" (effectively midnight, except for days on which daylight savings time changes occur) at the beginning of the service date. For times occurring after midnight on the service date, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins. If you don't have separate times for arrival and departure at a stop, enter the same value for **arrival_time** and **departure_time**.<br/><br/>Scheduled stops where the vehicle strictly adheres to the specified arrival and departure times are timepoints. For example, if a transit vehicle arrives at a stop before the scheduled departure time, it will hold until the departure time. If this stop is not a timepoint, use either an empty string value for the **departure_time** field or provide an interpolated time (further, indicate that interpolated times are provided via the **timepoint** field with a value of zero). If interpolated times are indicated with **timepoint**=0, then time points must be indicated with a value of 1 for the **timepoint** field. Provide departure times for all stops that are time points.<br/><br/>A departure time must be specified for the first and the last stop in a trip even if the vehicle does not allow boarding at the last stop.  Times must be eight digits in HH:MM:SS format (H:MM:SS is also accepted, if the hour begins with 0). Do not pad times with spaces. The following columns list stop times for a trip and the proper way to express those times in the **departure_time** field: |  |
|   |  | Time | departure_time value |
|   |  | 08:10:00 A.M. | 08:10:00 or 8:10:00 |
|   |  | 01:05:00 P.M. | 13:05:00 |
|   |  | 07:40:00 P.M. | 19:40:00 |
|   |  | 01:55:00 A.M. | 25:55:00 |
|   |  | **Note:** Trips that span multiple dates will have stop times greater than 24:00:00. For example, if a trip begins at 10:30:00 p.m. and ends at 2:15:00 a.m. on the following day, the stop times would be 22:30:00 and 26:15:00. Entering those stop times as 22:30:00 and 02:15:00 would not produce the desired results. |  |
|  stop_id | **Required** | The **stop_id** field contains an ID that uniquely identifies a stop. Multiple routes may use the same stop. The **stop_id** is referenced from the [stops.txt](#stopstxt) file. If **location_type** is used in [stops.txt](#stopstxt), all stops referenced in [stop_times.txt](#stop_timestxt) must have **location_type** of 0.  Where possible, **stop_id** values should remain consistent between feed updates. In other words, stop A with **stop_id 1** should have **stop_id 1** in all subsequent data updates. If a stop is not a time point, enter blank values for **arrival_time** and **departure_time**. |  |
|  stop_sequence | **Required** | The **stop_sequence** field identifies the order of the stops for a particular trip. The values for **stop_sequence** must be non-negative integers, and they must increase along the trip.  For example, the first stop on the trip could have a **stop_sequence** of 1, the second stop on the trip could have a **stop_sequence** of 23, the third stop could have a **stop_sequence** of 40, and so on. |  |
|  stop_headsign | Optional | The **stop_headsign** field contains the text that appears on a sign that identifies the trip's destination to passengers. Use this field to override the default **trip_headsign** when the headsign changes between stops. If this headsign is associated with an entire trip, use **trip_headsign** instead. |  |
|  pickup_type | Optional | The **pickup_type** field indicates whether passengers are picked up at a stop as part of the normal schedule or whether a pickup at the stop is not available. This field also allows the transit agency to indicate that passengers must call the agency or notify the driver to arrange a pickup at a particular stop. Valid values for this field are: |  |
|   |  | * **0** - Regularly scheduled pickup |  |
|   |  | * **1** - No pickup available |  |
|   |  | * **2** - Must phone agency to arrange pickup |  |
|   |  | * **3** - Must coordinate with driver to arrange pickup |  |
|   |  | The default value for this field is **0**. |  |
|  drop_off_type | Optional | The **drop_off_type** field indicates whether passengers are dropped off at a stop as part of the normal schedule or whether a drop off at the stop is not available. This field also allows the transit agency to indicate that passengers must call the agency or notify the driver to arrange a drop off at a particular stop. Valid values for this field are: |  |
|   |  | * **0** - Regularly scheduled drop off |  |
|   |  | * **1** - No drop off available |  |
|   |  | * **2** - Must phone agency to arrange drop off |  |
|   |  | * **3** - Must coordinate with driver to arrange drop off |  |
|   |  | The default value for this field is **0**. |  |
|  shape_dist_traveled | Optional | When used in the [stop_times.txt](#stop_timestxt) file, the **shape_dist_traveled** field positions a stop as a distance from the first shape point. The **shape_dist_traveled** field represents a real distance traveled along the route in units such as feet or kilometers. For example, if a bus travels a distance of 5.25 kilometers from the start of the shape to the stop, the **shape_dist_traveled** for the stop ID would be entered as "5.25". This information allows the trip planner to determine how much of the shape to draw when showing part of a trip on the map. The values used for **shape_dist_traveled** must increase along with **stop_sequence**: they cannot be used to show reverse travel along a route.  The units used for **shape_dist_traveled** in the [stop_times.txt](#stop_timestxt) file must match the units that are used for this field in the shapes.txt file. |  |
|  timepoint | Optional | The timepoint field can be used to indicate if the specified arrival and departure times for a stop are strictly adhered to by the transit vehicle or if they are instead approximate and/or interpolated times. The field allows a GTFS producer to provide interpolated stop times that potentially incorporate local knowledge, but still indicate if the times are approximate. For stop-time entries with specified arrival and departure times, valid values for this field are: |  |
|   |  | * **empty** - Times are considered exact. |  |
|   |  | * **0** - Times are considered approximate. |  |
|   |  | * **1** - Times are considered exact. |  |
|   |  | For stop-time entries without specified arrival and departure times, feed consumers must interpolate arrival and departure times. Feed producers may optionally indicate that such an entry is not a timepoint (value=0) but it is an error to mark a entry as a timepoint (value=1) without specifying arrival and departure times. |  |

### calendar.txt

File: **Required**

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  service_id | **Required** | The **service_id** contains an ID that uniquely identifies a set of dates when service is available for one or more routes. Each service_id value can appear at most once in a calendar.txt file. This value is dataset unique. It is referenced by the [trips.txt](#tripstxt) file. |
|  monday | **Required** | The monday field contains a binary value that indicates whether the service is valid for all Mondays. |
|   |  | * A value of **1** indicates that service is available for all Mondays in the date range. (The date range is specified using the **start_date** and **end_date** fields.) |
|   |  | * A value of **0** indicates that service is not available on Mondays in the date range. |
|   |  | **Note:** You may list exceptions for particular dates, such as holidays, in the [calendar_dates.txt](#calendar_datestxt) file. |
|  tuesday | **Required** | The tuesday field contains a binary value that indicates whether the service is valid for all Tuesdays. |
|   |  | A value of **1** indicates that service is available for all Tuesdays in the date range. (The date range is specified using the **start_date** and **end_date** fields.) |
|   |  | A value of **0** indicates that service is not available on Tuesdays in the date range. |
|   |  | **Note:** You may list exceptions for particular dates, such as holidays, in the [calendar_dates.txt](#calendar_datestxt) file. |
|  wednesday | **Required** | The wednesday field contains a binary value that indicates whether the service is valid for all Wednesdays. |
|   |  | A value of **1** indicates that service is available for all Wednesdays in the date range. (The date range is specified using the **start_date** and **end_date** fields.) |
|   |  | A value of **0** indicates that service is not available on Wednesdays in the date range. |
|   |  | **Note:** You may list exceptions for particular dates, such as holidays, in the [calendar_dates.txt](#calendar_datestxt) file. |
|  thursday | **Required** | The thursday field contains a binary value that indicates whether the service is valid for all Thursdays. |
|   |  | A value of **1** indicates that service is available for all Thursdays in the date range. (The date range is specified using the **start_date** and **end_date** fields.) |
|   |  | A value of **0** indicates that service is not available on Thursdays in the date range. |
|   |  | **Note:** You may list exceptions for particular dates, such as holidays, in the [calendar_dates.txt](#calendar_datestxt) file. |
|  friday | **Required** | The friday field contains a binary value that indicates whether the service is valid for all Fridays. |
|   |  | A value of **1** indicates that service is available for all Fridays in the date range. (The date range is specified using the **start_date** and **end_date** fields.) |
|   |  | A value of **0** indicates that service is not available on Fridays in the date range. |
|   |  | **Note:** You may list exceptions for particular dates, such as holidays, in the [calendar_dates.txt](#calendar_datestxt) file |
|  saturday | **Required** | The saturday field contains a binary value that indicates whether the service is valid for all Saturdays. |
|   |  | A value of **1** indicates that service is available for all Saturdays in the date range. (The date range is specified using the **start_date** and **end_date** fields.) |
|   |  | A value of **0** indicates that service is not available on Saturdays in the date range. |
|   |  | **Note:** You may list exceptions for particular dates, such as holidays, in the [calendar_dates.txt](#calendar_datestxt) file. |
|  sunday | **Required** | The sunday field contains a binary value that indicates whether the service is valid for all Sundays. |
|   |  | A value of **1** indicates that service is available for all Sundays in the date range. (The date range is specified using the **start_date** and **end_date** fields.) |
|   |  | A value of **0** indicates that service is not available on Sundays in the date range. |
|   |  | **Note:** You may list exceptions for particular dates, such as holidays, in the [calendar_dates.txt](#calendar_datestxt) file. |
|  start_date | **Required** | The **start_date** field contains the start date for the service.  The start_date field's value should be in YYYYMMDD format. |
|  end_date | **Required** | The **end_date** field contains the end date for the service. This date is included in the service interval.  The **end_date** field's value should be in YYYYMMDD format. |

### calendar_dates.txt

File: **Optional**

The calendar_dates table allows you to explicitly activate or disable service IDs by date. You can use it in two ways.

* Recommended: Use calendar_dates.txt in conjunction with [calendar.txt](#calendartxt), where calendar_dates.txt defines any exceptions to the default service categories defined in the [calendar.txt](#calendartxt) file. If your service is generally regular, with a few changes on explicit dates (for example, to accomodate special event services, or a school schedule), this is a good approach.
* Alternate: Omit [calendar.txt](#calendartxt), and include ALL dates of service in calendar_dates.txt. If your schedule varies most days of the month, or you want to programmatically output service dates without specifying a normal weekly schedule, this approach may be preferable.

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  service_id | **Required** | The **service_id** contains an ID that uniquely identifies a set of dates when a service exception is available for one or more routes. Each (service_id, date) pair can only appear once in calendar_dates.txt. If the a service_id value appears in both the calendar.txt and calendar_dates.txt files, the information in calendar_dates.txt modifies the service information specified in [calendar.txt](#calendartxt). This field is referenced by the [trips.txt](#tripstxt) file. |
|  date | **Required** | The **date** field specifies a particular date when service availability is different than the norm. You can use the **exception_type** field to indicate whether service is available on the specified date. The **date** field's value should be in YYYYMMDD format. |
|  exception_type | **Required** | The **exception_type** indicates whether service is available on the date specified in the date field. |
|   |  |*  A value of **1** indicates that service has been added for the specified date. |
|   |  |* A value of **2** indicates that service has been removed for the specified date. |
|   |  | For example, suppose a route has one set of trips available on holidays and another set of trips available on all other days. You could have one **service_id** that corresponds to the regular service schedule and another **service_id** that corresponds to the holiday schedule. For a particular holiday, you would use the calendar_dates.txt file to add the holiday to the holiday **service_id** and to remove the holiday from the regular **service_id** schedule. |

### fare_attributes.txt

File: **Optional**

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  fare_id | **Required** | The **fare_id** field contains an ID that uniquely identifies a fare class. The **fare_id** is dataset unique. |
|  price | **Required** | The **price** field contains the fare price, in the unit specified by **currency_type**. |
|  currency_type | **Required** | The **currency_type** field defines the currency used to pay the fare. Please use the ISO 4217 alphabetical currency codes which can be found at the following URL: http://en.wikipedia.org/wiki/ISO_4217. |
|  payment_method | **Required** | The **payment_method** field indicates when the fare must be paid. Valid values for this field are: |
|   |  | * **0** - Fare is paid on board. |
|   |  | * **1** - Fare must be paid before boarding. |
|  transfers | **Required** | The transfers field specifies the number of transfers permitted on this fare. Valid values for this field are: |
|   |  | * **0** - No transfers permitted on this fare. |
|   |  | * **1** - Passenger may transfer once. |
|   |  | * **2** - Passenger may transfer twice. |
|   |  | * **(empty)** - If this field is empty, unlimited transfers are permitted. |
|  agency_id | Optional | Required for feeds with multiple agencies defined in the agency.txt file. Each fare attribute must specify an agency_id value to indicate which agency the fare applies to. |
|  transfer_duration | Optional | The **transfer_duration** field specifies the length of time in seconds before a transfer expires.  When used with a **transfers** value of 0, the **transfer_duration** field indicates how long a ticket is valid for a fare where no transfers are allowed. Unless you intend to use this field to indicate ticket validity, **transfer_duration** should be omitted or empty when **transfers** is set to 0. |

### fare_rules.txt

File: **Optional**

The fare_rules table allows you to specify how fares in fare_attributes.txt apply to an itinerary. Most fare structures use some combination of the following rules:

* Fare depends on origin or destination stations.
* Fare depends on which zones the itinerary passes through.
* Fare depends on which route the itinerary uses.

For examples that demonstrate how to specify a fare structure with fare_rules.txt and fare_attributes.txt, see [FareExamples](https://code.google.com/p/googletransitdatafeed/wiki/FareExamples) in the GoogleTransitDataFeed open source project wiki.

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  fare_id | **Required** | The **fare_id** field contains an ID that uniquely identifies a fare class. This value is referenced from the [fare_attributes.txt](#fare_attributestxt) file. |
|  route_id | Optional | The **route_id** field associates the fare ID with a route. Route IDs are referenced from the [routes.txt](#routestxt) file. If you have several routes with the same fare attributes, create a row in fare_rules.txt for each route. |
|   |  | For example, if fare class "b" is valid on route "TSW" and "TSE", the fare_rules.txt file would contain these rows for the fare class: |
|   |  | `b,TSW` |
|   |  | `b,TSE` |
|  origin_id | Optional | The **origin_id** field associates the fare ID with an origin zone ID. Zone IDs are referenced from the [stops.txt](#stopstxt) file. If you have several origin IDs with the same fare attributes, create a row in fare_rules.txt for each origin ID. |
|   |  | For example, if fare class "b" is valid for all travel originating from either zone "2" or zone "8", the fare_rules.txt file would contain these rows for the fare class: |
|   |  | `b, , 2` |
|   |  | `b, , 8` |
|  destination_id | Optional | The **destination_id** field associates the fare ID with a destination zone ID. Zone IDs are referenced from the [stops.txt](#stopstxt) file. If you have several destination IDs with the same fare attributes, create a row in fare_rules.txt for each destination ID. |
|   |  | For example, you could use the origin_ID and destination_ID fields together to specify that fare class "b" is valid for travel between zones 3 and 4, and for travel between zones 3 and 5, the fare_rules.txt file would contain these rows for the fare class: |
|   |  | `b, , 3,4` |
|   |  | `b, , 3,5` |
|  contains_id | Optional | The **contains_id** field associates the fare ID with a zone ID, referenced from the [stops.txt](#stopstxt) file. The fare ID is then associated with itineraries that pass through every contains_id zone. |
|   |  | For example, if fare class "c" is associated with all travel on the GRT route that passes through zones 5, 6, and 7 the fare_rules.txt would contain these rows: |
|   |  | `c,GRT,,,5` |
|   |  | `c,GRT,,,6` |
|   |  | `c,GRT,,,7` |
|   |  | Because all contains_id zones must be matched for the fare to apply, an itinerary that passes through zones 5 and 6 but not zone 7 would not have fare class "c". For more detail, see [FareExamples](https://code.google.com/p/googletransitdatafeed/wiki/FareExamples) in the GoogleTransitDataFeed project wiki. |

### shapes.txt

File: **Optional**

Shapes describe the physical path that a vehicle takes, and are defined in the file shapes.txt. Shapes belong to Trips, and consist of a sequence of points. Tracing the points in order provides the path of the vehicle. The points do not need to match stop locations.

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  shape_id | **Required** | The **shape_id** field contains an ID that uniquely identifies a shape. |
|  shape_pt_lat | **Required** | The **shape_pt_lat** field associates a shape point's latitude with a shape ID. The field value must be a valid WGS 84 latitude. Each row in shapes.txt represents a shape point in your shape definition. |
|   |  | For example, if the shape "A_shp" has three points in its definition, the shapes.txt file might contain these rows to define the shape: |
|   |  | `A_shp,37.61956,-122.48161,0` |
|   |  | `A_shp,37.64430,-122.41070,6` |
|   |  | `A_shp,37.65863,-122.30839,11` |
|  shape_pt_lon | **Required** | The **shape_pt_lon** field associates a shape point's longitude with a shape ID. The field value must be a valid WGS 84 longitude value from -180 to 180. Each row in shapes.txt represents a shape point in your shape definition. |
|   |  | For example, if the shape "A_shp" has three points in its definition, the shapes.txt file might contain these rows to define the shape: |
|   |  | `A_shp,37.61956,-122.48161,0` |
|   |  | `A_shp,37.64430,-122.41070,6` |
|   |  | `A_shp,37.65863,-122.30839,11` |
|  shape_pt_sequence | **Required** | The **shape_pt_sequence** field associates the latitude and longitude of a shape point with its sequence order along the shape. The values for **shape_pt_sequence** must be non-negative integers, and they must increase along the trip. |
|   |  | For example, if the shape "A_shp" has three points in its definition, the shapes.txt file might contain these rows to define the shape: |
|   |  | `A_shp,37.61956,-122.48161,0` |
|   |  | `A_shp,37.64430,-122.41070,6` |
|   |  | `A_shp,37.65863,-122.30839,11` |
|  shape_dist_traveled | Optional | When used in the shapes.txt file, the **shape_dist_traveled** field positions a shape point as a distance traveled along a shape from the first shape point. The **shape_dist_traveled** field represents a real distance traveled along the route in units such as feet or kilometers. This information allows the trip planner to determine how much of the shape to draw when showing part of a trip on the map. The values used for **shape_dist_traveled** must increase along with shape_pt_sequence: they cannot be used to show reverse travel along a route.  |
|   |  | The units used for **shape_dist_traveled** in the shapes.txt file must match the units that are used for this field in the [stop_times.txt](#stop_timestxt) file. |
|   |  | For example, if a bus travels along the three points defined above for A_shp, the additional **shape_dist_traveled** values (shown here in kilometers) would look like this: |
|   |  | `A_shp,37.61956,-122.48161,0,0` |
|   |  | `A_shp,37.64430,-122.41070,6,6.8310` |
|   |  | `A_shp,37.65863,-122.30839,11,15.8765` |

### frequencies.txt

File: **Optional**

This table is intended to represent schedules that don't have a fixed list of stop times. When trips are defined in frequencies.txt, the trip planner ignores the absolute values of the **arrival_time** and **departure_time** fields for those trips in [stop_times.txt](#stop_timestxt). Instead, the **stop_times** table defines the sequence of stops and the time difference between each stop.

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  trip_id | **Required** | The **trip_id** contains an ID that identifies a trip on which the specified frequency of service applies. Trip IDs are referenced from the [trips.txt](#tripstxt) file. |
|  start_time | **Required** | The **start_time** field specifies the time at which service begins with the specified frequency. The time is measured from "noon minus 12h" (effectively midnight, except for days on which daylight savings time changes occur) at the beginning of the service date. For times occurring after midnight, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins. E.g. 25:35:00. |
|  end_time | **Required** | The **end_time** field indicates the time at which service changes to a different frequency (or ceases) at the first stop in the trip. The time is measured from "noon minus 12h" (effectively midnight, except for days on which daylight savings time changes occur) at the beginning of the service date. For times occurring after midnight, enter the time as a value greater than 24:00:00 in HH:MM:SS local time for the day on which the trip schedule begins. E.g. 25:35:00. |
|  headway_secs | **Required** | The **headway_secs** field indicates the time between departures from the same stop (headway) for this trip type, during the time interval specified by **start_time** and **end_time**. The headway value must be entered in seconds. |
|   |  | Periods in which headways are defined (the rows in frequencies.txt) shouldn't overlap for the same trip, since it's hard to determine what should be inferred from two overlapping headways. However, a headway period may begin at the exact same time that another one ends, for instance: |
|   |  | `A, 05:00:00, 07:00:00, 600` |
|   |  | `B, 07:00:00, 12:00:00, 1200` |
|  exact_times | Optional | The **exact_times** field determines if frequency-based trips should be exactly scheduled based on the specified headway information. Valid values for this field are: |
|   |  |* **0** or **(empty)** - Frequency-based trips are not exactly scheduled. This is the default behavior. |
|   |  |* **1** - Frequency-based trips are exactly scheduled. For a frequencies.txt row, trips are scheduled starting with trip_start_time = start_time + x * headway_secs for all x in (0, 1, 2, ...) where trip_start_time < end_time. |
|   |  | The value of **exact_times** must be the same for all frequencies.txt rows with the same **trip_id**. If **exact_times** is 1 and a frequencies.txt row has a **start_time** equal to **end_time**, no trip must be scheduled. When **exact_times** is 1, care must be taken to choose an **end_time** value that is greater than the last desired trip start time but less than the last desired trip start time + **headway_secs**. |

### transfers.txt

File: **Optional**

Trip planners normally calculate transfer points based on the relative proximity of stops in each route. For potentially ambiguous stop pairs, or transfers where you want to specify a particular choice, use transfers.txt to define additional rules for making connections between routes.

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  from_stop_id | **Required** | The **from_stop_id** field contains a stop ID that identifies a stop or station where a connection between routes begins. Stop IDs are referenced from the [stops.txt](#stopstxt) file. If the stop ID refers to a station that contains multiple stops, this transfer rule applies to all stops in that station. |
|  to_stop_id | **Required** | The **to_stop_id** field contains a stop ID that identifies a stop or station where a connection between routes ends. Stop IDs are referenced from the [stops.txt](#stopstxt) file. If the stop ID refers to a station that contains multiple stops, this transfer rule applies to all stops in that station. |
|  transfer_type | **Required** | The **transfer_type** field specifies the type of connection for the specified (from_stop_id, to_stop_id) pair. Valid values for this field are: |
|   |  | * **0** or **(empty)** - This is a recommended transfer point between two routes. |
|   |  | * **1** - This is a timed transfer point between two routes. The departing vehicle is expected to wait for the arriving one, with sufficient time for a passenger to transfer between routes. |
|   |  | * **2** - This transfer requires a minimum amount of time between arrival and departure to ensure a connection. The time required to transfer is specified by **min_transfer_time**. |
|   |  | * **3** - Transfers are not possible between routes at this location. |
|  min_transfer_time | Optional | When a connection between routes requires an amount of time between arrival and departure (transfer_type=2), the **min_transfer_time** field defines the amount of time that must be available in an itinerary to permit a transfer between routes at these stops. The min_transfer_time must be sufficient to permit a typical rider to move between the two stops, including buffer time to allow for schedule variance on each route. |
|   |  | The min_transfer_time value must be entered in seconds, and must be a non-negative integer. |

### feed_info.txt

File: **Optional**

The file contains information about the feed itself, rather than the services that the feed describes. GTFS currently has an [agency.txt](#agencytxt) file to provide information about the agencies that operate the services described by the feed. However, the publisher of the feed is sometimes a different entity than any of the agencies (in the case of regional aggregators). In addition, there are some fields that are really feed-wide settings, rather than agency-wide.

|  Field Name | Required | Details |
|  ------ | ------ | ------ |
|  feed_publisher_name | **Required** | The **feed_publisher_name** field contains the full name of the organization that publishes the feed. (This may be the same as one of the **agency_name** values in [agency.txt](#agencytxt).) GTFS-consuming applications can display this name when giving attribution for a particular feed's data. |
|  feed_publisher_url | **Required** | The **feed_publisher_url** field contains the URL of the feed publishing organization's website. (This may be the same as one of the **agency_url** values in [agency.txt](#agencytxt).) The value must be a fully qualified URL that includes **http**:// or **https**://, and any special characters in the URL must be correctly escaped. See http://www.w3.org/Addressing/URL/4_URI_Recommentations.html for a description of how to create fully qualified URL values. |
|  feed_lang | Required | The **feed_lang** field contains a IETF BCP 47 language code specifying the default language used for the text in this feed. This setting helps GTFS consumers choose capitalization rules and other language-specific settings for the feed. For an introduction to IETF BCP 47, please refer to http://www.rfc-editor.org/rfc/bcp/bcp47.txt and http://www.w3.org/International/articles/language-tags/. |
|  feed_start_date | Optional | The feed provides complete and reliable schedule information for service in the period from the beginning of the **feed_start_date** day to the end of the **feed_end_date** day. Both days are given as dates in YYYYMMDD format as for [calendar.txt](#calendartxt), or left empty if unavailable. The **feed_end_date** date must not precede the **feed_start_date** date if both are given. Feed providers are encouraged to give schedule data outside this period to advise of likely future service, but feed consumers should treat it mindful of its non-authoritative status. If **feed_start_date** or **feed_end_date** extend beyond the active calendar dates defined in [calendar.txt](#calendartxt) and [calendar_dates.txt](#calendar_datestxt), the feed is making an explicit assertion that there is no service for dates within the **feed_start_date** or **feed_end_date** range but not included in the active calendar dates. |
|  feed_end_date | Optional | (see above) |
|  feed_version | Optional | The feed publisher can specify a string here that indicates the current version of their GTFS feed. GTFS-consuming applications can display this value to help feed publishers determine whether the latest version of their feed has been incorporated. |