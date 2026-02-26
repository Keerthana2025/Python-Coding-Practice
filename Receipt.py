1. Python Exercise 1.1: The Receipt
Create a Python program that generates a formatted receipt based on user input.

Your program should:

Ask the user for the name of the item (string).
Ask for the price of the item (float).
Ask for the quantity (integer).
Calculate the subtotal (Price × Quantity).
Calculate tax (5% of the subtotal).
Print a formatted receipt showing all details and the Total Cost.
Sample Interaction:
Input
Output
Apple
1.50
10
Enter item name: Apple
Enter price: 1.50
Enter quantity: 10
--------------------
Item: Apple
Subtotal: $15.0
Tax (5%): $0.75
--------------------
TOTAL: $15.75
Python 3

CODE: 
# 1. inputs (Item name, Price, Quantity)
name = input("Enter item name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
print("----------------------------")
# 2. Calculate Subtotal
subtotal = price * quantity
# 3. Calculate Tax (5%) and Total
tax = subtotal * 0.05
total = subtotal + tax
# 4. Print the Receipt
print("Receipt")
print("Item: ", name)
print("Price: ", price)
print("Quantity: ", quantity)
print("---------------------------")
print("Subtotal: ", subtotal)
print("Tax (5%): ", tax)
print("---------------------------")
print("Total: ", total)

OUTPUT:
Enter item name: Apple
Enter price: 1.50
Enter quantity: 10
----------------------------
Receipt
Item:  Apple
Price:  1.5
Quantity:  10
---------------------------
Subtotal:  15.0
Tax (5%):  0.75
---------------------------
Total:  15.75

=== Code Execution Successful ===
