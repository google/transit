# JaveScript/Node.js

To use the `gtfs-realtime-bindings` JavaScript Node.js classes in your own project, you need to first install [our Node.js npm package](https://www.npmjs.com/package/gtfs-realtime-bindings):

```
npm install gtfs-realtime-bindings
```

These bindings are designed to be used in the [Node.js](https://nodejs.org/) environment, but with some effort, they can probably be used in other JavaScript environments as well.

The following Node.js code snippet demonstrates downloading a GTFS realtime data feed from a particular URL, parsing it as a `FeedMessage` (the root type of the GTFS realtime schema), and iterating over the results.

```javascript
var GtfsRealtimeBindings = require('gtfs-realtime-bindings');
var request = require('request');

var requestSettings = {
  method: 'GET',
  url: 'URL OF YOUR GTFS-REALTIME SOURCE GOES HERE',
  encoding: null
};
request(requestSettings, function (error, response, body) {
  if (!error && response.statusCode == 200) {
    var feed = GtfsRealtimeBindings.transit_realtime.FeedMessage.decode(body);
    feed.entity.forEach(function(entity) {
      if (entity.trip_update) {
        console.log(entity.trip_update);
      }
    });
  }
});
```

For more details, see the [JavaScript / Node.js project page](https://github.com/google/gtfs-realtime-bindings/tree/master/nodejs).
