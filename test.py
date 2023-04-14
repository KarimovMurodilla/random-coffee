names = []

while True:
    name = input("Enter name: ")

    if name == 'stop':
        break
    
    else:
        names.append(name)

print("Count of users: ", len(names))