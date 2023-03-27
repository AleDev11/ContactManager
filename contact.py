class Contact:
    def __init__(self):
        self.id = 0
        self.email = ""
        self.name = ""
        self.lastname = ""
        self.password = ""
    def __init__(self, id, email, name, lastname, password):
        self.id = id
        self.email = email
        self.name = name
        self.lastname = lastname
        self.password = password

    def __str__(self):
        return "ID: " + str(self.id) + " Email: " + self.email + " Name: " + self.name + " Lastname: " + self.lastname + " Password: " + self.password