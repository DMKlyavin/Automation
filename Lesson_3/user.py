class User:

    def __init__(self, firstname, lastname):
        self.fn = firstname
        self.ln = lastname

    def print_firstname(self):
        print(self.fn)

    def print_lastname(self):
        print(self.ln)

    def print_lastname_and_firstname(self):
        print(self.fn, self.ln)
