class User:
    def __Init__(self, login, password, name, surname, address):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname
        self.address = address

    def login(self, input_login, input_password):
        input_login = input("Podaj login: ", )
        input_password = input("Podaj haslo: ", ) #zahashować!
