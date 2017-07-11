La especificación GTFS en tiempo real admite el envío de tres tipos diferentes de datos en tiempo real. Si bien la sintaxis del archivo [gtfs-realtime.proto](gtfs-realtime.proto) permite que se mezclen distintos tipos de entidades para un feed, solo se puede usar un tipo de entidad por feed. Los resúmenes se ofrecen a continuación, con la documentación completa proporcionada en la sección correspondiente.

## Actualizaciones de viaje

#### "El autobús X tiene una demora de cinco minutos".

Las actualizaciones de viaje ofrecen información acerca de fluctuaciones en el horario. Esperamos recibir actualizaciones de viaje para todos los viajes programados cuya duración se puede predecir en tiempo real. Estas actualizaciones ofrecerían un horario de llegada o salida para las diferentes paradas de la ruta. Las actualizaciones de viaje también pueden brindar información en situaciones más complejas, como cuando los viajes se cancelan o agregan al programa, o como cuando su trayecto se modifica.

[Más información acerca de las Actualizaciones de viaje...](trip-updates.md)

## Alertas de servicio

#### "La estación Y está cerrada por tareas de construcción".

Las alertas de servicio ofrecen información acerca de los problemas más graves que puede sufrir una entidad en particular. En general, se expresan a través de una descripción textual de la interrupción.

Pueden representar los problemas que sufren:

*   las estaciones,
*   las líneas,
*   la red completa,
*   etc.

Una alerta de servicio a menudo consiste en una descripción textual del problema. También permitimos que se incluyan las URL de los sitios en los que se ofrecen más detalles e información más estructurada para poder entender a quién afecta una alerta de servicio.

[Más información acerca de las Alertas de servicio...](service-alerts.md)

## Posiciones de los vehículos

#### "Este autobús se encuentra en la posición X a la hora Y".

La posición de un vehículo ofrece datos básicos acerca de un vehículo en particular de la red.

La información más importante consiste en la latitud y longitud donde se encuentra el vehículo. Sin embargo, también podemos usar datos acerca de las lecturas del cuentakilómetros y velocidad actuales del vehículo.

[Más información acerca las actualizaciones de las Posiciones de los vehículos...](vehicle-positions.md)
