cart_items = [
    {"item": "laptop", "price": 1200.00, "category": "electronics"},
    {"item": "malformed_entry", "price": -50.00, "category": "error"},
    {"item": "desk_chair", "price": 250.00, "category": "furniture"},
    {"item": "coffee_mug", "price": 15.00, "category": "kitchen"}
]

currency_choice = input("Please enter your choice of currency(usd/eur): ").lower()

if (currency_choice == "usd"):
    symbol = "$"
    price_multiplier = 1.0
    promo_code = input("Please input your promo code: ").upper()
    if (promo_code == "SAVE20"):
        discount = 20.0
    else:
        discount = 0.0    
    gross_subtotal = 0.0

    for item in cart_items:
        if (item["price"] <= 0 or item["category"] == "error"):
            print(f"Discarding corrupted row: {item}")
            continue
        else:
            adjusted_price = item["price"] * price_multiplier
            gross_subtotal += adjusted_price
    final_balance = gross_subtotal - discount      

    print("="*46)
    print(f"{'BILLING LEDGER':^46}")
    print("="*46)
    print(f"{'PRICE':<32}{f'{symbol}{gross_subtotal:,.2f}':>14}")
    print(f"{'DISCOUNT':<32}{f'{symbol}{discount:,.2f}':>14}")
    print(f"{'FINAL BALANCE':<32}{f'{symbol}{final_balance:,.2f}':>14}")
    print("="*46)
    print(f"{'COMPLETED':^46}")
    print("="*46)

elif (currency_choice == "eur"):
    symbol = "€"    
    price_multiplier = 0.92
    promo_code = input("Please input your promo code: ").upper()
    if (promo_code == "SAVE20"):
        discount = 20.0
    else:
        discount = 0.0  
    gross_subtotal = 0.0
    for item in cart_items:
        if (item["price"] <= 0) or  (item["category"] == "error"):
            print(f"Discarding corrupted row: {item}")
            continue
        else:
            adjusted_price = item["price"] * price_multiplier
            gross_subtotal += adjusted_price
    final_balance = gross_subtotal - discount   

    print("="*46)
    print(f"{'BILLING LEDGER':^46}")
    print("="*46)
    print(f"{'PRICE':<32}{f'{symbol}{gross_subtotal:,.2f}':>14}")
    print(f"{'DISCOUNT':<32}{f'{symbol}{discount:,.2f}':>14}")
    print(f"{'FINAL BALANCE':<32}{f'{symbol}{final_balance:,.2f}':>14}")
    print("="*46)
    print(f"{'COMPLETED':^46}")
    print("="*46) 





else:
    print(f"WARNING: Invalid currency")
    exit()
