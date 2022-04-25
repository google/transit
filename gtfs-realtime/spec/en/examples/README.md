### Plain text feed examples

The following examples show a textual representation of feeds. During development it is more convenient to produce ASCII protocol buffer output for easier debugging. You can compare your text output with these examples to check for the validity of data.

*   [Alerts](alerts.asciipb)
*   [Trip update (full dataset)](trip-updates-full.asciipb)

### Migration guides

The following migration guides can help consumers and producers transition from "unofficial" practices to new "official" features of the spec:
* [Transition from ADDED to DUPLICATED trips](migration-duplicated.md) - A duplicated trip is new trip that is the same as an existing scheduled trip except for service start date and time. This [migration guide](migration-duplicated.md) defines how existing producers and consumers that were using the `ADDED` enumeration to represent duplicated trips should transition to the `DUPLICATED` enumeration. 