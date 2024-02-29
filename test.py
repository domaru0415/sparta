class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print("name:", self.name)
        print("username:", self.username)
        pass


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        pass


members = []

member1 = Member("A", "a", "pw1")
member2 = Member("B", "b", "pw2")
member3 = Member("C", "c", "pw3")

members.append(member1)
members.append(member2)
members.append(member3)

print("Members:")
for member in members:
    print(member.name)

posts = []

post1 = Post("title 1", "content 1 by A", "a")
post2 = Post("title 2", "content 2 by B", "b")
post3 = Post("title 3", "content 3 by C", "c")
post4 = Post("title 4", "content 4 by A", "a")
post5 = Post("title 5", "content 5 by B", "b")
post6 = Post("title 6", "content 6 by C", "c")
post7 = Post("title 7", "content 7 by A", "a")
post8 = Post("title 8", "content 8 by B", "b")
post9 = Post("title 9", "content 9 by C", "c")

posts.extend([post1, post2, post3, post4, post5, post6, post7, post8, post9])

print("\nPosts by A:")
for post in posts:
    if post.author == "a":
        print(post.title)

print("\nPosts containing 'content 6':")
for post in posts:
    if "content 6" in post.content:
        print(post.title)
