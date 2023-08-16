
# Advanced Python Decorator Functions
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


# Decorator to authenticate the login
def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Ivan")
create_blog_post(new_user)
