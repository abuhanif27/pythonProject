class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def __str__(self):
        return f"{self.name.center(25)} | {self.email.center(25)} | {self.phone.center(25)} | {self.address.center(25)}"
