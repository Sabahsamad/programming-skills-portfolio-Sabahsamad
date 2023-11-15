#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
#such as Reykjavik is in Iceland. Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

#defining a function
def describe_city(name,country="INDIA"):
    print(f'{name} is in {country}')

#Call the function for three different cities
describe_city("delhi")
describe_city("Mumbai")
describe_city("Kerala") #This will use new default country value