import re
import os
import PyPDF2
import requests

# URL del PDF
urls=[]
for url in set(urls):
    response = requests.get(url, verify=False)

    # Guardar el PDF temporalmente
    with open('temp.pdf', 'wb') as file:
        file.write(response.content)


    # Leer el PDF temporal
    def extract_information(pdf_path):
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in range(len(reader.pages)):
                text += reader.pages[0].extract_text()
        return text

    pdf_text = extract_information('temp.pdf')

    # Buscar el nombre del paciente
    name_match = re.search(r'Nivel Salarial:\s*([A-Z ]+)', pdf_text)
    if name_match:
        patient_name = name_match.group(1).strip()
    else:
        patient_name = 'desconocido'

    # Limpiar el nombre del paciente para eliminar caracteres no deseados
    patient_name = re.sub(r'[^A-Za-z0-9 ]+', '', patient_name)

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
    output_dir = os.path.join(os.getcwd(), patient_id+" "+patient_name, invoice_id)
    os.makedirs(output_dir, exist_ok=True)

    # Mover el PDF a la nueva ubicación
    output_path = os.path.join(output_dir, f'{invoice_id}.pdf')
    os.rename('temp.pdf', output_path)

    print(f'Archivo guardado en: {output_path}')

