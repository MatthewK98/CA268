print("Enter a name and number, or a name and ? to query (!! to exit)")
contacts = {}
while True:
    line = input()
    if line == "!!":
        break
    line = line.split()
    name = line[0]
    num = line[1]
    if name not in contacts and num == "?":
        print("Sorry, there is no {}".format(name))

    elif num != "?":
        contacts[name] = num
    
    elif num == "?":
        print("{} has number {}".format(name, contacts[name]))
print("Bye")