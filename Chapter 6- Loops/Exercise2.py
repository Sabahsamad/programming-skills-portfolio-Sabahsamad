while True:
    age_input = input("Enter you age or 'quit' to exit : ")
    if age_input.lower() == 'quit':
        break
    try:
        age = int(age_input)
    except ValueError:
        print ("Please enter a valid age")
        continue
    if age < 3:
        ticket_cost = 0
    elif 3 <= age <= 12:
        ticket_cost = 15
    else:
        ticket_cost = 20

    print (f"The cost of your movie ticket is {ticket_cost} dhs")