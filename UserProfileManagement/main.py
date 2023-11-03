class User:
    def __init__ (self, username, name, email):
        self.username = username
        self.name = name
        self.email = email



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


def insert(self, user):
    pass

def find(self, user):
    pass

def update(self, user):
    pass

def list(self, user):
    pass