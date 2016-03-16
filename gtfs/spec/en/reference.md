**Revised February 3, 2016. See [Revision History](changes#RevisionHistory) for
more details.**

This document explains the types of files that comprise a GTFS transit feed and
defines the fields used in all of those files.

## Table of Contents

1.  [Term Definitions](#TermDefinitions)
2.  [Feed Files](#FeedFiles)
3.  [File Requirements](#FileRequirements)
4.  [Field Definitions](#FieldDefinitions)
    -   [agency.txt](#agency_fields)
    -   [stops.txt](#stops_fields)
    -   [routes.txt](#routes_fields)
    -   [trips.txt](#trips_fields)
    -   [stop\_times.txt](#stop_times_fields)
    -   [calendar.txt](#calendar_fields)
    -   [calendar\_dates.txt](#calendar_dates_fields)
    -   [fare\_attributes.txt](#fare_attributes_fields)
    -   [fare\_rules.txt](#fare_rules_fields)
    -   [shapes.txt](#shapes_fields)
    -   [frequencies.txt](#frequencies_fields)
    -   [transfers.txt](#transfers_fields)
    -   [feed\_info.txt](#feed_info_fields)

## Term Definitions

This section defines terms that are used throughout this document.

-   **Field required** - The field column must be included in your feed, and a
    value must be provided for each record. Some required fields permit an empty
    string as a value. To enter an empty string, just omit any text between the
    commas for that field. Note that 0 is interpreted as "a string of value 0",
    and is not an empty string. Please see the field definition for details.
-   **Field optional** - The field column may be omitted from your feed. If you
    choose to include an optional column, each record in your feed must have a
    value for that column. You may include an empty string as a value for
    records that do not have values for the column. Some optional fields permit
    an empty string as a value. To enter an empty string, just omit any text
    between the commas for that field. Note that 0 is interpreted as "a string
    of value 0", and is not an empty string.
-   **Dataset unique** - The field contains a value that maps to a single
    distinct entity within the column. For example, if a route is assigned the
    ID **1A**, then no other route may use that route ID. However, you may
    assign the ID **1A** to a location because locations are a different type of
    entity than routes.

## Feed Files

This specification defines the following files along with their associated
content:

  Filename                                          Required       Defines
  ------------------------------------------------- -------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [agency.txt](#agency_fields)                      **Required**   One or more transit agencies that provide the data in this feed.
  [stops.txt](#stops_fields)                        **Required**   Individual locations where vehicles pick up or drop off passengers.
  [routes.txt](#routes_fields)                      **Required**   Transit routes. A route is a group of trips that are displayed to riders as a single service.
  [trips.txt](#trips_fields)                        **Required**   Trips for each route. A trip is a sequence of two or more stops that occurs at specific time.
  [stop\_times.txt](#stop_times_fields)             **Required**   Times that a vehicle arrives at and departs from individual stops for each trip.
  [calendar.txt](#calendar_fields)                  **Required**   Dates for service IDs using a weekly schedule. Specify when service starts and ends, as well as days of the week where service is available.
  [calendar\_dates.txt](#calendar_dates_fields)     Optional       Exceptions for the service IDs defined in the calendar.txt file. If calendar\_dates.txt includes ALL dates of service, this file may be specified instead of calendar.txt.
  [fare\_attributes.txt](#fare_attributes_fields)   Optional       Fare information for a transit organization's routes.
  [fare\_rules.txt](#fare_rules_fields)             Optional       Rules for applying fare information for a transit organization's routes.
  [shapes.txt](#shapes_fields)                      Optional       Rules for drawing lines on a map to represent a transit organization's routes.
  [frequencies.txt](#frequencies_fields)            Optional       Headway (time between trips) for routes with variable frequency of service.
  [transfers.txt](#transfers_fields)                Optional       Rules for making connections at transfer points between routes.
  [feed\_info.txt](#feed_info_fields)               Optional       Additional information about the feed itself, including publisher, version, and expiration information.

## File Requirements

The following requirements apply to the format and contents of your files:

-   All files in a General Transit Feed Spec (GTFS) feed must be saved as
    comma-delimited text.
-   The first line of each file must contain field names. Each subsection of the
    [Field Definitions](#FieldDefinitions) section corresponds to one of the
    files in a transit feed and lists the field names you may use in that file.
-   All field names are case-sensitive.
-   Field values may not contain tabs, carriage returns or new lines.
-   Field values that contain quotation marks or commas must be enclosed within
    quotation marks. In addition, each quotation mark in the field value must be
    preceded with a quotation mark. This is consistent with the manner in which
    Microsoft Excel outputs comma-delimited (CSV) files. For more information on
    the CSV file format, see
    [http://tools.ietf.org/html/rfc4180](http://tools.ietf.org/html/rfc4180).\
     The following example demonstrates how a field value would appear in a
    comma-delimited file:
    -   **Original field value:** `Contains         "quotes", commas and text`
    -   **Field value in CSV
        file:**` "Contains         ""quotes"", commas and text"`
-   Field values must not contain HTML tags, comments or escape sequences.
-   Remove any extra spaces between fields or field names. Many parsers consider
    the spaces to be part of the value, which may cause errors.
-   Each line must end with a CRLF or LF linebreak character.
-   Files should be encoded in UTF-8 to support all Unicode characters. Files
    that include the Unicode byte-order mark (BOM) character are acceptable.
    Please see the [Unicode FAQ](http://unicode.org/faq/utf_bom.html#BOM) for
    more information on the BOM character and UTF-8.
-   Zip the files in your feed.

## Field Definitions

## agency.txt {.first"}

File: **Required**

+----------------------------+----------------------------+----------------------------+
| Field Name                 | **Required**               | Details                    |
+============================+============================+============================+
| agency\_id                 | Optional                   | The **agency\_id** field   |
|                            |                            | is an ID that uniquely     |
|                            |                            | identifies a transit       |
|                            |                            | agency. A transit feed may |
|                            |                            | represent data from more   |
|                            |                            | than one agency. The       |
|                            |                            | **agency\_id** is dataset  |
|                            |                            | unique. This field is      |
|                            |                            | optional for transit feeds |
|                            |                            | that only contain data for |
|                            |                            | a single agency.           |
+----------------------------+----------------------------+----------------------------+
| agency\_name               | **Required**               | The **agency\_name** field |
|                            |                            | contains the full name of  |
|                            |                            | the transit agency. Google |
|                            |                            | Maps will display this     |
|                            |                            | name.                      |
+----------------------------+----------------------------+----------------------------+
| agency\_url                | **Required**               | The **agency\_url** field  |
|                            |                            | contains the URL of the    |
|                            |                            | transit agency. The value  |
|                            |                            | must be a fully qualified  |
|                            |                            | URL that includes          |
|                            |                            | **http://** or             |
|                            |                            | **https://**, and any      |
|                            |                            | special characters in the  |
|                            |                            | URL must be correctly      |
|                            |                            | escaped. See               |
|                            |                            | [http://www.w3.org/Address |
|                            |                            | ing/URL/4\_URI\_Recommenta |
|                            |                            | tions.html](http://www.w3. |
|                            |                            | org/Addressing/URL/4_URI_R |
|                            |                            | ecommentations.html)       |
|                            |                            | for a description of how   |
|                            |                            | to create fully qualified  |
|                            |                            | URL values.                |
+----------------------------+----------------------------+----------------------------+
| agency\_timezone           | **Required**               | The **agency\_timezone**   |
|                            |                            | field contains the         |
|                            |                            | timezone where the transit |
|                            |                            | agency is located.         |
|                            |                            | Timezone names never       |
|                            |                            | contain the space          |
|                            |                            | character but may contain  |
|                            |                            | an underscore. Please      |
|                            |                            | refer to                   |
|                            |                            | [http://en.wikipedia.org/w |
|                            |                            | iki/List\_of\_tz\_zones](h |
|                            |                            | ttp://en.wikipedia.org/wik |
|                            |                            | i/List_of_tz_zones)        |
|                            |                            | for a list of valid        |
|                            |                            | values. If multiple        |
|                            |                            | agencies are specified in  |
|                            |                            | the feed, each must have   |
|                            |                            | the same                   |
|                            |                            | **agency\_timezone**.      |
+----------------------------+----------------------------+----------------------------+
| agency\_lang               | Optional                   | The **agency\_lang** field |
|                            |                            | contains a two-letter ISO  |
|                            |                            | 639-1 code for the primary |
|                            |                            | language used by this      |
|                            |                            | transit agency. The        |
|                            |                            | language code is           |
|                            |                            | case-insensitive (both en  |
|                            |                            | and EN are accepted). This |
|                            |                            | setting defines            |
|                            |                            | capitalization rules and   |
|                            |                            | other language-specific    |
|                            |                            | settings for all text      |
|                            |                            | contained in this transit  |
|                            |                            | agency's feed. Please      |
|                            |                            | refer to                   |
|                            |                            | [http://www.loc.gov/standa |
|                            |                            | rds/iso639-2/php/code\_lis |
|                            |                            | t.php](http://www.loc.gov/ |
|                            |                            | standards/iso639-2/php/cod |
|                            |                            | e_list.php "the ISO 639-2  |
|                            |                            | code                       |
|                            |                            |           list") for a     |
|                            |                            | list of valid values.      |
+----------------------------+----------------------------+----------------------------+
| agency\_phone              | Optional                   | The **agency\_phone**      |
|                            |                            | field contains a single    |
|                            |                            | voice telephone number for |
|                            |                            | the specified agency. This |
|                            |                            | field is a string value    |
|                            |                            | that presents the          |
|                            |                            | telephone number as        |
|                            |                            | typical for the agency's   |
|                            |                            | service area. It can and   |
|                            |                            | should contain punctuation |
|                            |                            | marks to group the digits  |
|                            |                            | of the number. Dialable    |
|                            |                            | text (for example,         |
|                            |                            | TriMet's "503-238-RIDE")   |
|                            |                            | is permitted, but the      |
|                            |                            | field must not contain any |
|                            |                            | other descriptive text.    |
+----------------------------+----------------------------+----------------------------+
| agency\_fare\_url          | Optional                   | The **agency\_fare\_url**  |
|                            |                            | specifies the URL of a web |
|                            |                            | page that allows a rider   |
|                            |                            | to purchase tickets or     |
|                            |                            | other fare instruments for |
|                            |                            | that agency online. The    |
|                            |                            | value must be a fully      |
|                            |                            | qualified URL that         |
|                            |                            | includes **http://** or    |
|                            |                            | **https://**, and any      |
|                            |                            | special characters in the  |
|                            |                            | URL must be correctly      |
|                            |                            | escaped. See               |
|                            |                            | [http://www.w3.org/Address |
|                            |                            | ing/URL/4\_URI\_Recommenta |
|                            |                            | tions.html](http://www.w3. |
|                            |                            | org/Addressing/URL/4_URI_R |
|                            |                            | ecommentations.html)       |
|                            |                            | for a description of how   |
|                            |                            | to create fully qualified  |
|                            |                            | URL values.                |
+----------------------------+----------------------------+----------------------------+
| agency\_email              | Optional                   | The **agency\_email**      |
|                            |                            | field contains a single    |
|                            |                            | valid email address        |
|                            |                            | actively monitored by the  |
|                            |                            | agency’s customer service  |
|                            |                            | department. This email     |
|                            |                            | address will be considered |
|                            |                            | a direct contact point     |
|                            |                            | where transit riders can   |
|                            |                            | reach a customer service   |
|                            |                            | representative at the      |
|                            |                            | agency.                    |
+----------------------------+----------------------------+----------------------------+

## stops.txt

File: Required

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| stop\_id                   | **Required**               | The **stop\_id** field     |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a stop |
|                            |                            | or station. Multiple       |
|                            |                            | routes may use the same    |
|                            |                            | stop. The **stop\_id** is  |
|                            |                            | dataset unique.            |
+----------------------------+----------------------------+----------------------------+
| stop\_code                 | Optional                   | The **stop\_code** field   |
|                            |                            | contains short text or a   |
|                            |                            | number that uniquely       |
|                            |                            | identifies the stop for    |
|                            |                            | passengers. Stop codes are |
|                            |                            | often used in phone-based  |
|                            |                            | transit information        |
|                            |                            | systems or printed on stop |
|                            |                            | signage to make it easier  |
|                            |                            | for riders to get a stop   |
|                            |                            | schedule or real-time      |
|                            |                            | arrival information for a  |
|                            |                            | particular stop.           |
|                            |                            |                            |
|                            |                            | The stop\_code field       |
|                            |                            | should only be used for    |
|                            |                            | stop codes that are        |
|                            |                            | displayed to passengers.   |
|                            |                            | For internal codes, use    |
|                            |                            | **stop\_id**. This field   |
|                            |                            | should be left blank for   |
|                            |                            | stops without a code.      |
+----------------------------+----------------------------+----------------------------+
| stop\_name                 | **Required**               | The **stop\_name** field   |
|                            |                            | contains the name of a     |
|                            |                            | stop or station. Please    |
|                            |                            | use a name that people     |
|                            |                            | will understand in the     |
|                            |                            | local and tourist          |
|                            |                            | vernacular.                |
+----------------------------+----------------------------+----------------------------+
| stop\_desc                 | Optional                   | The **stop\_desc** field   |
|                            |                            | contains a description of  |
|                            |                            | a stop. Please provide     |
|                            |                            | useful, quality            |
|                            |                            | information. Do not simply |
|                            |                            | duplicate the name of the  |
|                            |                            | stop.                      |
+----------------------------+----------------------------+----------------------------+
| stop\_lat                  | **Required**               | The **stop\_lat** field    |
|                            |                            | contains the latitude of a |
|                            |                            | stop or station. The field |
|                            |                            | value must be a valid WGS  |
|                            |                            | 84 latitude.               |
+----------------------------+----------------------------+----------------------------+
| stop\_lon                  | **Required**               | The **stop\_lon** field    |
|                            |                            | contains the longitude of  |
|                            |                            | a stop or station. The     |
|                            |                            | field value must be a      |
|                            |                            | valid WGS 84 longitude     |
|                            |                            | value from -180 to 180.    |
+----------------------------+----------------------------+----------------------------+
| zone\_id                   | Optional                   | The **zone\_id** field     |
|                            |                            | defines the fare zone for  |
|                            |                            | a stop ID. Zone IDs are    |
|                            |                            | required if you want to    |
|                            |                            | provide fare information   |
|                            |                            | using                      |
|                            |                            | [fare\_rules.txt](#fare_ru |
|                            |                            | les_fields).               |
|                            |                            | If this stop ID represents |
|                            |                            | a station, the zone ID is  |
|                            |                            | ignored.                   |
+----------------------------+----------------------------+----------------------------+
| stop\_url                  | Optional                   | The **stop\_url** field    |
|                            |                            | contains the URL of a web  |
|                            |                            | page about a particular    |
|                            |                            | stop. This should be       |
|                            |                            | different from the         |
|                            |                            | **agency\_url**and the     |
|                            |                            | **route\_url** fields.     |
|                            |                            |                            |
|                            |                            | The value must be a fully  |
|                            |                            | qualified URL that         |
|                            |                            | includes **http://** or    |
|                            |                            | **https://**, and any      |
|                            |                            | special characters in the  |
|                            |                            | URL must be correctly      |
|                            |                            | escaped. See               |
|                            |                            | [http://www.w3.org/Address |
|                            |                            | ing/URL/4\_URI\_Recommenta |
|                            |                            | tions.html](http://www.w3. |
|                            |                            | org/Addressing/URL/4_URI_R |
|                            |                            | ecommentations.html)       |
|                            |                            | for a description of how   |
|                            |                            | to create fully qualified  |
|                            |                            | URL values.                |
+----------------------------+----------------------------+----------------------------+
| location\_type             | Optional                   | The                        |
|                            |                            | **location\_type**field    |
|                            |                            | identifies whether this    |
|                            |                            | stop ID represents a stop  |
|                            |                            | or station. If no location |
|                            |                            | type is specified, or the  |
|                            |                            | location\_type is blank,   |
|                            |                            | stop IDs are treated as    |
|                            |                            | stops. Stations may have   |
|                            |                            | different properties from  |
|                            |                            | stops when they are        |
|                            |                            | represented on a map or    |
|                            |                            | used in trip planning.     |
|                            |                            |                            |
|                            |                            | The location type field    |
|                            |                            | can have the following     |
|                            |                            | values:                    |
|                            |                            |                            |
|                            |                            | -   **0** or blank - Stop. |
|                            |                            |     A location where       |
|                            |                            |     passengers board or    |
|                            |                            |     disembark from a       |
|                            |                            |     transit vehicle.       |
|                            |                            | -   **1** - Station. A     |
|                            |                            |     physical structure or  |
|                            |                            |     area that contains one |
|                            |                            |     or more stop.          |
+----------------------------+----------------------------+----------------------------+
| parent\_station            | Optional                   | For stops that are         |
|                            |                            | physically located inside  |
|                            |                            | stations, the              |
|                            |                            | **parent\_station** field  |
|                            |                            | identifies the station     |
|                            |                            | associated with the stop.  |
|                            |                            | To use this field,         |
|                            |                            | stops.txt must also        |
|                            |                            | contain a row where this   |
|                            |                            | stop ID is assigned        |
|                            |                            | location type=1.           |
|                            |                            |                            |
|                            |                            |   This stop ID represents. |
|                            |                            | ..          This entry's l |
|                            |                            | ocation type...   This ent |
|                            |                            | ry's parent\_station field |
|                            |                            |  contains...               |
|                            |                            |   ------------------------ |
|                            |                            | ----------- -------------- |
|                            |                            | ----------------- -------- |
|                            |                            | -------------------------- |
|                            |                            | -------------------------- |
|                            |                            | -------------------------- |
|                            |                            | -------------------------- |
|                            |                            | -----------                |
|                            |                            |   A stop located inside a  |
|                            |                            | station.    0 or blank     |
|                            |                            |                   The stop |
|                            |                            |  ID of the station where t |
|                            |                            | his stop is located. The s |
|                            |                            | top referenced by parent\_ |
|                            |                            | station must have location |
|                            |                            | \_type=1.                  |
|                            |                            |   A stop located outside a |
|                            |                            |  station.   0 or blank     |
|                            |                            |                   A blank  |
|                            |                            | value. The parent\_station |
|                            |                            |  field doesn't apply to th |
|                            |                            | is stop.                   |
|                            |                            |   A station.               |
|                            |                            |             1              |
|                            |                            |                   A blank  |
|                            |                            | value. Stations can't cont |
|                            |                            | ain other stations.        |
+----------------------------+----------------------------+----------------------------+
| stop\_timezone             | Optional                   | The **stop\_timezone**     |
|                            |                            | field contains the         |
|                            |                            | timezone in which this     |
|                            |                            | stop or station is         |
|                            |                            | located. Please refer to   |
|                            |                            | [Wikipedia List of         |
|                            |                            | Timezones](http://en.wikip |
|                            |                            | edia.org/wiki/List_of_tz_z |
|                            |                            | ones)                      |
|                            |                            | for a list of valid        |
|                            |                            | values. If omitted, the    |
|                            |                            | stop should be assumed to  |
|                            |                            | be located in the timezone |
|                            |                            | specified by               |
|                            |                            | [agency\_timezone](#agency |
|                            |                            | _agency_timezone_field)    |
|                            |                            | in agency.txt.             |
|                            |                            |                            |
|                            |                            | When a stop has a parent   |
|                            |                            | station, the stop is       |
|                            |                            | considered to be in the    |
|                            |                            | timezone specified by the  |
|                            |                            | parent station's           |
|                            |                            | **stop\_timezone** value.  |
|                            |                            | If the parent has no       |
|                            |                            | **stop\_timezone** value,  |
|                            |                            | the stops that belong to   |
|                            |                            | that station are assumed   |
|                            |                            | to be in the timezone      |
|                            |                            | specified by               |
|                            |                            | **agency\_timezone**, even |
|                            |                            | if the stops have their    |
|                            |                            | own **stop\_timezone**     |
|                            |                            | values. In other words, if |
|                            |                            | a given stop has a         |
|                            |                            | **parent\_station** value, |
|                            |                            | any **stop\_timezone**     |
|                            |                            | value specified for that   |
|                            |                            | stop must be ignored.      |
|                            |                            |                            |
|                            |                            | Even if **stop\_timezone** |
|                            |                            | values are provided in     |
|                            |                            | stops.txt, the times in    |
|                            |                            | stop\_times.txt should     |
|                            |                            | continue to be specified   |
|                            |                            | as time since midnight in  |
|                            |                            | the timezone specified by  |
|                            |                            | **agency\_timezone** in    |
|                            |                            | agency.txt. This ensures   |
|                            |                            | that the time values in a  |
|                            |                            | trip always increase over  |
|                            |                            | the course of a trip,      |
|                            |                            | regardless of which        |
|                            |                            | timezones the trip         |
|                            |                            | crosses.                   |
+----------------------------+----------------------------+----------------------------+
| wheelchair\_boarding       | Optional                   | The                        |
|                            |                            | **wheelchair\_boarding**   |
|                            |                            | field identifies whether   |
|                            |                            | wheelchair boardings are   |
|                            |                            | possible from the          |
|                            |                            | specified stop or station. |
|                            |                            | The field can have the     |
|                            |                            | following values:          |
|                            |                            |                            |
|                            |                            | -   **0** (or empty) -     |
|                            |                            |     indicates that there   |
|                            |                            |     is no accessibility    |
|                            |                            |     information for the    |
|                            |                            |     stop                   |
|                            |                            | -   **1** - indicates that |
|                            |                            |     at least some vehicles |
|                            |                            |     at this stop can be    |
|                            |                            |     boarded by a rider in  |
|                            |                            |     a wheelchair           |
|                            |                            | -   **2** - wheelchair     |
|                            |                            |     boarding is not        |
|                            |                            |     possible at this stop  |
|                            |                            |                            |
|                            |                            | When a stop is part of a   |
|                            |                            | larger station complex, as |
|                            |                            | indicated by a stop with a |
|                            |                            | **parent\_station** value, |
|                            |                            | the stop's                 |
|                            |                            | **wheelchair\_boarding**   |
|                            |                            | field has the following    |
|                            |                            | additional semantics:      |
|                            |                            |                            |
|                            |                            | -   **0** (or empty) - the |
|                            |                            |     stop will inherit its  |
|                            |                            |     **wheelchair\_boarding |
|                            |                            | **                         |
|                            |                            |     value from the parent  |
|                            |                            |     station, if specified  |
|                            |                            |     in the parent          |
|                            |                            | -   **1** - there exists   |
|                            |                            |     some accessible path   |
|                            |                            |     from outside the       |
|                            |                            |     station to the         |
|                            |                            |     specific stop /        |
|                            |                            |     platform               |
|                            |                            | -   **2** - there exists   |
|                            |                            |     no accessible path     |
|                            |                            |     from outside the       |
|                            |                            |     station to the         |
|                            |                            |     specific stop /        |
|                            |                            |     platform               |
+----------------------------+----------------------------+----------------------------+

## routes.txt

File: Required

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| route\_id                  | **Required**               | The **route\_id** field    |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a      |
|                            |                            | route. The **route\_id**   |
|                            |                            | is dataset unique.         |
+----------------------------+----------------------------+----------------------------+
| agency\_id                 | Optional                   | The **agency\_id** field   |
|                            |                            | defines an agency for the  |
|                            |                            | specified route. This      |
|                            |                            | value is referenced from   |
|                            |                            | the                        |
|                            |                            | [agency.txt](#agency_field |
|                            |                            | s)                         |
|                            |                            | file. Use this field when  |
|                            |                            | you are providing data for |
|                            |                            | routes from more than one  |
|                            |                            | agency.                    |
+----------------------------+----------------------------+----------------------------+
| route\_short\_name         | **Required**               | The **route\_short\_name** |
|                            |                            | contains the short name of |
|                            |                            | a route. This will often   |
|                            |                            | be a short, abstract       |
|                            |                            | identifier like "32",      |
|                            |                            | "100X", or "Green" that    |
|                            |                            | riders use to identify a   |
|                            |                            | route, but which doesn't   |
|                            |                            | give any indication of     |
|                            |                            | what places the route      |
|                            |                            | serves. At least one of    |
|                            |                            | **route\_short\_name** or  |
|                            |                            | **route\_long\_name** must |
|                            |                            | be specified, or           |
|                            |                            | potentially both if        |
|                            |                            | appropriate. If the route  |
|                            |                            | does not have a short      |
|                            |                            | name, please specify a     |
|                            |                            | **route\_long\_name** and  |
|                            |                            | use an empty string as the |
|                            |                            | value for this field.      |
+----------------------------+----------------------------+----------------------------+
| route\_long\_name          | **Required**               | The **route\_long\_name**  |
|                            |                            | contains the full name of  |
|                            |                            | a route. This name is      |
|                            |                            | generally more descriptive |
|                            |                            | than the                   |
|                            |                            | **route\_short\_name** and |
|                            |                            | will often include the     |
|                            |                            | route's destination or     |
|                            |                            | stop. At least one of      |
|                            |                            | **route\_short\_name** or  |
|                            |                            | **route\_long\_name** must |
|                            |                            | be specified, or           |
|                            |                            | potentially both if        |
|                            |                            | appropriate. If the route  |
|                            |                            | does not have a long name, |
|                            |                            | please specify a           |
|                            |                            | **route\_short\_name** and |
|                            |                            | use an empty string as the |
|                            |                            | value for this field.      |
+----------------------------+----------------------------+----------------------------+
| route\_desc                | Optional                   | The **route\_desc** field  |
|                            |                            | contains a description of  |
|                            |                            | a route. Please provide    |
|                            |                            | useful, quality            |
|                            |                            | information. Do not simply |
|                            |                            | duplicate the name of the  |
|                            |                            | route. For example, "A     |
|                            |                            | trains operate between     |
|                            |                            | Inwood-207 St, Manhattan   |
|                            |                            | and Far Rockaway-Mott      |
|                            |                            | Avenue, Queens at all      |
|                            |                            | times. Also from about 6AM |
|                            |                            | until about midnight,      |
|                            |                            | additional A trains        |
|                            |                            | operate between Inwood-207 |
|                            |                            | St and Lefferts Boulevard  |
|                            |                            | (trains typically          |
|                            |                            | alternate between Lefferts |
|                            |                            | Blvd and Far Rockaway)."   |
+----------------------------+----------------------------+----------------------------+
| route\_type                | **Required**               | The **route\_type** field  |
|                            |                            | describes the type of      |
|                            |                            | transportation used on a   |
|                            |                            | route. Valid values for    |
|                            |                            | this field are:            |
|                            |                            |                            |
|                            |                            | -   **0** - Tram,          |
|                            |                            |     Streetcar, Light rail. |
|                            |                            |     Any light rail or      |
|                            |                            |     street level system    |
|                            |                            |     within a metropolitan  |
|                            |                            |     area.                  |
|                            |                            | -   **1** - Subway, Metro. |
|                            |                            |     Any underground rail   |
|                            |                            |     system within a        |
|                            |                            |     metropolitan area.     |
|                            |                            | -   **2** - Rail. Used for |
|                            |                            |     intercity or           |
|                            |                            |     long-distance travel.  |
|                            |                            | -   **3** - Bus. Used for  |
|                            |                            |     short- and             |
|                            |                            |     long-distance bus      |
|                            |                            |     routes.                |
|                            |                            | -   **4** - Ferry. Used    |
|                            |                            |     for short- and         |
|                            |                            |     long-distance boat     |
|                            |                            |     service.               |
|                            |                            | -   **5** - Cable car.     |
|                            |                            |     Used for street-level  |
|                            |                            |     cable cars where the   |
|                            |                            |     cable runs beneath the |
|                            |                            |     car.                   |
|                            |                            | -   **6** - Gondola,       |
|                            |                            |     Suspended cable car.   |
|                            |                            |     Typically used for     |
|                            |                            |     aerial cable cars      |
|                            |                            |     where the car is       |
|                            |                            |     suspended from the     |
|                            |                            |     cable.                 |
|                            |                            | -   **7** - Funicular. Any |
|                            |                            |     rail system designed   |
|                            |                            |     for steep inclines.    |
+----------------------------+----------------------------+----------------------------+
| route\_url                 | Optional                   | The **route\_url** field   |
|                            |                            | contains the URL of a web  |
|                            |                            | page about that particular |
|                            |                            | route. This should be      |
|                            |                            | different from the         |
|                            |                            | **agency\_url**.\          |
|                            |                            |  \                         |
|                            |                            |  The value must be a fully |
|                            |                            | qualified URL that         |
|                            |                            | includes **http://** or    |
|                            |                            | **https://**, and any      |
|                            |                            | special characters in the  |
|                            |                            | URL must be correctly      |
|                            |                            | escaped. See               |
|                            |                            | [http://www.w3.org/Address |
|                            |                            | ing/URL/4\_URI\_Recommenta |
|                            |                            | tions.html](http://www.w3. |
|                            |                            | org/Addressing/URL/4_URI_R |
|                            |                            | ecommentations.html)       |
|                            |                            | for a description of how   |
|                            |                            | to create fully qualified  |
|                            |                            | URL values.                |
+----------------------------+----------------------------+----------------------------+
| route\_color               | Optional                   | In systems that have       |
|                            |                            | colors assigned to routes, |
|                            |                            | the **route\_color** field |
|                            |                            | defines a color that       |
|                            |                            | corresponds to a route.    |
|                            |                            | The color must be provided |
|                            |                            | as a six-character         |
|                            |                            | hexadecimal number, for    |
|                            |                            | example, 00FFFF. If no     |
|                            |                            | color is specified, the    |
|                            |                            | default route color is     |
|                            |                            | white (FFFFFF).            |
|                            |                            |                            |
|                            |                            | The color difference       |
|                            |                            | between **route\_color**   |
|                            |                            | and **route\_text\_color** |
|                            |                            | should provide sufficient  |
|                            |                            | contrast when viewed on a  |
|                            |                            | black and white screen.    |
|                            |                            | The [W3C Techniques for    |
|                            |                            | Accessibility Evaluation   |
|                            |                            | And Repair Tools           |
|                            |                            | document](http://www.w3.or |
|                            |                            | g/TR/AERT#color-contrast)  |
|                            |                            | offers a useful algorithm  |
|                            |                            | for evaluating color       |
|                            |                            | contrast. There are also   |
|                            |                            | helpful online tools for   |
|                            |                            | choosing contrasting       |
|                            |                            | colors, including the      |
|                            |                            | [snook.ca Color Contrast   |
|                            |                            | Check                      |
|                            |                            | application](http://snook. |
|                            |                            | ca/technical/colour_contra |
|                            |                            | st/colour.html).           |
+----------------------------+----------------------------+----------------------------+
| route\_text\_color         | Optional                   | The **route\_text\_color** |
|                            |                            | field can be used to       |
|                            |                            | specify a legible color to |
|                            |                            | use for text drawn against |
|                            |                            | a background of            |
|                            |                            | **route\_color**. The      |
|                            |                            | color must be provided as  |
|                            |                            | a six-character            |
|                            |                            | hexadecimal number, for    |
|                            |                            | example, FFD700. If no     |
|                            |                            | color is specified, the    |
|                            |                            | default text color is      |
|                            |                            | black (000000).            |
|                            |                            |                            |
|                            |                            | The color difference       |
|                            |                            | between **route\_color**   |
|                            |                            | and **route\_text\_color** |
|                            |                            | should provide sufficient  |
|                            |                            | contrast when viewed on a  |
|                            |                            | black and white screen.    |
+----------------------------+----------------------------+----------------------------+

## trips.txt

File: Required

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| route\_id                  | **Required**               | The **route\_id** field    |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a      |
|                            |                            | route. This value is       |
|                            |                            | referenced from the        |
|                            |                            | [routes.txt](#routes_field |
|                            |                            | s)                         |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| service\_id                | **Required**               | The **service\_id**        |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a set  |
|                            |                            | of dates when service is   |
|                            |                            | available for one or more  |
|                            |                            | routes. This value is      |
|                            |                            | referenced from the        |
|                            |                            | [calendar.txt](#calendar_f |
|                            |                            | ields)                     |
|                            |                            | or                         |
|                            |                            | [calendar\_dates.txt](#cal |
|                            |                            | endar_dates_fields)        |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| trip\_id                   | **Required**               | The **trip\_id** field     |
|                            |                            | contains an ID that        |
|                            |                            | identifies a trip. The     |
|                            |                            | **trip\_id** is dataset    |
|                            |                            | unique.                    |
+----------------------------+----------------------------+----------------------------+
| trip\_headsign             | Optional                   | The **trip\_headsign**     |
|                            |                            | field contains the text    |
|                            |                            | that appears on a sign     |
|                            |                            | that identifies the trip's |
|                            |                            | destination to passengers. |
|                            |                            | Use this field to          |
|                            |                            | distinguish between        |
|                            |                            | different patterns of      |
|                            |                            | service in the same route. |
|                            |                            | If the headsign changes    |
|                            |                            | during a trip, you can     |
|                            |                            | override the               |
|                            |                            | **trip\_headsign** by      |
|                            |                            | specifying values for the  |
|                            |                            | the                        |
|                            |                            | [stop\_headsign](#stop_tim |
|                            |                            | es_stop_headsign_field)    |
|                            |                            | field in                   |
|                            |                            | [stop\_times.txt](#stop_ti |
|                            |                            | mes_fields).               |
+----------------------------+----------------------------+----------------------------+
| trip\_short\_name          | Optional                   | The **trip\_short\_name**  |
|                            |                            | field contains the text    |
|                            |                            | that appears in schedules  |
|                            |                            | and sign boards to         |
|                            |                            | identify the trip to       |
|                            |                            | passengers, for example,   |
|                            |                            | to identify train numbers  |
|                            |                            | for commuter rail trips.   |
|                            |                            | If riders do not commonly  |
|                            |                            | rely on trip names, please |
|                            |                            | leave this field blank.    |
|                            |                            |                            |
|                            |                            | A **trip\_short\_name**    |
|                            |                            | value, if provided, should |
|                            |                            | uniquely identify a trip   |
|                            |                            | within a service day; it   |
|                            |                            | should not be used for     |
|                            |                            | destination names or       |
|                            |                            | limited/express            |
|                            |                            | designations.              |
+----------------------------+----------------------------+----------------------------+
| direction\_id              | Optional                   | The **direction\_id**      |
|                            |                            | field contains a binary    |
|                            |                            | value that indicates the   |
|                            |                            | direction of travel for a  |
|                            |                            | trip. Use this field to    |
|                            |                            | distinguish between        |
|                            |                            | bi-directional trips with  |
|                            |                            | the same                   |
|                            |                            | [route\_id](#trips_route_i |
|                            |                            | d_field).                  |
|                            |                            | This field is not used in  |
|                            |                            | routing; it provides a way |
|                            |                            | to separate trips by       |
|                            |                            | direction when publishing  |
|                            |                            | time tables. You can       |
|                            |                            | specify names for each     |
|                            |                            | direction with             |
|                            |                            | the**trip\_headsign**      |
|                            |                            | field.                     |
|                            |                            |                            |
|                            |                            | -   **0** - travel in one  |
|                            |                            |     direction (e.g.        |
|                            |                            |     outbound travel)       |
|                            |                            | -   **1** - travel in the  |
|                            |                            |     opposite direction     |
|                            |                            |     (e.g. inbound travel)  |
|                            |                            |                            |
|                            |                            | For example, you could use |
|                            |                            | the trip\_headsign and     |
|                            |                            | direction\_id fields       |
|                            |                            | together to assign a name  |
|                            |                            | to travel in each          |
|                            |                            | direction for a set of     |
|                            |                            | trips. A trips.txt file    |
|                            |                            | could contain these rows   |
|                            |                            | for use in time tables:    |
|                            |                            |                            |
|                            |                            | `trip_id,...,trip_headsign |
|                            |                            | ,direction_id 1234,...,to  |
|                            |                            | Airport,0 1505,...,to Down |
|                            |                            | town,1`                    |
+----------------------------+----------------------------+----------------------------+
| block\_id                  | Optional                   | The **block\_id** field    |
|                            |                            | identifies the block to    |
|                            |                            | which the trip belongs. A  |
|                            |                            | block consists of two or   |
|                            |                            | more sequential trips made |
|                            |                            | using the same vehicle,    |
|                            |                            | where a passenger can      |
|                            |                            | transfer from one trip to  |
|                            |                            | the next just by staying   |
|                            |                            | in the vehicle. The        |
|                            |                            | **block\_id** must be      |
|                            |                            | referenced by two or more  |
|                            |                            | trips in trips.txt.        |
+----------------------------+----------------------------+----------------------------+
| shape\_id                  | Optional                   | The **shape\_id** field    |
|                            |                            | contains an ID that        |
|                            |                            | defines a shape for the    |
|                            |                            | trip. This value is        |
|                            |                            | referenced from the        |
|                            |                            | [shapes.txt](#shapes_field |
|                            |                            | s)                         |
|                            |                            | file. The shapes.txt file  |
|                            |                            | allows you to define how a |
|                            |                            | line should be drawn on    |
|                            |                            | the map to represent a     |
|                            |                            | trip.                      |
+----------------------------+----------------------------+----------------------------+
| wheelchair\_accessible     | Optional                   | -   **0** (or empty) -     |
|                            |                            |     indicates that there   |
|                            |                            |     is no accessibility    |
|                            |                            |     information for the    |
|                            |                            |     trip                   |
|                            |                            | -   **1** - indicates that |
|                            |                            |     the vehicle being used |
|                            |                            |     on this particular     |
|                            |                            |     trip can accommodate   |
|                            |                            |     at least one rider in  |
|                            |                            |     a wheelchair           |
|                            |                            | -   **2** - indicates that |
|                            |                            |     no riders in           |
|                            |                            |     wheelchairs can be     |
|                            |                            |     accommodated on this   |
|                            |                            |     trip                   |
+----------------------------+----------------------------+----------------------------+
| bikes\_allowed             | Optional                   | -   **0** (or empty) -     |
|                            |                            |     indicates that there   |
|                            |                            |     is no bike information |
|                            |                            |     for the trip           |
|                            |                            | -   **1** - indicates that |
|                            |                            |     the vehicle being used |
|                            |                            |     on this particular     |
|                            |                            |     trip can accommodate   |
|                            |                            |     at least one bicycle   |
|                            |                            | -   **2** - indicates that |
|                            |                            |     no bicycles are        |
|                            |                            |     allowed on this trip   |
+----------------------------+----------------------------+----------------------------+

## stop\_times.txt

File: Required

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| trip\_id                   | **Required**               | The **trip\_id** field     |
|                            |                            | contains an ID that        |
|                            |                            | identifies a trip. This    |
|                            |                            | value is referenced from   |
|                            |                            | the                        |
|                            |                            | [trips.txt](#trips_fields) |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| arrival\_time              | **Required**               | The **arrival\_time**      |
|                            |                            | specifies the arrival time |
|                            |                            | at a specific stop for a   |
|                            |                            | specific trip on a route.  |
|                            |                            | The time is measured from  |
|                            |                            | "noon minus 12h"           |
|                            |                            | (effectively midnight,     |
|                            |                            | except for days on which   |
|                            |                            | daylight savings time      |
|                            |                            | changes occur) at the      |
|                            |                            | beginning of the service   |
|                            |                            | date. For times occurring  |
|                            |                            | after midnight on the      |
|                            |                            | service date, enter the    |
|                            |                            | time as a value greater    |
|                            |                            | than 24:00:00 in HH:MM:SS  |
|                            |                            | local time for the day on  |
|                            |                            | which the trip schedule    |
|                            |                            | begins. If you don't have  |
|                            |                            | separate times for arrival |
|                            |                            | and departure at a stop,   |
|                            |                            | enter the same value for   |
|                            |                            | **arrival\_time** and      |
|                            |                            | **departure\_time**.       |
|                            |                            |                            |
|                            |                            | If this stop isn't a time  |
|                            |                            | point, use an empty string |
|                            |                            | value for the              |
|                            |                            | **arrival\_time** and      |
|                            |                            | **departure\_time**        |
|                            |                            | fields. Stops without      |
|                            |                            | arrival times will be      |
|                            |                            | scheduled based on the     |
|                            |                            | nearest preceding timed    |
|                            |                            | stop. To ensure accurate   |
|                            |                            | routing, please provide    |
|                            |                            | arrival and departure      |
|                            |                            | times for all stops that   |
|                            |                            | are time points. Do not    |
|                            |                            | interpolate stops.         |
|                            |                            |                            |
|                            |                            | You must specify arrival   |
|                            |                            | and departure times for    |
|                            |                            | the first and last stops   |
|                            |                            | in a trip.                 |
|                            |                            |                            |
|                            |                            | Times must be eight digits |
|                            |                            | in HH:MM:SS format         |
|                            |                            | (H:MM:SS is also accepted, |
|                            |                            | if the hour begins with    |
|                            |                            | 0). Do not pad times with  |
|                            |                            | spaces. The following      |
|                            |                            | columns list stop times    |
|                            |                            | for a trip and the proper  |
|                            |                            | way to express those times |
|                            |                            | in the **arrival\_time**   |
|                            |                            | field:                     |
|                            |                            |                            |
|                            |                            |   Time            arrival\ |
|                            |                            | _time value                |
|                            |                            |   --------------- -------- |
|                            |                            | -------------              |
|                            |                            |   08:10:00 A.M.   08:10:00 |
|                            |                            |  or 8:10:00                |
|                            |                            |   01:05:00 P.M.   13:05:00 |
|                            |                            |   07:40:00 P.M.   19:40:00 |
|                            |                            |   01:55:00 A.M.   25:55:00 |
|                            |                            |                            |
|                            |                            | **Note:** Trips that span  |
|                            |                            | multiple dates will have   |
|                            |                            | stop times greater than    |
|                            |                            | **24:00:00**. For example, |
|                            |                            | if a trip begins at        |
|                            |                            | 10:30:00 p.m. and ends at  |
|                            |                            | 2:15:00 a.m. on the        |
|                            |                            | following day, the stop    |
|                            |                            | times would be             |
|                            |                            | **22:30:00** and           |
|                            |                            | **26:15:00**. Entering     |
|                            |                            | those stop times as        |
|                            |                            | **22:30:00** and           |
|                            |                            | **02:15:00** would not     |
|                            |                            | produce the desired        |
|                            |                            | results.                   |
+----------------------------+----------------------------+----------------------------+
| departure\_time            | **Required**               | The **departure\_time**    |
|                            |                            | specifies the departure    |
|                            |                            | time from a specific stop  |
|                            |                            | for a specific trip on a   |
|                            |                            | route. The time is         |
|                            |                            | measured from "noon minus  |
|                            |                            | 12h" (effectively          |
|                            |                            | midnight, except for days  |
|                            |                            | on which daylight savings  |
|                            |                            | time changes occur) at the |
|                            |                            | beginning of the service   |
|                            |                            | date. For times occurring  |
|                            |                            | after midnight on the      |
|                            |                            | service date, enter the    |
|                            |                            | time as a value greater    |
|                            |                            | than 24:00:00 in HH:MM:SS  |
|                            |                            | local time for the day on  |
|                            |                            | which the trip schedule    |
|                            |                            | begins. If you don't have  |
|                            |                            | separate times for arrival |
|                            |                            | and departure at a stop,   |
|                            |                            | enter the same value for   |
|                            |                            | **arrival\_time** and      |
|                            |                            | **departure\_time**.       |
|                            |                            |                            |
|                            |                            | If this stop isn't a time  |
|                            |                            | point, use an empty string |
|                            |                            | value for the              |
|                            |                            | **arrival\_time** and      |
|                            |                            | **departure\_time**        |
|                            |                            | fields. Stops without      |
|                            |                            | arrival times will be      |
|                            |                            | scheduled based on the     |
|                            |                            | nearest preceding timed    |
|                            |                            | stop. To ensure accurate   |
|                            |                            | routing, please provide    |
|                            |                            | arrival and departure      |
|                            |                            | times for all stops that   |
|                            |                            | are time points. Do not    |
|                            |                            | interpolate stops.         |
|                            |                            |                            |
|                            |                            | You must specify arrival   |
|                            |                            | and departure times for    |
|                            |                            | the first and last stops   |
|                            |                            | in a trip.                 |
|                            |                            |                            |
|                            |                            | Times must be eight digits |
|                            |                            | in HH:MM:SS format         |
|                            |                            | (H:MM:SS is also accepted, |
|                            |                            | if the hour begins with    |
|                            |                            | 0). Do not pad times with  |
|                            |                            | spaces. The following      |
|                            |                            | columns list stop times    |
|                            |                            | for a trip and the proper  |
|                            |                            | way to express those times |
|                            |                            | in the **departure\_time** |
|                            |                            | field:                     |
|                            |                            |                            |
|                            |                            |   Time            departur |
|                            |                            | e\_time value              |
|                            |                            |   --------------- -------- |
|                            |                            | ---------------            |
|                            |                            |   08:10:00 A.M.   08:10:00 |
|                            |                            |  or 8:10:00                |
|                            |                            |   01:05:00 P.M.   13:05:00 |
|                            |                            |   07:40:00 P.M.   19:40:00 |
|                            |                            |   01:55:00 A.M.   25:55:00 |
|                            |                            |                            |
|                            |                            | **Note:** Trips that span  |
|                            |                            | multiple dates will have   |
|                            |                            | stop times greater than    |
|                            |                            | **24:00:00**. For example, |
|                            |                            | if a trip begins at        |
|                            |                            | 10:30:00 p.m. and ends at  |
|                            |                            | 2:15:00 a.m. on the        |
|                            |                            | following day, the stop    |
|                            |                            | times would be             |
|                            |                            | **22:30:00** and           |
|                            |                            | **26:15:00**. Entering     |
|                            |                            | those stop times as        |
|                            |                            | **22:30:00** and           |
|                            |                            | **02:15:00** would not     |
|                            |                            | produce the desired        |
|                            |                            | results.                   |
+----------------------------+----------------------------+----------------------------+
| stop\_id                   | **Required**               | The **stop\_id** field     |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a      |
|                            |                            | stop. Multiple routes may  |
|                            |                            | use the same stop. The     |
|                            |                            | stop\_id is referenced     |
|                            |                            | from the                   |
|                            |                            | [stops.txt](#stops_fields) |
|                            |                            | file. If location\_type is |
|                            |                            | used in stops.txt, all     |
|                            |                            | stops referenced in        |
|                            |                            | stop\_times.txt must have  |
|                            |                            | location\_type of 0.       |
|                            |                            |                            |
|                            |                            | Where possible,            |
|                            |                            | **stop\_id** values should |
|                            |                            | remain consistent between  |
|                            |                            | feed updates. In other     |
|                            |                            | words, stop A with         |
|                            |                            | **stop\_id** **1** should  |
|                            |                            | have **stop\_id 1** in all |
|                            |                            | subsequent data updates.   |
|                            |                            | If a stop is not a time    |
|                            |                            | point, enter blank values  |
|                            |                            | for **arrival\_time** and  |
|                            |                            | **departure\_time**.       |
+----------------------------+----------------------------+----------------------------+
| stop\_sequence             | **Required**               | The **stop\_sequence**     |
|                            |                            | field identifies the order |
|                            |                            | of the stops for a         |
|                            |                            | particular trip. The       |
|                            |                            | values for                 |
|                            |                            | **stop\_sequence** must be |
|                            |                            | non-negative integers, and |
|                            |                            | they must increase along   |
|                            |                            | the trip.                  |
|                            |                            |                            |
|                            |                            | For example, the first     |
|                            |                            | stop on the trip could     |
|                            |                            | have a **stop\_sequence**  |
|                            |                            | of **1**, the second stop  |
|                            |                            | on the trip could have a   |
|                            |                            | **stop\_sequence** of      |
|                            |                            | **23**, the third stop     |
|                            |                            | could have a               |
|                            |                            | **stop\_sequence** of      |
|                            |                            | **40**, and so on.         |
+----------------------------+----------------------------+----------------------------+
| stop\_headsign             | Optional                   | The **stop\_headsign**     |
|                            |                            | field contains the text    |
|                            |                            | that appears on a sign     |
|                            |                            | that identifies the trip's |
|                            |                            | destination to passengers. |
|                            |                            | Use this field to override |
|                            |                            | the default                |
|                            |                            | [trip\_headsign](#trips_tr |
|                            |                            | ip_headsign_field)         |
|                            |                            | when the headsign changes  |
|                            |                            | between stops. If this     |
|                            |                            | headsign is associated     |
|                            |                            | with an entire trip, use   |
|                            |                            | [trip\_headsign](#trips_tr |
|                            |                            | ip_headsign_field)         |
|                            |                            | instead.                   |
+----------------------------+----------------------------+----------------------------+
| pickup\_type               | Optional                   | The **pickup\_type** field |
|                            |                            | indicates whether          |
|                            |                            | passengers are picked up   |
|                            |                            | at a stop as part of the   |
|                            |                            | normal schedule or whether |
|                            |                            | a pickup at the stop is    |
|                            |                            | not available. This field  |
|                            |                            | also allows the transit    |
|                            |                            | agency to indicate that    |
|                            |                            | passengers must call the   |
|                            |                            | agency or notify the       |
|                            |                            | driver to arrange a pickup |
|                            |                            | at a particular stop.      |
|                            |                            | Valid values for this      |
|                            |                            | field are:                 |
|                            |                            |                            |
|                            |                            | -   **0** - Regularly      |
|                            |                            |     scheduled pickup       |
|                            |                            | -   **1** - No pickup      |
|                            |                            |     available              |
|                            |                            | -   **2** - Must phone     |
|                            |                            |     agency to arrange      |
|                            |                            |     pickup                 |
|                            |                            | -   **3** - Must           |
|                            |                            |     coordinate with driver |
|                            |                            |     to arrange pickup      |
|                            |                            |                            |
|                            |                            | The default value for this |
|                            |                            | field is **0**.            |
+----------------------------+----------------------------+----------------------------+
| drop\_off\_type            | Optional                   | The **drop\_off\_type**    |
|                            |                            | field indicates whether    |
|                            |                            | passengers are dropped off |
|                            |                            | at a stop as part of the   |
|                            |                            | normal schedule or whether |
|                            |                            | a drop off at the stop is  |
|                            |                            | not available. This field  |
|                            |                            | also allows the transit    |
|                            |                            | agency to indicate that    |
|                            |                            | passengers must call the   |
|                            |                            | agency or notify the       |
|                            |                            | driver to arrange a drop   |
|                            |                            | off at a particular stop.  |
|                            |                            | Valid values for this      |
|                            |                            | field are:                 |
|                            |                            |                            |
|                            |                            | -   **0** - Regularly      |
|                            |                            |     scheduled drop off     |
|                            |                            | -   **1** - No drop off    |
|                            |                            |     available              |
|                            |                            | -   **2** - Must phone     |
|                            |                            |     agency to arrange drop |
|                            |                            |     off                    |
|                            |                            | -   **3** - Must           |
|                            |                            |     coordinate with driver |
|                            |                            |     to arrange drop off    |
|                            |                            |                            |
|                            |                            | The default value for this |
|                            |                            | field is **0**.            |
+----------------------------+----------------------------+----------------------------+
| shape\_dist\_traveled      | Optional                   | When used in the           |
|                            |                            | stop\_times.txt file, the  |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | field positions a stop as  |
|                            |                            | a distance from the first  |
|                            |                            | shape point. The           |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | field represents a real    |
|                            |                            | distance traveled along    |
|                            |                            | the route in units such as |
|                            |                            | feet or kilometers. For    |
|                            |                            | example, if a bus travels  |
|                            |                            | a distance of 5.25         |
|                            |                            | kilometers from the start  |
|                            |                            | of the shape to the stop,  |
|                            |                            | the                        |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | for the stop ID would be   |
|                            |                            | entered as "5.25". This    |
|                            |                            | information allows the     |
|                            |                            | trip planner to determine  |
|                            |                            | how much of the shape to   |
|                            |                            | draw when showing part of  |
|                            |                            | a trip on the map. The     |
|                            |                            | values used for            |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | must increase along with   |
|                            |                            | **stop\_sequence**: they   |
|                            |                            | cannot be used to show     |
|                            |                            | reverse travel along a     |
|                            |                            | route.\                    |
|                            |                            |  \                         |
|                            |                            |  The units used for        |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | in the stop\_times.txt     |
|                            |                            | file must match the units  |
|                            |                            | that are used for this     |
|                            |                            | field in the               |
|                            |                            | [shapes.txt](#shapes_field |
|                            |                            | s)                         |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| timepoint                  | Optional                   | The **timepoint** field    |
|                            |                            | can be used to indicate if |
|                            |                            | the specified arrival and  |
|                            |                            | departure times for a stop |
|                            |                            | are strictly adhered to by |
|                            |                            | the transit vehicle or if  |
|                            |                            | they are instead           |
|                            |                            | approximate and/or         |
|                            |                            | interpolated times. The    |
|                            |                            | field allows a GTFS        |
|                            |                            | producer to provide        |
|                            |                            | interpolated stop times    |
|                            |                            | that potentially           |
|                            |                            | incorporate local          |
|                            |                            | knowledge, but still       |
|                            |                            | indicate if the times are  |
|                            |                            | approximate. For stop-time |
|                            |                            | entries with specified     |
|                            |                            | arrival and departure      |
|                            |                            | times, valid values for    |
|                            |                            | this field are:            |
|                            |                            |                            |
|                            |                            | -   **empty** - Times are  |
|                            |                            |     considered exact.      |
|                            |                            | -   **0** - Times are      |
|                            |                            |     considered             |
|                            |                            |     approximate.           |
|                            |                            | -   **1** - Times are      |
|                            |                            |     considered exact.      |
|                            |                            |                            |
|                            |                            | For stop-time entries      |
|                            |                            | without specified arrival  |
|                            |                            | and departure times, feed  |
|                            |                            | consumers must interpolate |
|                            |                            | arrival and departure      |
|                            |                            | times. Feed producers may  |
|                            |                            | optionally indicate that   |
|                            |                            | such an entry is not a     |
|                            |                            | timepoint (value=0) but it |
|                            |                            | is an error to mark a      |
|                            |                            | entry as a timepoint       |
|                            |                            | (value=1) without          |
|                            |                            | specifying arrival and     |
|                            |                            | departure times.           |
+----------------------------+----------------------------+----------------------------+

## calendar.txt

File: Required

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| service\_id                | **Required**               | The **service\_id**        |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a set  |
|                            |                            | of dates when service is   |
|                            |                            | available for one or more  |
|                            |                            | routes. Each service\_id   |
|                            |                            | value can appear at most   |
|                            |                            | once in a calendar.txt     |
|                            |                            | file. This value is        |
|                            |                            | dataset unique. It is      |
|                            |                            | referenced by the          |
|                            |                            | [trips.txt](#trips_fields) |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| monday                     | **Required**               | The **monday** field       |
|                            |                            | contains a binary value    |
|                            |                            | that indicates whether the |
|                            |                            | service is valid for all   |
|                            |                            | Mondays.                   |
|                            |                            |                            |
|                            |                            | -   A value of **1**       |
|                            |                            |     indicates that service |
|                            |                            |     is available for all   |
|                            |                            |     Mondays in the date    |
|                            |                            |     range. (The date range |
|                            |                            |     is specified using the |
|                            |                            |     **[start\_date](#calen |
|                            |                            | dar_start_date_field)**    |
|                            |                            |     and                    |
|                            |                            |     **[end\_date](#calenda |
|                            |                            | r_end_date_field)**        |
|                            |                            |     fields.)               |
|                            |                            | -   A value of **0**       |
|                            |                            |     indicates that service |
|                            |                            |     is not available on    |
|                            |                            |     Mondays in the date    |
|                            |                            |     range.                 |
|                            |                            |                            |
|                            |                            | **Note:** You may list     |
|                            |                            | exceptions for particular  |
|                            |                            | dates, such as holidays,   |
|                            |                            | in the                     |
|                            |                            | [calendar\_dates.txt](#cal |
|                            |                            | endar_dates_fields)        |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| tuesday                    | **Required**               | The **tuesday** field      |
|                            |                            | contains a binary value    |
|                            |                            | that indicates whether the |
|                            |                            | service is valid for all   |
|                            |                            | Tuesdays.                  |
|                            |                            |                            |
|                            |                            | -   A value of **1**       |
|                            |                            |     indicates that service |
|                            |                            |     is available for all   |
|                            |                            |     Tuesdays in the date   |
|                            |                            |     range. (The date range |
|                            |                            |     is specified using the |
|                            |                            |     **[start\_date](#calen |
|                            |                            | dar_start_date_field)**    |
|                            |                            |     and                    |
|                            |                            |     **[end\_date](#calenda |
|                            |                            | r_end_date_field)**        |
|                            |                            |     fields.)               |
|                            |                            | -   A value of **0**       |
|                            |                            |     indicates that service |
|                            |                            |     is not available on    |
|                            |                            |     Tuesdays in the date   |
|                            |                            |     range.                 |
|                            |                            |                            |
|                            |                            | **Note:** You may list     |
|                            |                            | exceptions for particular  |
|                            |                            | dates, such as holidays,   |
|                            |                            | in the                     |
|                            |                            | [calendar\_dates.txt](#cal |
|                            |                            | endar_dates_fields)        |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| wednesday                  | **Required**               | The **wednesday** field    |
|                            |                            | contains a binary value    |
|                            |                            | that indicates whether the |
|                            |                            | service is valid for all   |
|                            |                            | Wednesdays.                |
|                            |                            |                            |
|                            |                            | -   A value of **1**       |
|                            |                            |     indicates that service |
|                            |                            |     is available for all   |
|                            |                            |     Wednesdays in the date |
|                            |                            |     range. (The date range |
|                            |                            |     is specified using the |
|                            |                            |     **[start\_date](#calen |
|                            |                            | dar_start_date_field)**    |
|                            |                            |     and                    |
|                            |                            |     **[end\_date](#calenda |
|                            |                            | r_end_date_field)**        |
|                            |                            |     fields.)               |
|                            |                            | -   A value of **0**       |
|                            |                            |     indicates that service |
|                            |                            |     is not available on    |
|                            |                            |     Wednesdays in the date |
|                            |                            |     range.                 |
|                            |                            |                            |
|                            |                            | **Note:** You may list     |
|                            |                            | exceptions for particular  |
|                            |                            | dates, such as holidays,   |
|                            |                            | in the                     |
|                            |                            | [calendar\_dates.txt](#cal |
|                            |                            | endar_dates_fields)        |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| thursday                   | **Required**               | The **thursday** field     |
|                            |                            | contains a binary value    |
|                            |                            | that indicates whether the |
|                            |                            | service is valid for all   |
|                            |                            | Thursdays.                 |
|                            |                            |                            |
|                            |                            | -   A value of **1**       |
|                            |                            |     indicates that service |
|                            |                            |     is available for all   |
|                            |                            |     Thursdays in the date  |
|                            |                            |     range. (The date range |
|                            |                            |     is specified using the |
|                            |                            |     **[start\_date](#calen |
|                            |                            | dar_start_date_field)**    |
|                            |                            |     and                    |
|                            |                            |     **[end\_date](#calenda |
|                            |                            | r_end_date_field)**        |
|                            |                            |     fields.)               |
|                            |                            | -   A value of **0**       |
|                            |                            |     indicates that service |
|                            |                            |     is not available on    |
|                            |                            |     Thursdays in the date  |
|                            |                            |     range.                 |
|                            |                            |                            |
|                            |                            | **Note:** You may list     |
|                            |                            | exceptions for particular  |
|                            |                            | dates, such as holidays,   |
|                            |                            | in the                     |
|                            |                            | [calendar\_dates.txt](#cal |
|                            |                            | endar_dates_fields)        |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| friday                     | **Required**               | The **friday** field       |
|                            |                            | contains a binary value    |
|                            |                            | that indicates whether the |
|                            |                            | service is valid for all   |
|                            |                            | Fridays.                   |
|                            |                            |                            |
|                            |                            | -   A value of **1**       |
|                            |                            |     indicates that service |
|                            |                            |     is available for all   |
|                            |                            |     Fridays in the date    |
|                            |                            |     range. (The date range |
|                            |                            |     is specified using the |
|                            |                            |     **[start\_date](#calen |
|                            |                            | dar_start_date_field)**    |
|                            |                            |     and                    |
|                            |                            |     **[end\_date](#calenda |
|                            |                            | r_end_date_field)**        |
|                            |                            |     fields.)               |
|                            |                            | -   A value of **0**       |
|                            |                            |     indicates that service |
|                            |                            |     is not available on    |
|                            |                            |     Fridays in the date    |
|                            |                            |     range.                 |
|                            |                            |                            |
|                            |                            | **Note:** You may list     |
|                            |                            | exceptions for particular  |
|                            |                            | dates, such as holidays,   |
|                            |                            | in the                     |
|                            |                            | [calendar\_dates.txt](#cal |
|                            |                            | endar_dates_fields)        |
|                            |                            | file                       |
+----------------------------+----------------------------+----------------------------+
| saturday                   | **Required**               | The **saturday** field     |
|                            |                            | contains a binary value    |
|                            |                            | that indicates whether the |
|                            |                            | service is valid for all   |
|                            |                            | Saturdays.                 |
|                            |                            |                            |
|                            |                            | -   A value of **1**       |
|                            |                            |     indicates that service |
|                            |                            |     is available for all   |
|                            |                            |     Saturdays in the date  |
|                            |                            |     range. (The date range |
|                            |                            |     is specified using the |
|                            |                            |     **[start\_date](#calen |
|                            |                            | dar_start_date_field)**    |
|                            |                            |     and                    |
|                            |                            |     **[end\_date](#calenda |
|                            |                            | r_end_date_field)**        |
|                            |                            |     fields.)               |
|                            |                            | -   A value of **0**       |
|                            |                            |     indicates that service |
|                            |                            |     is not available on    |
|                            |                            |     Saturdays in the date  |
|                            |                            |     range.                 |
|                            |                            |                            |
|                            |                            | **Note:** You may list     |
|                            |                            | exceptions for particular  |
|                            |                            | dates, such as holidays,   |
|                            |                            | in the                     |
|                            |                            | [calendar\_dates.txt](#cal |
|                            |                            | endar_dates_fields)        |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| sunday                     | **Required**               | The **sunday** field       |
|                            |                            | contains a binary value    |
|                            |                            | that indicates whether the |
|                            |                            | service is valid for all   |
|                            |                            | Sundays.                   |
|                            |                            |                            |
|                            |                            | -   A value of **1**       |
|                            |                            |     indicates that service |
|                            |                            |     is available for all   |
|                            |                            |     Sundays in the date    |
|                            |                            |     range. (The date range |
|                            |                            |     is specified using the |
|                            |                            |     **[start\_date](#calen |
|                            |                            | dar_start_date_field)**    |
|                            |                            |     and                    |
|                            |                            |     **[end\_date](#calenda |
|                            |                            | r_end_date_field)**        |
|                            |                            |     fields.)               |
|                            |                            | -   A value of **0**       |
|                            |                            |     indicates that service |
|                            |                            |     is not available on    |
|                            |                            |     Sundays in the date    |
|                            |                            |     range.                 |
|                            |                            |                            |
|                            |                            | **Note:** You may list     |
|                            |                            | exceptions for particular  |
|                            |                            | dates, such as holidays,   |
|                            |                            | in the                     |
|                            |                            | [calendar\_dates.txt](#cal |
|                            |                            | endar_dates_fields)        |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| start\_date                | **Required**               | The **start\_date** field  |
|                            |                            | contains the start date    |
|                            |                            | for the service.           |
|                            |                            |                            |
|                            |                            | The **start\_date**        |
|                            |                            | field's value should be in |
|                            |                            | YYYYMMDD format.           |
+----------------------------+----------------------------+----------------------------+
| end\_date                  | **Required**               | The **end\_date** field    |
|                            |                            | contains the end date for  |
|                            |                            | the service. This date is  |
|                            |                            | included in the service    |
|                            |                            | interval.                  |
|                            |                            |                            |
|                            |                            | The **end\_date** field's  |
|                            |                            | value should be in         |
|                            |                            | YYYYMMDD format.           |
+----------------------------+----------------------------+----------------------------+

## calendar\_dates.txt

File: Optional

The calendar\_dates table allows you to explicitly activate or disable service
IDs by date. You can use it in two ways.

-   Recommended: Use calendar\_dates.txt in conjunction with calendar.txt, where
    calendar\_dates.txt defines any exceptions to the default service categories
    defined in the **calendar.txt** file. If your service is generally regular,
    with a few changes on explicit dates (for example, to accomodate special
    event services, or a school schedule), this is a good approach.
-   Alternate: Omit calendar.txt, and include ALL dates of service in
    calendar\_dates.txt. If your schedule varies most days of the month, or you
    want to programmatically output service dates without specifying a normal
    weekly schedule, this approach may be preferable.

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| service\_id                | **Required**               | The **service\_id**        |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a set  |
|                            |                            | of dates when a service    |
|                            |                            | exception is available for |
|                            |                            | one or more routes. Each   |
|                            |                            | (service\_id, date) pair   |
|                            |                            | can only appear once in    |
|                            |                            | calendar\_dates.txt. If    |
|                            |                            | the a service\_id value    |
|                            |                            | appears in both the        |
|                            |                            | calendar.txt and           |
|                            |                            | calendar\_dates.txt files, |
|                            |                            | the information in         |
|                            |                            | calendar\_dates.txt        |
|                            |                            | modifies the service       |
|                            |                            | information specified in   |
|                            |                            | [calendar.txt](#calendar_f |
|                            |                            | ields).                    |
|                            |                            | This field is referenced   |
|                            |                            | by the                     |
|                            |                            | [trips.txt](#trips_fields) |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| date                       | **Required**               | The **date** field         |
|                            |                            | specifies a particular     |
|                            |                            | date when service          |
|                            |                            | availability is different  |
|                            |                            | than the norm. You can use |
|                            |                            | the                        |
|                            |                            | **[exception\_type](#calen |
|                            |                            | dar_dates_exception_type_f |
|                            |                            | ield)**                    |
|                            |                            | field to indicate whether  |
|                            |                            | service is available on    |
|                            |                            | the specified date.        |
|                            |                            |                            |
|                            |                            | The **date** field's value |
|                            |                            | should be in YYYYMMDD      |
|                            |                            | format.                    |
+----------------------------+----------------------------+----------------------------+
| exception\_type            | **Required**               | The **exception\_type**    |
|                            |                            | indicates whether service  |
|                            |                            | is available on the date   |
|                            |                            | specified in the           |
|                            |                            | **[date](#calendar_dates_d |
|                            |                            | ate_field)**               |
|                            |                            | field.                     |
|                            |                            |                            |
|                            |                            | -   A value of **1**       |
|                            |                            |     indicates that service |
|                            |                            |     has been added for the |
|                            |                            |     specified date.        |
|                            |                            | -   A value of **2**       |
|                            |                            |     indicates that service |
|                            |                            |     has been removed for   |
|                            |                            |     the specified date.    |
|                            |                            |                            |
|                            |                            | For example, suppose a     |
|                            |                            | route has one set of trips |
|                            |                            | available on holidays and  |
|                            |                            | another set of trips       |
|                            |                            | available on all other     |
|                            |                            | days. You could have one   |
|                            |                            | **[service\_id](#calendar_ |
|                            |                            | service_id_field)**        |
|                            |                            | that corresponds to the    |
|                            |                            | regular service schedule   |
|                            |                            | and another                |
|                            |                            | **[service\_id](#calendar_ |
|                            |                            | service_id_field)**        |
|                            |                            | that corresponds to the    |
|                            |                            | holiday schedule. For a    |
|                            |                            | particular holiday, you    |
|                            |                            | would use the              |
|                            |                            | calendar\_dates.txt file   |
|                            |                            | to add the holiday to the  |
|                            |                            | holiday                    |
|                            |                            | **[service\_id](#calendar_ |
|                            |                            | service_id_field)**        |
|                            |                            | and to remove the holiday  |
|                            |                            | from the regular           |
|                            |                            | **[service\_id](#calendar_ |
|                            |                            | service_id_field)**        |
|                            |                            | schedule.                  |
+----------------------------+----------------------------+----------------------------+

## fare\_attributes.txt

File: Optional

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| fare\_id                   | **Required**               | The **fare\_id** field     |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a fare |
|                            |                            | class. The **fare\_id** is |
|                            |                            | dataset unique.            |
+----------------------------+----------------------------+----------------------------+
| price                      | **Required**               | The **price** field        |
|                            |                            | contains the fare price,   |
|                            |                            | in the unit specified by   |
|                            |                            | **currency\_type**.        |
+----------------------------+----------------------------+----------------------------+
| currency\_type             | **Required**               | The **currency\_type**     |
|                            |                            | field defines the currency |
|                            |                            | used to pay the fare.      |
|                            |                            | Please use the ISO 4217    |
|                            |                            | alphabetical currency      |
|                            |                            | codes which can be found   |
|                            |                            | at the following URL:      |
|                            |                            | [http://en.wikipedia.org/w |
|                            |                            | iki/ISO\_4217](http://en.w |
|                            |                            | ikipedia.org/wiki/ISO_4217 |
|                            |                            | ).                         |
+----------------------------+----------------------------+----------------------------+
| payment\_method            | **Required**               | The **payment\_method**    |
|                            |                            | field indicates when the   |
|                            |                            | fare must be paid. Valid   |
|                            |                            | values for this field are: |
|                            |                            |                            |
|                            |                            | -   **0** - Fare is paid   |
|                            |                            |     on board.              |
|                            |                            | -   **1** - Fare must be   |
|                            |                            |     paid before boarding.  |
+----------------------------+----------------------------+----------------------------+
| transfers                  | **Required**               | The **transfers** field    |
|                            |                            | specifies the number of    |
|                            |                            | transfers permitted on     |
|                            |                            | this fare. Valid values    |
|                            |                            | for this field are:        |
|                            |                            |                            |
|                            |                            | -   **0** - No transfers   |
|                            |                            |     permitted on this      |
|                            |                            |     fare.                  |
|                            |                            | -   **1** - Passenger may  |
|                            |                            |     transfer once.         |
|                            |                            | -   **2** - Passenger may  |
|                            |                            |     transfer twice.        |
|                            |                            | -   **(empty)** - If this  |
|                            |                            |     field is empty,        |
|                            |                            |     unlimited transfers    |
|                            |                            |     are permitted.         |
+----------------------------+----------------------------+----------------------------+
| transfer\_duration         | Optional                   | The **transfer\_duration** |
|                            |                            | field specifies the length |
|                            |                            | of time in seconds before  |
|                            |                            | a transfer expires.        |
|                            |                            |                            |
|                            |                            | When used with a           |
|                            |                            | **transfers** value of 0,  |
|                            |                            | the **transfer\_duration** |
|                            |                            | field indicates how long a |
|                            |                            | ticket is valid for a fare |
|                            |                            | where no transfers are     |
|                            |                            | allowed. Unless you intend |
|                            |                            | to use this field to       |
|                            |                            | indicate ticket validity,  |
|                            |                            | **transfer\_duration**     |
|                            |                            | should be omitted or empty |
|                            |                            | when **transfers** is set  |
|                            |                            | to 0.                      |
+----------------------------+----------------------------+----------------------------+

## fare\_rules.txt

File: Optional

The fare\_rules table allows you to specify how fares in fare\_attributes.txt
apply to an itinerary. Most fare structures use some combination of the
following rules:

-   Fare depends on origin or destination stations.
-   Fare depends on which zones the itinerary passes through.
-   Fare depends on which route the itinerary uses.

For examples that demonstrate how to specify a fare structure with
fare\_rules.txt and fare\_attributes.txt, see
[FareExamples](http://code.google.com/p/googletransitdatafeed/wiki/FareExamples)
in the GoogleTransitDataFeed open source project wiki.

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| fare\_id                   | **Required**               | The **fare\_id** field     |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a fare |
|                            |                            | class. This value is       |
|                            |                            | referenced from the        |
|                            |                            | [fare\_attributes.txt](#fa |
|                            |                            | re_attributes_fields)      |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| route\_id                  | Optional                   | The **route\_id** field    |
|                            |                            | associates the fare ID     |
|                            |                            | with a route. Route IDs    |
|                            |                            | are referenced from the    |
|                            |                            | [routes.txt](#routes_field |
|                            |                            | s)                         |
|                            |                            | file. If you have several  |
|                            |                            | routes with the same fare  |
|                            |                            | attributes, create a row   |
|                            |                            | in fare\_rules.txt for     |
|                            |                            | each route.                |
|                            |                            |                            |
|                            |                            | For example, if fare class |
|                            |                            | "b" is valid on route      |
|                            |                            | "TSW" and "TSE", the       |
|                            |                            | fare\_rules.txt file would |
|                            |                            | contain these rows for the |
|                            |                            | fare class:                |
|                            |                            |                            |
|                            |                            | `b,TSWb,TSE`               |
+----------------------------+----------------------------+----------------------------+
| origin\_id                 | Optional                   | The **origin\_id** field   |
|                            |                            | associates the fare ID     |
|                            |                            | with an origin [zone       |
|                            |                            | ID](#stops_zone_id_field). |
|                            |                            | Zone IDs are referenced    |
|                            |                            | from the                   |
|                            |                            | [stops.txt](#stops_fields) |
|                            |                            | file. If you have several  |
|                            |                            | origin IDs with the same   |
|                            |                            | fare attributes, create a  |
|                            |                            | row in fare\_rules.txt for |
|                            |                            | each origin ID.            |
|                            |                            |                            |
|                            |                            | For example, if fare class |
|                            |                            | "b" is valid for all       |
|                            |                            | travel originating from    |
|                            |                            | either zone "2" or zone    |
|                            |                            | "8", the fare\_rules.txt   |
|                            |                            | file would contain these   |
|                            |                            | rows for the fare class:   |
|                            |                            |                            |
|                            |                            | `b, , 2b, , 8 `            |
+----------------------------+----------------------------+----------------------------+
| destination\_id            | Optional                   | The **destination\_id**    |
|                            |                            | field associates the fare  |
|                            |                            | ID with a destination      |
|                            |                            | [zone                      |
|                            |                            | ID](#stops_zone_id_field). |
|                            |                            | Zone IDs are referenced    |
|                            |                            | from the                   |
|                            |                            | [stops.txt](#stops_fields) |
|                            |                            | file. If you have several  |
|                            |                            | destination IDs with the   |
|                            |                            | same fare attributes,      |
|                            |                            | create a row in            |
|                            |                            | fare\_rules.txt for each   |
|                            |                            | destination ID.            |
|                            |                            |                            |
|                            |                            | For example, you could use |
|                            |                            | the origin\_ID and         |
|                            |                            | destination\_ID fields     |
|                            |                            | together to specify that   |
|                            |                            | fare class "b" is valid    |
|                            |                            | for travel between zones 3 |
|                            |                            | and 4, and for travel      |
|                            |                            | between zones 3 and 5, the |
|                            |                            | fare\_rules.txt file would |
|                            |                            | contain these rows for the |
|                            |                            | fare class:                |
|                            |                            |                            |
|                            |                            | `b, , 3,4b, , 3,5`         |
+----------------------------+----------------------------+----------------------------+
| contains\_id               | Optional                   | The **contains\_id** field |
|                            |                            | associates the fare ID     |
|                            |                            | with a [zone               |
|                            |                            | ID](#stops_zone_id_field), |
|                            |                            | referenced from the        |
|                            |                            | [stops.txt](#stops_fields) |
|                            |                            | file. The fare ID is then  |
|                            |                            | associated with            |
|                            |                            | itineraries that pass      |
|                            |                            | through every contains\_id |
|                            |                            | zone.                      |
|                            |                            |                            |
|                            |                            | For example, if fare class |
|                            |                            | "c" is associated with all |
|                            |                            | travel on the GRT route    |
|                            |                            | that passes through zones  |
|                            |                            | 5, 6, and 7 the            |
|                            |                            | fare\_rules.txt would      |
|                            |                            | contain these rows:\       |
|                            |                            |  \                         |
|                            |                            |                            |
|                            |                            | `c,GRT,,,5c,GRT,,,6c,GRT,, |
|                            |                            | ,7`                        |
|                            |                            |                            |
|                            |                            | Because all contains\_id   |
|                            |                            | zones must be matched for  |
|                            |                            | the fare to apply, an      |
|                            |                            | itinerary that passes      |
|                            |                            | through zones 5 and 6 but  |
|                            |                            | not zone 7 would not have  |
|                            |                            | fare class "c". For more   |
|                            |                            | detail, see                |
|                            |                            | [FareExamples](http://code |
|                            |                            | .google.com/p/googletransi |
|                            |                            | tdatafeed/wiki/FareExample |
|                            |                            | s)                         |
|                            |                            | in the                     |
|                            |                            | GoogleTransitDataFeed      |
|                            |                            | project wiki.              |
+----------------------------+----------------------------+----------------------------+

## shapes.txt

File: Optional

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| shape\_id                  | **Required**               | The **shape\_id** field    |
|                            |                            | contains an ID that        |
|                            |                            | uniquely identifies a      |
|                            |                            | shape.                     |
+----------------------------+----------------------------+----------------------------+
| shape\_pt\_lat             | **Required**               | The **shape\_pt\_lat**     |
|                            |                            | field associates a shape   |
|                            |                            | point's latitude with a    |
|                            |                            | shape ID. The field value  |
|                            |                            | must be a valid WGS 84     |
|                            |                            | latitude. Each row in      |
|                            |                            | shapes.txt represents a    |
|                            |                            | shape point in your shape  |
|                            |                            | definition.                |
|                            |                            |                            |
|                            |                            | For example, if the shape  |
|                            |                            | "A\_shp" has three points  |
|                            |                            | in its definition, the     |
|                            |                            | shapes.txt file might      |
|                            |                            | contain these rows to      |
|                            |                            | define the shape:          |
|                            |                            |                            |
|                            |                            | `A_shp,37.61956,-122.48161 |
|                            |                            | ,0             A_shp,37.64 |
|                            |                            | 430,-122.41070,6           |
|                            |                            |    A_shp,37.65863,-122.308 |
|                            |                            | 39,11`                     |
+----------------------------+----------------------------+----------------------------+
| shape\_pt\_lon             | **Required**               | The **shape\_pt\_lon**     |
|                            |                            | field associates a shape   |
|                            |                            | point's longitude with a   |
|                            |                            | shape ID. The field value  |
|                            |                            | must be a valid WGS 84     |
|                            |                            | longitude value from -180  |
|                            |                            | to 180. Each row in        |
|                            |                            | shapes.txt represents a    |
|                            |                            | shape point in your shape  |
|                            |                            | definition.                |
|                            |                            |                            |
|                            |                            | For example, if the shape  |
|                            |                            | "A\_shp" has three points  |
|                            |                            | in its definition, the     |
|                            |                            | shapes.txt file might      |
|                            |                            | contain these rows to      |
|                            |                            | define the shape:          |
|                            |                            |                            |
|                            |                            | `A_shp,37.61956,-122.48161 |
|                            |                            | ,0             A_shp,37.64 |
|                            |                            | 430,-122.41070,6           |
|                            |                            |    A_shp,37.65863,-122.308 |
|                            |                            | 39,11`                     |
+----------------------------+----------------------------+----------------------------+
| shape\_pt\_sequence        | **Required**               | The                        |
|                            |                            | **shape\_pt\_sequence**    |
|                            |                            | field associates the       |
|                            |                            | latitude and longitude of  |
|                            |                            | a shape point with its     |
|                            |                            | sequence order along the   |
|                            |                            | shape. The values for      |
|                            |                            | **shape\_pt\_sequence**    |
|                            |                            | must be non-negative       |
|                            |                            | integers, and they must    |
|                            |                            | increase along the trip.   |
|                            |                            |                            |
|                            |                            | For example, if the shape  |
|                            |                            | "A\_shp" has three points  |
|                            |                            | in its definition, the     |
|                            |                            | shapes.txt file might      |
|                            |                            | contain these rows to      |
|                            |                            | define the shape:          |
|                            |                            |                            |
|                            |                            | `A_shp,37.61956,-122.48161 |
|                            |                            | ,0             A_shp,37.64 |
|                            |                            | 430,-122.41070,6           |
|                            |                            |    A_shp,37.65863,-122.308 |
|                            |                            | 39,11         `            |
+----------------------------+----------------------------+----------------------------+
| shape\_dist\_traveled      | Optional                   | When used in the           |
|                            |                            | shapes.txt file, the       |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | field positions a shape    |
|                            |                            | point as a distance        |
|                            |                            | traveled along a shape     |
|                            |                            | from the first shape       |
|                            |                            | point. The                 |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | field represents a real    |
|                            |                            | distance traveled along    |
|                            |                            | the route in units such as |
|                            |                            | feet or kilometers. This   |
|                            |                            | information allows the     |
|                            |                            | trip planner to determine  |
|                            |                            | how much of the shape to   |
|                            |                            | draw when showing part of  |
|                            |                            | a trip on the map. The     |
|                            |                            | values used                |
|                            |                            | for**shape\_dist\_traveled |
|                            |                            | **                         |
|                            |                            | must increase along with   |
|                            |                            | **shape\_pt\_sequence**:   |
|                            |                            | they cannot be used to     |
|                            |                            | show reverse travel along  |
|                            |                            | a route. \                 |
|                            |                            |  \                         |
|                            |                            |  The units used for        |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | in the shapes.txt file     |
|                            |                            | must match the units that  |
|                            |                            | are used for this field in |
|                            |                            | the                        |
|                            |                            | [stop\_times.txt](#stop_ti |
|                            |                            | mes_fields)                |
|                            |                            | file.                      |
|                            |                            |                            |
|                            |                            | For example, if a bus      |
|                            |                            | travels along the three    |
|                            |                            | points defined above for   |
|                            |                            | A\_shp, the additional     |
|                            |                            | **shape\_dist\_traveled**  |
|                            |                            | values (shown here in      |
|                            |                            | kilometers) would look     |
|                            |                            | like this:                 |
|                            |                            |                            |
|                            |                            | `A_shp,37.61956,-122.48161 |
|                            |                            | ,0,0             A_shp,37. |
|                            |                            | 64430,-122.41070,6,6.8310  |
|                            |                            |             A_shp,37.65863 |
|                            |                            | ,-122.30839,11,15.8765`    |
+----------------------------+----------------------------+----------------------------+

## frequencies.txt

File: Optional

This table is intended to represent schedules that don't have a fixed list of
stop times. When trips are defined in frequencies.txt, the trip planner ignores
the absolute values of the [arrival\_time](#stop_times_arrival_time_field) and
[departure\_time](#stop_times_departure_time_field) fields for those trips in
[stop\_times.txt](#stop_times_fields). Instead, the stop\_times table defines
the sequence of stops and the time difference between each stop.

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| trip\_id                   | **Required**               | The **trip\_id** contains  |
|                            |                            | an ID that identifies a    |
|                            |                            | trip on which the          |
|                            |                            | specified frequency of     |
|                            |                            | service applies. Trip IDs  |
|                            |                            | are referenced from the    |
|                            |                            | [trips.txt](#trips_fields) |
|                            |                            | file.                      |
+----------------------------+----------------------------+----------------------------+
| start\_time                | **Required**               | The **start\_time** field  |
|                            |                            | specifies the time at      |
|                            |                            | which service begins with  |
|                            |                            | the specified frequency.   |
|                            |                            | The time is measured from  |
|                            |                            | "noon minus 12h"           |
|                            |                            | (effectively midnight,     |
|                            |                            | except for days on which   |
|                            |                            | daylight savings time      |
|                            |                            | changes occur) at the      |
|                            |                            | beginning of the service   |
|                            |                            | date. For times occurring  |
|                            |                            | after midnight, enter the  |
|                            |                            | time as a value greater    |
|                            |                            | than 24:00:00 in HH:MM:SS  |
|                            |                            | local time for the day on  |
|                            |                            | which the trip schedule    |
|                            |                            | begins. E.g. 25:35:00.     |
+----------------------------+----------------------------+----------------------------+
| end\_time                  | **Required**               | The **end\_time** field    |
|                            |                            | indicates the time at      |
|                            |                            | which service changes to a |
|                            |                            | different frequency (or    |
|                            |                            | ceases) at the first stop  |
|                            |                            | in the trip. The time is   |
|                            |                            | measured from "noon minus  |
|                            |                            | 12h" (effectively          |
|                            |                            | midnight, except for days  |
|                            |                            | on which daylight savings  |
|                            |                            | time changes occur) at the |
|                            |                            | beginning of the service   |
|                            |                            | date. For times occurring  |
|                            |                            | after midnight, enter the  |
|                            |                            | time as a value greater    |
|                            |                            | than 24:00:00 in HH:MM:SS  |
|                            |                            | local time for the day on  |
|                            |                            | which the trip schedule    |
|                            |                            | begins. E.g. 25:35:00.     |
+----------------------------+----------------------------+----------------------------+
| headway\_secs              | **Required**               | The **headway\_secs**      |
|                            |                            | field indicates the time   |
|                            |                            | between departures from    |
|                            |                            | the same stop (headway)    |
|                            |                            | for this trip type, during |
|                            |                            | the time interval          |
|                            |                            | specified by               |
|                            |                            | **start\_time** and        |
|                            |                            | **end\_time**. The headway |
|                            |                            | value must be entered in   |
|                            |                            | seconds.                   |
|                            |                            |                            |
|                            |                            | Periods in which headways  |
|                            |                            | are defined (the rows in   |
|                            |                            | frequencies.txt) shouldn't |
|                            |                            | overlap for the same trip, |
|                            |                            | since it's hard to         |
|                            |                            | determine what should be   |
|                            |                            | inferred from two          |
|                            |                            | overlapping headways.      |
|                            |                            | However, a headway period  |
|                            |                            | may begin at the exact     |
|                            |                            | same time that another one |
|                            |                            | ends, for instance:        |
|                            |                            |                            |
|                            |                            | `A, 05:00:00, 07:00:00, 60 |
|                            |                            | 0             B, 07:00:00, |
|                            |                            |  12:00:00, 1200 `          |
+----------------------------+----------------------------+----------------------------+
| exact\_times               | Optional                   | The **exact\_times** field |
|                            |                            | determines if              |
|                            |                            | frequency-based trips      |
|                            |                            | should be exactly          |
|                            |                            | scheduled based on the     |
|                            |                            | specified headway          |
|                            |                            | information. Valid values  |
|                            |                            | for this field are:        |
|                            |                            |                            |
|                            |                            | -   **0** or **(empty)** - |
|                            |                            |     Frequency-based trips  |
|                            |                            |     are not exactly        |
|                            |                            |     scheduled. This is the |
|                            |                            |     default behavior.      |
|                            |                            | -   **1** -                |
|                            |                            |     Frequency-based trips  |
|                            |                            |     are exactly scheduled. |
|                            |                            |     For a frequencies.txt  |
|                            |                            |     row, trips are         |
|                            |                            |     scheduled starting     |
|                            |                            |     with                   |
|                            |                            |     `trip_start_time = sta |
|                            |                            | rt_time + x             *  |
|                            |                            | headway_secs`              |
|                            |                            |     for all `x` in         |
|                            |                            |     `(0, 1, 2, ...)` where |
|                            |                            |     `trip_start_time       |
|                            |                            |        < end_time`.        |
|                            |                            |                            |
|                            |                            | The value of               |
|                            |                            | **exact\_times** must be   |
|                            |                            | the same for all           |
|                            |                            | frequencies.txt rows with  |
|                            |                            | the same **trip\_id**. If  |
|                            |                            | **exact\_times** is **1**  |
|                            |                            | and a frequencies.txt row  |
|                            |                            | has a **start\_time**      |
|                            |                            | equal to **end\_time**, no |
|                            |                            | trip must be scheduled.    |
|                            |                            | When **exact\_times** is   |
|                            |                            | **1**, care must be taken  |
|                            |                            | to choose an **end\_time** |
|                            |                            | value that is greater than |
|                            |                            | the last desired trip      |
|                            |                            | start time but less than   |
|                            |                            | the last desired trip      |
|                            |                            | start time +               |
|                            |                            | **headway\_secs**.         |
+----------------------------+----------------------------+----------------------------+

## transfers.txt

File: Optional

Trip planners normally calculate transfer points based on the relative proximity
of stops in each route. For potentially ambiguous stop pairs, or transfers where
you want to specify a particular choice, use transfers.txt to define additional
rules for making connections between routes.

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| from\_stop\_id             | **Required**               | The **from\_stop\_id**     |
|                            |                            | field contains a stop ID   |
|                            |                            | that identifies a stop or  |
|                            |                            | station where a connection |
|                            |                            | between routes begins.     |
|                            |                            | Stop IDs are referenced    |
|                            |                            | from the                   |
|                            |                            | [stops.txt](#stops_fields) |
|                            |                            | file. If the stop ID       |
|                            |                            | refers to a station that   |
|                            |                            | contains multiple stops,   |
|                            |                            | this transfer rule applies |
|                            |                            | to all stops in that       |
|                            |                            | station.                   |
+----------------------------+----------------------------+----------------------------+
| to\_stop\_id               | **Required**               | The **to\_stop\_id** field |
|                            |                            | contains a stop ID that    |
|                            |                            | identifies a stop or       |
|                            |                            | station where a connection |
|                            |                            | between routes ends. Stop  |
|                            |                            | IDs are referenced from    |
|                            |                            | the                        |
|                            |                            | [stops.txt](#stops_fields) |
|                            |                            | file. If the stop ID       |
|                            |                            | refers to a station that   |
|                            |                            | contains multiple stops,   |
|                            |                            | this transfer rule applies |
|                            |                            | to all stops in that       |
|                            |                            | station.                   |
+----------------------------+----------------------------+----------------------------+
| transfer\_type             | **Required**               | The **transfer\_type**     |
|                            |                            | field specifies the type   |
|                            |                            | of connection for the      |
|                            |                            | specified (from\_stop\_id, |
|                            |                            | to\_stop\_id) pair. Valid  |
|                            |                            | values for this field are: |
|                            |                            |                            |
|                            |                            | -   **0** or **(empty)** - |
|                            |                            |     This is a recommended  |
|                            |                            |     transfer point between |
|                            |                            |     two routes.            |
|                            |                            | -   **1** - This is a      |
|                            |                            |     timed transfer point   |
|                            |                            |     between two routes.    |
|                            |                            |     The departing vehicle  |
|                            |                            |     is expected to wait    |
|                            |                            |     for the arriving one,  |
|                            |                            |     with sufficient time   |
|                            |                            |     for a passenger to     |
|                            |                            |     transfer between       |
|                            |                            |     routes.                |
|                            |                            | -   **2** - This transfer  |
|                            |                            |     requires a minimum     |
|                            |                            |     amount of time between |
|                            |                            |     arrival and departure  |
|                            |                            |     to ensure a            |
|                            |                            |     connection. The time   |
|                            |                            |     required to transfer   |
|                            |                            |     is specified by        |
|                            |                            |     **min\_transfer\_time* |
|                            |                            | *.                         |
|                            |                            | -   **3** - Transfers are  |
|                            |                            |     not possible between   |
|                            |                            |     routes at this         |
|                            |                            |     location.              |
+----------------------------+----------------------------+----------------------------+
| min\_transfer\_time        | Optional                   | When a connection between  |
|                            |                            | routes requires an amount  |
|                            |                            | of time between arrival    |
|                            |                            | and departure              |
|                            |                            | (transfer\_type=2), the    |
|                            |                            | **min\_transfer\_time**    |
|                            |                            | field defines the amount   |
|                            |                            | of time that must be       |
|                            |                            | available in an itinerary  |
|                            |                            | to permit a transfer       |
|                            |                            | between routes at these    |
|                            |                            | stops. The                 |
|                            |                            | min\_transfer\_time must   |
|                            |                            | be sufficient to permit a  |
|                            |                            | typical rider to move      |
|                            |                            | between the two stops,     |
|                            |                            | including buffer time to   |
|                            |                            | allow for schedule         |
|                            |                            | variance on each route.    |
|                            |                            |                            |
|                            |                            | The min\_transfer\_time    |
|                            |                            | value must be entered in   |
|                            |                            | seconds, and must be a     |
|                            |                            | non-negative integer.      |
+----------------------------+----------------------------+----------------------------+

## feed\_info.txt

File: Optional

The file contains information about the feed itself, rather than the services
that the feed describes. GTFS currently has an [agency.txt](#agency_fields) file
to provide information about the agencies that operate the services described by
the feed. However, the publisher of the feed is sometimes a different entity
than any of the agencies (in the case of regional aggregators). In addition,
there are some fields that are really feed-wide settings, rather than
agency-wide.

+----------------------------+----------------------------+----------------------------+
| Field Name                 | Required                   | Details                    |
+============================+============================+============================+
| feed\_publisher\_name      | **Required**               | The                        |
|                            |                            | **feed\_publisher\_name**  |
|                            |                            | field contains the full    |
|                            |                            | name of the organization   |
|                            |                            | that publishes the feed.   |
|                            |                            | (This may be the same as   |
|                            |                            | one of the                 |
|                            |                            | **agency\_name** values in |
|                            |                            | [agency.txt](#agency_field |
|                            |                            | s).)                       |
|                            |                            | GTFS-consuming             |
|                            |                            | applications can display   |
|                            |                            | this name when giving      |
|                            |                            | attribution for a          |
|                            |                            | particular feed's data.    |
+----------------------------+----------------------------+----------------------------+
| feed\_publisher\_url       | **Required**               | The                        |
|                            |                            | **feed\_publisher\_url**   |
|                            |                            | field contains the URL of  |
|                            |                            | the feed publishing        |
|                            |                            | organization's website.    |
|                            |                            | (This may be the same as   |
|                            |                            | one of the **agency\_url** |
|                            |                            | values in                  |
|                            |                            | [agency.txt](#agency_field |
|                            |                            | s).)                       |
|                            |                            | The value must be a fully  |
|                            |                            | qualified URL that         |
|                            |                            | includes **http://** or    |
|                            |                            | **https://**, and any      |
|                            |                            | special characters in the  |
|                            |                            | URL must be correctly      |
|                            |                            | escaped. See               |
|                            |                            | [http://www.w3.org/Address |
|                            |                            | ing/URL/4\_URI\_Recommenta |
|                            |                            | tions.html](http://www.w3. |
|                            |                            | org/Addressing/URL/4_URI_R |
|                            |                            | ecommentations.html)       |
|                            |                            | for a description of how   |
|                            |                            | to create fully qualified  |
|                            |                            | URL values.                |
+----------------------------+----------------------------+----------------------------+
| feed\_lang                 | **Required**               | The **feed\_lang** field   |
|                            |                            | contains a IETF BCP 47     |
|                            |                            | language code specifying   |
|                            |                            | the default language used  |
|                            |                            | for the text in this feed. |
|                            |                            | This setting helps GTFS    |
|                            |                            | consumers choose           |
|                            |                            | capitalization rules and   |
|                            |                            | other language-specific    |
|                            |                            | settings for the feed. For |
|                            |                            | an introduction to IETF    |
|                            |                            | BCP 47, please refer to    |
|                            |                            | [http://www.rfc-editor.org |
|                            |                            | /rfc/bcp/bcp47.txt](http:/ |
|                            |                            | /www.rfc-editor.org/rfc/bc |
|                            |                            | p/bcp47.txt)               |
|                            |                            | and                        |
|                            |                            | [http://www.w3.org/Interna |
|                            |                            | tional/articles/language-t |
|                            |                            | ags/](http://www.w3.org/In |
|                            |                            | ternational/articles/langu |
|                            |                            | age-tags/).                |
+----------------------------+----------------------------+----------------------------+
| feed\_start\_date          | Optional                   | The feed provides complete |
|                            |                            | and reliable schedule      |
| feed\_end\_date            |                            | information for service in |
|                            |                            | the period from the        |
|                            |                            | beginning of the           |
|                            |                            | **feed\_start\_date** day  |
|                            |                            | to the end of the          |
|                            |                            | **feed\_end\_date** day.   |
|                            |                            | Both days are given as     |
|                            |                            | dates in YYYYMMDD format   |
|                            |                            | as for                     |
|                            |                            | [calendar.txt](#calendar_f |
|                            |                            | ields),                    |
|                            |                            | or left empty if           |
|                            |                            | unavailable. The           |
|                            |                            | **feed\_end\_date** date   |
|                            |                            | must not precede the       |
|                            |                            | **feed\_start\_date** date |
|                            |                            | if both are given. Feed    |
|                            |                            | providers are encouraged   |
|                            |                            | to give schedule data      |
|                            |                            | outside this period to     |
|                            |                            | advise of likely future    |
|                            |                            | service, but feed          |
|                            |                            | consumers should treat it  |
|                            |                            | mindful of its             |
|                            |                            | non-authoritative status.  |
|                            |                            | If **feed\_start\_date**   |
|                            |                            | or **feed\_end\_date**     |
|                            |                            | extend beyond the active   |
|                            |                            | calendar dates defined in  |
|                            |                            | calendar.txt and           |
|                            |                            | calendar\_dates.txt, the   |
|                            |                            | feed is making an explicit |
|                            |                            | assertion that there is no |
|                            |                            | service for dates within   |
|                            |                            | the **feed\_start\_date**  |
|                            |                            | or **feed\_end\_date**     |
|                            |                            | range but not included in  |
|                            |                            | the active calendar dates. |
+----------------------------+----------------------------+----------------------------+
| feed\_version              | Optional                   | The feed publisher can     |
|                            |                            | specify a string here that |
|                            |                            | indicates the current      |
|                            |                            | version of their GTFS      |
|                            |                            | feed. GTFS-consuming       |
|                            |                            | applications can display   |
|                            |                            | this value to help feed    |
|                            |                            | publishers determine       |
|                            |                            | whether the latest version |
|                            |                            | of their feed has been     |
|                            |                            | incorporated.              |
+----------------------------+----------------------------+----------------------------+


