
# The values we want from the user
nickname = str(input("Please enter your nickname: "))
id = int(input("Please enter your id: "))
name = str(input("Please enter your name: "))
surname = str(input("Please enter your surname: "))
height = float(input("Please enter your height: "))

# Formats of user-entered values
print("Nickname:{} ".format(nickname))
print("ID:{} ".format(id))
print("Name:{} ".format(name))
print("Surname:{}".format(surname))
print("Height:{}".format(height))

# Types of values entered by the user
print(f"type of nickname : {type(nickname)} ")
print(f"type of id : {type(id)} ")
print(f"type of name : {type(name)} ")
print(f"type of surname : {type(surname)} ")
print(f"type of height : {type(height)} ")
