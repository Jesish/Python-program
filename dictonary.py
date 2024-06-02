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
