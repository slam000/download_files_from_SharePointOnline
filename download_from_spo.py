import os
import csv
from shareplum import Site
from shareplum.site import Version

# Ruta de la carpeta local donde deseas descargar los archivos
carpeta_destino = "/ruta/a/tu/carpeta/destino"

# URL del sitio de SharePoint Online
url_sitio_sharepoint = "https://tuempresa.sharepoint.com/sites/TuSitioSharepoint"
url_sitio = "https://tuempresa.sharepoint.com"

# Obtener nombre de usuario y contraseña de SharePoint Online desde variables de entorno
usuario_sharepoint = os.getenv('SHAREPOINT_USER')
contrasena_sharepoint = os.getenv('SHAREPOINT_PASSWORD')

# Asegurarse de que las credenciales están presentes
if not usuario_sharepoint or not contrasena_sharepoint:
    raise ValueError("Las credenciales de SharePoint no están configuradas en las variables de entorno.")

# Ruta al archivo CSV
archivo_csv = "/ruta/al/archivo/csv"

# Lista para almacenar detalles de archivos descargados
detalles_descargas = []

try:
    # Iniciar sesión en SharePoint Online
    with Site(url_sitio_sharepoint, version=Version.v2016, auth=(usuario_sharepoint, contrasena_sharepoint)) as site:
    
        # Leer el archivo CSV con punto y coma como delimitador
        with open(archivo_csv, newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                ua = row["UA"]
                relative_url = row["RelativeURL"]
                file_name = os.path.basename(relative_url)

                # Crear una carpeta con el nombre UA si no existe
                carpeta_ua = os.path.join(carpeta_destino, ua)
                os.makedirs(carpeta_ua, exist_ok=True)

                # Construir la URL completa del archivo
                archivo_url = f"{url_sitio}{relative_url}"

                # Descargar el archivo desde SharePoint Online
                with site.open_file(archivo_url) as file:
                    with open(os.path.join(carpeta_ua, file_name), "wb") as f:
                        f.write(file.read())

                # Agregar detalles de la descarga a la lista
                detalles_descargas.append({
                    "UA": ua,
                    "Ruta_Local": os.path.join(carpeta_ua, file_name)
                })

except Exception as e:
    print(f"Se produjo un error durante la ejecución del script: {e}")

# Crear un archivo CSV con los detalles de las descargas
archivo_csv_descargas = "/ruta/al/archivo/csv/de/salida"
with open(archivo_csv_descargas, "w", newline='') as csv_file:
    fieldnames = ["UA", "Ruta_Local"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for detalle in detalles_descargas:
        writer.writerow(detalle)

print("Descarga completada. Detalles guardados en descargas.csv.")

