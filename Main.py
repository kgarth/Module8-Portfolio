from ItemToPurchase import ItemToPurchase

def create_items(qty):
    item_list = []

    for i in range(qty):
        print(f'Item {i + 1}')
        while True:
            try:
                temp_name = input('Enter the item name:\n')

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
                print('Please enter a value greater than zero.')

        while True:
            try:
                temp_qty = int(input('Enter the item quantity:\n'))

                if temp_qty <= 0:
                    raise ValueError
                break
            except ValueError:
                print('Please enter a value greater than zero.')

        item_list.append(ItemToPurchase(temp_name, temp_price, temp_qty))

    return item_list

def main():
    item_list = create_items(2)
    total_cost = 0

    print('{:^30}'.format('TOTAL COST'))

    for item in item_list:
        total_cost += (item.item_price * item.item_quantity)
        print('{:^30}'.format(item.print_item_cost()))

    print('{:^30}'.format(f'Total: ${total_cost}'))

if __name__ == '__main__':main()