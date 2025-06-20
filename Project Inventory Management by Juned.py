import time

file = open("inventory.txt", "r")
data = file.read() 
# Extracting the initial values from the file
frames = int(data.split()[2])
sunglasses = int(data.split()[5]) 
total = frames + sunglasses
inventory = {"frames": frames, "sunglasses": sunglasses}
cart_frame = 0
cart_sunglass = 0 
cart  = {"frame_cart": cart_frame , "sunglass_cart": cart_sunglass}

usernames = ["admin","juned", "user"]
login_ids = {"admin": "admin123", "juned":"juned123", "user": "user123"}

# This program allows the user to add frames and sunglasses to their inventory.
# It keeps track of the total number of items and displays the current count of frames and sunglasses.

def main():
    global frames , sunglasses , total , inventory , cart, usernames
    print("Welcome to the Sunglasses and Frames Inventory System!")
    while True:
        print(f"Current frames: {frames}, Current sunglasses: {sunglasses}")
        print("You can add more frames or sunglasses in inventory.")
        print("To place an order add the products into cart.")
        print("1. Add to inventory")
        print("2. Add to cart")
        print("3. Place order")
        print("4. Exit")
        choice = input("Enter your choice (1-3): ")
        print()
        if choice == '4':
            print("Exiting the program.")
            print()
            break
        elif choice == '1':
            add_to_inventory()
        elif choice == '2':
            add_to_cart()
        elif choice == "3":
            place_order()
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1)
    file = open("inventory.txt", "w")
    file.write(f"Total frames: {frames}\n")
    file.write(f"Total sunglasses: {sunglasses}\n")
    file.write(f"Total items in inventory: {total}\n")  
    #file.write(f"Inventory details: {inventory}\n")
    file.close()
    print("Inventory details saved to inventory.txt")
    file = open("inventory.txt", "r")
    print("Reading inventory details from inventory.txt:")
    print(file.read())
    file.close()
    



def add_to_inventory():
    global frames , sunglasses, total , inventory, cart , usernames
    user = input("Enter your username: ")
    password = input("Enter your password: ")
    print()
    if user in usernames and login_ids.get(user) == password:
        print(f"Current frames: {frames}, Current sunglasses: {sunglasses} in inventory.")
        print("You can add more frames or sunglasses.")
        print("What do you want to add in inventory?\n" \
        "1: Frames\n" \
        "2: Sunglasses\n"
        "3: Back")
        add_to = input("Enter your choice (1-2): ")
        print()
        if add_to == "1":
            add_frame()
            return
        elif add_to == "2":
            add_sunglass()
            return   
        elif add_to == "3":
            return    
        else: 
            print("Please enter a valid response.")

    else:
        print("Please enter a valid username and passward")




def add_frame():
    global frames , sunglasses, total , inventory, cart
    print("Adding frames to the inventory...")
    more_frames = int(input("How many frames you want to add? "))
    print()
    frames += more_frames 
    total = frames + sunglasses
    print(f"{more_frames} frames added in the inventory.")
    inventory = {"frames": frames, "sunglasses": sunglasses}
    print(f"Updated inventory: {inventory}")
    print()
    return frames 

def add_sunglass():
    global frames , sunglasses , total, inventory ,cart
    print("Adding sunglasses to the inventory...")
    more_sunglasses = int(input("How many sunglasses you want to add? "))
    print()
    sunglasses += more_sunglasses 
    total = frames + sunglasses
    print(f"{more_sunglasses} sunglasses added in the inventory.")
    inventory = {"frames": frames, "sunglasses": sunglasses}
    print(f"Updated inventory: {inventory}")
    print()
    return sunglasses


def add_to_cart():
    global frames , sunglasses , cart_frame , cart_sunglass, total, inventory,cart
    print("Select your option to add in cart: \n"
    "1: Frame\n"
    "2: Sunglass\n"
    "3: Back ")
    cart_options = input("Enter your choice (1-2): ")
    print()
    if cart_options == "1":
        frame_cart()
        add_to_cart()
        # print("Do you want to add more product into cart? ")
        # add_more = input("To add more product into cart enter 'yes")
    elif cart_options == "2":
        sunglass_cart()
        add_to_cart()
    elif cart_options == "3":
        return
    else:
        print("Please enter a valid option from the list.")
    cart = {"frame_cart": cart_frame , "sunglass_cart": cart_sunglass}
    return cart
    

def frame_cart():
    global frames , sunglasses , cart_frame , cart_sunglass ,total, inventory,cart
    frames_in_cart = int(input("enter the numbers of frames to add in cart: "))
    #frames -= frames_in_cart 
    #total = frames + sunglasses
    while frames_in_cart > frames:
        print(f"Only {frames} frames are available in inventory.")
        frames_in_cart = int(input("enter the numbers of frames to add in cart: "))
    cart_frame += frames_in_cart 
    print(f"{frames_in_cart} frames added in cart.")
    cart = {"frame_cart": cart_frame , "sunglass_cart": cart_sunglass}
    print(cart)
    #print(f"Total frames and sunglasses are: {total} amoung there are {frames} and {sunglasses}")
    inventory = {"frames": frames, "sunglasses": sunglasses}

    print()
    return cart_frame 



def sunglass_cart():
    global frames , sunglasses , cart_frame , cart_sunglass,total, inventory,cart
    sunglasses_in_cart = int(input("enter the numbers of sunglasses to add in cart: "))
    #sunglasses -= sunglasses_in_cart 
     #total = frames + sunglasses
    while sunglasses_in_cart > sunglasses:
        print(f"Only {sunglasses} sunglasses are available in inventory.")
        sunglasses_in_cart = int(input("enter the numbers of sunglasses to add in cart: "))
    cart_sunglass += sunglasses_in_cart
    print(f"{sunglasses_in_cart} sunglasses added in cart.")
    cart = {"frame_cart": cart_frame , "sunglass_cart": cart_sunglass}
    print(cart)
    #print(f"Total frames and sunglasses are: {total} amoung there are {frames} and {sunglasses}")
    inventory = {"frames": frames, "sunglasses": sunglasses}
   
    print()
    return cart_sunglass


def place_order():
    global frames , sunglasses, total ,inventory,  cart_frame , cart_sunglass, cart
    print(f"You have {cart_frame} frames and {cart_sunglass} sunglasses in your cart.")
    confirmation = input("To confirm your order enter 'Yes' to cancel enter 'No': ").strip().lower()
    print()
    if confirmation == "no":
        print("Order not placed.")
        delete_cart = input("Do you want to delete cart? ").strip().lower()
        print()
        if delete_cart == "yes":
            clear_cart()
    
        print("Taking you to homepage\n"
        "To exit enter '4' ")
        print()
        return 
    else:
        cart = {"frame_cart": cart_frame , "sunglass_cart": cart_sunglass}
        if cart_frame == 0  and cart_sunglass == 0 :
            print("Please add some products into cart first.")
            print()
        else:
            print(f"Placing order for the {cart}")
            frames -= cart_frame
            sunglasses -= cart_sunglass
            total =  frames + sunglasses
            cart_frame = 0 
            cart_sunglass = 0 
            inventory = {"frames": frames, "sunglasses": sunglasses}
            print(f"Updated inventory: {inventory}")
            print()
            return cart 


def clear_cart():
    global frames , sunglasses, total ,inventory,  cart_frame , cart_sunglass, cart
    cart_frame = 0 
    cart_sunglass = 0 
    cart = {"frame_cart": cart_frame , "sunglass_cart": cart_sunglass}
    print(cart)
    #print(f"Updated inventory: {inventory}")
    print()
    




if __name__ == "__main__":
    main()