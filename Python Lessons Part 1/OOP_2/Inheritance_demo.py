class User:
    active_user = 0
    @classmethod
    def display_active_users(cls):
        return f"Şu anda aktif {cls.active_user} user var"
    def __init__(self,firstname,lastname) :
        self.firstname = firstname
        self.lastname = lastname
        User.active_user += 1
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
class Moderator(User):
    def __init__(self, firstname, lastname,community):
        super().__init__(firstname, lastname)
        self.community = community
print(User.display_active_users())
u1 = User("Fehmi","Demirkan")
m1 = Moderator("Barry","Allen","Software")
print(User.display_active_users())

