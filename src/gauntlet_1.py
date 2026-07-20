server_count = int(input("Number of servers needed: "))
total_hourly_cost = 0.0
for server_number in range(1, server_count + 1):
    instance_family = input("What's the instance(compute/memory): ").lower()
    if(instance_family == "compute"):
        rate = 0.10
    elif(instance_family == "memory"):
        rate = 0.25
    else:
        print(f"Invalid family: Skipping server {server_number}")
        continue
    hours_needed = int(input("How many hours needed: "))
    server_cost = hours_needed * rate
    if(server_cost > 500.00):
        print(f"BUDGET EXCEEDDED: Server {server_number} rejected")
        continue
    else:
        total_hourly_cost += rate
print("="*40)
print(f"{'TOTAL PROJECTED HOURLY SPEND':^40}")
print("="*40)
print(f"{'Total Cost Per Hour':<25}{f'${total_hourly_cost:,.2f}':>15}")        
print("="*40)
print(f"{'COMPLETED':^40}")
print("="*40)