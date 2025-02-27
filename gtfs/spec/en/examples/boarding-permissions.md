## Introduction

The examples below describe how to use `stop_times.txt` and `boarding_permissions.txt` effectively to describe where and when passengers can bring a vehicle on board.

### Example: London Underground

London Underground does not allow bicycles to be carried in the "deep tube" sections of the network, and only allows bicycles to be carried outside peak hours on Monday to Friday.

These can be specified in the following way, using trips on the Jubilee line as an example where the "deep tube" runs between Finchley Road and Canning Town:

`stop_times.txt`

| `trip_id` | `service_id` | `stop_id`       | `stop_sequence` | `boarding_permission_id` |
|-----------|--------------|-----------------|-----------------|--------------------------|
| 924       | Mon to Fri   | Stanmore        | `0`             | `tfl_weekday`            |
| 924       | Mon to Fri   | Canons Park     | `1`             | `tfl_weekday`            |
| ...       | ...          | ...             | ...             | ...                      |
| 924       | Mon to Fri   | West Hampstead  | `9`             | `tfl_weekday`            |
| 924       | Mon to Fri   | Finchley Road   | `10`            | `deep_tube`              |
| 924       | Mon to Fri   | Swiss Cottage   | `11`            | `deep_tube`              |
| 924       | ...          | ...             | ...             | ...                      |
| 924       | Mon to Fri   | North Greenwich | `23`            | `deep_tube`              |
| 924       | Mon to Fri   | Canning Town    | `24`            | `tfl_weekday`            |
| 924       | Mon to Fri   | West Ham        | `25`            | `tfl_weekday`            |
| 924       | Mon to Fri   | Stratford       | `26`            | `tfl_weekday`            |
| 925       | Sun          | Stanmore        | `0`             | `tfl_weekend`            |
| 925       | Sun          | Canons Park     | `1`             | `tfl_weekend`            |
| ...       | ...          | ...             | ...             | ...                      |
| 925       | Sun          | West Hampstead  | `9`             | `tfl_weekend`            |
| 925       | Sun          | Finchley Road   | `10`            | `deep_tube`              |
| 925       | Sun          | Swiss Cottage   | `11`            | `deep_tube`              |
| 925       | ...          | ...             | ...             | ...                      |
| 925       | Sun          | North Greenwich | `23`            | `deep_tube`              |
| 925       | Sun          | Canning Town    | `24`            | `tfl_weekend`            |
| 925       | Sun          | West Ham        | `25`            | `tfl_weekend`            |
| 925       | Sun          | Stratford       | `26`            | `tfl_weekend`            |

`boarding_permissions.txt`

| `boarding_permission_id` | `vehicle` | `carriage_permission` | `start_time` | `end_time` |
|--------------------------|-----------|-----------------------|--------------|------------|
| tfl_weekday              | `1`       | `1`                   | `07:30:00`   | `09:30:00` |
| tfl_weekday              | `1`       | `1`                   | `16:00:00`   | `19:00:00` |
| tfl_weekday              | `1`       | `0`                   |              |            |
| tfl_weekend              | `1`       | `0`                   |              |            |
| deep_tube                | `1`       | `1`                   |              |            |

In the above table, `deep_tube` is used for all stop times where bikes cannot be carried further at any time,
`tfl_weekday` is used for all stop times where bikes cannot be carried during peak hours, but can be carried at other times without reservation,
and `tfl_weekend` is used for all stop times where bikes can be freely carried.

### Example: ferries which do not accept foot passengers

The following ferry does not accept foot passengers. Passengers with a bike or a motorcycle can turn up without making a reservation,
but passenger with a car must book with the agency to arrange pick up and drop off at specific piers.

`stop_times.txt`

| `trip_id` | `stop_id` | `stop_sequence` | `pickup_type` | `drop_off_type` | `boarding_permission_id` |
|-----------|-----------|-----------------|---------------|-----------------|--------------------------|
| X         | A         | 0               | 1             | 1               | ferry                    |
| X         | B         | 1               | 1             | 1               | ferry                    |
| X         | C         | 2               | 1             | 1               | ferry                    |
| X         | D         | 3               | 1             | 1               | ferry                    |
| X         | E         | 4               | 1             | 1               | ferry                    |

`boarding_permissions.txt`

| `boarding_permission_id` | `vehicle` | `pickup_permission` | `drop_off_permission` |
|--------------------------|-----------|---------------------|-----------------------|
| ferry                    | 1         | 0                   | 0                     |
| ferry                    | 2         | 0                   | 0                     |
| ferry                    | 3         | 2                   | 2                     |