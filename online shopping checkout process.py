
print("------------ Online Shopping Checkout System ------------")
num_items = int(input("Enter number of items: "))                         # Input number of items
total = 0
for i in range(num_items):                                               # Loop through each item
    price = float(input(f"Enter price of item {i+1}: "))
    qty = int(input(f"Enter quantity of item {i+1}: "))
    total += price * qty
discount = 0
if total > 1000:
    discount = total * 0.1
tax = (total - discount) * 0.05
final_total = total - discount + tax
print("------------ Online Shopping Checkout System ------------")                  # Printing the total bill
print("Subtotal:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Total:", final_total)
print("Select Payment Method:")
print("1. Credit Card")
print("2. Cash on Delivery (COD)")
choice = input("Enter your choice (1 or 2): ")    
if choice == '1':
            card_number = int(input("Enter your credit card number: "))
            print("Processing Credit Card payment...")
            # In a real system, this calls a payment API.
            # Simulating a successful transaction for this block.
            payment_successful = True
            payment_status = "Success"
elif choice == '2':
            address = str(input("Enter your delivery address: "))
            print("Verifying Cash on Delivery (COD)...")
            #Simulating a successful transaction after redirection.
            payment_successful = True
            payment_status = "Success"
else:
            print("Invalid choice. Please enter '1' or '2'.") # Invalid choice handling
            payment_successful = False   
if payment_successful:
            #for the rest of Order Finalization steps
            print(f"Payment Status: {payment_status}. Proceeding to order finalization...")
            print("Order is confirmed.")
print("Thank you for shopping with us!")       # Final thank you message
print("-----------------------------------------------------------------")