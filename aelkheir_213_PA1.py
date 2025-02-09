# PART A - Taking Inputs
print("--- Part A: inputs ---")
guests = int(input("Number of guests:"))
adults = int(input("Adult guests:"))
catering = float(input("Catering cost per guest:"))
beverage = float(input("Beverage cost per guest:"))
length = int(input("Square cake length (in inches):"))

# PART B - Cost Calculations
food_cost = guests * catering
minors = guests - adults
minor_cost = beverage * 0.35
beverage_cost = (adults * beverage) + (minors * minor_cost)
total_cost = food_cost + beverage_cost

# Printing Cost Calculation Results
print("\n--- Part B: cost ---")
print(f"The food costs ${food_cost:.2f}.")
print(f"The beverages cost ${beverage_cost:.2f}.")
print(f"The total cost is ${total_cost:.2f}.")

# PART C - Cake Edge Calculations
piece_size = 3
pieces_per_row = length // piece_size
total_pieces = pieces_per_row ** 2
edge_pieces = (pieces_per_row * 4) - 4
edge_percentage = round((edge_pieces / total_pieces) * 100, 1)

# Printing Cake Edge Results
print("\n--- Part C: cake edges ---")
print(f"There are {edge_pieces} edge pieces on each cake.")
print(f"{edge_percentage}% of the cake is edge pieces.")

# PART D - Extra Cake Calculations
pieces_per_row = length // 3
total_pieces_per_cake = pieces_per_row ** 2

# One piece per guest
cakes_needed_one = (guests // total_pieces_per_cake) + 1
extra_pieces_one = (cakes_needed_one * total_pieces_per_cake) - guests

# Two pieces per guest
cakes_needed_two = ((guests * 2) // total_pieces_per_cake) + 1
extra_pieces_two = (cakes_needed_two * total_pieces_per_cake) - (guests * 2)

# Printing Extra Cake Results
print("\n--- Part D: extra cake ---")
print(f"The caterer needs {cakes_needed_one} cake(s)")
print(f"and there will be {extra_pieces_one} extra pieces.")
print("BUT, for *two* pieces of cake per guest:")
print(f"The caterer needs {cakes_needed_two} cake(s)")
print(f"and there will be {extra_pieces_two} extra pieces.")
