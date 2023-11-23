class UserDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r') as file:
                users = {}
                for line in file:
                    user_data = line.strip().split(',')
                    user_id = int(user_data[0])
                    name = user_data[1]
                    age = int(user_data[2])
                    email = user_data[3]
                    users[user_id] = {'name': name, 'age': age, 'email': email}
                return users
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open(self.file_path, 'w') as file:
            for user_id, user_info in self.users.items():
                file.write(f"ID: {user_id}\nName: {user_info['name']}\nAge: {user_info['age']}\nEmail: {user_info['email']}\n\n")

    def insert_user(self):
        user_id = int(input("Enter user ID: "))
        name = input("Enter user name: ")
        age = int(input("Enter user age: "))
        email = input("Enter user email: ")

        if user_id not in self.users:
            self.users[user_id] = {'name': name, 'age': age, 'email': email}
            self.save_users()
            print(f"User with ID {user_id} added successfully.")
        else:
            print(f"User with ID {user_id} already exists. Use update operation to modify the user.")

    def update_user(self):
        user_id = int(input("Enter user ID to update: "))
        if user_id in self.users:
            name = input(f"Enter new name for user {user_id}: ")
            age = int(input(f"Enter new age for user {user_id}: "))
            email = input(f"Enter new email for user {user_id}: ")

            self.users[user_id]['name'] = name
            self.users[user_id]['age'] = age
            self.users[user_id]['email'] = email

            self.save_users()
            print(f"User with ID {user_id} updated successfully.")
        else:
            print(f"User with ID {user_id} does not exist. Use insert operation to add a new user.")

    def list_all_users(self):
        if not self.users:
            print("No users in the database.")
        else:
            print("List of all users:")
            for user_id, user_info in self.users.items():
                print(f"User ID: {user_id}, Name: {user_info['name']}, Age: {user_info['age']}, Email: {user_info['email']}")

# Example usage:
file_path = 'user_database.txt'
user_db = UserDatabase(file_path)

while True:
    print("1. Insert new user")
    print("2. Update user")
    print("3. List all users")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        user_db.insert_user()
    
    elif choice == '2':
        user_db.update_user()

    elif choice == '3':
        user_db.list_all_users()

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
