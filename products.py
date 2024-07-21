class Product:
    # validates the input if not correct it raises an error
    def __init__(self, name: str, price: float, quantity: int):

        if not name:
            raise ValueError("Kindly add a product name.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        # Initialising the instance variables
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    # using getter to return thr current quantity of the prodduct and setter to set a new quantity
    def get_quantity(self) -> int:
        # Returns quantity of the product
        return self.quantity

    def set_quantity(self, quantity: int):
        # Check the new number for the quantity
        if quantity < 0:
            raise ValueError("Quantity can't be negative.")
        # Set the new quantity and deactivate the product if quantity is 0
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        # Return the active status of the product
        return self.active

    def activate(self):
        # Product activation
        self.active = True

    def deactivate(self):
        # Product deactivation
        self.active = False

    def show(self) -> str:
        # Provides a string version of the product.
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        # Verify the purchasing amount.
        if quantity <= 0:
            raise ValueError("Quantity to buy should be positive.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")

        # Calculate the total price of the purchase
        total_price = quantity * self.price

        # Update the product quantity
        self.quantity -= quantity

        # Deactivate the product if quantity reaches zero
        if self.quantity == 0:
            self.deactivate()

        return total_price


# Testing
if __name__ == "__main__":
    # Create product instances
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    # Buy some products
    print(f"Total price for 50 Bose earbuds: {bose.buy(50)}")
    print(f"Total price for 100 MacBook Air M2: {mac.buy(100)}")

    # Checking if the MacBook Air M2 is active
    print(mac.is_active())

    # Show the product details
    print(bose.show())
    print(mac.show())

    # Update the quantity
    bose.set_quantity(1000)
    print(bose.show())
