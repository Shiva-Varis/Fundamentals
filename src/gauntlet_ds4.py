incoming_logs = [
    {"user": "olumide", "phone": "08011112222", "source": "mobile"},
    {"user": "   chioma   ", "phone": "08033334444", "source": "web"},
    {"user": "olumide", "phone": "08011112222", "source": "web"},  
    {"user": "bisi", "phone": "08055556666", "source": "mobile"},
    {"user": "chioma", "phone": "08033334444", "source": "mobile"} 
]
seen_identities = set()
master_registry = []
for i in incoming_logs:
    cleaned_user = i["user"].lower().strip()
    identity_packet = (cleaned_user, i["phone"])
    if (identity_packet in seen_identities):
        print(f"Duplicate packet dropped for: {cleaned_user}")
        continue
    else:
        seen_identities.add(identity_packet)
        clean_profile = {"name": cleaned_user, "contact": i["phone"], "device": i["source"]} 
        master_registry.append(clean_profile)
        print(f"Resolved new identity: {cleaned_user}")

print("="*45)
print(f"{'SYSTEM GOVERNANCE AUDIT':^45}")
print("="*45)
print(f"{'Total Raw Packets Ingested':<33}{len(incoming_logs):>12}")
print(f"{'Total Unique Identities Resolved':<33}{len(master_registry):>12}")
print("="*45)
print(f"{'COMPLETED':^45}")
print("="*45)
print(f"Raw Master Registery: {master_registry}")