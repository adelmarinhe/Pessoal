class Restaurant:
    def __init__(self, menu_items: dict, book_table: dict, customer_orders: dict):
        self.menu_items = menu_items
        self.book_table = book_table
        self.customer_orders = customer_orders

    def add_item_to_menu(self):
        item_type = str(input("Item type"))
        new_item = str(input("Item name"))
        self.menu_items[item_type].append(new_item)

    def book_tables(self):
        reservation_number = int(input())
        customer_name = str(input("Customer name"))
        customer_number = int(input("Number of customers on the table"))
        self.book_table[reservation_number] = [customer_name, customer_number]

    def customer_order(self):
        customer = str(input("Customer name"))
        self.customer_orders[customer] = []
        entry = str(input("Entry"))
        main_course = str(input("Main course"))
        dessert = str(input("Dessert"))
        if entry in self.menu_items['entry']:
            self.customer_orders[customer].append(entry)
        if main_course in self.menu_items['main course']:
            self.customer_orders[customer].append(main_course)
        if dessert in self.menu_items['dessert']:
            self.customer_orders[customer].append(dessert)

    def print_menu(self):
        print(self.menu_items)
    def print_reservations(self):
        print(self.book_table)
    def print_orders(self):
        print(self.customer_orders)

menu = {'entry': ['salad'], 'main course': ['lasagna'], 'dessert': ['pudding']}
tables = {}
orders = {}

r = Restaurant(menu,tables,orders)

r.add_item_to_menu()
r.add_item_to_menu()
r.book_tables()
r.customer_order()
r.print_menu()
r.print_reservations()
r.print_orders()