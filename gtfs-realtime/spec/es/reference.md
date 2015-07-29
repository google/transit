Un feed GTFS en tiempo real permite que las empresas de transporte público brinden a los consumidores información en tiempo real acerca de las interrupciones de sus servicios (estaciones cerradas, líneas que no funcionan, demoras importantes, etc.), la ubicación de sus vehículos y tiempos de llegada esperados. 

Las especificaciones de la versión 1.0 del feed se abordan y documentan en este sitio.

### Definiciones de términos

*   **obligatorio**: uno
*   **repetido**: cero o más
*   **mensaje**: tipo complejo
*   **enum.**: lista de valores fijos

## Índice de elementos

*   [FeedMessage](#FeedMessage)
    *   [FeedHeader](#FeedHeader)
        *   [Incrementality](#Incrementality)
    *   [FeedEntity](#FeedEntity)
        *   [TripUpdate](#TripUpdate)
            *   [TripDescriptor](#TripDescriptor)
                *   [ScheduleRelationship](#ScheduleRelationship_TripDescriptor)
            *   [VehicleDescriptor](#VehicleDescriptor)
            *   [StopTimeUpdate](#StopTimeUpdate)
                *   [StopTimeEvent](#StopTimeEvent)
                *   [ScheduleRelationship](#ScheduleRelationship_StopTimeUpdate)
        *   [VehiclePosition](#VehiclePosition)
            *   [TripDescriptor](#TripDescriptor)
                *   [ScheduleRelationship](#ScheduleRelationship_TripDescriptor)
            *   [Position](#Position)
        *   [Alert](#Alert)
            *   [TimeRange](#TimeRange)
            *   [EntitySelector](#EntitySelector)
                *   [TripDescriptor](#TripDescriptor)
                    *   [ScheduleRelationship](#ScheduleRelationship_TripDescriptor)
            *   [Cause](#Cause)
            *   [Effect](#Effect)
            *   [TranslatedString](#TranslatedString)
                *   [Translation](#Translation)

# Elementos

## _mensaje_ FeedMessage

El contenido de un mensaje de feed. Cada mensaje en el flujo de datos se obtiene como una respuesta a una solicitud HTTP GET adecuada. Un feed en tiempo real siempre se define en relación con un feed GTFS existente. Todos los ID de entidades se resuelven en relación con el feed GTFS. 

Un feed depende de algunas configuraciones externas:

*   El feed GTFS correspondiente.
*   La aplicación del feed (actualizaciones, posiciones o alertas). Un feed debe contener únicamente elementos de las aplicaciones correspondientes; todas las otras entidades se ignorarán.
*   Frecuencia de sondeo, controlada por min_update_delay, max_update_delay.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **header** | [FeedHeader](#FeedHeader) | obligatorio | Metadatos sobre este feed y mensaje del feed |
| **entity** | [FeedEntity](#FeedEntity) | repetido | Contenido del feed |

## _mensaje_ FeedHeader

Metadatos sobre un feed, incluido en los mensajes del feed

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **gtfs_realtime_version** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | obligatorio | Especificación de la versión del feed. La versión actual es 1.0. |
| **incrementality** | [Incrementality](#Incrementality) | opcional |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Esta marca de tiempo identifica el momento en que se ha creado el contenido de este feed (en la hora del servidor). En la hora de POSIX (es decir, cantidad de segundos desde el 1.° de enero de 1970 00:00:00 UTC). Para evitar el desvío de tiempos entre los sistemas que producen y que consumen información en tiempo real, se recomienda derivar la marca de tiempo desde un servidor de tiempo. Es absolutamente aceptable usar servidores de estrato 3 o, incluso, inferiores, porque las diferencias de tiempo de hasta un par de segundos son tolerables. |

## _enum._ Incrementality

Determina si la búsqueda actual es incremental.

*   **FULL_DATASET**: la actualización de este feed sobrescribirá toda la información en tiempo real anterior para el feed. Por lo tanto, se espera que esta actualización proporcione un resumen completo de toda la información en tiempo real conocida.
*   **DIFFERENTIAL**: en este momento, este modo **no está admitido** y su comportamiento **no se especifica** para los feeds que usan este modo. Existen debates sobre la [lista de correo](http://groups.google.com/group/gtfs-realtime) de GTFS en tiempo real, relacionados con la especificación completa del comportamiento del modo DIFFERENTIAL, y la documentación se actualizará cuando esos debates finalicen.

### Valores

| _**Valor**_ |
|-------------|
| **FULL_DATASET** |
| **DIFFERENTIAL** |

## _mensaje_ FeedEntity

La definición (o actualización) de una entidad en el feed de transporte público. Si la entidad no se elimina, uno de los campos "trip_update", "vehicle" y "alert" debe completarse.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | obligatorio | Identificador único del feed para esta entidad. Los identificadores se usan solamente para proporcionar soporte de incrementalidad. Las entidades reales a las que hace referencia el feed deben especificarse mediante selectores explícitos (ver EntitySelector más adelante para obtener más información). |
| **is_deleted** | [bool](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Establece si esta entidad debe eliminarse. Es relevante solo para las búsquedas incrementales. |
| **trip_update** | [TripUpdate](#TripUpdate) | opcional | Datos sobre las demoras de salida en tiempo real de un viaje. |
| **vehicle** | [VehiclePosition](#VehiclePosition) | opcional | Datos sobre la posición en tiempo real de un vehículo. |
| **alert** | [Alert](#Alert) | opcional | Datos sobre las alertas en tiempo real. |

## _mensaje_ TripUpdate

Actualización en tiempo real del progreso de un vehículo en un viaje. También consulta el debate general del [tipo de feed de actualizaciones del viaje](./trip-updates).

Según el valor de ScheduleRelationship, TripUpdate puede especificar lo siguiente:

*   Un viaje que avanza según la programación.
*   Un viaje que avanza por una ruta, pero que no tiene una programación fija.
*   Un viaje que se ha agregado o se ha quitado en relación con una programación.

Las actualizaciones pueden ser para eventos de llegada/salida futuros y previstos, o para eventos pasados que ya ocurrieron. En la mayoría de los casos, la información sobre los eventos pasados es un valor medido, por lo tanto, se recomienda que su valor de incertidumbre sea 0\. Aunque puede haber algunos casos en que esto no sea así, por lo que se admiten valores de incertidumbre distintos de 0 para los eventos pasados. Si el valor de incertidumbre de una actualización no es 0, entonces la actualización es una predicción aproximada para un viaje que no se ha completado o la medición no es precisa o la actualización fue una predicción para el pasado que no se ha verificado después de que ocurrió el evento. 

Ten en cuenta que la actualización puede describir un viaje que ya se ha completado. En este caso, es suficiente con proporcionar una actualización para la última parada del viaje. Si el tiempo de llegada para la última parada es en el pasado, el cliente concluirá que todo el viaje es pasado (es posible, aunque inconsecuente, proporcionar también actualizaciones para las paradas anteriores). Esta opción es más relevante para un viaje que se ha completado antes de lo que establecía la programación, pero que según esta, el viaje todavía se está realizando en este momento. Quitar las actualizaciones de este viaje podría hacer que el cliente considere que el viaje todavía se está realizando. Ten en cuenta que el proveedor del feed tiene permitido, aunque no está obligado, a purgar las actualizaciones pasadas (en este caso esto sería útil).

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **trip** | [TripDescriptor](#TripDescriptor) | obligatorio | El viaje al cual se aplica este mensaje. Puede haber una entidad de TripUpdate, como máximo, para cada instancia de viaje real. Si no hay ninguna, entonces no habrá información de predicciones disponible. *No* significa que el viaje se está realizando de acuerdo con la programación. |
| **vehicle** | [VehicleDescriptor](#VehicleDescriptor) | opcional | Información adicional sobre el vehículo con el cual se está realizando este viaje. |
| **stop_time_update** | [StopTimeUpdate](#StopTimeUpdate) | repetido | Las actualizaciones de StopTimes para el viaje (futuras, como las predicciones, y, en algunos casos, pasadas, es decir, aquellas que ya ocurrieron). Las actualizaciones deben ordenarse por secuencia de parada y deben aplicarse a todas las siguientes paradas del viaje hasta la próxima especificada. |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Momento en el que se midió el progreso en tiempo real del vehículo. En tiempo de POSIX (es decir, la cantidad de segundos desde el 1.° de enero de 1970 00:00:00 UTC). |

## _mensaje_ StopTimeEvent

Información de horarios para un único evento previsto (sea la llegada o la salida). Los horarios consisten en la información sobre demoras o tiempos estimados y la incertidumbre.

*   La demora (delay) debe usarse cuando la predicción se realiza con relación a una programación existente en GTFS.
*   El tiempo (time) debe darse aunque no haya una programación prevista. Si se especifican tanto el tiempo como la demora, el tiempo será prioritario (aunque, por lo general, el tiempo, si se otorga para un viaje programado, debe ser igual al tiempo programado en GTFS + la demora).

La incertidumbre se aplica de la misma forma tanto al tiempo como a la demora. La incertidumbre especifica el error esperado en una demora real (pero ten en cuenta, que todavía no definimos su significado estadístico preciso). Es posible que la incertidumbre sea 0, por ejemplo, para los trenes que funcionan con un control de horarios por computadora.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **delay** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | La demora (en segundos) puede ser positiva (significa que el vehículo está retrasado) o negativa (significa que el vehículo está adelantado). Una demora de 0 significa que el vehículo está yendo a tiempo. |
| **time** | [int64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Evento como tiempo absoluto. En tiempo de POSIX (es decir, la cantidad de segundos desde el 1.° de enero de 1970 00:00:00 UTC). |
| **uncertainty** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Si se omite la incertidumbre, se interpreta como desconocida. Para especificar una predicción completamente certera, establece la incertidumbre en 0. |

## _mensaje_ StopTimeUpdate

La actualización en tiempo real para los eventos de llegada o de salida para una determinada parada de un viaje. Consulta el debate general de las actualizaciones de tiempos de parada en la documentación de [TripDescriptor](#TripDescriptor) y [del tipo de feed de actualizaciones de viaje](./trip-updates).

Las actualizaciones se pueden proporcionar tanto para eventos pasados como futuros. El productor tiene permitido, aunque no está obligado, a desestimar los eventos pasados.
 La actualización está vinculada a una parada específica sea a través de stop_sequence o de stop_id, de manera que uno de estos campos debe definirse, necesariamente.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **stop_sequence** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Debe ser la misma que la de stop_times.txt en el feed GTFS correspondiente. |
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Debe ser el mismo que el de stops.txt en el feed GTFS correspondiente. |
| **arrival** | [StopTimeEvent](#StopTimeEvent) | opcional |
| **departure** | [StopTimeEvent](#StopTimeEvent) | opcional |
| **schedule_relationship** | [ScheduleRelationship](#ScheduleRelationship_StopTimeUpdate) | opcional | La relación predeterminada es SCHEDULED. |

## _enum._ ScheduleRelationship

La relación entre este StopTime y la programación estática

### Valores

| _**Valor**_ | _**Comentario**_ |
|-------------|------------------|
| **SCHEDULED** | El vehículo está avanzando según su programación estática de paradas, aunque no necesariamente de acuerdo con los tiempos de la programación. Este es el comportamiento **predeterminado**. Al menos debe proporcionarse uno de los valores de llegada y de salida. Si la programación para esta parada contiene los tiempos de llegada y de salida, entonces también debe contener estos dos valores la actualización. Una actualización son solo una salida, digamos, cuando la programación tiene ambos datos, indica que el viaje se termina antes en esta parada. |
| **SKIPPED** | La parada se omite, es decir, el vehículo no se detendrá en esta parada. Los valores de llegada y salida son opcionales. |
| **NO_DATA** | No se proporcionan datos para esta parada. Esto indica que no hay información en tiempo real disponible. Cuando se establece NO_DATA, esto se propaga en las siguientes paradas, de manera que esta es la forma recomendada de especificar desde qué parada no tienes información en tiempo real. Cuando se establece NO_DATA, no se deben proporcionar los datos de llegada ni de salida. |

## _mensaje_ VehiclePosition

Información de posicionamiento en tiempo real para un vehículo dado

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **trip** | [TripDescriptor](#TripDescriptor) | opcional | El viaje que está haciendo este vehículo. Puede estar vacío o parcialmente vacío si el vehículo no puede identificarse con una instancia de viaje dada. |
| **vehicle** | [VehicleDescriptor](#VehicleDescriptor) | opcional | Información adicional sobre el vehículo que está realizando el viaje. Cada entrada debe tener un ID de vehículo **único**. |
| **position** | [Position](#Position) | opcional | Posición actual de este vehículo. |
| **current_stop_sequence** | [uint32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | El índice de la secuencia de parada de la parada actual. El significado de current_stop_sequence (es decir, la parada a la que hace referencia) está determinado por current_status. Si falta el valor en current_status, se asume IN_TRANSIT_TO. |
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Identifica la parada actual. El valor debe ser el mismo que el de stops.txt en el feed GTFS correspondiente. |
| **current_status** | [VehicleStopStatus](#VehicleStopStatus) | opcional | El estado exacto del vehículo con respecto a la parada actual. Se ignora si falta el valor en current_stop_sequence. |
| **timestamp** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Momento en el cual se midió la posición del vehículo. En tiempo de POSIX (es decir, la cantidad de segundos desde el 1.° de enero de 1970 00:00:00 UTC). |
| **congestion_level** | [CongestionLevel](#CongestionLevel) | opcional |

## _enum._ VehicleStopStatus

### Valores

| _**Valor**_ | _**Comentario**_ |
|-------------|------------------|
| **INCOMING_AT** | El vehículo está a punto de llegar a la parada (en la visualización de la parada, el símbolo del vehículo, por lo general, parpadea). |
| **STOPPED_AT** | El vehículo está detenido en la parada. |
| **IN_TRANSIT_TO** | El vehículo ha salido de la parada anterior y está en tránsito. |

## _enum._ CongestionLevel

El nivel de congestión que está afectando al vehículo.

### Valores

| _**Valor**_ |
|-------------|
| **UNKNOWN_CONGESTION_LEVEL** |
| **RUNNING_SMOOTHLY** |
| **STOP_AND_GO** |
| **CONGESTION** |
| **SEVERE_CONGESTION** |

## _mensaje_ Alert

Una alerta que indica que existe algún tipo de incidente en la red de transporte público.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **active_period** | [TimeRange](#TimeRange) | repetido | Tiempo durante el cual debe mostrarse la alerta al usuario. Si falta, la alerta se mostrará durante todo el tiempo que aparezca en el feed. Si se otorgan varios intervalos, la alerta se mostrará durante todos ellos. |
| **informed_entity** | [EntitySelector](#EntitySelector) | repetido | Entidades a cuyos usuarios debemos notificar esta alerta. |
| **cause** | [Cause](#Cause) | opcional |
| **effect** | [Effect](#Effect) | opcional |
| **url** | [TranslatedString](#TranslatedString) | opcional | La URL que proporciona información adicional sobre la alerta. |
| **header_text** | [TranslatedString](#TranslatedString) | opcional | Encabezado de la alerta. Esta cadena de texto sin formato se resaltará, por ejemplo, en negrita. |
| **description_text** | [TranslatedString](#TranslatedString) | opcional | Descripción de la alerta. A esta cadena de texto sin formato se le aplicará el formato del cuerpo de la alerta (o se mostrará en una solicitud explícita de "expansión" realizada por el usuario ). La información de la descripción debe completar la información del encabezado. |

## _enum._ Cause

Causa de la alerta

### Valores

| _**Valor**_ |
|-------------|
| **UNKNOWN_CAUSE** |
| **OTHER_CAUSE** |
| **TECHNICAL_PROBLEM** |
| **STRIKE** |
| **DEMONSTRATION** |
| **ACCIDENT** |
| **HOLIDAY** |
| **WEATHER** |
| **MAINTENANCE** |
| **CONSTRUCTION** |
| **POLICE_ACTIVITY** |
| **MEDICAL_EMERGENCY** |

## _enum._ Effect

El efecto de este problema en la entidad afectada.

### Valores

| _**Valor**_ |
|-------------|
| **NO_SERVICE** |
| **REDUCED_SERVICE** |
| **SIGNIFICANT_DELAYS** |
| **DETOUR** |
| **ADDITIONAL_SERVICE** |
| **MODIFIED_SERVICE** |
| **OTHER_EFFECT** |
| **UNKNOWN_EFFECT** |
| **STOP_MOVED** |

## _mensaje_ TimeRange

Un intervalo de tiempo. El intervalo se considera activo `t` si `t` es mayor o igual que la hora de inicio y mejor que la hora de finalización.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **start** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Hora de inicio, en tiempo de POSIX (es decir, la cantidad de segundos desde el 1.° de enero de 1970 00:00:00 UTC). Si falta esta información, el intervalo comienza con el valor infinito negativo. |
| **end** | [uint64](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Hora de finalización, en tiempo de POSIX (es decir, la cantidad de segundos desde el 1.° de enero de 1970 00:00:00 UTC). Si falta esta información, el intervalo finaliza con el valor infinito positivo. |

## _mensaje_ Position

La posición geográfica de un vehículo

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **latitude** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | obligatorio | Grados norte, en el sistema de coordenadas WGS-84 |
| **longitude** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | obligatorio | Grados este, en el sistema de coordenadas WGS-84 |
| **bearing** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Orientación, en grados, en el sentido de las agujas del reloj desde el norte verdadero, es decir, 0 es el norte y 90 es el este. Esta puede ser la orientación de la brújula, o la dirección hacia la próxima parada o la ubicación intermedia. Esto no debe deducirse a partir de la secuencia de posiciones anteriores, que los clientes pueden calcular a partir de los datos anteriores. |
| **odometer** | [double](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | El valor del odómetro en metros. |
| **speed** | [float](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Velocidad momentánea medida por el vehículo, en metros por segundo. |

## _mensaje_ TripDescriptor

Un descriptor que identifica una instancia de un viaje de GTFS o todas las instancias de un viaje por una ruta. Para especificar una sola instancia de viaje, se define trip_id (y si fuera necesario, start_time). Si también se define route_id, debe ser el mismo que uno a los cuales corresponda el viaje dado. Para especificar todos los viajes de una determinada ruta, solo se debe definir route_id. Ten en cuenta que si no se conoce el trip_id, entonces los identificadores de la secuencia de la estación en TripUpdate no son suficientes y, también, se deberán proporcionar los identificadores de parada. Además, se deben proporcionar las horas absolutas de llegada/salida.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **trip_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | El identificador de viaje del feed GTFS al cual hace referencia este selector. Para los viajes sin frecuencia extendida, este campo es suficiente para identificar de forma unívoca al viaje. Para los viajes con frecuencia extendida, también podrían necesitarse start_time y start_date. |
| **route_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | El identificador de la ruta de GTFS al que hace referencia este selector. |
| **start_time** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | La hora de inicio programada de esta instancia de viaje. Este campo debe proporcionarse solo si el viaje tiene frecuencia extendida en el feed GTFS. El valor debe corresponder precisamente a la hora de inicio especificada para la ruta del feed GTFS más algunos múltiplos de headway_secs. El formato del campo es el mismo que el de GTFS/frequencies.txt/start_time, es decir, 11:15:35 o 25:15:35. |
| **start_date** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | La fecha de inicio programada de esta instancia de viaje. Este campo debe proporcionarse para desambiguar los viajes que están tan retrasados que pueden superponerse con un viaje programado para el día siguiente. Por ejemplo, para un tren que sale a las 8:00 y a las 20:00 todos los días, y está 12 horas retrasado, habrá dos viajes distintos a la misma hora. Este campo puede proporcionarse, pero no es obligatorio para las programaciones en las cuales las superposiciones son imposibles, por ejemplo, un servicio que funciona según una programación horaria donde un vehículo que está una hora retrasado deja de considerarse relacionado a la programación. En formato AAAAMMDD. |
| **schedule_relationship** | [ScheduleRelationship](#ScheduleRelationship_TripDescriptor) | opcional |

## _enum._ ScheduleRelationship

La relación entre este viaje y la programación estática. Si un viaje se realiza de acuerdo con la programación temporal, no se refleja en GTFS, y por lo tanto, no debe marcarse como SCHEDULED, sino como ADDED.

### Valores

| _**Valor**_ | _**Comentario**_ |
|-------------|------------------|
| **SCHEDULED** | Viaje que se está realizando de acuerdo con su programación de GTFS, o que está realizándose tan parecido al viaje programado que se puede asociar con él. |
| **ADDED** | Un viaje adicional que se agregó además de una programación existente, por ejemplo, para reemplazar un vehículo averiado o para responder a una carga repentina de pasajeros. |
| **UNSCHEDULED** | Un viaje que se está realizando sin ninguna programación asociada, por ejemplo, cuando no existe ninguna programación. |
| **CANCELED** | Un viaje que existió en la programación, pero que luego se eliminó. |
| **REPLACEMENT** | Un viaje que reemplaza una parte de la programación estática. Si el selector de viaje identifica determinada instancia de viaje, entonces solamente esa instancia se reemplaza. Si el selector identifica una ruta, entonces todos los viajes de la ruta se reemplazan.<br>El reemplazo se aplica solamente a la parte del viaje que se suministra. Por ejemplo, consideremos una ruta que pasa por las paradas A,B,C,D,E,F y un viaje REPLACEMENT proporciona datos para las paradas A,B,C. Entonces, los horarios para las paradas D,E,F todavía se toman de la programación estática.<br>Un feed debe suministrar varios viajes REPLACEMENT. En este caso, la parte de la programación estática que se reemplaza es la suma de las definiciones de todos los feeds. Por lo general, todos los viajes REPLACEMENT deben corresponder a la misma ruta o a instancias de viaje individuales. |

## _mensaje_ VehicleDescriptor

Información de identificación para el vehículo que realiza el viaje.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Identificación interna del sistema para el vehículo. Debe ser **única** para cada vehículo y se usa para hacer un seguimiento del vehículo en la medida en que avanza en el sistema. Este identificador debe ser visible para el usuario final; para ello debes usar el campo **label** |
| **label** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Etiqueta visible para el usuario, es decir, que se debe mostrar al pasajero para ayudarlo a identificar el vehículo correcto. |
| **license_plate** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | La patente del vehículo. |

## _mensaje_ EntitySelector

Un selector para una entidad en un feed GTFS. Los valores de los campos deben coincidir con los campos correspondientes del feed GTFS. Debe otorgarse al menos un especificador. Si se otorgan muchos, entonces la coincidencia debe hacerse con todos los especificadores dados.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **agency_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional |
| **route_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional |
| **route_type** | [int32](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional |
| **trip** | [TripDescriptor](#TripDescriptor) | opcional |
| **stop_id** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional |

## _mensaje_ TranslatedString

Un mensaje internacionalizado que contiene versiones por idioma de un fragmento de texto o una URL. Se seleccionará una de las cadenas de un mensaje. La resolución se realiza de la siguiente manera: si el idioma de la IU coincide con el código de idioma de una traducción, se elije la primera traducción coincidente. Si un idioma de IU predetermiando (por ejemplo, inglés) coincide con el código de idioma de una traducción, se elije la primera traducción coincidente. Si alguna traducción tiene un código de idioma no especificado, se elija esa traducción.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **translation** | [Translation](#Translation) | repetido | Se debe proporcionar al menos una traducción. |

## _mensaje_ Translation

Una cadena localizada asignada a un idioma.

### Campos

| _**Nombre del campo**_ | _**Tipo**_ | _**Cardinalidad**_ | _**Descripción**_ |
|------------------------|------------|--------------------|-------------------|
| **text** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | obligatorio | Una cadena UTF-8 que contiene el mensaje. |
| **language** | [string](https://developers.google.com/protocol-buffers/docs/proto#scalar) | opcional | Código de idioma BCP-47\. Se puede omitir si el idioma es desconocido o si no se realiza ninguna internacionalización para el feed. Al menos una traducción puede tener una etiqueta de idioma no especificado. |
