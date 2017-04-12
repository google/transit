La posición del vehículo se utiliza para proporcionar información generada automáticamente sobre la ubicación del mismo, como la generada por un GPS a bordo. Se debe proporcionar una sola posición por cada vehículo que pueda hacerlo.

El viaje que el vehículo está realizando actualmente se debe proporcionar a través de un [descriptor de viaje](reference.md#VehicleDescriptor). También se puede proporcionar un [descriptor de vehículo](reference.md#VehicleDescriptor) que especifique un vehículo físico concreto sobre el cual estás proporcionando actualizaciones. La documentación se proporciona más abajo.

Se puede proporcionar una **marca de tiempo** que indique el momento en el que se tomó la lectura de la posición. Hay que tener en cuenta que esta es diferente de la marca de tiempo en el encabezado del feed, que es el tiempo en el que el servidor generó este mensaje.

También se puede proporcionar un **paso actual** (ya sea como stop_sequence o stop_id). Este es una referencia a la parada a la que el vehículo se está dirigiendo o en la que ya se detuvo.

## Posición

La posición contiene los datos de ubicación (Vehicle Position) del vehículo. Los campos de latitud y longitud son obligatorios; los demás campos son opcionales. Estos tipos de datos son:

*   **Latitud**: grados Norte, en el sistema de coordenadas WGS-84.
*   **Longitud**: grados Este, en el sistema de coordenadas WGS-84.
*   **Rumbo**: la dirección hacia la que el vehículo está orientado.
*   **Odómetro**: la distancia que el vehículo ha recorrido.
*   **Velocidad**: velocidad instantánea medida por el vehículo, en metros por segundo.

## Nivel de tráfico

La posición del vehículo también permite que la empresa especifique el nivel de tráfico que el vehículo está experimentando en el instante actual. El tráfico se puede clasificar en las siguientes categorías:

*   Nivel de tráfico desconocido.
*   Tráfico fluido.
*   Tráfico intermitente.
*   Atasco.
*   Atrasco grave.

A la empresa le corresponde interpretar nuestra ponderación del tráfico. Desde nuestra perspectiva, la congestión grave solo se utilizaría en situaciones en las que el tráfico está tan congestionado que las personas están abandonando sus vehículos.

## Grado de ocupación del vehículo

La posición del vehículo permite a la empresa especificar el grado de ocupación del vehículo, que puede ser clasificado en la siguientes categorías:

*   Vacío.
*   Muchos asientos libres.
*   Pocos asientos libres.
*   Sitio sólo de pie.
*   Sitio sólo de pie y apretados.
*   Lleno.
*   No admite más pasajeros.

Este campo todavía es **experimental** y está sujeto a cambios. Podría pasar a adoptarse formalmente más adelante.

## Estado de parada del vehículo

El estado de parada del vehículo está más relacionado con el estado de una parada a la que se está aproximando o en la que ya está. Se puede ajustar a cualquiera de estos valores.

*   **Llegando a**: el vehículo está a punto de llegar a la parada indicada.
*   **Detenido en**: el vehículo está detenido en la parada indicada.
*   **En camino a**: la parada indicada es la siguiente parada para el vehículo: **predeterminado**.

## Descriptor de vehículo

El descriptor de vehículo describe un vehículo físico concreto y puede contener cualquiera de los siguientes atributos:

*   **ID**: sistema interno de identificación del vehículo. Debe ser único para el vehículo.
*   **Identificador**: un identificador visible para el usuario, por ejemplo el nombre de un tren.
*   **Matrícula**: la matrícula real del vehículo.
