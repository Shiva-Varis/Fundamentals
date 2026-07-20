blacklisted_skus = ("defective_battery", "expired_sensor")
current_inventory = {
    "wireless_mouse": 140,
    "hdmi_cable": 310,
    "mechanical_keyboard": 45
}
incoming_product = input("List of incoming product shipments: ").strip().lower().split(",")
unique_shipment_batch = set(incoming_product)

for i in unique_shipment_batch:
    if (i in blacklisted_skus):
        print(f"CONTRABAND DETECTED: Seizing {i}")
        continue
    elif (i in current_inventory):
        current_inventory[i] += 50
        print(f"Restocking: {i} increased by 50 units.")
    else:
        current_inventory.update({i: 10})         

print("="*42)
print(f"{'STORAGE MANIFEST':^42}")
print("="*42)
for i, x in current_inventory.items():
    display_name = i.replace("_", " ").title()
    print(f"{display_name:<30}{f'{x:,}':>12}")
print("="*42)    
