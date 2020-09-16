username = input("What is your username: ")
password = input("Please input your password: ")

password_length = len(password)
hidden_password = '*'*password_length

print(f"Your username is {username} and your password is {hidden_password} with length {password_length}")