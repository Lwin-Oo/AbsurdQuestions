class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

class UserManager:
    def __init__(self):
        self.users = []

    def insert(self, user):
        self.users.append(user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, username, new_user_data):
        for user in self.users:
            if user.username == username:
                user.name, user.email = new_user_data
                return True
        return False

    def list_all_users(self):
        return self.users

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

def write_user_information(user_information, users):
    with open(user_information, 'w') as file:
        for user in users:
            file.write(f'Username: {user.username}\n')
            file.write(f'Name: {user.name}\n')
            file.write(f'Email: {user.email}\n')
            file.write('\n')

# Initialize the UserManager and read user information from the file
user_manager = UserManager()
user_information = 'user_information.txt'
users = read_user_information(user_information)

while True:
    print("1. Insert new user")
    print("2. Update user")
    print("3. List all users")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        name_input = input("Name: ")
        username_input = input("Username: ")
        email_input = input("Email: ")
        new_user = User(username_input, name_input, email_input)
        user_manager.insert(new_user)
        users.append(new_user)
        write_user_information(user_information, users)
        print("User inserted successfully.")
    
    elif choice == '2':
        username = input("Enter the username of the user to update: ")
        new_name = input("New name: ")
        new_email = input("New email: ")
        if user_manager.update(username, (new_name, new_email)):
            write_user_information(user_information, users)
            print("User updated successfully.")
        else:
            print(f"User with username '{username}' not found.")
    
    elif choice == '3':
        all_users = user_manager.list_all_users()
        for user in all_users:
            print(f"Name: {user.name}, Username: {user.username}, Email: {user.email}")
    
    elif choice == '4':
        print("Goodbye!")
        break
