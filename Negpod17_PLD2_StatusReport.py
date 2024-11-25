# Base class representing any person
class Person:
    def __init__(self, name, location, contact_info):
        self.name = name
        self.location = location
        self.contact_info = contact_info


# Farmer class inherits from Person
class Farmer(Person):
    def __init__(self, name, location, contact_info, products, price, stock):
        super().__init__(name, location, contact_info)
        self.products = products
        self.price = price
        self.stock = stock  # New attribute for product stock

    @staticmethod
    def get_farmer_info():
        # Catalog of farmers with sample data
        farmers_catalog = [
            Farmer('Peter', 'Kanombe', '0782548484', 'Apples', 200, 50),
            Farmer('John', 'Busanza', '0788888821', 'Beans', 350, "100 kg"),
            Farmer('Fred', 'Remera', '0799999934', 'Bananas', 100, 80),
            Farmer('Gisa', 'Kimironko', '0788888888', 'Maize', 400, "200 kg"),
            Farmer('Alex', 'Kanombe', '0782548484', 'Apples', 150, 93),
            Farmer('Martin', 'Gisozi', '0782548484', 'Bananas', 50,95),
            Farmer('Karinijabo', 'Kimironko', '0782548484', 'Wheat', 200, "100 kg"),
            Farmer('Yefuta', 'Remera', '0782548484', 'cucumber', 200, 59),
            Farmer('Daniella', 'Kicukiro', '0782548484', 'Millet', 240, "125 kg" ),
            Farmer('Irakoze ', 'Kabuga', '0782548484', 'Eggs', 100, 300),
            Farmer('Iyera', 'Kacyiru', '0782548484', 'Cassava', 200, 60),
            Farmer('Bizimana', 'Kibagabaga', '0782548484', 'Cabbage', 250, 70),
            Farmer('Keza', 'Nyamirambo', '0782548484', 'Tomatoes', 50, 400),
            Farmer('Sandrine', 'Gisozi', '0782548484', 'Brocolli', 300, 67),
        ]
        return farmers_catalog


def register_farmer():
    # Function to register a new farmer in the system
    print("Registration of a new farmer")
    name = input("Enter your name: ").strip()
    location = input("Enter your location: ").strip()

    # Contact Info Validation: Must be 10 digits and start with '078' or '079'
    while True:
        contact_info = input("Enter your contacts (10 digits, starting with 078 or 079): ").strip()
        if len(contact_info) == 10 and (
                contact_info.startswith('078') or contact_info.startswith('079')) and contact_info.isdigit():
            break
        else:
            print("Invalid contact info! Please enter a valid contact number (10 digits, starting with 078 or 079).")

    product = input("Enter the product you sell: ").strip()
    price = int(input("Enter the price for each unit: ").strip())
    stock = int(input("Enter the available stock quantity: ").strip())

    # Create and return new Farmer object with collected information
    new_farmer = Farmer(name, location, contact_info, product, price, stock)
    return new_farmer


