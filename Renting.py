# import datetime
# import random
# # import display

# # Getting the current date and time
# dateAndTime = datetime.datetime.now()
# presentDateAndTime = dateAndTime.strftime("%m/%d/%Y")

# def showingEquipments(equipments):
#     print(equipments)
#     with open("equipment_data.txt", "q") as e:
#         for product_id, information in equipments.items():
#             if information['Quantity'] > 0:
#                 e.write = (
#                     f"{information['Product Name']}, {information['Brand']}, {information['Price']}, {information['Quantity']}\n")

# def forCustomer():
#     global customerName
#     global isInitiated
#     isInitiated = True
#     print("\n|---------Enter some information of customer for generating receipt.---------")
    
#     while isInitiated:
#         customerName = input("Enter the Customer Name:").strip()

#         if customerName == "":
#             print("\n||||||||   Please provide the name of the customer   ||||||||\n")
#             isInitiated = True
#         elif customerName.isalpha():
#             renting = random.randint(1, 500)
#             with open(customerName+"_   Rent_Receipt.txt", "w") as cFile:
#                 cFile.write("""
# <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Luna Ivy Shop ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>
# <~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Rent Receipt ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>""")
#                 cFile.write(f"Rent No: {renting}\t\t\t\t\t\t\t\t\t\t Date: {presentDateAndTime}\n")
#                 cFile.write(f"\t\t\t\t\t\t\tCustomer Name: {customerName}\n\n")
#                 cFile.write(
#                     "\t__________________________________________________________________________________________\n\t")
#                 cFile.write("{:<18} {:<15} {:<15} {:<15}{:}".format("Product Name",
#                                                                            "Brand", "Price", "Quantity", "Total"))
#                 cFile.write(
#                     "\n\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\t")
#                 break
#         else:
#             print(
#                 "\n||||||||||  Please, Input Proper String Name Without Space  |||||||||||\n")
#             isInitiated = True
#     return isInitiated

# def renting_equipments(isInitiated):
#     nev = display.equipments_x()
#     display.prod_tables(nev)

#     print("\n")
#     global totalAmount
#     totalAmount = 0
#     global rented 
#     rented = False



#     while isInitiated:
#         isInitiated = True
#         try:
#             print("\n\t~~~~~~~~~~~~~Type a Product ID of Equipment you want to rent.~~~~~~~~~~~~~")
#             product_id = int(input(" = "))
#             if product_id in nev.keys():
#                 quan = int(input("\n\t~~~~~~~~~~~~~Enter the quantity of equipment to rent~~~~~~~~~~~~~\n = "))
#                 if quan <= 0:
#                     print("\n|||||||| Please enter a valid value in quantity. |||||||")
#                 elif quan <= nev[product_id]["Quantity"]:
#                     price = int(nev[product_id]["Price"].replace("$", ""))
#                     totalAmount += price * quan

#                     with open(f"{customerName}_Rent_Receipt.txt", "a+") as cn:
#                         cn.write("{:<18} {:<15} {:<15} {:<15}{:}".format(nev[product_id]["Product Name"],
#                                                                          nev[product_id]["Brand"],
#                                                                          nev[product_id]["Price"], quan,
#                                                                          price * quan))
#                         cn.write("\n\t")
#                     nev[product_id]["Quantity"] -= quan
#                 else:
#                     print("\n|||||||| Insufficient quantity of equipment ||||||||\n")
#             else:
#                 print("\n||||||||  Product ID not found / Look Product ID carefully!||||||||\n")
#                 isInitiated = True

#             lease = True
#             while lease:
#                 print("\n\tWould you like to rent any other products? (y - yes / n - No)?")
#                 mb = input("=")
#                 if mb.lower() == "no":
#                     isInitiated = False
#                     lease = False
#                 elif mb.lower() == "yes":
#                     lease = False
#                 else:
#                     print("\n||||||| Choose the option you want: yes or no? |||||||\n")
#         except ValueError:
#             print("\n|||||||| Please, provide valid input. ||||||||\n")
#             isInitiated = True

#     # Update the equipment data file after rentals
#     display.showingEquipments(nev)
    
#     Alltogether(totalAmount)

# def Alltogether(grandPrice):
#     print("""
#              ____________________________________________________
#              |            How would you like to rent?             |
#              |____________________________________________________|
#              |              i. Physical                           |
#              |              ii. Online                            |
#              |____________________________________________________| """)

#     while True:
#         try:
#             choice = int(input("= "))
#             if choice == 2:
#                 c_price = grandPrice + 500
#                 with open(f"{customerName}_Rent_receipt.txt", "a+") as cn:
#                     cn.write(
#                         """\n\t________________________________________________________________\n""")
#                     cn.write(
#                         "                   Total Price: $" + str(grandPrice) + "\n")
#                     cn.write(
#                         "                   Shipping Charge: $500\n")
#                     cn.write(
#                         "                   Total with Shipping charge: $" + str(c_price))
#                     cn.write(
#                         """\n\t----------------------------------------------------------------\n""")

#                     cn.write(
#                         """\n\t------------------------------  THANK YOU !  ------------------------------\n""")
#                 print("<<    Successfully rented.   >>")
#                 return
#             elif choice == 1:
#                 with open(f"{customerName}_Rent_Receipt.txt", "a+") as cn:
#                     cn.write(
#                         """\n\t________________________________________________________________\n""")
#                     cn.write(
#                         "                   Total Price: $" + str(grandPrice) + "\n")
#                     cn.write(
#                         """\n\t----------------------------------------------------------------\n""")
#                 print("<<    Successfully rented.   >>")
#                 return
#             else:
#                 print("\n\t---------- Please, choose a given option 1 or 2 ----------\n")
#         except:
#             print("\n|||||||| Please, Enter a valid integer option ||||||||\n")
#         grandPrice = 0