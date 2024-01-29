import re

class User:
  def __init__(self, user, name, surname, tyil, email):
    self.user = user
    self.name = name
    self.surname = surname
    self.tyil = tyil
    andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
    while True:
      if re.match(andoza, email):
        self.email = email
        break
      else:
        print(email)
        email = input("Emailni to'g'ri kiriting!")
    

  def get_user(self):
    return self.user

  def get_name(self):
    return self.name

  def get_surname(self):
    return self.surname

  def get_tyil(self):
    return self.tyil
  
  def get_email(self):
    return self.email

  def get_info(self):
    return f"\n{self.user} foydalanuvchi haqida ma'lumot: \nIsmi: {self.name}  Familiyasi: {self.surname} \nTug'ilgan yili: {self.tyil} \nE-pochta manzili: {self.email}"


user1 = User('User1', 'Kessak', 'Toshev', 1900, 'www.kessakgmail.com')
user2 = User('User2', 'Loybek', 'Turpoqov', 1980, 'www.loybek@gmail.com')

print(user1.get_info())
print(user2.get_info())
print(type(user1))
