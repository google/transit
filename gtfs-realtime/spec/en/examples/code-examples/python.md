# Python

To use the `gtfs-realtime-bindings` Python classes in your own project, you need to first install the module from the [PyPI repository](https://pypi.python.org/pypi/gtfs-realtime-bindings).

```python
# Using easy_install
easy_install --upgrade gtfs-realtime-bindings

# Using pip
pip install --upgrade gtfs-realtime-bindings
```

The following code snippet demonstrates downloading a GTFS-realtime data feed from a particular URL, parsing it as a `FeedMessage` (the root type of the GTFS-realtime schema), and iterating over the results.

```python
from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.urlopen('URL OF YOUR GTFS-REALTIME SOURCE GOES HERE')
feed.ParseFromString(response.read())
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print entity.trip_update
```

For more details, see the [Python project page](https://github.com/google/gtfs-realtime-bindings/tree/master/python).
