# # import time
# # from tabulate import tabulate

# # localtime = time.asctime(time.localtime(time.time()))  # for local time
# # text = "WELCOME TO DATTEBAYO WELCOME SHOP"
# # dis = 990  # bringing the text to center
# # centext = "  " * dis + text
# # print(centext)
# # print(localtime)
# # print("\n")

# # print("Choose the task you want to perform by selecting its respective number:")
# # print("1. View equipment details.")
# # print("2. Rent equipment.")
# # print("3. Return equipment.")
# # print("4. Exit the program.")

# # x = int(input("Enter your choice:"))

# # if x == 1:
# #     data = [
# #         ["name", "Brand name", "price", "quantity available"],
# #         ["Velvet Table Cloth", "Saathi", "$8", "20"],
# #         ["Microphone Set", "Audio Technica", "$189", "15"],
# #         ["Disco Light Set", "Sonoff", "$322", "24"],
# #         ["7.1 Surround Sound Speaker Set", "Dolby", "$489", "4"],
# #         ["Dinner Table 8x5", "Panda Furnitures", "$344", "8"]
# #     ]

# #     table = tabulate(data, headers="firstrow", tablefmt="fancy_grid")
# #     padding = (dis - len(table.splitlines()[0])) // 2
# #     print(" " * padding + table)

# # elif x == 2:
# #         name=input("Enter your name:")
# #         eqname=int(input("Enter the corresponding number of what you want to rent:"))
# #         if eqname==1:
# #             piece1=int(input("Enter how many piece of Table cloth you want to rent:"))
# #             if piece1<21 and piece1>0:
# #                 print("daatebayo u bought it")
# #             else:
# #                 print("We are out of stock")
# #         elif eqname==2:
# #             piece2=int(input("Enter how many piece of Miicrophone set you want to rent:"))
# #             if piece2<16 and piece2>0:
# #                 print("daatebayo u bought it")
# #             else:
# #                 print("We are out of stock")

# #         elif eqname==3:
# #             piece3=int(input("Enter how many piece of Disco light set you want to rent:"))
# #             if piece3<25 and piece3>0:
# #                 print("daatebayo u bought it")
# #             else:
# #                 print("We are out of stock")
# #         elif eqname==4:
# #             piece4=int(input("Enter how many piece of 7.1 Surround Sound Speaker Set you want to rent:"))
# #             if piece4<5 and piece4>0:
# #                 print("daatebayo u bought it")
# #             else:
# #                 print("We are out of stock")
# #         elif eqname==5:
# #             piece5=int(input("Enter how many piece of Dinner Table 8x5 you want to rent:"))
# #             if piece5<9 and piece5>0:
# #                 print("daatebayo u bought it")
# #             else:
# #                 print("We are out of stock")
# #         else:
# #             print("Enter the correct number revewing the table.")

# # elif x == 3:
# #     name=input("Enter your name:")
# #     eqname=input("Enter the corresponding number of what you want to return:")
# # elif x == 4:
# #     print("THANK YOU")
# # else:
# #     print("please choose correct number givien.")







# import time
# # import Renting
# from tabulate import tabulate 

# def topic ():
#     print(time.asctime(time.localtime(time.time())))#for local time
#     text = "WELCOME TO DATTEBAYO WELCOME SHOP"
#     dis=990 #bringing the text to center
#     print("  " * dis + text)
#     print("")
# topic()

# #To choose tasks
# def task():
#     (print(""" Choose what task you want to peform by choosing its respective number.
#                     1.TO SEE THE DETAILS OF EQUPIMENT.
#                     2.TO RENT THE EQUIPMENTS.
#                     3.TO RETUEN THE EQUPMENTS.
#                     4.TO END THE PROGRAM."""))
    

# #for making a table
# def showequip():
#    f = open("read.txt")
#    data=f.readlines()
#    headers = data[0].strip().split(",")
#    table_data = [line.strip().split(",") for line in data[1:]]
#    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
   

# #for renting
# def renting():
#     name = input("Enter your name:")
#     eqname = int(input("Enter the corresponding number of what you want to rent:"))

#     equipments= {
#         1: ("Table cloth", 21),
#         2: ("Microphone set", 16),
#         3: ("Disco light set", 25),
#         4: ("7.1 Surround Sound Speaker Set", 5),
#         5: ("Dinner Table 8x5", 9)
#     }
#     while True:
#         if eqname in equipments:
#             equipmentname, limit = equipments[eqname]
#             number = int(input(f"Enter how many pieces of {equipmentname} you want to rent:"))
#             if 0 < number < limit:
#                 print("daatebayo u bought it")
#                 break
#             else:
#                 print("We are out of stock")
#         else:
#             print("Please enter the correct number by reviewing the table.")
#             break

#     # invoice= open("invoice.txt","w") 
#     # invoice.write("########Invoice of renting equipments########") + "\n"
#     # invoice.write("--------------Daatebayo renting shop------------------------")+"\n"
#     # invoice.write("Information of customer")+"\n"
#     # invoice.write(f"--------Customer name : {name}------------")+"\n"

    
    
          


