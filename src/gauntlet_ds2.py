tenant_profiles = {
    "alpha_corp": {"max_payload_mb": 50, "security_clearance": "high"},
    "beta_llc": {"max_payload_mb": 15, "security_clearance": "standard"}
}

total_bytes_processed = 0
flagged_breach_count = 0

while (True):
    tenant_id = input("Input your Tenant Id: ").lower()
    if (tenant_id == "exit"):
        print(f"Powering down gateway monitor.")
        break

    elif (tenant_id in tenant_profiles):
        print(f"ACCESS GRANTED") 
        payload_size = int(input("Input packets payload size: "))
        if (payload_size > tenant_profiles[tenant_id]["max_payload_mb"]) :
            print(f"SPIKE DETECTED: {tenant_id} exceeded data threshold. Packet dropped.")
            flagged_breach_count += 1
            continue
        else:
            print(f"Packet verified. {payload_size}MB piped to storage.")
            total_bytes_processed += payload_size

    else:
        print(f"ACCESS DENIED: Unkown Tenant {tenant_id}. Routing packet to quarantine.")
        flagged_breach_count += 1
        continue       

print("="*48)
print(f"{'SUMMARY':^48}")
print("="*48)
print(f"{'BYTES PROCESSED':<34}{f'{total_bytes_processed:,}MB':>14}")
print(f"{'FLAGGED SECURITY ANOMALIES':<34}{flagged_breach_count:>14}")
print("="*48)
print(f"{'COMPLETED':^48}")
print("="*48)