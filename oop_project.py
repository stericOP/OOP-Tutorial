class Chatbook:
  def __init__(self):
    self.username = ''
    self.password = ''
    self.loggedin = False
    self.menu()

  def menu(self):
    user_input = input(""""Welcome to Chatbook || How would you like to continue?
                           1- Press 1 to signup
                           2- Press 2 to signin
                           3- Press 3 to write a post
                           4- Press 4 to message a friend
                           5- Press any key to signup""")

    if user_input == '1':
      self.signup()
    elif user_input == '2':
      self.signin()
    elif user_input == '3':
      pass
    elif user_input == '4':
      pass
    else:
      exit()

  def signup(self):
    email = input("Enter your email here -> ")
    pswd = input("Setup your password -> ")
    self.username = email
    self.password = pswd
    print("You have signed up to ChatBook")
    print("\n")
    self.menu() 

  def signin(self):
    if self.username == '' and self.password == '':
      print("Please Signup first by clicking 1")
    else:
      username = input("Enter your email/username here -> ")
      pswd = input("enter your password here -> ")
      if(self.username == username and self.password == pswd):
        print("You have signed in successfully")
        self.loggedin = True
      else: 
        print("Incorrect username/password")
    print("\n")
    self.menu()  


chat = Chatbook()