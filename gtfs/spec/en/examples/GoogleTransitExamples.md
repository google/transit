## Introduction
The fare\_attributes.txt and fare_rules.txt files in the [Google Transit Feed Specification](https://github.com/MobilityData/transit/blob/master/gtfs/spec/en/reference.md) can be confusing. The following examples work through different kinds of fare structures and show how to represent them in a Google transit feed.

### Fare Examples

* Example 1: All trips have the same fare, unlimited transfers<br>
* Example 2: All trips have the same fare, no transfers<br>
* Example 3: All trips have the same fare, transfers allowed<br>
* Example 4: Different pricing for local and express routes<br>
* Example 5: Buying a transfer increases the fare<br>
* Example 6: Fare depends on station pairs, how you get there doesn't matter<br>
* Example 7: Fare depends on zones<br>

### Example 1: All trips have the same fare, unlimited transfers


Suppose Demo Transit Agency has the following fare structure:

* riders pay $1.00 on boarding (`price`=`1.00`, `currency`=`USD`, `payment_method`=`0`)
* a ticket is good for all vehicles and doesn't expire (`transfers` is empty)
* passengers can ride as long as they like. (`transfer_duration` is omitted)

Since all trips have the same fare, Demo Transit can omit fare_rules.txt.

fare_attributes.txt

| fare_id | price | currency_type | payment_method |transfers |
|:-----|:-----|:-----|:-----|:-----|
| only_fare | 1.00 | USD | 0 | |

#### Calculating an adult fare
The trip planner calculates a fare of $1.00 for each leg of the itinerary that includes a change of vehicle. However, unlimited transfers are permitted, so the trip planner only displays the lowest charge. Adult fare: $1.00

<hr>

### Example 2: All trips have the same fare, no transfers
Suppose Demo Transit Agency has the following fare structure:

* riders pay $1.00 on boarding (`price`=`1.00`, `currency`=`USD`, `payment_method`=`0`)
* passengers can ride as long as they like. (`transfer_duration` is omitted)
* any change in vehicles requires a new fare. (`transfers`=`0`)

Since all trips have the same fare, Demo Transit can omit fare_rules.txt.

fare_attributes.txt

| fare_id | price | currency_type | payment_method | transfers |
|:--------------|:----------|:-------------------|:--------------------|:--------------|
| only_fare | 1.00 | USD | 0 | 0 |

#### Calculating an adult fare
The trip planner calculates a fare of $1.00 for each leg of the itinerary that includes a change of vehicle. So an itinerary that requires a change of buses would be $2.00.

<hr>

### Example 3: All trips have the same fare, transfers allowed
Suppose Demo Transit Agency has the following fare structure:

* riders pay $1 on boarding (`price`=`1.00`, `currency`=`USD`, `payment_method`=`0`)
* unlimited transfers are allowed within 90 minutes (`transfers` is empty,`transfer_duration`=`5400`)

Since all trips have the same fare, Demo Transit can omit fare_rules.txt.

fare_attributes.txt

| fare_id | price | currency_type | payment_method | transfers | transfer_duration |
|:--------------|:----------|:-------------------|:--------------------|:--------------|:-----------------------|
| only_fare | 1.00 | USD | 0 | | 5400 |

#### Calculating an adult fare
The trip planner calculates a fare of $1.00 for each leg of the itinerary that includes a change of vehicle. Then it calculates the time for the itinerary. If the itinerary time is less than 90 minutes, the fare is $1.00.

<hr>

### Example 4: Different pricing for local and express routes
Suppose Demo Transit Agency has the following fare structure:

* riders pay $1.75 on boarding local buses (route 1)
* riders pay $5.00 on boarding express buses (routes 2 and 3)
* transfers aren't allowed.

Since some trips cost more than others, Demo Transit must include fare_rules.txt, and each route must have an entry to associate it with a fare.

fare_attributes.txt

| fare_id | price | currency_type | payment_method | transfers |
|:--------------|:----------|:-------------------|:----------------|:--------------|
| local_fare | 1.75 | USD | 0 | 0 | | express_fare | 5.00 | USD | 0 | 0 |

fare_rules.txt

| fare_id | route_id |
|:-------------|:--------------|
| local_fare | Route_1 |
| express_fare | Route_2 |
| express_fare | Route_3 |

#### Calculating an adult fare
The $5.00 fare is only applicable if you ride routes 2 or 3. The $1.75 fare only applies on route 1. If an itinerary uses routes 1 and 2, the fare is $6.75.

<hr>

### Example 5: Buying a transfer increases the fare
Suppose Demo Transit Agency has the following fare structure:

* riders pay $1.75 on boarding local buses
* riders can pay an extra $0.25 on boarding to purchase a transfer
* transfers purchased are valid for 90 minutes

Since these rules apply to all trips, Demo Transit can omit fare_rules.txt.

fare_attributes.txt

| fare_id | price | currency_type | payment_method | transfers | transfer_duration |
|:--------------|:----------|:-------------------|:--------------------|:--------------|:-----------------------|
| simple_fare | 1.75 | USD | 0 | 0 | |
| plustransfer_fare | 2.00 | USD | 0 | | 5400 |

#### Calculating an adult fare
Technically, both fares apply on itinerary that has no transfers. However, the trip planner always chooses the least expensive applicable fare:

* For an itinerary with one transfer, `simple_fare` is $3.50 vs. $2.00 when a transfer is purchased. So the trip planner will report $2.00 fare on all itineraries that require a change of vehicle.
* For an itinerary with no transfers, $1.75 fare is less than `plustransfer_fare` of $2.00. So if an itinerary doesn't require a change of vehicle, the fare is $1.75.

<hr>

### Example 6: Fare depends on station pairs, how you get there doesn't matter
In this example only the entry and exit points from the system matter.

To define this fare structure for the feed, each station must have its own unique zone ID defined in stops.txt. Each station is considered a single zone.

The fare\_attributes.txt and fare\_rules.txt files define one row for each pair of stations.
In fare\_attributes.txt, the `origin_id` and `destination_id` fields identify station pairs by zone ID.

fare_attributes.txt

| fare_id | price | currency_type | payment_method | transfers |
|:--------------|:----------|:-------------------|:--------------------|:--------------|
| S1\_to\_S2 | 1.75 | USD | 0 | |
| S1\_to\_S3 | 3.25 | USD | 0 | |
| S1\_to\_S4 | 4.55 | USD | 0 | |
| ... | | | | |
| S10\_to\_S1 | 5.65 | USD | 0 | |

fare_rules.txt

| fare_id | origin_id | destination_id |
|:-------------|:---------------|:--------------------|
| S1\_to\_S2 | S1 | S2 |
| S1\_to\_S3 | S1 | S3 |
| S1\_to\_S4 | S1 | S4 |
| ... | | |
| S10\_to\_S1 | S10 | S1 |

#### Calculating an adult fare
The trip planner calculates an itinerary, and then looks up the fare rules until it finds a matching origin/destination station pair.

The public feed from [SF Bay Area BART](https://www.bart.gov/schedules/developers/gtfs) provides a real-world illustration of this type of fare structure.

<hr>

### Example 7: Fare depends on zones
Suppose Demo Transit Agency has a concentric three-zone system, where fares depend on which zones a rider passes through during an itinerary.

To define this fare structure for the feed, fare\_attributes.txt and fare\_rules.txt must contain a line for each possible combination of zones. For very complex cross-zone fare structures, it may be simpler to programmatically output fare\_rules.txt using origin and destination to define fares.

fare_attributes.txt

| fare_id | price | currency_type | payment_method | transfers |
|:--------------|:----------|:-------------------|:--------------------|:--------------| | F1 | 4.15 | USD | 0 | |
| F2 | 2.20 | USD | 0 | |
| F3 | 2.20 | USD | 0 | |
| F4 | 2.95 | USD | 0 | |
| F5 | 1.25 | USD | 0 | |
| F6 | 1.95 | USD | 0 | |
| F7 | 1.95 | USD | 0 | |

fare_rules.txt

| fare_id | contains_id |
|:-------------|:-----------------|
| F1 | 1 |
| F1 | 2 |
| F1 | 3 |
| F2 | 1 |
| F2 | 2 |
| F3 | 1 |
| F3 | 3 |
| F4 | 2 |
| F4 | 3 |
| F5 | 1 |
| F6 | 2 |
| F7 | 3 |


#### Calculating an adult fare
Let's look more closely at the definitions in fare_rules.txt.

* F1 applies to any trip that passes through zones (1,2,3).
* F2 applies to any trip that passes through zones (1,2).
* F3 applies to any trip that passes through zones (1,3).
* F4 applies to any trip that passes through zones (2,3).
* F5 applies to any trip that passes through zone 1 only.
* F6 applies to any trip that passes through zone 2 only.
* F7 applies to any trip that passes through zone 3 only.

The trip planner calculates an itinerary, and then looks up the fare rules to determine the fares that apply based on zone. Since F1 also includes travel in zone 1, only F4 ($2.95) applies to a trip from zone 2 to zone 3.

A fare rule only applies when the set of zones passed through in an itinerary exactly matches the set specified by the fare rule. For a trip between zones 2 and 3, the trip planner reports $2.95 as the adult fare.

The public feed from [Portland TriMet](http://developer.trimet.org/GTFS.shtml) provides a real-world illustration of this type of fare structure.
