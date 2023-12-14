#write a program where you can take 5 numbers as an input from user and print their #sum , average
v=int(input("Enter Number : "))
w=int(input("Enter Number : "))
x=int(input("Enter Number : "))
y=int(input("Enter Number : "))
z=int(input("Enter Number : "))
print(v+w+x+y+z)
#write a programin which you can display list of your 5 favourite things and print the list
A=input("Enter fav things : ")
B=input("Enter fav things : ")
C=input("Enter fav things : ")
D=input("Enter fav things : ")
E=input("Enter fav things : ")
things=[A,B,C,D,E]
print(things)
#create a nested dictionary to store the iteam category , iteam name , iteam code, price, and stock and display the list of iteams using function 
items = {
    'item1': {
        'category': 'CHIPS',
        'name': 'Lays',
        'code': 'L123',
        'price': 3.00,
        'stock': 50
    },
    'item2': {
        'category': 'CHOCOLATE',
        'name': 'Kitkat',
        'code': 'K123',
        'price': 2.50,
        'stock': 70
    },
    
    # Add more items as needed
}

# Accessing information for 'item1'
print("Category:", items['item1']['category'])
print("Name:", items['item1']['name'])
print("Code:", items['item1']['code'])
print("Price:", items['item1']['price'])
print("Stock:", items['item1']['stock'])
# Accessing information for 'item2'
print("Category:", items['item2']['category'])
print("Name:", items['item2']['name'])
print("Code:", items['item2']['code'])
print("Price:", items['item2']['price'])
print("Stock:", items['item2']['stock'])