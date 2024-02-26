import re

from Backend.src.parser_generic import MedicalDOCParser

class PatientDetailsParser(MedicalDOCParser):
    def __init__(self,text):
        MedicalDOCParser.__init__(self,text)

    def parse(self):
        return {'patient_name':self.get_patient_name(),
        'phone_number':self.get_patient_phone_number(),
        'medical_problems':self.get_medical_problems(),
        'hepatitis_b_vaccination':self.get_hepatitis_b_vaccinations()
        }

    def get_patient_name(self):
        pattern = 'Patient.Information(.*?)\(\d{3}\)'

        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        name=''
        if matches:
            name = self.remove_noise_from_name(matches[0])
        return name

    def get_patient_phone_number(self):
        pattern = 'Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0][-1]

    def get_medical_problems(self):
        pattern = 'List any Medical Problems .*?:(.*)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()

    def get_hepatitis_b_vaccinations(self):
        pattern = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if matches:
            return matches[0].strip()


    def remove_noise_from_name(self,name):
            name = name.replace('Birth Date', '').strip()
            date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
            date_matches = re.findall(date_pattern, name)

            if date_matches:
                date = date_matches[0][0]
                name = name.replace(date, '').strip()
            return name

#if __name__ == '__main__':
    document_text = '''17/12/2020

    Patient Medical Record

    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight’
    9264 Ash Dr 95
    New York City, 10005 .
    United States Height:
    190
    In Casc of Emergency
    7 ee
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    Home phone United States
    (990) 375-4621
    Work phone

    Genera! Medical History

    a

    a

    a ea A CE i a

    Chicken Pox (Varicella): Measies:

    IMMUNE IMMUNE

    Have you had the Hepatitis B vaccination?
    No

    List any Medical Problems (asthma, seizures, headaches):

    Migraine

    be

    CO
    nat
     aa
     oo'''
   # pp =PatientDetailsParser(document_text)
   # print(pp.parse())