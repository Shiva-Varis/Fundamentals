while (True):
    systolic_blood_pressure = int(input("Enter Patient's Systolic Blood Pressure: "))
    if (systolic_blood_pressure == 0):
        print(f"End of batch telemetry received.")
        break
    elif (systolic_blood_pressure < 0 or systolic_blood_pressure > 300):
        print(f"Sensor glitch detected. Discarding reading.")
        continue
    elif (systolic_blood_pressure > 180):
        print(f"EMERGENCY: Hypertensive Crisis! Dispatch medical team!")
    elif (systolic_blood_pressure < 90):
        print(f"WARNING: Hypotension detected. Monitor patient closely.")
    else: 
        print(f"Vitals stable. Logged.")
                            