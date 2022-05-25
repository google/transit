# Ruby

To use the `gtfs-realtime-bindings` classes in your own project, you need to first install [Ruby gem](https://rubygems.org/gems/gtfs-realtime-bindings):

```
gem install gtfs-realtime-bindings
```

The following code snippet demonstrates downloading a GTFS realtime data feed from a particular URL, parsing it as a `FeedMessage` (the root type of the GTFS realtime schema), and iterating over the results.

```ruby
require 'protobuf'
require 'google/transit/gtfs-realtime.pb'
require 'net/http'
require 'uri'

data = Net::HTTP.get(URI.parse("URL OF YOUR GTFS-REALTIME SOURCE GOES HERE"))
feed = Transit_realtime::FeedMessage.decode(data)
for entity in feed.entity do
  if entity.field?(:trip_update)
    p entity.trip_update
  end
end
```

For more details, see the [Ruby project page](https://github.com/google/gtfs-realtime-bindings/tree/master/ruby).