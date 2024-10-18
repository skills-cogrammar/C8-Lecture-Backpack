# ===========================
# MODELS
# ===========================

# The 'OrderStatus' class defines the possible states of an order.
# This keeps order status management cohesive, as the statuses are centralized here.
class OrderStatus:
    PENDING = "PENDING"
    PREPARING = "PREPARING"
    READY = "READY"
    COMPLETED = "COMPLETED"

# The 'PaymentStatus' class defines possible states of a payment.
# Again, keeping it cohesive by managing payment statuses here.
class PaymentStatus:
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

# The 'Product' class represents a single product in the café menu.
# This is cohesive because it focuses on one task: modeling product data.
# The class has low coupling, meaning it can easily interact with other classes without much dependency.
class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

# 'OrderItem' class represents a product and its quantity in an order.
# Cohesion is strong here because it focuses on calculating the subtotal for an item.
# It has a low coupling with other classes, only depending on the 'Product' class to calculate the price.
class OrderItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    # Calculates the total price of the current item (price * quantity).
    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

# The 'Order' class represents an entire order made by a customer.
# It has high cohesion because it focuses only on managing items within an order and calculating totals.
# It has low coupling, as it only interacts with 'OrderItem' and 'OrderStatus'.
class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items = []  # List of OrderItems
        self.status = OrderStatus.PENDING  # Initial order status
        self.total_amount = 0.0  # Total price of the order

    # Adds an item to the order and updates the total amount.
    def add_item(self, item: OrderItem):
        self.items.append(item)
        self.calculate_total()  # Recalculate the total every time an item is added

    # Calculates the total price of all items in the order.
    def calculate_total(self):
        self.total_amount = sum(item.calculate_subtotal() for item in self.items)

    # Updates the status of the order (e.g., from PENDING to PREPARING).
    def update_status(self, status: OrderStatus):
        self.status = status


# ===========================
# CONTROLLERS
# ===========================

# The 'OrderController' class acts as the "Controller" in the MVC pattern.
# It has high cohesion as it focuses on business logic, managing orders.
# This controller manages the interaction between the view and the model (Order, OrderItem, etc.).
class OrderController:
    def __init__(self):
        self.orders = {}  # Dictionary to store orders by their ID
        self.next_order_id = 1  # Auto-incrementing order ID

    # Creates a new order and stores it in the orders dictionary.
    # It returns the created order.
    def create_order(self) -> Order:
        order = Order(self.next_order_id)  # Create a new Order object
        self.orders[self.next_order_id] = order  # Store the order
        self.next_order_id += 1  # Increment the order ID for the next order
        return order

    # Adds an item to an existing order.
    # This method is cohesive, handling a specific task: adding items to orders.
    def add_item_to_order(self, order_id: int, product: Product, quantity: int):
        if order_id in self.orders:
            order = self.orders[order_id]
            item = OrderItem(product, quantity)
            order.add_item(item)  # Use the Order model to add the item
            return True  # Item added successfully
        return False  # Order not found

    # Updates the status of an existing order.
    # Again, this function is focused on a single task: updating the order's status.
    def update_order_status(self, order_id: int, status: OrderStatus):
        if order_id in self.orders:
            self.orders[order_id].update_status(status)
            return True
        return False

    # Retrieves an order by its ID.
    def get_order(self, order_id: int) -> Order:
        return self.orders.get(order_id)


# ===========================
# VIEWS (User Interface)
# ===========================

# The 'CafeView' class represents the "View" in the MVC pattern.
# It interacts with the user (e.g., displays menu, collects inputs) and calls the controller to manage business logic.
# This class has high cohesion, as it handles only the user interface-related tasks.
# It has low coupling because it communicates only with the controller, not with the model directly.
class CafeView:
    def __init__(self, controller: OrderController):
        self.controller = controller  # Reference to the controller to interact with
        # Define the product menu as a dictionary of Product objects
        self.menu = {
            1: Product(1, "Espresso", 2.50),
            2: Product(2, "Latte", 3.50),
            3: Product(3, "Cappuccino", 3.00),
            4: Product(4, "Tea", 2.00)
        }

    # Displays the product menu to the user.
    def display_menu(self):
        print("\n=== CAFÉ MENU ===")
        for id, product in self.menu.items():
            print(f"{id}. {product.name}: ${product.price:.2f}")

    # Handles the order-taking process (user input).
    # This is cohesive because it focuses on interacting with the user and delegating tasks to the controller.
    def take_order(self):
        order = self.controller.create_order()  # Create a new order via the controller
        print(f"\nNew Order Created - Order #{order.order_id}")
        
        # Loop to take items for the order
        while True:
            self.display_menu()  # Show the product menu
            choice = input("\nEnter product number (or 'done' to finish): ")

            if choice.lower() == 'done':
                break

            try:
                product_id = int(choice)
                if product_id not in self.menu:
                    print("Invalid product number!")
                    continue

                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Invalid quantity!")
                    continue

                # Add item to order via the controller
                self.controller.add_item_to_order(
                    order.order_id, 
                    self.menu[product_id], 
                    quantity
                )
                print("Item added to order!")

            except ValueError:
                print("Invalid input!")

        # After items are added, display the order summary
        self.display_order_summary(order.order_id)

    # Displays the summary of an order, including all items and total amount.
    def display_order_summary(self, order_id: int):
        order = self.controller.get_order(order_id)  # Get the order via the controller
        if order:
            print("\n=== ORDER SUMMARY ===")
            print(f"Order #{order.order_id}")
            for item in order.items:
                print(f"{item.product.name} x{item.quantity}: ${item.calculate_subtotal():.2f}")
            print(f"Total: ${order.total_amount:.2f}")
            print(f"Status: {order.status}")


# ===========================
# MAIN (Application Entry Point)
# ===========================

# The 'main' function runs the café ordering system.
# It creates instances of the controller and view, which follow the MVC architecture.
def main():
    controller = OrderController()  # Create the controller
    view = CafeView(controller)  # Pass the controller to the view
    
    while True:
        print("\n=== CAFÉ ORDER SYSTEM ===")
        print("1. New Order")
        print("2. View Order")
        print("3. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            view.take_order()  # Start the process of taking a new order
        elif choice == "2":
            order_id = int(input("Enter order number: "))
            view.display_order_summary(order_id)  # View the details of an existing order
        elif choice == "3":
            print("Thank you for using our system!")
            break
        else:
            print("Invalid choice!")

# Run the program
if __name__ == "__main__":
    main()
