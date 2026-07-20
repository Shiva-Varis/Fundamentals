total_ingested_psi = 0.0
valid_reading_count = 0

while (True):
    asset_code = input("Input current station sensor asset code: ").lower()
    if (asset_code == "shutdown"):
        print(f"Normal operator termination requested. Running diagnostics...")
        break
    else:
        psi_reading = float(input("Input systems current pressure: "))
        if (psi_reading <= 0.0):
            print(f"SENSOR GLITCH: Discarding zero/negative anomaly value on Asset {asset_code}.")
            continue
        elif (psi_reading > 850):
            print(f"CRITICAL OVER-PRESSURE DETECTED: Emergency blowoff valve deployed on Asset {asset_code}!")
            break
        else:
            total_ingested_psi += psi_reading
            valid_reading_count += 1
            print(f"Telemetry recorded for Asset {asset_code}.")
if (valid_reading_count > 0):
    average_operating_pressure = total_ingested_psi / valid_reading_count                
else:
    average_operating_pressure = 0.0

print("="*42)
print(f"{'ASSET LOG':^42}")
print("="*42)
print(f"{'AVERAGE PRESSURE:':<30}{f'{average_operating_pressure:.3f}PSI':>12}")
print("="*42)
print(f"{'COMPLETED':^42}")
print("="*42)