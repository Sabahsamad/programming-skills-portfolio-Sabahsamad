#Exercise 4: Stages of Life :ballot_box_with_check:
'''Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
•If the person is less than 3 years old, print a message that the person is a baby.
•If the person is at least 3 years old but less than 5, print a message that the person is a toddler.
•If the person is at least 5 years old but less than 14, print a message that the person is a kid.
•If the person is at least 14 years old but less than 21, print a message that the person is a teenager.
•If the person is at least 21 years old but less than 66, print a message that the person is an adult.
•If the person is age 66 or older, print a message that the person is an elder.'''

Age = 18
if Age < 3:
    print("Aww! You're still a baby.")
elif Age < 5:
    print("Hey! You're a toddler.")
elif Age < 14:
    print("Hey! You're a kid.")
elif Age < 21:
    print("Hey! You're a teenager.")
elif Age < 66:
    print("Hey! You're an adult.")
else:
    print("Hey! You're an elder.")