
# Descarga de Archivos desde SharePoint Online

## Descripción
Este proyecto contiene un script en Python para descargar archivos desde un sitio de SharePoint Online a una carpeta local. Además, registra los detalles de las descargas en un archivo CSV. Este scritp forma parte de un proceso de migración y puede que las políticas que sean necesarian en tu proceso no sean las mismas por lo que será necesario que revises el script.

## Requerimientos
- Python 3.x
- Módulos de Python especificados en `requirements.txt`

## Configuración
- Configurar las variables de entorno `SHAREPOINT_USER` y `SHAREPOINT_PASSWORD` con las credenciales de SharePoint.
- Especificar la ruta del archivo CSV de entrada y la carpeta de destino en el script.

## Uso
Ejecutar el script `descargar_sharepoint.py` para iniciar la descarga de archivos. Los detalles de las descargas se registrarán en un archivo CSV.

## Seguridad
Las credenciales de SharePoint no se almacenan en el script. En su lugar, se utilizan variables de entorno para mayor seguridad.

## License
Este proyecto está licenciado bajo MIT.

## Configuración de Variables de Entorno en Linux

### Configuración Temporal
Para configurar las variables de entorno `SHAREPOINT_USER` y `SHAREPOINT_PASSWORD` temporalmente (solo para la sesión actual de la terminal), use los siguientes comandos en la terminal:

```bash
export SHAREPOINT_USER="tu_usuario_sharepoint"
export SHAREPOINT_PASSWORD="tu_contraseña_sharepoint"
```

### Configuración Permanente
Para configurar las variables de manera permanente, agréguelas a su archivo `~/.bashrc` o `~/.bash_profile`:

1. Abra el archivo con un editor de texto (por ejemplo, `nano ~/.bashrc`).
2. Agregue las siguientes líneas al final del archivo:

    ```bash
    export SHAREPOINT_USER="tu_usuario_sharepoint"
    export SHAREPOINT_PASSWORD="tu_contraseña_sharepoint"
    ```

3. Guarde y cierre el archivo.
4. Recargue el archivo `.bashrc` ejecutando `source ~/.bashrc` o reinicie su sesión.

### Consideraciones de Seguridad
- Tenga cuidado al almacenar credenciales en archivos de configuración, especialmente en entornos compartidos o menos seguros.
- Considere utilizar gestores de secretos o servicios de almacenamiento de credenciales para entornos de producción.
