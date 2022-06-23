class User:

    # Constructor - Initialize attributes for every new object created
    def __init__(self, username, id):
        self.username = username
        self.id = id
        # Some attributes may need a default value, e.g. insta accounts start with 0 followers, no need to pass that always
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("Bob", "01")
user2 = User("May", "02")

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

print(user1.id)