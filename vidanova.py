import keyboard
import pyperclip
import time 
import os
import re
import PyPDF2
import requests
import shutil
from dotenv import load_dotenv
load_dotenv()

class vidanova(object):
    # C:\Users\TEMP\Desktop\TEST\VIDANOVA
    def __init__(self, path=os.getenv("PATH_SAVE" + "\\TEST")):
        self._path = f'{path}'
    
    def obtenerData(self):
        global copied_data
        
        while True:
            # Comprobar si algo se ha copiado al portapapeles (Ctrl + C)
            if keyboard.is_pressed('ctrl+c'):
                # Obtener el contenido del portapapeles y añadirlo a la lista
                time.sleep(0.5)
                copied_text = pyperclip.paste()
                if(os.getenv('URL_FIND') in copied_text):
                    id_factura = self.getDataFromPattern(text=copied_text)
                    urlFactura = os.getenv('URL_INIT') + id_factura + os.getenv('URL_END') 
                    self.guardarPDF(urlFactura)
                    os.system('cls') # or os.system('clear') for linux or mac
                    print("Your files are located in: ", self.getPath())

    def guardarPDF(self, url):
        response = requests.get(url, verify=False)

        # Guardar el PDF temporalmente
        with open('temp.pdf', 'wb') as file:
            file.write(response.content)


        # Leer el PDF temporal
        def extract_information(pdf_path):
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = reader.pages[0].extract_text()
            return text

        pdf_text = extract_information('temp.pdf')

        # Buscar el nombre del paciente
        name_match = re.search(r'Nivel Salarial:\s*([\w\sÁÉÍÓÚÑáéíóúñ]+)', pdf_text)
        if name_match:
            patient_name = name_match.group(1).strip()
        else:
            patient_name = 'desconocido'

        # Limpiar el nombre del paciente para eliminar caracteres no deseados
        patient_name = re.sub(r'[^A-Za-z0-9ÁÉÍÓÚÑáéíóúñ\s]+', '', patient_name)
        patient_name = re.sub(r'[<>:"/\\|?*\n\r]+', '', patient_name)
        # Eliminar FEMENIDO O MASCULINO
        patient_name = re.sub(r'FEMENINO|MASCULINO', '', patient_name)
        # Eliminar dias de la semana, mayusculas o minusculas
        patient_name = re.sub(r'LUNES|MARTES|MIÉRCOLES|JUEVES|VIERNES|SÁBADO|DOMINGO|lunes|martes|miércoles|jueves|viernes|sábado|domingo', '', patient_name)
        patient_name = patient_name.strip()
        # Buscar la cédula del paciente
        id_match = re.search(r'\d{2} Año\(s\) \d{1,2} Mes\(es\) \d{1,2} Dia\(s\)(\d+)', pdf_text)
        if id_match:
            patient_id = id_match.group(1).strip()
        else:
            patient_id = 'sin_id'


        # Suponiendo que el ID de factura tiene el formato "V123456"
        id_match = re.search(r'V\s?\d+', pdf_text)
        invoice_id = id_match.group(0) if id_match else 'sin_id'


        # Crear la carpeta si no existe
        output_dir = os.path.join(self.getPath(), patient_id+" "+patient_name, invoice_id)
        os.makedirs(output_dir, exist_ok=True)

        # Mover el PDF a la nueva ubicación
        output_path = os.path.join(output_dir, f'{invoice_id}.pdf')
        shutil.move('temp.pdf', output_path)

        print(f'Archivo guardado en: {output_path}')

    # pattern to search maybe: rP196_ESTADOITEMS:(\d+),0 or any other
    def getDataFromPattern(self, patternToSearch=r"P196_ESTADOITEMS:(\d+),0", text=""):
        pattern = re.compile(patternToSearch)
        match = pattern.search(text)
        if match:
            print(match.group(1))
            item = match.group(1)
        else:
            print('No se encontró el parámetro P196_ESTADOITEMS en la URL.')
        data = item
        return data
    def getPath(self):
        return self._path
    