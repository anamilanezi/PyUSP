class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0          # Providing a default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "anamilanezi")
print(f"User id: {user_1.id}")
print(f"Username: {user_1.username}")
print(f"Num of followers: {user_1.followers}")

user_2 = User("002", "willgraham")

user_1.follow(user_2)

print(f"{user_1.username} followers: {user_1.followers}")
print(f"{user_1.username} follows: {user_1.following}")
print(f"{user_2.username} followers: {user_2.followers}")
print(f"{user_2.username} follows: {user_2.following}")