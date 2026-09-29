# Simple Backend for My Zomato

menu = {
    "Pizza": 299,
    "Burger": 149,
    "Biryani": 199
}

def place_order(item, quantity):
    if item in menu:
        total = menu[item] * quantity
        print(f"Order placed: {quantity} x {item}")
        print(f"Total Bill: Rs {total}")
        print("Thank you for ordering from My Zomato!")
    else:
        print("Sorry, item not available")

# Test order
print("Welcome to My Zomato Backend")
print("Menu:", menu)
place_order("Pizza", 2)
