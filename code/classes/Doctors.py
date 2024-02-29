class Doctor():
    def __init__(self, firstname: str, surname: str, address: str, email: str):
        self.doctor_id = 0  # TODO - add function to generate the ID
        self.firstname = firstname
        self.surname = surname
        self.address = address
        self.email = email


class Specialist(Doctor):
    def __init__(self, firstname: str, surname: str, address: str, email: str, specilization: str, experience: int):
        super().__init__(firstname, surname, address, email)
        self.specilization = specilization
        self.experience = experience