##Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
#medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size="large", message="I love Python"):
    print(f"Creating a {size} shirt with the message: {message}")

#Make a large shirt with the default message
make_shirt()

#Make a medium shirt with the default message
make_shirt(size="Large")

#Make a shirt of any size with a different message
make_shirt(size="Large", message='Python is the best programming language!')