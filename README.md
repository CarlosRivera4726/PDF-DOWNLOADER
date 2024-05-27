# PDF DOWNLOADER 📝

He creado este programa, para la optimización para descargar una factura a traves del id obtenido de la url del programa que usamos en Vidanova, el cual es un poco lento, pero con esto tomamos la url de la factura, apartir de aqui sacamos el id y cómo abren una ventana con la factura entonces le damos ese id, completamos la url y ya con python terminamos descargando el pdf, este pdf tenemos que guardarlo en un directorio y que venga con sus datos, por ejemplo: cedula de ciudadania y su nombre completo y dentro de esta carpeta colocamos la/las facturas que tenga el paciente

## Run Locally

Clone the project

```bash
  git clone https://github.com/CarlosRivera4726/download_pdf
```

Go to the project directory

```bash
  cd download-pdf
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
to use Linux or Mac you need to change the command os.system("cls") to os.system("clear")

```bash
python3 main.py
```

## Tech Stack

**Server:** Python3

## Agradecimiento 🤚🤚

Gracias por ver este repositorio y si quieren pueden apoyar para más
