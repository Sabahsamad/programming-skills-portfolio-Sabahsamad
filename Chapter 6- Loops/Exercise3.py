#Write a loop that never ends, and run it. (To end the loop, press ctrl-C or close the window displaying the output.)

while True:
    age = input("How old are you? ")
    
    age = int(age)
    if age < 3:
        print("Your ticket is free")
    elif age < 12:
        print("Your ticket is $15") 
    else:
        print("Your ticket is $20")