raw_transactions = [
    {"tx_id": " TX-1001 ", "amount": "450000.00", "fee": "1500.00", "status": "settled"},
    {"tx_id": "tx-1002", "amount": "0.00", "fee": "0.00", "status": "settled"},               
    {"tx_id": "  TX-1003 ", "amount": "1250000.50", "fee": "2500.00", "status": "settled"},
    {"tx_id": "tx-1004", "amount": "80000.00", "fee": "CORRUPTED", "status": "settled"},      
    {"tx_id": "TX-1005", "amount": "320000.00", "status": "settled"},                          
    {"tx_id": "tx-1006", "amount": "950000.00", "fee": "3000.00", "status": "flagged"}        
]

settled_records = list(filter(lambda ttx : ttx['status'] == 'settled', raw_transactions))
clean_id = list(map(lambda fs : {**fs, 'tx_id': fs['tx_id'].strip().upper()}, settled_records))
processed_settlements = []

for r in clean_id:
    try:
        parsed_amt = float(r['amount'])
        parsed_fee = float(r['fee'])
        fee_percentage = (parsed_fee / parsed_amt) * 100
        net_settlement = parsed_amt - parsed_fee
    except KeyError:
        print(f"[ERROR] {r['tx_id']}: Missing transacion key.") 
    except ValueError:
        print(f"[ERROR] {r['tx_id']}: Malformed numeric value.")    
    except ZeroDivisionError:
        print(f"[ERROR] {r['tx_id']}: Zero amount transaction: cannot compute fee ratio.")
    else:           
        processed_settlements.append((r['tx_id'], net_settlement, fee_percentage))

from functools import reduce
net_settlement_values = [t[1] for t in processed_settlements]
total_net_settled = reduce(lambda x, y : x + y, net_settlement_values)

print("="*50)
print(f"{'OPERATIONAL DASHBOARD':^50}")
print("="*50)
print(f"{'ID':<30}{'NET SETTLEMENT':>20}")
for ps in processed_settlements:
    print(f"{ps[0]:<30}{f'{ps[1]:,.2f}':>20}")
print("-"*50)
print(f"{'Total Net Settled Volume:':<30}{f'{total_net_settled:,.2f}':>20}")
print("="*50) 
print(f"{'COMPLETED':^50}")
print("="*50)   