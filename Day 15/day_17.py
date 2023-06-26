# Creating a class
class User:
    
    # Constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # Creating a method
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "John")
user_2 = User("002", "Ivan")

print(user_1.id)
print(user_1.username)

print(user_2.id)
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

