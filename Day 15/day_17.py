# Creating a class
class User:
    
    # Constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username


user_1 = User("001", "John")
user_2 = User("002", "Ivan")

print(user_1.id)
print(user_1.username)

print(user_2.id)
print(user_2.username)

