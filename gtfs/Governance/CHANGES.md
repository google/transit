>**Governance Framework Transition**
>- **As of July 7, 2025**, all new Pull Requests are subject to the **[new GTFS Schedule Governance Framework](introduction.md)**.
>- Pull Requests opened **before July 7, 2025** will continue to follow the **Former Governance** outlined in this section.
>   - This includes the following PRs: [567](https://github.com/google/transit/pull/567), [561](https://github.com/google/transit/pull/561), [556](https://github.com/google/transit/pull/556), [546](https://github.com/google/transit/pull/546), [545](https://github.com/google/transit/pull/545), [533](https://github.com/google/transit/pull/533), [515](https://github.com/google/transit/pull/515), [502](https://github.com/google/transit/pull/502), [498](https://github.com/google/transit/pull/498), [483](https://github.com/google/transit/pull/483), [423](https://github.com/google/transit/pull/423).
>- Once all PRs opened prior to July 7, 2025 are resolved, this page and the process outlined in it will be fully deprecated.

The GTFS Specification is not set in stone. Instead, it is an open specification developed and maintained by the community of transit agencies, developers, and other stakeholders who use GTFS. It is expected that this community of producers and consumers of GTFS data will have proposals for extending the spec to enable new capabilities. To help manage that process, the following procedures and guidelines have been established.

### Specification amendment process
The official specification, reference and documentation are written in English. If a translation to a different language differs from the English original, the latter takes precedence. All communication is performed in English.

1. Create a git branch with update of all relevant parts of protocol definition, specification and documentation files (except for translations).
1. Create pull request on https://github.com/google/transit. Pull request must contain an extended description of the patch. The creator of the pull request becomes the _advocate_.
1. Once pull request is registered, it must be announced by its advocate in the [GTFS Changes mailing list](https://groups.google.com/forum/#!forum/gtfs-changes), including a link to the pull request. Once announced, the pull request is considered a proposal.  The pull request should also be edited to contain a link to the Google Groups announcement so they can easily be cross-referenced.
  	- Since the advocate is a contributor, they must sign the [Contributor License Agreement](../../CONTRIBUTING.md) before pull request can be accepted.
1. The discussion of the proposal follows. Pull request comments should be used as the sole discussion forum.
  	- The discussion lasts for as long as the advocate feels necessary, but must be at least 7 calendar days.
  	- The advocate is responsible for timely update of the proposal (i.e. pull request) based on the comments for which they agree to.
  	- At any point in time the advocate can claim proposal abandoned.
1. The advocate can call for a vote on a version of the proposal at any point in time following the initial 7-day interval required for discussion.
  	- Before calling for a vote, at least one GTFS producer and one GTFS consumer should implement the proposed change.  It is expected that the GTFS producer(s) include the change in a public-facing GTFS feed and provide a link to that data within the pull request comments, and that the GTFS consumer(s) provides a link in the pull request comments to an application that is utilizing the change in a non-trivial manner (i.e, it is supporting new or improved functionality).
1. Vote lasts the minimum period sufficient to cover 14 full calendar days. Vote ends at 23:59:59 UTC.
  	- The advocate should announce the specific end time at the start of the vote.
  	- During voting period only editorial changes to the proposal are allowed (typos, wording may change as long as it does not change the meaning).
  	- Anyone is allowed to vote yes/no in a form of comment to the pull request, and votes can be changed until the end of the voting period.
    If a voter changes her vote, it is recommended to do it by updating the original vote comment by striking through the vote and writing the new vote.
  	- Votes before the start of the voting period are not considered.
	- Opening and closing of votes must be announced on the [GTFS Changes mailing list](https://groups.google.com/forum/#!forum/gtfs-changes).
1. The proposal is accepted if there is a unanimous consensus yes with at least 3 votes.
  	- The proposer's vote does not count towards the 3 vote total. For example, if Proposer X creates a pull request and votes yes, and User Y and Z vote yes, this is counted as 2 total yes votes.
  	- Votes against shall be motivated, and ideally provide actionable feedback.
  	- If the vote has failed, then the advocate may choose to continue work on the proposal, or to abandon the proposal.
    Either decision of the advocate must be announced in the [GTFS Changes mailing list](https://groups.google.com/forum/#!forum/gtfs-changes).
  	- If the advocate continues the work on proposal then a new vote can be called for at any point in time.
1. Any pull request remaining inactive for 30 calendar days will be closed. When a pull request is closed, the corresponding proposal is considered abandoned. The advocate may reopen the pull request at any time if they wish to continue or maintain the conversation.
1. If the proposal is accepted:
  	- Google is committed to merging the voted upon version of the pull request (provided that the contributors have signed the [CLA](../../CONTRIBUTING.md)), and performing the pull request within 5 business days.
  	- Translations must not be included into the original pull request.
    Google is responsible for eventually updating relevant translations into supported languages, but pure translation pull requests from the community are welcome and will be accepted as soon as all editorial comments are addressed.
1. The final result of the pull request (accepted or abandoned) should be announced on the same Google Groups thread where the pull request was originally announced.

### Guiding Principles
In order to preserve the original vision of GTFS, a number of guiding principles have been established to take into consideration when extending the spec:

#### Feeds should be easy to create and edit
We chose CSV as the basis for the specification because it's easy to view and edit using spreadsheet programs and text editors, which is helpful for smaller agencies. It's also straightforward to generate from most programming languages and databases, which is good for publishers of larger feeds.

#### Feeds should be easy to parse
Feed readers should be able to extract the information they're looking for with as little work as possible. Changes and additions to the feed should be as broadly useful as possible, to minimize the number of code paths that readers of the feed need to implement. (However, making creation easier should be given precedence, since there will ultimately be more feed publishers than feed readers.)

#### The spec is about passenger information
GTFS is primarily concerned with passenger information. That is, the spec should include information that can help power tools for riders, first and foremost. There is potentially a large amount of operations-oriented information that transit agencies might want to transmit internally between systems. GTFS is not intended for that purpose and there are potentially other operations-oriented data-standards that may be more appropriate.

#### Changes to the spec should be backwards-compatible
When adding features to the specification, we want to avoid making changes that will make existing feeds invalid. We don't want to create more work for existing feed publishers until they want to add capabilities to their feeds. Also, whenever possible, we want existing parsers to be able to continue to read the older parts of newer feeds.

#### Speculative features are discouraged
Every new feature adds complexity to the creation and reading of feeds. Therefore, we want to take care to only add features that we know to be useful. Ideally, any proposal will have been tested by generating data for a real transit system that uses the new feature and writing software to read and display it. Note that the GTFS readily allows for extensions to the format through the addition of extra columns and files that are ignored by the official parsers & validators, so proposals can be easily prototyped and tested on existing feeds.