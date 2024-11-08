class Person:
    def __int__(self, name, location, contact_info):
        self.name=name
        self.location=location
        self.contact_info=contact_info


class Farmer(Person):
    def __init__(self, name, location, contact_info, products, price):
        super().__int__(name, location, contact_info)
        self.products=products
        self.price=price

    @staticmethod
    def get_farmer_info():
        farmers_catalog= [
            Farmer('Peter','Kanombe','0782548484','Apples and Mangoes',"200 Frw"),
            Farmer('John', 'Busanza', '0788888821','Beans ','350FRW per KG'),
            Farmer('Fred','Remera', '0799999934', 'Banana','100FRW'),
            Farmer('Gisa', 'Kimironko', '0788888888', 'Maize','400 FRW per KG')

        ]
        return farmers_catalog
def register_farmer():
       print("Registration of a new farmer")
       name=input("Enter your name").strip()
       location=input("Enter your location").strip()
       contact_info=input("Enter your contacts").strip()
       product=input("Enter the product your sell ").strip()
       price=input("Enter the price for each unit").strip()

       new_farmer= Farmer(name,location,contact_info,product,price)
       return new_farmer
def main():
    farmer_list= Farmer.get_farmer_info()

    while True:
        print("1: Registering a new farmer")
        print("2:Watch farmers and their products")
        print("3:Exit")
        choice = input("Enter you Choice from (1-3):").strip()

        if choice == '1':
            new_farmer=register_farmer()
            farmer_list.append(new_farmer)
            print("\n You have registered successfully!!\n")

        elif choice == '2':

            print(f"{'Name':<11} {'Location:':<13} {'Contacts':<13} {'Products':<15} {'Price (Per unit or KG)':<14}")
            print('-' * 67)
            for farmer in farmer_list:
                print(f"{farmer.name:<11} {farmer.location:<13} {farmer.contact_info:<13} {farmer.products:<15} {farmer.price:<14}")

        elif choice == '3':
            print("Exiting the program")
            break

        else:
          print('You entered the wrong option try again')
          print()

if __name__ == "__main__":
     main()