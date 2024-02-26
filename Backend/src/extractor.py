from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import util
from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

POPPLER_PATH=r'C:\poppler-24.02.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe' #image to text conversion this tessarcat is engine

def extract(file_path, file_format):

 #Step 1: Extracting text from pdf file
    pages = convert_from_path(file_path,poppler_path=POPPLER_PATH)  # poppler used to change pdf 2 image
    document_text=''

    if len(pages)>0:
       page = pages[0]
       processed_image =  util.preprocess_image(page)
       text = pytesseract.image_to_string(processed_image, lang='eng')
       document_text = '\n' +text





    #step 2: extract fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse() #extract data from prescription

    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse() #extract data from patient details

    else:
        raise Exception(f"Invalid document format: {file_format}")

    return extracted_data



if __name__== '__main__':
    data = extract('../resources/prescription/pre_1.pdf','prescription')
    print(data)
