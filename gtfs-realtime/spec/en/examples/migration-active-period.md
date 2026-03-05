## Migration Guide - Transition from active_period to communication_period and impact_period 

The GTFS-realtime `alert.active_period` was defined as *“Time when the alert should be shown to the user. If missing, the alert will be shown as long as it appears in the feed. If multiple ranges are given, the alert will be shown during all of them.”*

There was an ambiguity in this definition where the “time when the alert should be shown to the user” can be construed both as:
- Time when the user is informed of the alert.
- Time when the service disruption resulting from the alert is in effect.

To resolve this ambiguity, `communication_period` and `impact_period` are introduced.
- `communication_period`: Time when the alert should be shown to the user strictly for informative reasons.
- `impact_period`: Time when the services are affected by the alert.

To ensure the implementation of the new fields while keeping backward compatibility and taking into consideration infrastructure costs, the community agreed to assign `active_period` as deprecated but allow it to coexist with `communication_period` and `impact_period`.

This migration guide defines how to interpret the coexistence of all 3 fields together, and outlines steps for gradual migration into the new fields `communication_period` and `impact_period`. The goal is to convince producers and consumers to gradually start using `communication_period` and `impact_period` instead of `active_period`.

## Producers
For producers, you can continue having all 3 fields in the same alert. Try to specify `communication_period` and `impact_period` in as many alerts as you can, especially alerts with NO_SERVICE. 

**Do not duplicate alerts to separate active_period from the new fields!** Set one alert per actual service incident, you can specify `communication_period`, ‘impact_period` and `active_period`.

Whenever an alert has `communication_period` and `impact_period` specified, it is recommended to not include `active_period` (it is already an optional field).

To promote best practices, it is recommended to specify `communication_period` and `impact_period` together as much as possible.

All of the following examples are valid.
### The recommended option

````
alert {
“communication_period”: [{ "start": …, "end": … } ], ← Time when the user is informed of the alert.
"impact_period": [ { "start": …, "end": … } ], ← Time when the service disruption resulting from the alert is in effect. Can be multiple time periods if the service disruption is recurring.
...
}
````

### Other valid options that are not recommended

````
alert {
“active_period”: [{ "start": …, "end": … } ],
“communication_period”: [{ "start": …, "end": … } ],
"impact_period": [ { "start": …, "end": … } ],
...
} 
````


````
alert {
“active_period”: [{ "start": …, "end": … } ],
"impact_period": [ { "start": …, "end": … } ],
...
} 
````


````
alert {
“active_period”: [{ "start": …, "end": … } ],
“communication_period”: [{ "start": …, "end": … } ],
...
} 
````


````
alert {
“active_period”: [{ "start": …, "end": … } ],
...
} 
````


````
alert {
“communication_period”: [{ "start": …, "end": … } ],
...
} 
````


````
alert {
“impact_period”: [{ "start": …, "end": … } ],
...
} 
````

It is suggested that you notify existing consumers (e.g., via a developer mailing list) that the use of `active_period` is being deprecated by a set deadline and that consumers should start using `commnication_period` and `impact_period` instead. This migration guide should be included, with an emphasis on the *"Consumer"* section. After the deadline passes, you can remove `active_period` entities from your feed and publish only the `commnication_period` and `impact_period`.

## Consumers

For consumers, you can interpret the fields based on their spec definition.
- If `active_period` exists with `communication_period` and `impact_period`, **ignore `active_period`** and use the other two fields.

- If `active_period` exists with `impact_period`, **ignore `active_period`** and do not interpret it as `communication_period`.

- If `active_period` exists with `communication_period`, **ignore `active_period`** and do not interpret it as `impact_period`.

- If `active_period` exists alone, then use it.
