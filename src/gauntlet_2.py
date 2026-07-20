vault_locked = True
alarm_tripped = False
invalid_attempts = 0

while(vault_locked == True):
    clearance_key = input("Input key: ").lower()
    if(clearance_key == "override_master"):
        print(f"MASTER OVERRIDE DETECTED: Unlocking vault.")
        vault_locked = False
    elif(clearance_key == "bypass"):
        print(f"Maintenance mode active. Skipping validation step.")
        continue
    elif(clearance_key == "threat"):
        print(f"SILENT ALARM TRIPPED!")
        alarm_tripped = True
        break
    else:
        invalid_attempts += 1
        if(invalid_attempts == 3):
            print(f"MAXIMUM ATTEMPTS EXCEEDED: Terminal locked down")    
            break                
if (vault_locked):
    display_status = "LOCKED"    
else:    
    display_status = "UNLOCKED"
if (alarm_tripped):
    display_status = "BREACHED"   
print("="*40)
print(f"{'DASHBOARD':^40}")
print("="*40)
print(f"{'VAULT STATUS:':<30}{display_status:>10}")
print(f"{'INVALID ATTEMPTS':<30}{invalid_attempts:>10}")
print("="*40)
print(f"{'FINISHED':^40}")
print("="*40)