# def returning():
    
#         name = input("Enter your name:")
#         eqname = int(input("Enter the corresponding number of the equipment you want to return:"))

#         # Equipment information dictionary
#         equipments = {
#             1: ("Table cloth", 21),
#             2: ("Microphone set", 16),
#             3: ("Disco light set", 25),
#             4: ("7.1 Surround Sound Speaker Set", 5),
#             5: ("Dinner Table 8x5", 9)
#         }
#         while True:
#             if eqname in equipments:
#                     equipment_name, limit = equipments[eqname]
#                     number = int(input(f"Enter how many pieces of {equipment_name} you want to return:"))

#                     if 0 < number < limit:
#                         print("daatebayo u returned it")
#                         break
#                     else:
#                         print(f"Please enter a valid quantity for {equipment_name}.")
#             else:
#                     print("Please enter the correct number by reviewing the table.")
#                     break



# while True:
#     task()
#     choice= int(input("Enter your choice:"))
#     if choice==1:
#         showequip()
#     elif choice==2:
#         renting()
#     elif choice==3:
#         returning()
#     elif choice==4:
#         print("Thank you")
#         break
#     else:
#         print("please choose correct number given.")



















# # def read_equipment_file(filename):
# #     equipment_list = []
# #     with open(filename, 'r') as file:
# #         for line in file:
# #             name, brand, price, stock = line.strip().split(', ')
# #             equipment_list.append({'name': name, 'brand': brand, 'price': float(price[1:]), 'stock': int(stock)})
# #     return equipment_list

# # def display_available_equipment(equipment_list):
# #     print("Available Equipment:")
# #     for i, equipment in enumerate(equipment_list, start=1):
# #         print(f"{i}. {equipment['name']} ({equipment['brand']}) - ${equipment['price']} (Stock: {equipment['stock']})")

# # def generate_invoice(transaction_type, equipment, customer):
# #     with open('invoices.txt', 'a') as file:
# #         file.write(f"\n{transaction_type} Invoice:")
# #         file.write(f"\nEquipment: {equipment['name']} ({equipment['brand']})")
# #         file.write(f"\nPrice per 5-day rental: ${equipment['price']}")
# #         file.write(f"\nCustomer: {customer}")
# #         file.write("\n---------------------------------\n")

# # def update_stock(equipment_list, equipment_name, quantity):
# #     for equipment in equipment_list:
# #         if equipment['name'] == equipment_name:
# #             equipment['stock'] -= quantity

# # def main():
# #     equipment_list = read_equipment_file('equipment.txt')
# #     display_available_equipment(equipment_list)

# #     while True:
# #         print("\nMenu:")
# #         print("1. Rent Equipment")
# #         print("2. Return Equipment")
# #         print("3. Exit")

# #         choice = input("Enter your choice (1/2/3): ")

# #         if choice == '1':
# #             display_available_equipment(equipment_list)
# #             selection = int(input("Enter the number corresponding to the equipment you want to rent: "))
# #             quantity = int(input("Enter the quantity you want to rent: "))
# #             equipment = equipment_list[selection - 1]

# #             if equipment['stock'] >= quantity:
# #                 customer_name = input("Enter your name: ")
# #                 total_rental_fee = quantity * equipment['price']
# #                 generate_invoice("Rental", equipment, customer_name)
# #                 update_stock(equipment_list, equipment['name'], quantity)
# #                 print(f"\n{quantity} {equipment['name']} rented to {customer_name}.")
# #                 print(f"Total Rental Fee: ${total_rental_fee}")
# #             else:
# #                 print("Insufficient stock. Please choose a lower quantity.")

# #         elif choice == '2':
# #             display_available_equipment(equipment_list)
# #             selection = int(input("Enter the number corresponding to the equipment you want to return: "))
# #             quantity = int(input("Enter the quantity you want to return: "))
# #             equipment = equipment_list[selection - 1]

# #             if equipment['stock'] + quantity <= equipment['initial_stock']:
# #                 customer_name = input("Enter your name: ")
# #                 generate_invoice("Return", equipment, customer_name)
# #                 update_stock(equipment_list, equipment['name'], -quantity)
# #                 print(f"\n{quantity} {equipment['name']} returned by {customer_name}.")
# #             else:
# #                 print("Invalid quantity. Please check the quantity you are returning.")

# #         elif choice == '3':
# #             print("Exiting the application.")
# #             break

# #         else:
# #             print("Invalid choice. Please try again.")

# # if __name__ == "__main__":
# #     main()







# # def txttodisnery():
# #     file=open("data.txt","r")
# #     dictonary={}
# #     cloth_id=1
# #     for line in file:
# #         line=line.replace("\n","")
# #         dictonary.update({cloth_id:line.split(",")})
# #         cloth_id=cloth_id+1
# #     file.close()
# #     print(dictonary[2][3])
# #     print(dictonary)

# #     return dictonary
# # txttodisnery()


   
