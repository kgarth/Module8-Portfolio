from re import L
from ItemToPurchase import ItemToPurchase
from ShoppingCart import ShoppingCart

def show_menu():
    print('{:^60}'.format(f'MENU'))
    print('{:^60}'.format(f'a - Add item to cart'))
    print('{:^60}'.format(f'r - Remove item from cart'))
    print('{:^60}'.format(f'c - Change item quantity'))
    print('{:^60}'.format(f'i - Output items\' descriptions'))
    print('{:^60}'.format(f'o - Output shopping cart'))
    print('{:^60}'.format(f'q - Quit'))
    print('{:^60}'.format(f'Choose an option:'))

def change_menu():
    print(f'n - Name: {confirm_item.item_name.title()}')
    print(f'p - Price: {confirm_item.item_price}')
    print(f'q - Quantity: {confirm_item.item_quantity}')
    print(f'd - Description: {confirm_item.item_quantity}')
    print(f'f - Finalize Changes')

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

def main():
    shopping_cart = ShoppingCart()

    while True:
        try:
            cust_name = input('Enter name of customer:\n').strip()

            if len(cust_name) == 0:
                raise Exception
            shopping_cart.customer_name = cust_name
            break
        except Exception:
            print('Please enter something.')

    while True:
        try:
            new_date = input('Enter today\'s date:\n').strip()

            if len(new_date) == 0:
                raise Exception
            shopping_cart.current_date = new_date
            break
        except Exception:
            print('Please enter a date.')
    
    show_menu()
    choice = get_user_choice()

    while choice != 'q':
        if choice == 'a':
            while True:
                try:
                    temp_name = input('Enter the item name:\n').strip().lower()

                    if len(temp_name) == 0:
                        raise Exception
                    break
                except Exception:
                    print('Please enter something.')

            while True:
                try:
                    temp_price = int(input('Enter the item price:\n'))

                    if temp_price <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print('Enter a value greater than zero.')

            while True:
                try:
                    temp_quantity = int(input('Enter the item quantity:\n'))

                    if temp_quantity <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print('Enter a value greater than zero.')

            while True:
                try:
                    temp_description = input('Enter item description:\n').strip()

                    if len(temp_description) == 0:
                        raise Exception
                    break
                except Exception:
                    print('Please enter something.')

            temp_item = ItemToPurchase(temp_name, temp_price, temp_quantity, temp_description)
            shopping_cart.add_item(temp_item)
            print(f'Total items in cart: {shopping_cart.get_num_items_in_cart()}')

        elif choice == 'r':
            while True:
                try:
                    temp_name = input('Enter name of item to remove:\n').strip().lower()
                    confirm_item = shopping_cart.get_item(temp_name)

                    if confirm_item == -1:
                        raise Exception
                    break
                except Exception:
                    print(f'{temp_name.title()} not found in cart.')

            print('Are you sure you want to remove:')
            print(f'Name: {confirm_item.item_name.title()}')
            print(f'Price: {confirm_item.item_price}')
            print(f'Quantity: {confirm_item.item_quantity}')
            print(f'Description: {confirm_item.item_description}')

            while True:
                try:
                    confirm = input('Please enter yes or no:\n').strip().lower()

                    if confirm not in ('yes', 'no'):
                        raise Exception
                    break
                except Exception:
                    print('Please enter yes or no.')

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

                    if confirm_item == -1:
                        raise Exception
                    break
                except Exception:
                    print(f'{temp_name.title()} not found in cart.')

            change_menu()

            while True:
                try:
                    change_choice = input('Enter menu option:\n').strip().lower()

                    if change_choice not in ('n', 'p', 'q', 'd', 'f'):
                        raise Exception
                    break
                except Exception:
                    print('Please choose an item from the menu.')

            while change_choice != 'f':
                if change_choice == 'n':
                    while True:
                        try:
                            new_name = input('Enter new item name:\n')

                            if len(new_name) == 0:
                                raise Exception
                            confirm_item.item_name = new_name
                            break
                        except Exception:
                            print('Please enter something.')

                elif change_choice == 'p':
                    while True:
                        try:
                            new_price = int(input('Enter new item price:\n'))

                            if new_price <= 0:
                                raise ValueError
                            confirm_item.item_price = new_price
                            break
                        except ValueError:
                            print('Please enter a number greater than zero.')

                elif change_choice == 'q':
                    while True:
                        try:
                            new_quantity = int(input('Enter new item quantity:\n'))

                            if new_quantity <= 0:
                                raise ValueError
                            confirm_item.item_quantity = new_quantity
                            break
                        except ValueError:
                            print('Please enter a number greater than zero')

                elif change_choice == 'd':
                    while True:
                        try:
                            new_description = input('Enter new item description:\n')

                            if len(new_description) == 0:
                                raise Exception
                            confirm_item.item_description = new_description
                            break
                        except Exception:
                            print('Please enter something.')
            else:
                shopping_cart.modify_item(confirm_item)
                print('Finalized changes.')

        elif choice == 'i':
            shopping_cart.print_descriptions()

        elif choice == 'o':
            shopping_cart.print_total()

        show_menu()
        choice = get_user_choice()

if __name__ == '__main__':main()