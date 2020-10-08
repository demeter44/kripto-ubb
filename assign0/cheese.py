cheeses = ["Muenster", "Cheddar", "Red Leicester"]

print("Good morning. Welcome to the National Cheese Emporium!")

finished = False
while not finished:
    query = input("What would you like?")
    if query in cheeses:
        print("We have "+query+" ,yessir.")
        finished = True
    elif query == "You... do have some cheese, don't you?" or query == "Have you in fact got any cheese here at all?":
        print("We have ")
        for cheese in cheeses:
            print(cheese)
        print("cheese(s)!")
    else:
        print("I'm afraid we don't have any "+query)

