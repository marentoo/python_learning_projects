class User:
    def __init__(self, name, age):
        self.name = name
        self.is_logged_in = False
        self. age = age

def is_authenticated_decorated(fun):
    def wrapper(*args):
        if args[0].is_logged_in == True or args[1]:
            fun(args[0])
        else:
            print("not auth error")
    return wrapper


@is_authenticated_decorated
def create_blog_post(user, second_user):
    print(f"This is {user.name}'s new blog post.")
    print(f"age verification: {user.age}")
    print(f"the other guy has: {second_user.age}")


user1 = User("mat", 18)
user1.is_logged_in = True

user2=User("john", 20)
user2.is_logged_in = True

create_blog_post(user1,user2)
