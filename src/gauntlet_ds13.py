raw_payloads = [
    {"app_id": "  app-alpha ", "active_users": "1500", "errors": "45", "status": "active"},
    {"app_id": "app-beta", "active_users": "0", "errors": "0", "status": "active"},           # Zero users!
    {"app_id": "app-gamma", "active_users": "800", "errors": "INVALID", "status": "active"},  # Malformed float/int!
    {"app_id": "app-delta", "active_users": "2500", "status": "active"},                      # Missing 'errors' key!
    {"app_id": "  app-epsilon  ", "active_users": "3200", "errors": "16", "status": "active"},
    {"app_id": "app-zeta", "active_users": "100", "errors": "5", "status": "suspended"}       # Non-active app!
]

clean_payload = list(filter(lambda raw_payloads : raw_payloads['status'] == "active", raw_payloads))

clean_id = list(map(lambda payload : {**payload, 'app_id': payload['app_id'].strip().lower()}, clean_payload))

valid_metrics = []

for i in clean_id:
    try:
        transformed_users = int(i['active_users'])
        transformed_errors = float(i['errors'])
        error_rate = (transformed_errors / transformed_users) * 100

    except KeyError:
        print(f"[ERROR] {i['app_id']}: Missing metric key")    
    except ValueError:
        print(f"[ERROR] {i['app_id']}: Malformed numeric metric")
    except ZeroDivisionError:
        print(f"[ERROR] {i['app_id']}: Zero active users, error rate undefined")      

    else:
        valid_metrics.append((i['app_id'], transformed_users, error_rate))

from functools import reduce
error_list = [e[2] for e in valid_metrics]
aggregate = reduce(lambda x, y : x + y, error_list)
average_error_rate = aggregate / len(valid_metrics)

print("="*50)
print(f"{'DASHBOARD OUTPUT':^50}")
print("="*50)
print(f"{'APP ID':<30}{'ERROR RATE':>20}")
for i in valid_metrics:
    print(f"{i[0]:<30}{f'{i[2]:.2f}%':>20}")
print(f"{'Average Error Rate':<30}{f'{average_error_rate:.2f}':>20}")    