GTFS en tiempo real es una especificación de feed que permite que las empresas de tranporte público proporcionen actualizaciones en tiempo real sobre su flota a los programadores de la aplicación. Es una extensión de [GTFS](https://developers.google.com/transit/gtfs/reference) (Especificación general de feeds de transporte público), un formato de datos abierto para los horarios de transporte público y la información geográfica asociada. GTFS en tiempo real fue diseñado en torno a la facilidad de implementación, buena interoperabilidad GTFS y un enfoque en la información al pasajero.

La especificación fue diseñada a través de una asociación de las empresas miembro de las [Actualizaciones del transporte público en tiempo real](https://developers.google.com/transit/google-transit#LiveTransitUpdates) iniciales, diferentes programadores de transporte público y Google. La especificación está publicada bajo la licencia [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0).

## ¿Cómo empiezo?

1.  Sigue leyendo el resumen general a continuación.
2.  Decide qué [tipos de feed](feed-types.md) proporcionarás.
3.  Consulta los [ejemplos de feeds](examples/).
4.  Crea tus propios feeds mediante la [referencia](reference.md).
5.  Publica tu feed.

## Resumen general de los tipos de feed GTFS en tiempo real

La especificación es compatible actualmente con los siguientes tipos de información:

*   **Actualizaciones de viaje**: retrasos, cancelaciones, cambios de ruta
*   **Alertas del servicio**: traslados de paradas o eventos imprevistos que afectan una estación, ruta o toda la red
*   **Posiciones del vehículo**: información sobre los vehículos, incluidos la ubicación y el nivel de congestión

Las actualizaciones de cada tipo se proporcionan en un feed separado. Los feeds se muestran a través de HTTP y se actualizan con frecuencia. El archivo en sí es un archivo binario normal, por lo que cualquier tipo de servidor web puede alojar y mostrar el archivo (es posible utilizar otros protocolos de transferencia también). Alternativamente, los servidores de aplicaciones web también se podrían utilizar, los cuales devolverán el feed como una respuesta a una solicitud GET de HTTP válida. No hay limitaciones en cuanto a la frecuencia ni al método exacto de cómo el feed debe ser actualizado o recuperado.

Ya que GTFS en tiempo real te permite presentar el estado _real_ de tu flota, el feed debe ser actualizado con frecuencia, de preferencia cuando se ingresen nuevos datos de tu sistema de ubicación automática de vehículos.

[Más información sobre los tipos de feed...](feed-types.md)

## Formato de los datos

El formato de intercambio de datos de GTFS en tiempo real se basa en [Búferes de protocolo](https://developers.google.com/protocol-buffers/).

Los búferes de protocolo son un mecanismo de lenguaje y plataforma neutral para serializar datos estructurados (como XML, pero más pequeño, rápido y simple). La estructura de datos se define en un archivo [gtfs-realtime.proto](gtfs-realtime.proto), que luego se utiliza para generar el código fuente para leer y escribir fácilmente tus datos estructurados desde y hacia una variedad de flujos de datos, mediante diferentes lenguajes, por ejemplo Java, C++ o Python.

[Más información sobre los búferes de protocolo](https://developers.google.com/protocol-buffers/)...

## Estructura de los datos

La jerarquía de los elementos y las definiciones de su tipo están especificadas en el archivo [gtfs-realtime.proto](gtfs-realtime.proto).

Este archivo de texto se utiliza para generar las bibliotecas necesarias en tu lenguaje de programación seleccionado. Estas bibliotecas proporcionan las clases y funciones necesarias para generar feeds GTFS en tiempo real válidos. Las bibliotecas no solo hacen que la creación del feed sea más fácil, sino que también garantizan que solo se produzcan feeds válidos.

[Más información sobre la estructura de los datos.](reference.md)

## Obtener ayuda

Para participar en los debates sobre GTFS en tiempo real y sugerir cambios y adiciones a la especificación, únete al [grupo de debate de GTFS en tiempo real](http://groups.google.com/group/gtfs-realtime).

## Google Maps y Actualizaciones de transporte público en tiempo real

Una de las posibles aplicaciones que utiliza GTFS en tiempo real es [Actualizaciones de transporte público en tiempo real](https://developers.google.com/transit/google-transit#LiveTransitUpdates), una función de Google Maps que proporciona a los usuarios información de transporte público en tiempo real. Si trabajas para una empresa de transporte público que está interesada en proporcionar actualizaciones en tiempo real para Google Maps, visita la [Página de socios de Google Transit](http://maps.google.com/help/maps/transit/partners/live-updates.html).