def place_order(farmer_list):
    customer_name = input("Enter your name: ").strip()
    customer_info = input("Enter your contact information: ").strip()

    # Contact Info Validation for Customer: Must be 10 digits and start with 078 or 079
    while True:
        if len(customer_info) == 10 and (
                customer_info.startswith('078') or customer_info.startswith('079')) and customer_info.isdigit():
            break
        else:
            print("Invalid contact info! Please enter a valid contact number (10 digits, starting with 078 or 079).")
            customer_info = input("Enter your contact information: ").strip()

    # Check if customer wants to place an order
    options = input(f"Hello {customer_name}, would you like to place an order? (Enter 'Y' for Yes or 'N' for No): ").upper().strip()

    if options == "Y":
        while True:
            print("\nHow would you like to proceed?")
            print("1: View all farmers and their products")
            print("2: Search for a specific product")
            choice = input("Enter your choice (1 or 2): ").strip()

            if choice == '1':
                # Show the list of all farmers and their products
                print("\nAvailable farmers and their products:")
                print(f"{'ID':7} {'Name':<11} {'Location:':<13} {'Contacts':<13} {'Products':<15} {'Price (per unit or kg (FRW))':<10} {'Stock':<12}")
                print('-' * 90)
                for idx, farmer in enumerate(farmer_list):
                    print(f"{idx + 1:<7} {farmer.name:<11} {farmer.location:<13} {farmer.contact_info:<13} {farmer.products:<15} {farmer.price:<10} {farmer.stock:<12}")

                # After showing the list, give the customer the option to purchase
                purchase_option = input("\nWould you like to proceed with purchasing a product? Enter 'Y' for Yes or 'N' to return to main menu: ").upper().strip()

                if purchase_option == 'Y':
                    while True:
                        farmer_id = input("\nEnter the ID of the farmer from the list that you would like to purchase from: ").strip()
                        if farmer_id.isdigit() and 1 <= int(farmer_id) <= len(farmer_list):
                            selected_farmer = farmer_list[int(farmer_id) - 1]


                            print(f"\nFarmer Selected: {selected_farmer.name}")
                            print(f"Product: {selected_farmer.products}")
                            print(f"Price per unit: {selected_farmer.price} FRW")
                            print(f"Available Stock: {selected_farmer.stock}")
                            print(f"Contact: {selected_farmer.contact_info}")

                            while True:
                                quantity = input("\nEnter the number of units you would like to purchase (or '0' to cancel): ").strip()
                                if quantity.isdigit():
                                    quantity = int(quantity)
                                    if quantity == 0:
                                        print("\nReturning to the main menu.")
                                        break
                                    if quantity <= selected_farmer.stock:
                                        total_cost = selected_farmer.price * quantity
                                        print(f"\nOrder Summary:")
                                        print(f"Farmer: {selected_farmer.name}")
                                        print(f"Product: {selected_farmer.products}")
                                        print(f"Price per unit: {selected_farmer.price} FRW")
                                        print(f"Quantity: {quantity}")
                                        print(f"Total Cost: {total_cost} FRW")
                                        print(f"Contact: {selected_farmer.contact_info}")

                                        confirm = input( "\nDo you confirm this purchase? Enter 'Y' for Yes or 'N' to cancel: ").upper().strip()
                                        if confirm == 'Y':
                                            selected_farmer.stock -= quantity
                                            print(
                                                f"\nThank you for your purchase, {customer_name}! Your order has been placed.")
                                            return
                                        else:
                                            print("\nOrder canceled. Returning to the main menu.")
                                            break
                                    else:
                                        print("\nInsufficient stock. Please enter a lower quantity.")
                                else:
                                    print("Invalid input! Please enter a valid quantity.")
                        else:
                            print("Invalid farmer ID! Returning to the main menu.")
                            break
                    continue

            elif choice == '2':
                while True:
                    product_name = input("\nEnter the product you want to search for: ").strip().lower()
                    matching_farmers = [farmer for farmer in farmer_list if product_name in farmer.products.lower()]

                    if matching_farmers:
                        print("\nFarmers offering the product:")
                        print(
                            f"{'ID':7} {'Name':<11} {'Location:':<13} {'Contacts':<13} {'Products':<15} {'Price (FRW)':<10} {'Stock':<10}")
                        print('-' * 90)
                        for idx, farmer in enumerate(matching_farmers):
                            print(
                                f"{idx + 1:<7} {farmer.name:<11} {farmer.location:<13} {farmer.contact_info:<13} {farmer.products:<15} {farmer.price:<10} {farmer.stock:<10}")

                        # After showing the search result, give the customer the option to purchase
                        purchase_option = input(
                            "\nWould you like to proceed with purchasing a product? Enter 'Y' for Yes or 'N' to return to main menu: ").upper().strip()

                        if purchase_option == 'Y':
                            while True:
                                farmer_id = input(
                                    "\nEnter the ID of the farmer from the list that you would like to purchase from: ").strip()
                                if farmer_id.isdigit() and 1 <= int(farmer_id) <= len(matching_farmers):
                                    selected_farmer = matching_farmers[int(farmer_id) - 1]

                                    print(f"\nFarmer Selected: {selected_farmer.name}")
                                    print(f"Product: {selected_farmer.products}")
                                    print(f"Price per unit: {selected_farmer.price} FRW")
                                    print(f"Available Stock: {selected_farmer.stock}")
                                    print(f"Contact: {selected_farmer.contact_info}")

                                    while True:
                                        quantity = input(
                                            "\nEnter the number of units you would like to purchase (or '0' to cancel): ").strip()
                                        if quantity.isdigit():
                                            quantity = int(quantity)
                                            if quantity == 0:
                                                print("\nReturning to the main menu.")
                                                break
                                            if quantity <= selected_farmer.stock:
                                                total_cost = selected_farmer.price * quantity
                                                print(f"\nOrder Summary:")
                                                print(f"Farmer: {selected_farmer.name}")
                                                print(f"Product: {selected_farmer.products}")
                                                print(f"Price per unit: {selected_farmer.price} FRW")
                                                print(f"Quantity: {quantity}")
                                                print(f"Total Cost: {total_cost} FRW")
                                                print(f"Contact: {selected_farmer.contact_info}")

                                                confirm = input(
                                                    "\nDo you confirm this purchase? Enter 'Y' for Yes or 'N' to cancel: ").upper().strip()
                                                if confirm == 'Y':
                                                    selected_farmer.stock -= quantity

                                                    print(
                                                        f"\nThank you for your purchase, {customer_name}! Your order has been placed.")
                                                    return
                                                else:
                                                    print("\nOrder canceled. Returning to the main menu.")
                                                    break
                                            else:
                                                print("\nInsufficient stock. Please enter a lower quantity.")
                                        else:
                                            print("Invalid input! Please enter a valid quantity.")
                                else:
                                    print("Invalid farmer ID! Returning to the main menu.")
                                    break
                            continue
                    else:
                        print("\nNo farmers currently offer that product.")
                        retry = input("\nWould you like to (1) Search again, (2) View all farmers, or (3) Exit to main menu? Enter your choice: ").strip()
                        if retry == '1':
                            continue
                        elif retry == '2':
                            print("\nAvailable farmers and their products:")
                            print(
                                f"{'ID':7} {'Name':<11} {'Location:':<13} {'Contacts':<13} {'Products':<15} {'Price (FRW)':<10} {'Stock':<10}")
                            print('-' * 90)
                            for idx, farmer in enumerate(farmer_list):
                                print(
                                    f"{idx + 1:<7} {farmer.name:<11} {farmer.location:<13} {farmer.contact_info:<13} {farmer.products:<15} {farmer.price:<10} {farmer.stock:<10}")
                            break
                        elif retry == '3':
                            return
                        else:
                            print("Invalid choice! Returning to main menu.")
                            return

                break

            else:
                print("Invalid choice! Please try again.")
                continue

    elif options == "N":
        print("Returning to main menu.")
    else:
        print("Invalid input! Returning to main menu.")


def main():
    farmer_list = Farmer.get_farmer_info()

    while True:
        print("WELCOME TO FARMER-TO-TABLE"),print("-"*25)
        print("1: Registering a new farmer")
        print("2: Place an order from a local farmer near you")
        print("3: Exit")
        choice = input("Enter your Choice from (1-3): ").strip()

        if choice == '1':
            new_farmer = register_farmer()
            farmer_list.append(new_farmer)
            print("\nYou have registered successfully!\n")

        elif choice == '2':
            place_order(farmer_list)

        elif choice == '3':
            print("Exiting the program")
            break

        else:
            print('You entered the wrong option, try again.')
            print()


if __name__ == "__main__":
    main()
