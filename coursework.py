import datetime
import time
from tabulate import tabulate

# from dictonary import Dictionary 
# from dictonary import Dictionary


def topic():
    print(time.asctime(time.localtime(time.time())))
    text = "WELCOME TO DATTEBAYO WELCOME SHOP"
    dis = 990 #bringing the text to center
    print("  " * dis + text)
    print("")

def Dictionary():
    file = open("read.txt", "r")
    dictionary = {}
    
    for line in file:
        line = line.strip()  # Remove leading and trailing whitespaces
        if line:
            parts = line.split(",")
            equipment_id = int(parts[0])
            name = parts[1]
            brand = parts[2]
            price = float(parts[3].replace("$", ""))
            quantity_available = int(parts[4])
            equipment_info = {
                "Name": name,
                "Brand": brand,
                "Price": price,
                "Quantity Available": quantity_available
            }
            dictionary[equipment_id] = equipment_info
    
    file.close()
    return dictionary

  

def task():
    print(""" Choose what task you want to perform by choosing its respective number.
    1. TO SEE THE DETAILS OF EQUIPMENT.
    2. TO RENT THE EQUIPMENT.
    3. TO RETURN THE EQUIPMENT.
    4. TO END THE PROGRAM.""")

def showequip():
    
        f = open("read.txt")
        data = f.readlines()
        f.close()
        headers = data[0].strip().split(",")
        table_data = [line.strip().split(",") for line in data[1:]]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
   

def renting():
    showequip()
    name = input("Enter your name: ")
   
    eqname = int(input("Enter the corresponding number of what you want to rent: "))
    equipments = []
    with open("read.txt", "r") as file:
        for line in file:
            name, brand, price, quantity = line.strip().split(", ")
            equipment = {
                "name": name,
                "brand": brand,
                "price": price,
                "quantity": int(quantity),
            }
            equipments.append(equipment)
    
    
    if eqname in equipments:
            equipmentname, limit = equipments[eqname]
            number = int(input(f"Enter how many pieces of {equipmentname} you want to rent: "))
            
            if 0 < number <= limit:  
                rentaldate=datetime.datetime.now()
                while True:
                    try:
                        rentdays= int(input(f"Enter the rental duration in days for {equipmentname}. "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")

                rentfor5 = rentdays // 5
                if rentdays% 5 != 0:
                    rentfor5 +=1
                    return rentfor5

                
                pricee = float(equipment_info.replace("$", ""))
                totalRentPrice = pricee * rentfor5
                print("Total Price:", totalRentPrice)
                invoice= f'''==== invoice of renting === 
                        customername:{name}

                '''

                filename = f" invoice.txt"
                with open (filename,"w") as filevariable:
                        filevariable.write(invoice)
                        print(filevariable)
                    
                print("dattebayo u rented it")


            else:
                print("Sorry, we are out of stock.")
            
            
           
    else:
            print("Please enter the correct number by reviewing the table.")

    
        
       
        
    
def returning():
    name = input("Enter your name: ")
    try:
        eqname = int(input("Enter the corresponding number of the equipment you want to return: "))
        equipments = {
            1: ("Table cloth", 20),
            2: ("Microphone set", 15),
            3: ("Disco light set", 24),
            4: ("7.1 Surround Sound Speaker Set", 4),
            5: ("Dinner Table 8x5", 8)
        }
        if eqname in equipments:
            equipment_name, limit = equipments[eqname]
            number = int(input(f"Enter how many pieces of {equipment_name} you want to return: "))
            if 0 < number <= limit:
                print("Daatebayo, you returned it.")
              

            else:
                print(f"Please enter a valid quantity for {equipment_name}.")
        else:
            print("Please enter the correct number by reviewing the table.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    topic()
    task()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            showequip()
        elif choice == 2:
            renting()
        elif choice == 3:
            returning()
        elif choice == 4:
            print("Thank you for using Dattebayo Welcome Shop!")
            break
        else:
            print("Please choose a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")