### Instalación de MySQL Community Server y Workbench

#### **En Windows**

1. **Descargar MySQL Installer**:

   - Ve al sitio oficial de MySQL: [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/).
   - Descarga el instalador (puedes elegir el instalador completo o el instalador web).
2. **Ejecutar el instalador**:

   - Abre el instalador descargado.
   - Selecciona la opción "Developer Default" para instalar MySQL Server, MySQL Workbench y otras herramientas útiles.
3. **Configurar MySQL Server**:

   - Durante la instalación, selecciona la versión de MySQL Server que deseas instalar.
   - Configura el tipo de servidor (por ejemplo, "Standalone MySQL Server").
   - Establece una contraseña para el usuario `root` y, opcionalmente, crea usuarios adicionales.
4. **Instalar MySQL Workbench**:

   - Asegúrate de que la opción para instalar MySQL Workbench esté seleccionada.
   - Completa la instalación.
5. **Verificar la instalación**:

   - Abre MySQL Workbench y conéctate al servidor MySQL usando las credenciales configuradas.

---

#### **En Ubuntu**

1. **Actualizar los repositorios**:

   ```bash
   sudo apt update
   ```
2. **Instalar MySQL Server**:

   ```bash
   sudo apt install mysql-server
   ```

   - Durante la instalación, MySQL se configurará automáticamente. Puedes verificar el estado del servicio con:
     ```bash
     sudo systemctl status mysql
     ```
3. **Configurar MySQL Server**:

   - Ejecuta el script de configuración segura:
     ```bash
     sudo mysql_secure_installation
     ```
   - Sigue las instrucciones para establecer una contraseña para el usuario `root` y mejorar la seguridad.
4. **Instalar MySQL Workbench**:

   ```bash
   sudo apt install mysql-workbench
   ```
5. **Verificar la instalación**:

   - Abre MySQL Workbench desde el menú de aplicaciones o ejecuta:
     ```bash
     mysql-workbench
     ```
   - Conéctate al servidor MySQL usando las credenciales configuradas.

---

#### **Notas adicionales**:

- **Comandos útiles para MySQL en Ubuntu**:

  - Iniciar el servicio:
    ```bash
    sudo systemctl start mysql
    ```
  - Detener el servicio:
    ```bash
    sudo systemctl stop mysql
    ```
  - Reiniciar el servicio:
    ```bash
    sudo systemctl restart mysql
    ```
- **Acceso a MySQL desde la terminal**:

  ```bash
  sudo mysql -u root -p
  ```
- **Documentación oficial**:

  - [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
  - [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)
