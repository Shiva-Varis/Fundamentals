events = [
    {"msisdn": "08031234567", "operator": "MTN_NG", "event_type": "call", "duration_seconds": " 120 ", "status": "success"},
    {"msisdn": "08129876543", "operator": "airtel_ng", "event_type": "call", "duration_seconds": "45", "status": "dropped"},
    {"msisdn": "08037654321", "operator": "mtn_ng ", "event_type": "data", "duration_seconds": "0", "status": "success"},
    {"msisdn": "08129876543", "operator": "AIRTEL_NG", "event_type": "sms", "duration_seconds": "0", "status": "success"},
    {"msisdn": "08031234567", "operator": "MTN_NG", "event_type": "call", "duration_seconds": "310", "status": "success"},
    {"msisdn": "07051112233", "operator": "AIRTL_NG", "event_type": "recharge", "duration_seconds": "0", "status": "success"},
    {"msisdn": "08031234567", "operator": " mtn_ng", "event_type": "data", "duration_seconds": "0", "status": "failed"},
    {"msisdn": "08129876543", "operator": "airtel_ng", "event_type": "call", "duration_seconds": "200", "status": "dropped"},
]
membership = {"mtn_ng", "airtel_ng"}

def clean_duration(time_str):
    return float(time_str.strip())

def clean_operator(operator_str):
    return operator_str.strip().lower()

def is_valid_operator(operator):
    return operator.strip().lower() in membership

def summarize_by_event_type(events):
    counts = {}
    for i in events:
        event_type = i.get("event_type") 
        counts[event_type] = counts.get(event_type, 0) + 1
    return counts

def find_long_calls(events, threshold_seconds):
    long_callers = [e['msisdn'] for e in events if e['event_type'] == "call" and clean_duration(e['duration_seconds']) > threshold_seconds]
    return long_callers

def most_active_subscriber(events):
    tally = {}
    activity = 0
    for ev in events: 
        user = ev.get("msisdn")
        tally[user] = tally.get(user, 0) + 1
    for key, value in tally.items():
        if value > activity:
            activity = value
            most_active = key
    return most_active        