from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

# Method to output the menu
def show_menu():  
    print('MENU')
    options = {
        'a': 'Add item to cart',
        'r': 'Remove item from cart',
        'c': 'Change item quantity',
        'i': 'Output items\' description',
        'o': 'Output shopping cart',
        'q': 'Quit'
    }
    for key, value in options.items():
        print(f'{key} - {value}')
    print()

# Method to output the change menu taking in a ItemToPurchase object
def change_menu(item):
    options = {
        'n': f'Name: {item.item_name.title()}',
        'p': f'Price: {item.item_price}',
        'q': f'Quantity: {item.item_quantity}',
        'd': f'Description: {item.item_description}',
        'f': 'Finalize Changes'
    }
    for key, value in options.items():
        print(f'{key} - {value}')
    print()

# Method to capture and validate input taking the prompt as a string, condition as a lambda expression
# and error_msg as a string and returning the captured value
def get_validated_input(prompt, condition, error_msg):
    while True:
        try:
            val = input(prompt).strip()

            if not condition(val):
                raise Exception
            return val
        except Exception:
            print(error_msg)

# Main code block
def main():
    shopping_cart = ShoppingCart() # Creates main ShoppingCart object

    # Capture, validate and store input
    cust_name = get_validated_input('Enter name of customer:\n', lambda x: len(x) > 0, 
                                    'Please enter something.')
    shopping_cart.customer_name = cust_name
    print() # Spacing

    new_date = get_validated_input('Enter today\'s date:\n', lambda x: len(x) > 0,
                                   'Please enter something.')
    shopping_cart.current_date = new_date
    print() 

    while True: # Main outer loop
        show_menu()
        
        # Capture and validate input
        choice = get_validated_input('Choose an option:\n', lambda x: x in ('a', 'r', 'c', 'i', 'o', 'q'),
                                     'Please enter a choice from the menu.').lower()

        if choice == 'q': # Using choice 'q' to exit menu.
            print('Exiting...')
            break

        elif choice == 'a': # Using choice 'a' for adding an item
            print()
            temp_name = get_validated_input('Enter the item name:\n', lambda x: len(x) > 0,
                                            'Please enter something.').lower()
            
            temp_price = int(get_validated_input('Enter the item price:\n', lambda x: int(x) > 0,
                                             'Enter a value greater than zero.'))

            temp_quantity = int(get_validated_input('Enter the item quantity:\n', lambda x: int(x) > 0,
                                                    'Enter a value greater than zero'))

            temp_description = get_validated_input('Enter item description:\n', lambda x: len(x) > 0,
                                                   'Please enter something.')
            
            # Creates an ItemToPurchase object from collected information from user
            temp_item = ItemToPurchase(temp_name, temp_price, temp_quantity, temp_description)
            # Stores new object into the ShoppingCart object
            shopping_cart.add_item(temp_item)
            print()
            print(f'Total items in cart: {shopping_cart.get_num_items_in_cart()}')
            print()

        elif choice == 'r': # Using choice 'r' for removing an item
            print()
            # Inner loop to capture input and collect item with name and if returned 'None' from
            # get_item() ShoppingCart method will raise an exception
            while True: 
                try:
                    temp_name = input('Enter name of item to remove:\n').strip().lower()
                    confirm_item = shopping_cart.get_item(temp_name)

                    if confirm_item is None:
                        raise Exception
                    break
                except Exception:
                    print(f'{temp_name.title()} not found in cart.')

            # Confirmation of deletion messaging
            print()
            print('Are you sure you want to remove:')
            print(f'Name: {confirm_item.item_name.title()}')
            print(f'Price: {confirm_item.item_price}')
            print(f'Quantity: {confirm_item.item_quantity}')
            print(f'Description: {confirm_item.item_description}')
            print()

            confirm = get_validated_input('Please enter yes or no:\n', lambda x: x in ('yes', 'no'),
                                          'Please enter a proper response.').lower()
            
            # 'yes' to remove, 'no' to cancel
            if confirm == 'yes': 
                shopping_cart.remove_item(temp_name)
                print(f'{temp_name.title()} has been removed.')
            else:
                print(f'Aborting removal of {temp_name.title()}')
        
        elif choice == 'c': # Using choice 'c' to modify an item.
            print()
            while True:
                try:
                    temp_name = input('Enter name of the item to change:\n').strip().lower()
                    confirm_item = shopping_cart.get_item(temp_name)

                    if confirm_item is None:
                        raise Exception
                    break
                except Exception:
                    print(f'{temp_name.title()} not found in cart.')

            # Inner loop to capture all changes made to item choice 'f' will finalize changes to shopping cart
            while True:
                print()
                change_menu(confirm_item)

                change_choice = get_validated_input('Enter menu option:\n', lambda x: x in ('n', 'p', 'q', 'd', 'f'),
                                                'Please choose an item from the menu.').lower()
                
                if change_choice == 'f':
                    shopping_cart.modify_item(confirm_item)
                    print('Finalized changes.')
                    print()
                    break

                elif change_choice == 'n': # Change Name
                    new_name = get_validated_input('Enter new item name:\n', lambda x: len(x) > 0,
                                                   'Please enter something.')
                    confirm_item.item_name = new_name
                    
                elif change_choice == 'p': # Change price
                    new_price = int(get_validated_input('Enter new item price:\n', lambda x: int(x) > 0,
                                                        'Please enter a number greater than zero.'))
                    confirm_item.item_price = new_price
                    
                elif change_choice == 'q': # Change quantity
                    new_quantity = int(get_validated_input('Enter new item quantity:\n', lambda x: int(x) > 0,
                                                           'Please enter a number greater than zero'))
                    confirm_item.item_quantity = new_quantity
                    
                elif change_choice == 'd': # Change description
                    new_description = get_validated_input('Enter new item description:\n', lambda x: len(x) > 0,
                                                          'Please enter something.')
                    confirm_item.item_description = new_description
                    
        elif choice == 'i': # Using choice 'i' to output description of items in cart
            shopping_cart.print_descriptions()

        elif choice == 'o': # Using choice 'o' to output the shopping cart total
            shopping_cart.print_total()

if __name__ == '__main__':main()