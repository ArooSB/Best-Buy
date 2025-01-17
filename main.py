from typing import List, Tuple
import products
import store


def display_menu():
    print("\nWelcome to Best Buy!")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store: store.Store):
    products = store.get_all_products()
    if not products:
        print("No products available at the moment.")
    else:
        for product in products:
            print(product.show())


def show_total_amount(store: store.Store):
    total_quantity = store.get_total_quantity()
    print(f"Total amount of all products in store: {total_quantity}")


def make_order(store: store.Store):
    products = store.get_all_products()
    if not products:
        print("No products available to order.")
        return

    print("Available products:")
    for idx, product in enumerate(products):
        print(f"{idx + 1}. {product.show()}")

    shopping_list = []
    while True:
        product_idx = int(input("Enter the product number to buy (0 to finish): ")) - 1
        if product_idx == -1:
            break
        if 0 <= product_idx < len(products):
            quantity = int(input(f"Enter quantity for {products[product_idx].name}: "))
            shopping_list.append((products[product_idx], quantity))
        else:
            print("Invalid product number.")

    if shopping_list:
        total_price = store.order(shopping_list)
        print(f"Total price of the order: {total_price} dollars.")


def start(store: store.Store):
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_amount(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
]

best_buy = store.Store(product_list)

if __name__ == "__main__":
    start(best_buy)
