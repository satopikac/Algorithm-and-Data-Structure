class User:
    def __init__(self,f_name,l_name):
        self.fname=f_name
        self.lname=l_name
        self.login_attempts =0

    def describe(self):
        print(f"{self.fname} {self.lname}")

    def greet(self):
        print(f"hello,{self.fname} {self.lname}")
    
    def incremenr_la(self):
        self.login_attempts += 1
    
    def reset(self):
        self.login_attempts =0
    
class Privileges:
    def __init__(self):
        self.privilege=['can add post','can delete post','can ban user']

class Admin(User):
    def __init__(self, f_name, l_name):
        super().__init__(f_name, l_name)
        self.privileges= Privileges()

    def show_privileges(self):
        print(self.privileges.privilege)