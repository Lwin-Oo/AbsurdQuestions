class User:
    def __init__ (self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

class UserManager:
    def __init__(self):
        self.users = []

    def insert(self, user):

        self.users.append(user)

    def find(self, user):
        pass

    def update(self, username, new_user_data):
        for users in self.users:
            if user.username == username:
                user.name, user.email = new_user_data
                return True
            return False


    def list_all_users(self):
        for user in self.users:
            print(f"Name: {user.name}, Username: {user.username}, Email: {user.email}")

def read_user_information(user_information):
    users = []
    with open(user_information, 'r') as file:
        lines = file.readlines()
        user_info = {}
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split(': ')
                user_info[key] = value
            else:
                users.append(User(user_info['Username'], user_info['Name'], user_info['Email']))
                user_info = {}
    return users

user_manager = UserManager()

user_information = 'user_information.txt'
users = read_user_information(user_information)

name_input = input("Name: ")
username_input = input("Username: ")
email_input = input("Email: ")
new_user = User(name_input, username_input, email_input)

user_manager.insert(new_user)

user_manager.list_all_users()
