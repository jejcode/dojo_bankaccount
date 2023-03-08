# Coding Dojo Python stack assignment:
# bank account

What I learned:
If I want to update a class attribute in the __init__, use the class name to
access it. However, within a class method, use "cls" to reference the attribute.
  Example:
  class User:
    all_users[]
    def __init__(self):
        User.all_users.append('user')
    
    @classmethod
    def display_all_users(cls):
        for user in cls.all_users:
            print(user)
    