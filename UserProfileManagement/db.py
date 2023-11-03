
class User:
    def __init__ (self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

user1 = User('tiffany', 'Tiffany Young', 'tiffany@gmail.com')
user2 = User('dara', 'Sandara Park', 'dara@gmail.com')
user3 = User('seulgi', 'Seulgi Kang', 'seulgi@gmail.com')
user4 = User('rose', 'Chaeyoung PArk', 'rose@gmail.com')
user5 = User('mina', 'Mina Myoi', 'mina@gmail.com')
user6 = User('winter', 'Min-jeong Kim', 'winter@gmail.com')
user7 = User('lia', 'Jisu Choi', 'lia@gmail.com')
user8 = User('liz', 'Jiwon Kim', 'liz@gmail.com')
user9 = User('sakura', 'Sakura Miyawaki', 'sakura@gmail.com')
user10 = User('hanni', 'Hanni Pham', 'hanni@gmail.com')


with open('user_information.txt', 'w') as file:
    for user in [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]:
        file.write(f'Username: {user.username}\n')
        file.write(f'Name: {user.name}\n')
        file.write(f'Email: {user.email}\n')
        file.write('\n')

print("User information has been written to 'user_information.txt'.")