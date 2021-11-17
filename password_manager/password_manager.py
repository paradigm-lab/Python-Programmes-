from cryptography.fernet import Fernet

#key + password + text to encrypt = random text
#random text + key + passwd = text to encrypt

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

#Funtion is an executable reuserable block of code
#pass is a keyword that does nothing it is just there so that you can't get like the indentation errors

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    #with is a keyword that help as to do things in after indetetion and it also close the file for as
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("Would you like to add the new password or view existing ones (view, add), press q to quit? ").lower()
    
    if mode == "q":
        break

    
    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue
