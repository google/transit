The GTFS Realtime Specification is not set in stone. Instead, it is an open specification developed and maintained by the community of transit agencies, developers, and other stakeholders who use GTFS Realtime. It is expected that this community of producers and consumers of GTFS Realtime data will have proposals for extending the spec to enable new capabilities. To help manage that process, the following procedures and guidelines have been established.

The official specification, reference and documentation are written in English. If a translation to a different language differs from the English original, the latter takes precedence. All communication is performed in English.

## Adding new fields to GTFS Realtime

When a producer or consumer is interested in adding a new field to the GTFS Realtime specification, they should open a new issue on the [GTFS Realtime GitHub repository](https://github.com/google/transit) describing the proposed field and announce this new field (including a link to the issue) on the [GTFS Realtime mailing list](https://groups.google.com/forum/#!forum/gtfs-realtime).

### *Experimental* fields

1. If the community can come to consensus (a) that the proposed field seems useful and (b) on the type of the field (`optional` vs `repeated`, `string` vs `int` vs `bool`), then a field number will be allocated in the GTFS Realtime message and a note will be made in the [.proto file](/gtfs-realtime/proto/gtfs-realtime.proto) and documentation that this is an *experimental* field that may change in the future.
      - Consensus is reached via a discussion and voting process that is the same as the below [Specification amendment process](#specification-amendment-process), but instead of unanimous consent only 80% yes votes are required for approval.
      - GTFS Realtime producers and consumers that wish to use the new *experimental* field will re-generate their library using the .proto file with the new field (e.g., Google will update the [gtfs-realtime-bindings library](https://github.com/google/gtfs-realtime-bindings)), and start populating and parsing the field with live data.
      - Once we are satisfied that the *experimental* field is worthwhile and both producers and consumers are using the field, then we will follow the below [Specification amendment process](#specification-amendment-process) to officially add the field to the spec.
      - If the *experimental* field is not adopted via the [Specification amendment process](#specification-amendment-process) within 2 years of being approved as an *experimental* field, it will be deprecated by adding `[deprecated=true]` next to the field value in the [.proto file](/gtfs-realtime/proto/gtfs-realtime.proto) file.  By using `[deprecated=true]` (instead of `RESERVED`), producers and consumers that have already adopted the field do not have to remove it from use.  Additionally, the field may be "un-deprecated" in the future if it is approved in a subsequent vote following the [Specification amendment process](#specification-amendment-process) (e.g., when additional producers and/or consumers start using the field).
 
1. If the new field is considered specific to a single producer or there is dispute over the data type, then we will assign a [custom extension](#extensions) to the producer so they can use the field in their own feed.  When possible we should avoid extensions and add fields useful to many agencies to the main specification to avoid fragmentation and extra work for consumers to support various extensions to the spec.

### Specification amendment process
1. Create a git branch with update of all relevant parts of protocol definition, specification and documentation files (except for translations).
1. Create pull request on https://github.com/google/transit. Pull request must contain an extended description of the patch. The creator of the pull request becomes the _advocate_.
1. Once pull request is registered, it must be announced by its advocate in the [GTFS Realtime mailing list](https://groups.google.com/forum/#!forum/gtfs-realtime). Once announced, the pull request is considered a proposal.
  	- Since the advocate is a contributor, they must sign the [Contributor License Agreement](../CONTRIBUTING.md) before pull request can be accepted.
1. The discussion of the proposal follows. Pull request comments should be used as the sole discussion forum.
  	- The discussion lasts for as long as the advocate feels necessary, but must be at least 7 calendar days.
  	- The advocate is responsible for timely update of the proposal (i.e. pull request) based on the comments for which they agree to.
  	- At any point in time the advocate can claim proposal abandoned.
1. The advocate can call for a vote on a version of the proposal at any point in time following the initial 7-day interval required for discussion.
    - Before calling for a vote, at least one GTFS-realtime producer and one GTFS-realtime consumer should implement the proposed change. It is expected that the GTFS-realtime producer(s) include the change in a public-facing GTFS-realtime feed and provide a link to that data within the pull request comments, and that the GTFS-realtime consumer(s) provides a link in the pull request comments to an application that is utilizing the change in a non-trivial manner (i.e, it is supporting new or improved functionality).
    - When calling for a vote, the advocate should clearly state whether the vote is for official adoption of the field into the spec or for an experimental field.
1. Vote lasts the minimum period sufficient to cover 7 full calendar days and 5 full Swiss business days. Vote ends at 23:59:59 UTC.
  	- The advocate should announce the specific end time at the start of the vote.
  	- During voting period only editorial changes to the proposal are allowed (typos, wording may change as long as it does not change the meaning).
  	- Anyone is allowed to vote yes/no in a form of comment to the pull request, and votes can be changed until the end of the voting period.
    If a voter changes her vote, it is recommended to do it by updating the original vote comment by striking through the vote and writing the new vote.
  	- Votes before the start of the voting period are not considered.
1. The proposal is accepted if there is a unanimous consensus yes with at least 3 votes.
  	- The proposer's vote does not count towards the 3 vote total. For example, if Proposer X creates a pull request and votes yes, and User Y and Z vote yes, this is counted as 2 total yes votes.
  	- Votes against shall be motivated, and ideally provide actionable feedback.
  	- If the vote has failed, then the advocate may choose to continue work on the proposal, or to abandon the proposal.
    Either decision of the advocate must be announced in the mailing list.
  	- If the advocate continues the work on proposal then a new vote can be called for at any point in time but no later than 30 calendar days after the end of the previous vote.
  	- If a vote was not called within 30 calendar days from the original proposal or 30 calendar days since end of the previous vote, then the proposal is abandoned.
1. If the proposal is abandoned, the corresponding pull request is closed.  Note that the advocate may choose to implement the feature as an [custom extension](#extensions) instead of part of the official spec.
1. If the proposal is accepted:
  	- Google is committed to merging the voted upon version of the pull request (provided that the contributors have signed the [CLA](../CONTRIBUTING.md)), and performing the pull request within 5 business days.
  	- Google is committed to timely updating https://github.com/google/gtfs-realtime-bindings repository. Commits to gtfs-realtime-bindigs that are a result of a proposal, should reference the pull request of the proposal.
  	- Translations must not be included into the original pull request.
    Google is responsible for eventually updating relevant translations into supported languages, but pure translation pull requests from the community are welcome and will be accepted as soon as all editorial comments are addressed.

### Guiding Principles
In order to preserve the original vision of GTFS Realtime, a number of guiding principles have been established to take into consideration when extending the spec:

#### Feeds should be efficient to produce and consume in realtime.
Realtime information is a continuous, dynamic stream of data that necessarily requires efficient processing. We chose Protocol Buffers as the basis for the specification because they offer a good trade-off in terms of ease of use for developers and in terms of efficiency for transmitting data. Unlike GTFS, we do not imagine many agencies will be editing GTFS Realtime feeds by hand. The choice of Protocol Buffers reflects the conclusion that most GTFS Realtime feeds will be produced and consumed programmatically.

#### The spec is about passenger information.
Like GTFS before it, GTFS Realtime is primarily concerned with passenger information. That is, the spec should include information that can help power tools for riders, first and foremost. There is potentially a large amount of operations-oriented information that transit agencies might want to transmit internally between systems. GTFS Realtime is not intended for that purpose and there are potentially other operations-oriented data-standards that may be more appropriate.

#### Changes to the spec should be backwards-compatible.
When adding features to the specification, we want to avoid making changes that will make existing feeds invalid. We don't want to create more work for existing feed publishers until they want to add capabilities to their feeds. Also, whenever possible, we want existing parsers to be able to continue to read the older parts of newer feeds. The conventions for extending Protocol Buffers will enforce backwards-compatibility to a certain extent. However, we wish to avoid semantic changes to existing fields that might break backwards-compatibility as well.

#### Speculative features are discouraged.
Every new feature adds complexity to creating and reading of feeds. Therefore, we want to take care to only add features that we know to be useful. Ideally, any proposal will have been tested by generating data for a real transit system that uses the new feature and writing software to read and display it.

### Extensions
To allow producers to add custom information to a GTFS Realtime feed, we will take advantage of the [Extensions feature of Protocol Buffers](https://developers.google.com/protocol-buffers/docs/proto#extensions). Extensions allow us to define a namespace in a Protocol Buffer message where third-party developers can define additional fields without the need to modify the original proto definition.

When possible we should avoid extensions and add fields useful to many agencies to the main specification to avoid fragmentation and extra work for consumers to support various extensions to the spec.  Before requesting an extension id, producers should propose adding the field to the specification (see [Adding new fields to GTFS Realtime](#adding-new-fields-to-gtfs-realtime))

To create a new extension, we will assign a producer the next available extension id, picked incrementally from a list of numbers starting at 1000 and going up and documented in the Extension Registry section found below.

These assigned extension ids corresponds to the tag ids available in the "extension" namespace for each GTFS Realtime message definition. Now that the developer has an assigned extension id, they will use that id when extending any and all GTFS Realtime messages. Even if the developer only plans to extend a single message, the assigned extension id will be reserved for ALL messages.

For a developer extending the spec, instead of adding a single field like a "string" or "int32" with their extension id, the preferred model is to define a new message like "MyTripDescriptorExtension", extend the underlying GTFS Realtime message with your new message, and then put all your new fields in there. This has the nice property that you can manage fields within your extension message however you want, without needing to reserve a new extension id from the master list.

```
message MyTripDescriptorExtension {
  optional string some_string = 1;
  optional bool some_bool = 2;
  ...
}
extend transit_realtime.TripDescriptor {
  optional MyTripDescriptorExtension my_trip_descriptor = YOUR_EXTENSION_ID;
}
```

### Extension Registry

|Extension ID|Developer|Contact|Details|
|------------|---------|-------|-------|
|1000|OneBusAway|[onebusaway-developers](http://groups.google.com/group/onebusaway-developers)|https://github.com/OneBusAway/onebusaway/wiki/GTFS-Realtime-Resources|
|1001|New York City MTA|[mtadeveloperresources](http://groups.google.com/group/mtadeveloperresources)|http://mta.info/developers/|
|1002|Google|[transit-realtime-partner-support@google.com](mailto:transit-realtime-partner-support@google.com)|Google Maps Live Transit Updates|
|1003|OVapi|gtfs-rt at ovapi.nl|http://gtfs.ovapi.nl|
|1004|Metra|[William Ashbaugh <w.l.ashbaugh@gmail.com>](mailto:w.l.ashbaugh@gmail.com)|
|1005|Metro-North Railroad|[John Larsen](mailto:mnrappdev@mnr.org)|
|1006|realCity|[David Varga](mailto:transit@realcity.io)|http://realcity.io|
|1007|NSW TrainLink|[Gregory Nicholls](mailto:gregory.nicholls@transport.nsw.gov.au)|[Group discussion](https://groups.google.com/d/msg/gtfs-realtime/G75O1zyQS_Q/VtNmTJvSAwAJ)|
|1008|SEPTA - Southeastern Pennsylvania Transportation Authority|[Gregory Apessos](mailto:GApessos@septa.org)|https://github.com/septadev|
|1009|Swiftly|[mike@goswift.ly](mailto:mike@goswift.ly)|[Group Discussion](https://groups.google.com/forum/#!msg/gtfs-realtime/mmnZV6L-2ls/wVWdknhLBwAJ)|
|1010|IBI Group|[Ritesh Warade](mailto:transitrealtime@ibigroup.com)|[GitHub proposal for new timestamps in Service Alerts](https://github.com/google/transit/pull/134)|
