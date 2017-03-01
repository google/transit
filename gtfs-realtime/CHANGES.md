The GTFS Realtime Specification is not set in stone. Instead, it is an open specification developed and maintained by the community of transit agencies, developers, and other stakeholders who use GTFS Realtime. It is expected that this community of producers and consumers of GTFS Realtime data will have proposals for extending the spec to enable new capabilities. To help manage that process, the following procedures and guidelines have been established.

### Specification amendment process
The official specification, reference and documentation are written in English. If a translation to a different language differs from the English original, the latter takes precedence. All communication is performed in English.

1. Create a git branch with update of all relevant parts of protocol definition, specification and documentation files (except for translations).
1. Create pull request on https://github.com/google/transit. Pull request must contain an extended description of the patch. The creator of the pull request becomes the _advocate_.
1. Once pull request is registered, it must be announced by its advocate in the [GTFS Realtime mailing list](https://groups.google.com/forum/#!forum/gtfs-realtime). Once announced, the pull request is considered a proposal.
  - Since the advocate is a contributor, they must sign the [Contributor License Agreement](../CONTRIBUTING.md) before pull request can be accepted.
1. The discussion of the proposal follows. Pull request comments should be used as the sole discussion forum.
  - The discussion lasts for as long as the advocate feels necessary, but must be at least 7 calendar days.
  - The advocate is responsible for timely update of the proposal (i.e. pull request) based on the comments for which they agree to.
  - At any point in time the advocate can claim proposal abandoned.
1. The advocate can call for a vote on a version of the proposal at any point in time following the initial 7-day interval required for discussion.
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
1. If the proposal is abandoned, the corresponding pull request is closed.
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

We will make use of extensions, described in the following section, to support new features. GTFS Realtime producers and consumers can first test a new feature in the extension space. When the feature is ready for official adoption, we will add the feature to the official GTFS Realtime proto definition itself.

### Extensions
To facilitate the testing of new features and to allow developers to add extra information to a GTFS Realtime feed, we will take advantage of the [Extensions feature of Protocol Buffers](https://developers.google.com/protocol-buffers/docs/proto#extensions). Extensions allow us to define a namespace in a Protocol Buffer message where third-party developers can define additional fields without the need to modify the original proto definition.

When a developer is interested in extending the GTFS Realtime Specification, they should contact the [GTFS Realtime mailing list](https://groups.google.com/forum/#!forum/gtfs-realtime) and we will assign them the next available extension id, picked incrementally from a list of numbers starting at 1000 and going up and documented in the Extension Registry section found below.

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
