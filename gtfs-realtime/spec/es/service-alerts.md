Las alertas de servicio te permiten proporcionar actualizaciones cada vez que se produce una interrupción en la red. Las demoras y cancelaciones de viajes individuales a menudo se deben comunicar a través de las [Actualizaciones de viaje](trip-updates.md).

Puedes proporcionar la siguiente información:

*   la URL del sitio en el que se ofrecen más detalles acerca de la alerta,
*   el texto del encabezado a modo de resumen de la alerta,
*   la descripción completa de la alerta que se mostrará junto al encabezado (la información no debe ser la misma en ambas partes).

### Período

La alerta aparecerá cuando corresponda en el transcurso del período establecido. Este período debe cubrir en su totalidad el lapso en el que el pasajero necesita la alerta.

Si no se establece ningún período, mostraremos la alerta el tiempo que esta se encuentre en el feed. Si se establecen varios períodos, mostraremos la alerta durante todos ellos.

### Selector de entidad

El selector de entidad te permite especificar exactamente qué partes de la red afecta una alerta, a fin de que le podamos mostrar al usuario solo las alertas más adecuadas. Puedes incluir varios selectores de entidad en el caso de las alertas que afectan muchas entidades.

Las entidades se seleccionan a través de los identificadores de la especificación GTFS y puedes elegir cualquiera de los siguientes:

*   Empresa: afecta toda la red.
*   Ruta: afecta toda la ruta.
*   Tipo de ruta: afecta cualquier ruta del tipo seleccionado; p. ej., todos los metros.
*   Viaje: afecta un viaje en particular.
*   Parada: afecta una parada en particular.

### Causa

¿Cuál es la causa de esta alerta? Puedes especificar cualquiera de las siguientes:

*   causa desconocida,
*   otra causa (que no se ve representada por ninguna de estas opciones),
*   problema técnico,
*   huelga,
*   manifestación,
*   accidente,
*   feriado,
*   clima,
*   tareas de mantenimiento,
*   tareas de construcción,
*   actividad policial,
*   emergencia médica.

### Efecto

¿Qué efecto tiene este problema en la entidad seleccionada? Puedes especificar cualquiera de los siguientes:

*   sin servicio,
*   servicio reducido,
*   demoras importantes (aquellas poco importantes se deben informar a través de las [Actualizaciones de viaje](trip-updates.md)),
*   desvío,
*   servicio adicional,
*   servicio modificado,
*   traslado de parada,
*   otro efecto (que no se ve representado por ninguna de estas opciones),
*   efecto desconocido.
