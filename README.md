# PDF DOWNLOADER 📝

### Programa de Optimización para Descarga de Facturas
Este programa ha sido diseñado para optimizar el proceso de descarga de facturas a través del ID obtenido de la URL en el sistema que utilizamos en Vidanova. Aunque el proceso puede ser algo lento, este programa simplifica considerablemente la tarea.

## Funcionamiento
Obtención del ID de la URL: El primer paso es obtener la URL de la factura desde el sistema de Vidanova. A partir de esta URL, extraemos el ID necesario para acceder a la factura.

Generación de la URL completa: Utilizando el ID obtenido, completamos la URL necesaria para acceder a la factura en cuestión.

Descarga del PDF: Una vez que tenemos la URL completa, utilizamos Python para automatizar el proceso de descarga del PDF de la factura.

## Organización de los Archivos
Es importante mantener una estructura ordenada para los archivos descargados. Por lo tanto, el programa realiza lo siguiente:

Creación de Directorios: Se crea un directorio para cada paciente, identificado por su cédula de ciudadanía y nombre completo.

Almacenamiento de Facturas: Dentro de cada directorio de paciente, se guardan las facturas correspondientes.
``` bash
└───Directorio_Pacientes
    ├───Cedula Nombre Apellido
    │   ├───Factura_1.pdf
    │   ├───Factura_2.pdf
    │   └───...
    └───...
```
## Personalización y Flexibilidad
Este programa está diseñado para ser altamente personalizable según las necesidades específicas del usuario. Las siguientes características permiten una adaptación sencilla:

### Variables de Entorno:
El programa utiliza variables de entorno para configurar rutas de directorio, nombres de archivos y otros parámetros. Esto facilita la adaptación del programa a diferentes entornos de trabajo sin necesidad de modificar el código fuente.
```JavaScript
// Ver el .env.example por si se quiere trabajar en local, sino colocar las varibles en el PATH

PATH_SAVE="YOUR_PATH"
// por si dejas abierto el programa y copias una url que no contenga un pdf o la dirección al PDF, lo que hará la lógica es usar esta variable e ignorar las demás
URL_FIND="YOUR URL TO FIND AND DONT COPY ANY OTHER THING"
URL_INIT="IF YOUR URL TO DOWNLOAD THE PDF FILE HAS A PARAMETER IN MID OF THIS LINK PUT HERE, ELSE REPLACE THE VARIABLE WITH YOUR URL"
URL_END="COMPLETE THE URL WITH THE REST OF THE PARAMETERS IF IS NECESARY, ELSE REPLACE THE VARIABLE WITH YOUR URL"

```
### Expresiones Regulares (Regex):
Las expresiones regulares se utilizan para extraer datos específicos de las facturas, como el número de identificación del paciente, el nombre completo y otros detalles relevantes. Estas expresiones regulares pueden ser modificadas según el formato de las facturas o los requisitos del usuario.

### Flexibilidad en la Estructura de Carpetas:
La estructura de carpetas proporcionada es un ejemplo de organización, pero puede ser ajustada según las preferencias del usuario o los requisitos del sistema de gestión de documentos.

Configuración de Valores Predeterminados: Se pueden definir valores predeterminados para simplificar el proceso de configuración inicial del programa. Estos valores pueden ser modificados posteriormente según sea necesario.

Con estas características, el programa ofrece una gran flexibilidad y adaptabilidad, permitiendo su uso en una variedad de contextos y escenarios sin comprometer la eficiencia ni la funcionalidad.

## Consideraciones

Velocidad: Aunque el proceso puede ser un poco lento, la automatización ahorra tiempo y esfuerzo en comparación con la descarga manual de cada factura.

Seguridad: Es importante garantizar que se respeten las políticas de seguridad y privacidad al manejar datos sensibles de los pacientes.

Con este programa, el proceso de descarga y organización de facturas se vuelve más eficiente y ordenado, facilitando la gestión administrativa en Vidanova.

## Run Locally

Clone the project

```bash
  git clone https://github.com/CarlosRivera4726/PDF-DOWNLOADER
```

Go to the project directory

```bash
  cd PDF-DOWNLOADER
```

Install dependencies manually

```bash
pip install keyboard
pip install PyPDF2
pip install pyperclip
pip install python-dotenv
```

or install dependencies using requirements.txt

```bash
pip install -r requirements.txt
```

Start the program

**Windows:**

```bash
py main.py
```

**Linux:**
If you want to use `Linux` or `Mac` you need to change the command os.system("cls") to os.system("clear") inside the file `vidanova.py` 

```bash
python3 main.py
```

## Tech Stack

**Server:** Python3

## Agradecimiento 🤚🤚

Gracias por ver este repositorio y si quieren pueden apoyar para más.
