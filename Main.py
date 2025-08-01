from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

def show_menu():
    def centered(msg):
        print(msg.center(60))

    centered('MENU')
    centered('a - Add item to cart')
    centered('r - Remove item from cart')
    centered('c - Change item quantity')
    centered('i - Output items\' descriptions')
    centered('o - Output shopping cart')
    centered('q - Quit')
    centered('Choose an option:')

def change_menu(item):
    options = {
        'n': f'Name: {item.item_name.title()}',
        'p': f'Name: {item.item_name.title()}',
        'q': f'Quantity: {item.item_quantity}',
        'd': f'Description: {item.item_description}',
        'f': 'Finalize Changes'
    }
    for key, value in options.items():
        print(f'{key} - {value}')

def get_user_choice():
    while True:
        try:
            user_input = input().strip().lower()

            if user_input not in ('a', 'r', 'c', 'i', 'o', 'q'):
                raise Exception
            break
        except Exception:
            print('Please enter a choice from the menu.')
    
    return user_input

def get_validated_input(prompt, condition, error_msg):
    while True:
        try:
            val = input(prompt).strip()

            if not condition(val):
                raise Exception
            return val
        except Exception:
            print(error_msg)

def main():
    shopping_cart = ShoppingCart()

    cust_name = get_validated_input('Enter name of customer:\n', lambda x: len(x) > 0, 
                                    'Please enter something.')
    shopping_cart.customer_name = cust_name

    new_date = get_validated_input('Enter today\'s date:\n', lambda x: len(x) > 0,
                                   'Please enter something.')
    shopping_cart.current_date = new_date
    
    

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 'q':
            print('Exiting...')
            break

        elif choice == 'a':
            temp_name = get_validated_input('Enter the item name:\n', lambda x: len(x) > 0,
                                            'Please enter something.').lower()
            
            temp_price = int(get_validated_input('Enter the item price:\n', lambda x: int(x) > 0,
                                             'Enter a value greater than zero.'))

            temp_quantity = int(get_validated_input('Enter the item quantity:\n', lambda x: int(x) > 0,
                                                    'Enter a value greater than zero'))

            temp_description = get_validated_input('Enter item description:\n', lambda x: len(x) > 0,
                                                   'Please enter something.')
            
            temp_item = ItemToPurchase(temp_name, temp_price, temp_quantity, temp_description)
            shopping_cart.add_item(temp_item)
            print(f'Total items in cart: {shopping_cart.get_num_items_in_cart()}')

        elif choice == 'r':
            while True:
                try:
                    temp_name = input('Enter name of item to remove:\n').strip().lower()
                    confirm_item = shopping_cart.get_item(temp_name)

                    if confirm_item is None:
                        raise Exception
                    break
                except Exception:
                    print(f'{temp_name.title()} not found in cart.')

            print('Are you sure you want to remove:')
            print(f'Name: {confirm_item.item_name.title()}')
            print(f'Price: {confirm_item.item_price}')
            print(f'Quantity: {confirm_item.item_quantity}')
            print(f'Description: {confirm_item.item_description}')

            confirm = get_validated_input('Please enter yes or no:\n', lambda x: x in ('yes', 'no'),
                                          'Please enter yes or no.').lower()
            
            if confirm == 'yes':
                shopping_cart.remove_item(temp_name)
                print(f'{temp_name.title()} has been removed.')
            else:
                print(f'Aborting removal of {temp_name.title()}')
        
        elif choice == 'c':
            while True:
                try:
                    temp_name = input('Enter name of the item to change:\n').strip().lower()
                    confirm_item = shopping_cart.get_item(temp_name)

                    if confirm_item is None:
                        raise Exception
                    break
                except Exception:
                    print(f'{temp_name.title()} not found in cart.')

            change_menu()

            change_choice = get_validated_input('Enter menu option:\n', lambda x: x in ('n', 'p', 'q', 'd', 'f'),
                                                'Please choose an item from the menu.').lower()
            
            while change_choice != 'f':
                if change_choice == 'n':
                    new_name = get_validated_input('Enter new item name:\n', lambda x: len(x) > 0,
                                                   'Please enter something.')
                    confirm_item.item_name = new_name
                    
                elif change_choice == 'p':
                    new_price = int(get_validated_input('Enter new item price:\n', lambda x: int(x) > 0,
                                                        'Please enter a number greater than zero.'))
                    confirm_item.item_price = new_price
                    
                elif change_choice == 'q':
                    new_quantity = int(get_validated_input('Enter new item quantity:\n', lambda x: int(x) > 0,
                                                           'Please enter a number greater than zero'))
                    confirm_item.item_quantity = new_quantity
                    
                elif change_choice == 'd':
                    new_description = get_validated_input('Enter new item description:\n', lambda x: len(x) > 0,
                                                          'Please enter something.')
                    confirm_item.item_description = new_description
                    
            else:
                shopping_cart.modify_item(confirm_item)
                print('Finalized changes.')

        elif choice == 'i':
            shopping_cart.print_descriptions()

        elif choice == 'o':
            shopping_cart.print_total()

if __name__ == '__main__':main()