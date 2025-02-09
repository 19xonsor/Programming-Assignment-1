## PART A
# I gathered the data from user by using inputs
print("--- Part A: inputs ---")
guests = int(input("Number of guests:"))
adults = int(input("Adult guests:"))
catering = float(input("Catering cost per guest:"))
beverage = float(input("Beverage cost per guest:"))
length = int(input("Square cake length (in inches):"))

# PART B
#I caculated the catering cost based on the numbers of guests, 
# and the cost for both food and beverages
# Calculate food cost
food_cost = guests * catering
minors = guests - adults # I used this formula to find the minors in the guests
minor_cost = beverage * 0.35  #I made beverage times 35% because minors pays only 35% 
# # to find the beverage cost of the guests.
beverage_cost = (adults * beverage) + (minors * minor_cost)
# Calculting the total cost of the food and beverage cost
total_cost = food_cost + beverage_cost

# Printing cost calculation results, I put newline to space out.
print("\n--- Part B: cost ---")
print(f"The food costs ${food_cost:.2f}.")
print(f"The beverages cost ${beverage_cost:.2f}.")
print(f"The total cost is ${total_cost:.2f}.")

# PART C
# Each piece of cake is 3 inchs by 3 inches, so piece_size is 3
piece_size = 3
#The cake is square with a side length
pieces_per_row = length // piece_size
#Since the cake has equal side lengths.
total_pieces = pieces_per_row ** 2
# edges in the 4 sides, - 4
edge_pieces = (pieces_per_row * 4) - 4
edge_percentage = round((edge_pieces / total_pieces) * 100, 1)

# Printing Cake Edge Results
print("\n--- Part C: cake edges ---")
print(f"There are {edge_pieces} edge pieces on each cake.")
print(f"{edge_percentage}% of the cake is edge pieces.")

#Part D

# Each piece of cake is 3x3 inches, I am trying to find how many pieces
pieces_per_row = length // 3
total_pieces_per_cake = pieces_per_row ** 2

# I divide the total of guests by the number of pieces per cake, 
# I added 1 after to round up, since I can't use ceil()
cakes_needed_one = (guests // total_pieces_per_cake) + 1
extra_pieces_one = (cakes_needed_one * total_pieces_per_cake) - guests

# I multiply total guests by 2, so each guest gets two pieces, then round up
cakes_needed_two = ((guests * 2) // total_pieces_per_cake) + 1
extra_pieces_two = (cakes_needed_two * total_pieces_per_cake) - (guests * 2)

# Printing extra cake results
print("\n--- Part D: extra cake ---")
print(f"The caterer needs {cakes_needed_one} cake(s)")
print(f"and there will be {extra_pieces_one} extra pieces.")
print("BUT, for *two* pieces of cake per guest:")
print(f"The caterer needs {cakes_needed_two} cake(s)")
print(f"and there will be {extra_pieces_two} extra pieces.")
