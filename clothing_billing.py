products = {
    'Shirts' : 500,
    'T-shirts' :500,
    'Jeans' : 1200,
    'Jackets':1200,
    'Trousers':1000
}

cart = []

def add_item():
    print('------------List of the Products---------')
    for item,price in products.items():
        print(f'{item} : {price}')

    item_name = input('Enter the item name:  ').title()
    if item_name not in products:
        print('Item not available')

    while True:
        try:
            quantity = int(input("Enter the no of quantity:  "))
            if quantity < 1:
                print('Quantity must be 1')
                continue
            break
        except ValueError:
            print('Quantity must be in digits')

    cart.append((item_name,quantity,products[item_name]))
    print(f'{item_name} x {quantity} ,added to the cart' )

def view_cart():
    if not cart:
        print('No item in the cart.')
        return
    print('Your cart:')
    total = 0
    for item, qty, price in cart:
        subTotal = qty * price
        total+= subTotal
        print(f'{item} x {qty} = {subTotal}')
        print(f'Toatl amount to pay : {total}')



while True:
    print('Clothing Store Billing')
    print('1. Add items')
    print('2. View Cart ')
    print('3. Exit')

    choice = input('Enter your choice:')
    if choice == '1':
        add_item()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        print(" Exiting. Thank you!")
        break
    else:
        print("❌ Invalid option.")

       

    

