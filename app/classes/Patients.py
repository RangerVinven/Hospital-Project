class Patient():
    def __init__(self, firstname, surname, postcode, address, phone, email):
        self.patient_id = 0
        self.firstname = firstname
        self.surname = surname
        self.postcode = postcode
        self.address = address
        self.phone = phone
        self.email = email


class InsuredPatient(Patient):
    def __init__(self, firstname, surname, postcode, address, phone, email, insurance_type, insurance_company_name, duration_of_insurance):
        super().__init__(firstname, surname, postcode, address, phone, email)
        
        self.insurance_type = insurance_type
        self.insurance_company_name = insurance_company_name
        self.duration_of_insurance = duration_of_insurance 
