# PHP

To use the `gtfs-realtime-bindings` PHP classes in your own project, you need to first add a dependency for the [google/gtfs-realtime-bindings](https://packagist.org/packages/google/gtfs-realtime-bindings) package in your [Composer-based](https://getcomposer.org/) PHP project.

In the `require` section of your composer.json file, add the dependency:

```json
"require": {
  "google/gtfs-realtime-bindings": "x.y.z"
}
```

Where `x.y.z` is the latest release version of the [package](https://packagist.org/packages/google/gtfs-realtime-bindings).

The following code snippet demonstrates downloading a GTFS realtime data feed from a particular URL, parsing it as a `FeedMessage` (the root type of the GTFS realtime schema), and iterating over the results.

```php
require_once 'vendor/autoload.php';

use transit_realtime\FeedMessage;

$data = file_get_contents("URL OF YOUR GTFS-REALTIME SOURCE GOES HERE");
$feed = new FeedMessage();
$feed->parse($data);
foreach ($feed->getEntityList() as $entity) {
  if ($entity->hasTripUpdate()) {
    error_log("trip: " . $entity->getId());
  }
}
```

For more details, see the [PHP project page](https://github.com/google/gtfs-realtime-bindings-php).
