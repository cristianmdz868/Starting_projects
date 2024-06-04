master_passwrd=input("Enter a master password: ")

def add():
    name=input("Name: ")
    passwd=input("Password: ")
    with open('password.txt','a') as f:
        f.write(name + "|" + passwd + "\n")

  
def view():
   with open('password.txt','r') as f:
       for line in f.readlines():
           data = line.rstrip()
           user, passw=data.split("|") # this uses | as a delimiter and gives each a new list
           print("User:", user, "Password", passw)
while True:
    
    mode= input("Decide whether you want to add or view a password (add or view): ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode =="view":
        view()
    else:
        print("That is incorrect")
        continue


