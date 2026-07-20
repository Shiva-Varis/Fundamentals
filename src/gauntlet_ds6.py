historical_blacklist = ["192.168.1.50", "10.0.0.12", "192.168.1.50", "172.16.5.4"]
active_threat_matrix = set(historical_blacklist)

while True:
    ip_input = input("Incoming connection attempt: ").strip().lower()
    if ip_input == "compile":
        break
    elif ip_input in active_threat_matrix:
        print(f"FIREWALL BLOCK: {ip_input} dropped dynamically")
    else:
        threat_level = int(input("Enter threat rating (1-5): "))
        if threat_level >= 3:
            active_threat_matrix.add(ip_input)
            print(f"IP {ip_input} blacklisted globally") 
        else:
            print(f"Connection low-risk. Passing token.")

print("="*40)
print(f"{'INCIDENT SUMMARY DASHBOARD':^40}") 
print("="*40) 
print(f"{'Total Active Shield Signatures':<28}{len(active_threat_matrix):>12}")
if "192.168.1.50" in active_threat_matrix:
    print(f"{'IP Address Present':<28}{'TRUE':>12}")
else:
    print(f"{'IP Address Present':<28}{'FALSE':>12}") 
print("="*40)
print(f"{'COMPLETED':^40}") 
print("="*40)       
