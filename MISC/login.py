# need to implement a way to add and "store" users username and password

# register the user
username = input("Please enter a username: ")
password = input("Please enter a password: ")


print("Rerouting back to login screen")


# Login attempt
login_username = input("Please enter your username: ")
login_password = input("Please enter your password: ")


# validate functions
def valid_username(stored_username, entered_username, stored_password, entered_password):
    if stored_username != entered_username:
        print("Sorry, incorrect username")
    else:
        valid_password(stored_password, entered_password)
        
        
def valid_password(stored_password, entered_password):
    if stored_password != entered_password:
        print("Sorry, incorrect password")
    else:
        print(success_message)
        
success_message = "!! Login successful !!"


# Call the username validation to start the process
valid_username(username, login_username, password, login_password)

