transactions = [
    {"sender": "Adaeze Okafor", "receiver": "Chinedu Eze", "amount": "15000.50", "currency": "NGN", "status": "success"},
    {"sender": "Tunde Bakare", "receiver": "Ngozi Umeh", "amount": "230000.00", "currency": "NGN", "status": "success"},
    {"sender": "Fatima Bello", "receiver": "Aisha Sule", "amount": "5000.75", "currency": "NGN", "status": "pending"},
    {"sender": "Emeka Nwosu", "receiver": "Blessing Uche", "amount": "89000.00", "currency": "NGN", "status": "failed"},
    {"sender": "Kelechi Obi", "receiver": "Chioma Ike", "amount": "1200000.00", "currency": "NGN", "status": "success"},
    {"sender": "Halima Yusuf", "receiver": "Ibrahim Musa", "amount": "3000.00", "currency": "NGN", "status": "sucess"},
    {"sender": "Grace Adeyemi", "receiver": "Peter Nnamdi", "amount": "67000.20", "currency": "NGN", "status": "failed"},
    {"sender": "Segun Alao", "receiver": "Bisi Ojo", "amount": "450000.00", "currency": "NGN", "status": "pendng"},
]
valid_statuses = {"success", "failed", "pending"}

def clean_amount(amount_str):
    try:
        float(amount_str.strip())
    except ValueError:
        print(f"[ERROR] Invalid value")
        return 0.0
    else:
        return float(amount_str.strip())      

def is_valid_status(status):
    return status.strip().lower() in valid_statuses    

def summarize_transactions(transactions):
    counts = {}
    for tx in transactions:
        status = tx.get("status")
        counts[status] = counts.get(status, 0) + 1
    return counts    

def find_high_value(transactions, threshold):
    senders = [t['sender'] for t in transactions if clean_amount(t['amount']) > threshold]
    return senders

def top_sender(transactions):
    if not transactions:
        return None
    best_so_far = 0
    for ttx in transactions:
        if clean_amount(ttx['amount']) > best_so_far:
            best_so_far = clean_amount(ttx['amount'])  
            lead_sender = ttx['sender']  
    return lead_sender            