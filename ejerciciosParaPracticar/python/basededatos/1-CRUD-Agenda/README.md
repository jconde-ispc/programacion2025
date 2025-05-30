Este archivo contiene un programa en Python que implementa un **CRUD (Crear, Leer, Actualizar, Eliminar)** para gestionar una agenda telefónica, pero en este caso, los datos se almacenan en una **base de datos MySQL** en lugar de un diccionario en memoria. Esto permite que los datos sean persistentes y accesibles desde múltiples usuarios o dispositivos.

### ¿Qué hace este programa?

1. **Crear la base de datos y la tabla:**

   - Si la base de datos `agenda_db` no existe, el programa la crea automáticamente.
   - También crea la tabla `personas` si no existe, con las columnas `dni`, `apellido`, `nombre`, `email` y `telefono`.
2. **Operaciones CRUD:**

   - **Crear (Agregar una persona):** Inserta un nuevo registro en la tabla `personas` con los datos ingresados por el usuario.
   - **Leer (Mostrar datos):** Permite listar todos los registros de la tabla `personas`.
   - **Actualizar (Modificar una persona):** Busca un registro por su `dni` y permite modificar sus datos.
   - **Eliminar (Eliminar una persona):** Elimina un registro de la tabla `personas` usando el `dni` como identificador.
   - **Salir:** Finaliza el programa y cierra la conexión con la base de datos.
3. **Persistencia de datos:** Los datos se almacenan en la base de datos MySQL, lo que significa que no se pierden al cerrar el programa.

---

### Diferencias entre usar un diccionario y una base de datos MySQL

| **Aspecto**             | **Diccionario en memoria**                                            | **Base de datos MySQL**                                                                     |
| ----------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Persistencia**        | Los datos son**volátiles** y se pierden al cerrar el programa.       | Los datos son**persistentes** y se almacenan en disco.                                      |
| **Acceso concurrente**  | Solo un usuario o programa puede acceder al diccionario en un momento dado. | Podría permitir el acceso concurrente de múltiples usuarios o programas desde distintos hosts. |
| **Escalabilidad**       | Limitado por la memoria RAM del sistema.                                    | Escalable para manejar grandes volúmenes de datos.                                               |
| **Consultas complejas** | No permite realizar consultas avanzadas (como búsquedas o filtros).        | Soporta consultas avanzadas con SQL.                                                              |
| **Facilidad de uso**    | Más simple de implementar y no requiere configuración adicional.          | Requiere configurar un servidor de base de datos y manejar conexiones.                            |
| **Seguridad**           | No tiene mecanismos de seguridad integrados.                                | Ofrece autenticación, permisos y encriptación.                                                  |

---

### Ejemplo práctico de diferencia:

1. **Diccionario en memoria:**

   - Si el programa se cierra, todos los datos de la agenda se pierden.
   - Solo un usuario puede usar la agenda a la vez.
2. **Base de datos MySQL:**

   - Los datos permanecen almacenados incluso después de cerrar el programa.
   - Varios usuarios podrían acceder a la agenda desde diferentes dispositivos al mismo tiempo.

---

### Conclusión

El uso de una base de datos relacionales (como MySQL, PostgreSQL, SQL Server, Oracle, entre otras) es más adecuado para aplicaciones que requieren persistencia de datos, acceso concurrente y escalabilidad. Por otro lado, un diccionario en memoria es útil para aplicaciones simples o temporales donde no se necesita guardar los datos después de la ejecución.
