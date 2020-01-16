class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []
        self.followers_list = []

    def follow(self, another_user):
        self.another_user = another_user
        #내가 다른사람을 팔로우
        self.following_list.append(self.another_user)
        #다른 사람이 나를 팔로우
        another_user.followers_list.append(self)

        # 몇명을 팔로우하는지 리턴

    def num_following(self):
        return len(self.following_list)

        # 팔로워가 몇명인지 리턴

    def num_followers(self):
        return len(self.followers_list)


user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())
