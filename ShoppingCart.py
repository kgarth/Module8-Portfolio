from ItemToPurchase import ItemToPurchase

class ShoppingCart():
    def __init__(self, name='none', date='January 1, 2020'):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)

    def remove_item(self, name):
        for pos, item in enumerate(self.cart_items):
            if name == item.item_name:
                self.cart_items.pop(pos)
                break
        else:
            print(f'{name} not found in cart.')

    def modify_item(self, ItemToPurchase):
        for pos, item in enumerate(self.cart_items):
            if ItemToPurchase.item_name == item.item_name:
                self.cart_items[pos] = ItemToPurchase
                break
        else:
            print(f'Item not found in cart.')

    def get_item(self, name):
        for pos, item in enumerate(self.cart_items):
            if name == item.item_name:
                return self.cart_items[pos]
        else:
            return None

    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        total_cost = 0
        
        for item in self.cart_items:
            total_cost += (item.item_price * item.item_quantity)

        return total_cost

    def print_total(self):
        print()
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'Number of Items: {self.get_num_items_in_cart()}')
        
        for item in self.cart_items:
            print(item.print_item_cost())

        print(f'Total: ${self.get_cost_of_cart()}')
        print()

    def print_descriptions(self):
        print()
        print(f'{self.customer_name}\'s Shopping Cart - {self.current_date}')
        print(f'Item Descriptions')

        for item in self.cart_items:
            print(item.print_item_description())
        print()