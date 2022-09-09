class Users:

    def __init__(self):
        print("Welcome to Dede's Flight Club!\nWe find the best deals and email you")
        self.first_name = input("What is your first name?\n").lower()
        self.surname = input("What is your last name?\n").lower()
        self.email = input("What is your email?\n").lower()
        confirmation = input("Type your email again?\n").lower()

        if self.email == confirmation:
            print("You're in the Club!")

        # print(f"First name: {self.first_name}\nLast name: {self.surname}\nEmail: {self.email}")