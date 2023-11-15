#Create a glossary with programming words and their meanings
glossary = {
    "Variable": "A named storage location in memory used to store data.",
    "Function": "A block of code that can be called to perform a specific task or operation.",
    "Loop": "A control structure that repeats a set of statements as long as a specified condition is met.",
    "Conditional Statement": "A statement that allows for different code to be executed depending on a condition.",
    "List": "An ordered collection of items, which can be of different data types."
}

#Print each word and its meaning neatly formatted with a newline between each pair
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")