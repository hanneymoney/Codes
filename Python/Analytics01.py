# Let list of Aisle character or alphabeth (strings)
Aisle = ["Bakery", "Dairy", "Dairy", "Dairy", "Cans"]

# Let list of Items character or alphabeth (strings)
Item = ["Bread", "Milk", "Cheese", "Yogurt", "Soup"]

# Let list of Price number (integer)
Price = [150, 90, 250, 95, 120]

#using for loop to fetch each data type entries and display the content.
ann = [type (Item) for Item in Aisle]
Baga = [type (Item) for Item in Item]
Fella = [type (Item) for Item in Price]

print("Aisle:", ann)
print("Item:", Baga)
print("Price:", Fella)

#using index to display the first item in the list
print(Item[0])


#using slicing to display the last entry in the item list

print(Item[-1]) 

#using index to display the second to the fourth entry in the item list
print(Item[1:4])


#counting the length of the price list

thelengthofpriceList = len(Price)
#let's assume the value is unknown.
assumption = 0
#I'm looping through the length of the price list
for p in range(thelengthofpriceList):
#adding every numbers found in the list.
    assumption = assumption + Price[p]
#displaying the output   
print("Using loop to calculate the total cost of the shopping price list is:", assumption)
    


# adding all the figures in the shopping list
#print(Price)
#In built method for summation
Total_cost = sum(Price)
print("Using in built function to calculate the total cost of the shopping price list is:", Total_cost)


# This line of code Initialize an empty list
shopping = []

# A for Loop fuction over the indices of the given lists
for i in range(len(Aisle)):
# creation of a dictionary for each item and append to the shopping list
    shopping.append({"Aisle": Aisle[i], "Item": Item[i], "Price": Price[i]})

# Now shopping contains the list of dictionaries

# Printing of  each item in the shopping price list on a new line
for item in shopping:
    print(item)
    
    
# Given data structured as a list of dictionaries
shopping = [
    {"Aisle": "Bakery", "Item": "Bread", "Price": 150},
    {"Aisle": "Dairy", "Item": "Milk", "Price": 90},
    {"Aisle": "Dairy", "Item": "Cheese", "Price": 250},
    {"Aisle": "Dairy", "Item": "Yogurt", "Price": 95},
    {"Aisle": "Cans", "Item": "Soup", "Price": 120}
]


#given a built in data structure to store the total spend by aisle  
total_spend_per_aisle = {}

# Now, Calculating the total spend per aisle
for item in shopping:
    # The get method returns 0 if the aisle is not already in the dictionary
    total_spend_per_aisle[item['Aisle']] = total_spend_per_aisle.get(item['Aisle'], 0) + item['Price']

# Output the total spend per aisle
for aisle, total in total_spend_per_aisle.items():
    print(f"Total spend in the {aisle} aisle: {total}")

# To handle new aisles, I added them to the shopping list as a new dictionaries
# and run the loop again,but no change in the code.

  
    
# I Populate the shopping list with the given data
for i in range(len(Aisle)):
    shopping.append({"Aisle": Aisle[i], "Item": Item[i], "Price": Price[i]})

# Then Initialize a dictionary to hold the total spend per aisle
total_spend_per_aisle = {}

# Also, Calculate the total spend per aisle
for item in shopping:
    # If the aisle is already in the dictionary, add the price to the total
    if item['Aisle'] in total_spend_per_aisle:
        total_spend_per_aisle[item['Aisle']] += item['Price']
    # If the aisle is not in the dictionary, initialize it with the current price
    else:
        total_spend_per_aisle[item['Aisle']] = item['Price']

# Output the total spend per aisle
for aisle, total in total_spend_per_aisle.items():
    print(f"Total spend in the {aisle} aisle: {total}")

# This code can easily handle new data with additional aisles.
# For example, if you add items from a 'Frozen' aisle, the code will automatically
# create a new category in the total_spend_per_aisle dictionary and calculate the total spend.


#creation of Aisle list 
Aisle = ["Bakery", "Dairy", "Dairy", "Dairy", "Cans"]
#creation of Item list 
Item = ["Bread", "Milk", "Cheese", "Yogurt", "Soup"]
#creation of price list 
Price = [150, 90, 250, 95, 120]

# Create a list of tuples using those three lists above 
Stuple= [(Aisle[i], Item[i], Price[i]) for i in range(len(Aisle))]

# and I Print the result
print(Stuple)

#I create three list and I used loop with Append method:
Aisle = ["Bakery", "Dairy", "Dairy", "Dairy", "Cans"]
Item = ["Bread", "Milk", "Cheese", "Yogurt", "Soup"]
Price = [150, 90, 250, 95, 120]

#I create a list of tuples using a loop with append
Stuple = []
for i in range(len(Aisle)):
    Stuple.append((Aisle[i], Item[i], Price[i]))

 #Print the result
print(Stuple)


#Using the built-in to define max function and it is named "highest_price":
def highest_price(prices):
#A documentation to descript the purpose of my fuction
    """Returns the highest price using the built-in max function."""
    return max(prices)

#prices list
Price = [150, 90, 250, 95, 120]

# I called the function and also pass print instruction to display the result
highest_price = highest_price(Price)
print(f"The highest price is: {highest_price}")

#new line
"\n"
#Using an "If Statement":
"\n"
def highest_price(prices):
#A documentation to descript the purpose of my fuction
    """Returns the highest price using a loop and if statement."""
    highest = prices[0]  # I'm assumping the first price is the highest initially
    for price in prices:
        if price > highest:
            highest = price
    return highest

#prices list
Price = [150, 90, 250, 95, 120]

# I called the function and also pass print instruction to display the result
highest_price = find_highest_price(Price)
print(f"The highest price is: {highest_price}")



#"\n"
