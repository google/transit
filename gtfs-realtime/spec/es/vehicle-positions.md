La posición del vehículo se utiliza para proporcionar información generada automáticamente sobre la ubicación de un vehículo, como de un dispositivo GPS a bordo. Se debe proporcionar una sola posición del vehículo para cada vehículo que puede proporcionarla.

El viaje que el vehículo está realizando actualmente se debe proporcionar a través de un [descriptor de viaje](reference.md#VehicleDescriptor). También puedes proporcionar un [descriptor de vehículo](reference.md#VehicleDescriptor) que especifique un vehículo físico preciso sobre el cual estás proporcionando actualizaciones. La documentación se proporciona a continuación.

Se puede proporcionar una **marca de tiempo** que indique el momento en el que se tomó la lectura de la posición. Ten en cuenta que esto es diferente de la marca de tiempo en el encabezado del feed, que es el tiempo en el que el servidor generó este mensaje.

También se puede proporcionar un **paso actual** (ya sea como stop_sequence o stop_id). Esto es una referencia a la parada a la que el vehículo se está dirigiendo o en la que ya se detuvo.

## Posición

La posición contiene los datos de ubicación dentro de Posición del vehículo. Los campos de latitud y longitud son obligatorios; los demás campos son opcionales. Estos tipos de datos son:

*   **Latitud**: grados Norte, en el sistema de coordenadas WGS-84.
*   **Longitud**: grados Este, en el sistema de coordenadas WGS-84.
*   **Rumbo**: la dirección en la que el vehículo se orienta.
*   **Odómetro**: la distancia que el vehículo ha recorrido.
*   **Velocidad**: velocidad instantánea medida por el vehículo, en metros por segundo.

## Nivel de congestión

La posición del vehículo también permite que la empresa especifique el nivel de congestión que el vehículo está experimentando en el momento. La congestión se puede clasificar en las siguientes categorías:

*   Nivel de congestión desconocido
*   Tráfico fluido
*   Tráfico intermitente
*   Congestión
*   Congestión grave

A la empresa le corresponde clasificar lo que clasificas como cada tipo de congestión. Nuestra orientación es que la congestión grave solo se utiliza en situaciones en las que el tráfico está tan congestionado que las personas están abandonando sus vehículos.

## VehicleStopStatus

El estado de parada del vehículo le da más significado al estado de un vehículo en relación con una parada a la que se está aproximando o en la que ya está. Se puede ajustar a cualquiera de estos valores.

*   **Llegando a**: el vehículo está a punto de llegar a la parada indicada.
*   **Detenido en**: el vehículo está detenido en la parada indicada.
*   **En camino a**: la parada indicada es la siguiente parada para el vehículo: **predeterminado**.

## Descriptor de vehículo

El descriptor de vehículo describe un vehículo físico preciso y puede contener cualquiera de los siguientes atributos:

*   **ID**: sistema interno de identificación del vehículo. Debe ser único para el vehículo.
*   **Etiqueta**: una etiqueta visible para el usuario, por ejemplo el nombre de un tren.
*   **Placa**: la placa real del vehículo.
