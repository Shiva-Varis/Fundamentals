warehouse_stock = {
    "thunderbolt_dock": 85,
    "ergonomic_chair": 12,
    "ultrawide_monitor": 24
}

quarantine_skus = {"industrial_laser", "vape_battery", "unknown_fluid"}
flagged_seizures = []
while True:
    raw_inventory = input("Enter inventory (separate by commas): ")
    if raw_inventory == "execute":
        break 
    inventory_list = raw_inventory.split(",")
    clean_inventory =[item.strip().lower() for item in inventory_list]
    processed_inventory = set(clean_inventory)
    for i in processed_inventory:
        if i in quarantine_skus:
            print(f"{i} is contraband")
            banned = (i, "CRITICAL_HAZARD")
            flagged_seizures.append(banned)
        elif i in warehouse_stock:
            warehouse_stock[i] += 15
        else:
            warehouse_stock[i] = 1

print("="*42)
print(f"{'STORAGE MANIFESTATION DASHBOARD':^42}")
print("="*42)
print(f"{'PRODUCT NAME':<30}{'INVENTORY COUNT':>12}")
for sku in warehouse_stock.keys():
    title_sku = sku.replace("_"," ").title()
    print(f"{title_sku:<30}{f'{count:,}':>12}")
print("="*42)
print(f"{'QUARANTINED INCIDENTS':^42}")
print("="*42)    
if not flagged_seizures:
    print(f"{'No contraband was detected during shift':^42}")
else:
    print(f"SUMMARY: {flagged_seizures}")     
print("="*42) 




        
