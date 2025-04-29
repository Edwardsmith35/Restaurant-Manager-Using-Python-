# Menu dictionary
menu = {
    'Burger': ('Main', 10.5, 1),
    'Soup': ('Appetizer', 5.0, 2),
    'Ice cream': ('Dessert', 3.5, 2),
    'Salad': ('Appetizer', 4, 1)
}

#----------------------------------------------------
def Expand_menu(menu, dish, type ,price, quantity):
	additional_items = {
	    str(dish): (str(type), int(price), int(quantity))
	}
	# Update `menu` with `additional_items`
	menu.update(additional_items)

#----------------------------------------------------
# Function to display the menu
def Display_menu():
    print("Menu:")
    for key, value in menu.items():
        print(f"{key} | {value[0]} | Price: {value[1]}$ | Available: {value[2]}")

#----------------------------------------------------
#Function to count dishes quantity 
def count_dish_types(dictionary):
    dish_types_numbers = {}
    for key, status in dictionary.items():
        dish_types_numbers[str(key)] = str(status[2])  # Store each dish name with its count as a string

    # Print each dish and its available number
    for dish, num_available in dish_types_numbers.items():
        print(f"{dish}, Available: {num_available}")

#----------------------------------------------------
def update_price(menu, dish, new_price):


  # Update the price of 'dish'
  Current_entry = menu[str(dish)]
  Current_entry = list(Current_entry)  # Convert to list
  Current_entry[1] = int(new_price)  # Update the price
  Current_entry = tuple(Current_entry)  # Convert back to tuple
  menu[dish] = Current_entry  # Update the dictionary
  
  return menu


#----------------------------------------------------
def Update_name(menu, dish, new_name):


  # Update the name of dish
  key_list = list(menu.keys())
  Old_key = dish
  if Old_key in key_list:
    print(f"Going to update {dish}'s name")
    Current_entry = menu[str(dish)]
    Current_entry = list(Current_entry)  # Convert to list
    
    Current_entry = tuple(Current_entry)  # Convert back to tuple
    menu[new_name] = Current_entry  # Update the dictionary
    menu.pop(Old_key)
  
    return menu
  else:
    print(f"{dish} doesn't exists in the Menu")

#----------------------------------------------------

def Restock(dish , quantity):
    if dish in list(menu.keys()):
       base_quantity = menu[dish][2]
       print(f"there were {base_quantity} of {dish}")
       New_quantity = base_quantity + quantity  
       print(f"Restocked {dish} to {New_quantity}")
       Current_entry = list(menu[dish])
       Current_entry[2] = New_quantity
       menu[dish] = tuple(Current_entry)
    else:
       print("Sorry, {dish} Doesn't exist in the Menu!")

#----------------------------------------------------
# Function to process the order
def new_order(order):
    Total_price = 0
    for item in order:
        if item in menu:
            Current_entry = list(menu[item])  # Convert to list to update the quantity

            # Check if there's enough quantity before decrementing
            if Current_entry[2] > 0:
                Total_price += Current_entry[1]  # Add the price to total
                Current_entry[2] -= 1  # Decrease the quantity
                menu[item] = tuple(Current_entry)  # Update the menu
            else:
                print(f"{item} is out of stock.")
        else:
            print(f"{item} doesn't exist in the menu.")
    
    # Display the order and total price
    print(f"Your Order: {order}")
    print(f"Total Price is: {Total_price}$")


#----------------------------------------------------
# Start the process
def Start():
    first_launch = True
    start = True
    while start:
        print()  # Adds space for readability
        if not first_launch:  # Change to 'if not first_launch'
            print("Serve another customer? Yes / No")
            New_customer = input().strip()
            if New_customer.lower() == 'yes':  # Fixed logical error
                first_launch = False  # Set to False if customer wants to continue
                continue  # Go to start of the loop
            else:
                start = False  # Stop the loop if no new customer

        print("Welcome Customer! Here is the Menu: please type in your order one item at a time!\n")
        Display_menu()

        order = []
        order_more = True
        while order_more:
            print()
            order.append(input("Enter dish: ").strip())  # Asking for dish input
            print("Add additional item? Y or N")
            Answer = input().strip()
            if Answer.lower() == 'y':
                print("What do you want to add?")
                continue  # Continue to add more items
            else:
                order_more = False  # End the ordering process
                break

        new_order(order)  # Process the order
        print("\nOrder complete!")
        start = False  # End the program or allow for another customer

#----------------------------------------------------
Start()
