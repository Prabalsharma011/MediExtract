
# To findout or extract the text from all text we used regular expression  and match it with text after mading  this we try to compat this

#def parse(self):
    #return {
        #'patients_name': self.get_name(),
        #'patient_address': self.get_address(),
        #'medicines': self.get_medicines(),
        #'Directions': self.get_directions(),
        #'Refill': self.get_refill()
    #}

#def get_name(self):
    #pattern = 'Name:(.*)Date'
    #matches = re.findall(pattern, self.text)
    #if len(matches) > 0:
        #return matches[0].strip()


#def get_address(self):
    #pattern = 'Address:(.*)\n'
    #matches = re.findall(pattern, self.text)
    #if len(matches) > 0:
        #return matches[0].strip()


#def get_medicines(self):
    #pattern = 'Address:[^\n]*(.*)Directions'
    #matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #if len(matches) > 0:
        #return matches[0].strip()


#def get_directions(self):
    #pattern = 'Directions:(.*)Refill'
    #matches = re.findall(pattern, self.text, flags=re.DOTALL)
    #if len(matches) > 0:
        #return matches[0].strip()


#def get_refill(self):
    #pattern = 'Refill:(.*)'
    #matches = re.findall(pattern, self.text)
    #if len(matches) > 0:
        #return matches[0].strip()