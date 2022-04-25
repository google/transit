Las actualizaciones de viaje representan fluctuaciones en el horario. Se espera recibirlas de todos los viajes programados que puedan proporcionarlas en tiempo real. Estas actualizaciones brindarían un horario de llegada o salida previsto para las paradas a lo largo de la ruta. Las actualizaciones de viaje también pueden prever escenarios más complejos en los cuales se cancelen o agreguen viajes al programa, o incluso se redirijan.

**Recordatorio:** En [GTFS](https://developers.google.com/transit/gtfs/), un viaje es una secuencia de dos o más paradas que tienen lugar a una hora específica.

Debe haber **como máximo** una actualización de viaje para cada viaje programado. En caso de no ser así, se concluirá que no hay datos en tiempo real disponibles para dicho viaje. El consumidor de datos **no** debe asumir que el viaje se está realizando de manera puntual.

## Actualizaciones de horario de paradas

Una actualización de viaje comprende una o más actualizaciones de los horarios de parada del vehículo, conocidas como [StopTimeUpdates](reference.md#StopTimeUpdate). Pueden proporcionarse para horarios de paradas pasados y futuros. Se permite brindar horarios de parada pasados, pero no es obligatorio hacerlo. En el caso de que se haga, ten en cuenta que no se debe proporcionar una actualización pasada si se refiere a un viaje todavía no programado para haber terminado (es decir, que finalizó antes de lo programado), ya que, de lo contrario, se concluirá que no hay actualización de ese viaje.

Cada [StopTimeUpdate](reference.md#StopTimeUpdate) está vinculada a una parada. Normalmente esto se puede hacer usando un GTFS stop_sequence o un GTFS stop_id. Sin embargo, en caso de que estés suministrando una actualización para un viaje sin un trip_id de GTFS, debes especificar el stop_id, ya que stop_sequence no tiene valor. El stop_id todavía debe hacer referencia a un stop_id en GTFS.

La actualización puede proporcionar un horario exacto para la **llegada** o la **salida** en una parada en [StopTimeUpdates](reference.md#StopTimeUpdate) mediante [StopTimeEvent](reference.md#StopTimeUpdate). Este debe contener un **horario** absoluto o un **retraso** (es decir, una compensación desde el horario programado en segundos). El retraso solo se puede utilizar en caso de que la actualización de viaje se refiera a un viaje de GTFS programado, en contraposición con un viaje basado en la frecuencia. En este caso, el horario debe ser igual al horario programado + el retraso. También se debe especificar la **incertidumbre** de la predicción junto con [StopTimeEvent](reference.md#StopTimeUpdate), que se analiza más detalladamente más abajo, en la sección [Incertidumbre](#Incertidumbre).

Para cada [StopTimeUpdate](reference.md#StopTimeUpdate), la relación de programación predeterminada es **programada**. (Ten en cuenta que ésta es diferente a la relación de programación para el viaje). Puedes cambiarla a **omitida** si la parada no se va a utilizar o a **sin datos** si solo tienes datos en tiempo real para parte del viaje.

**Las actualizaciones se deben clasificar por stop_sequence** (o stop_id, en el orden en que tienen lugar en el viaje).

Si faltan una o más paradas a lo largo del viaje, la actualización se propaga a todas las paradas subsiguientes. Esto significa que, en caso de no haber otra información, al actualizar un horario de parada para una cierta parada se cambiarán todas las paradas subsiguientes.

**Ejemplo 1**

Para un viaje con 20 paradas, una [StopTimeUpdate](reference.md#StopTimeUpdate) con retraso de llegada y retraso de salida de 0 ([StopTimeEvents](reference.md#StopTimeEvent)) para la stop_sequence de la parada actual, significa que el viaje está exactamente a horario.

**Ejemplo 2**

Para la misma instancia de viaje, se proporcionan tres [StopTimeUpdates](reference.md#StopTimeUpdate):

*   retraso de 300 segundos para la stop_sequence 3.
*   retraso de 60 segundos para la stop_sequence 8.
*   retraso de duración no especificada para la stop_sequence 10.

Esto se interpretará como:

*   las stop_sequences 3,4,5,6,7 tienen un retraso de 300 segundos.
*   las stop_sequences 8,9 tienen un retraso de 60 segundos.
*   las stop_sequences 10,..,20 tienen un retraso desconocido.

### Descriptor de viajes

La información suministrada por el descriptor de viajes depende de la relación de programación del viaje que estás actualizando. Hay varias opciones que puedes configurar:

| _**Valor**_ | _**Comentario**_ |
|-------------|------------------|
| **Programado** | Este viaje se está ejecutando de acuerdo con un programa de GTFS o se asemeja lo suficiente como para seguir estando asociado a él. |
| **Agregado** | Este viaje no estaba programado y se ha agregado. Por ejemplo, para satisfacer la demanda o reemplazar un vehículo averiado. |
| **Sin programar** | Este viaje está teniendo lugar, pero nunca está asociado con horario alguno. Por ejemplo, si no hay programa y los autobuses operan en un servicio de traslados. |
| **Cancelado** | Este viaje se programó pero ahora está eliminado. |

En la mayoría de los casos, se debe proporcionar el trip_id del viaje programado en GTFS con el que se relaciona esta actualización. En caso de que no se pueda vincular esta actualización con un viaje en GTFS, se puede brindar un route_id de GTFS, y una fecha y hora de inicio para el viaje. Generalmente, este es el caso de los viajes agregados, los que están sin programar y de algunos tipos de viajes de reemplazo.

## Incertidumbre

La incertidumbre se aplica tanto al horario como al valor de retraso de una [StopTimeUpdate](reference.md#StopTimeUpdate). La incertidumbre especifica, en términos generales, el error esperado en el retraso real como un entero en segundos (pero ten en cuenta que el significado estadístico concreto todavía no está definido). Es posible que la incertidumbre sea 0, por ejemplo, para los trenes conducidos bajo control de horarios por computadora.

Por ejemplo, un autobús de larga distancia que tiene un retraso estimado de 15 minutos y llega a su siguiente parada con una ventana de error de 4 minutos (es decir, +2/-2 minutos) tendrá una incertidumbre de 240.
