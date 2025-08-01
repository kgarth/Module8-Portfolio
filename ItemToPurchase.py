class ItemToPurchase():
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_cost(self):
        return f'{self.item_name.title()} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}'

    def print_item_description(self):
        return f'{self.item_name.title()}: {self.item_description}'