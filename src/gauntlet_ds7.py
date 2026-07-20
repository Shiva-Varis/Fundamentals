EXCHANGE_RATES = {"NGN": 0.00065, "GHS": 0.072, "KES": 0.0076, "USD": 1.0}
RISK_BLACKLIST = ("M_999", "M_777", "M_000")
raw_transactions = [
    {"tx_id": "TX101", "merchant": "M_101", "amount": 50000.0, "currency": "NGN", "status": "success"},
    {"tx_id": "TX102", "merchant": "M_999", "amount": 1200.0, "currency": "USD", "status": "success"}, 
    {"tx_id": "TX103", "merchant": "M_102", "amount": 350.0, "currency": "GHS", "status": "failed"},    
    {"tx_id": "TX101", "merchant": "M_101", "amount": 50000.0, "currency": "NGN", "status": "success"}, 
    {"tx_id": "TX104", "merchant": "M_103", "amount": 150000.0, "currency": "KES", "status": "success"},
    {"tx_id": "TX105", "merchant": "M_101", "amount": 850.0, "currency": "USD", "status": "success"}
]
deduped_transactions = []
seen_tx_ids = set()

for tx in raw_transactions: 
    current_id = tx["tx_id"]
    if current_id in seen_tx_ids:
        continue
    else:
        seen_tx_ids.add(current_id)
        deduped_transactions.append(tx)

successful = list(filter(lambda transactions : transactions["status"] == "success" and transactions["merchant"] not in RISK_BLACKLIST, deduped_transactions))

def normalize_and_tax(stream):
    currency = stream["currency"]
    usd_value = stream["amount"] * EXCHANGE_RATES[currency] 
    if usd_value > 100:
        fee = (3.5 / 100) * usd_value
    else:
        fee = (1.5 / 100) * usd_value
    processed = {"id": stream["tx_id"], "usd_base": usd_value, "fee": fee}    
    return processed

from functools import reduce
mapped_list = list(map(normalize_and_tax, successful)) 
usd_values_only = list(map(lambda tx: tx["usd_base"], mapped_list))
fee_values_only = list(map(lambda tx: tx["fee"], mapped_list))
usd_settlement = (reduce(lambda x, y : x + y, usd_values_only))
processing_fees = (reduce(lambda x, y: x + y, fee_values_only))    

print("="*46)
print(f"{'FINTECH COMPLIANCE AUDIT DISPATCH':^46}")
print("="*46)
print(f"{'Total Raw Packets Ingested':<32}{len(raw_transactions):>14}")
print(f"{'Deduplication Dropped Records':<32}{len(raw_transactions) - len(deduped_transactions):>14}")
print(f"{'Compliance Security Rejections':<32}{len(deduped_transactions) - len(successful):>14}")
print("-"*46)
print(f"{'UNIQUE SETTLED VALUES':<32}{f'${usd_settlement:,.2f}':>14}")
print(f"{'TOTAL FEES GENERATED':<32}{f'${processing_fees:,.2f}':>14}")
print("="*46)
print(f"{'SYSTEM AUDIT COMPLETED':^46}")
print("="*46)

