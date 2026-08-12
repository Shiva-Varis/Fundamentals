from functools import reduce

raw_stream = [
    {"service": " auth-service ", "latency_ms": "120", "requests": "1500", "errors": "15", "status": "active"},
    {"service": "billing-service", "latency_ms": "350", "requests": "0", "errors": "0", "status": "active"},        # Zero requests!
    {"service": "payment-gateway", "latency_ms": "SLOW", "requests": "800", "errors": "2", "status": "active"},    # Malformed numeric!
    {"service": "user-feed", "latency_ms": "90", "requests": "3000", "status": "active"},                          # Missing 'errors' key!
    {"service": "  analytics-api  ", "latency_ms": "210", "requests": "5000", "errors": "25", "status": "active"},
    {"service": "legacy-vault", "latency_ms": "500", "requests": "100", "errors": "50", "status": "deprecated"}   # Non-active status!
]

class PipelineSentinel():
    def __init__(self, pipeline_name):
        self.pipeline_name = pipeline_name
        self.valid_records = []
        self.audit_logs = []

    def clean_stream(self, raw_data):
        active_payloads = list(filter(lambda raw_data : raw_data['status'] == 'active', raw_data))
        clean_names = list(map(lambda ap : {**ap, 'service': ap['service'].strip().lower()}, active_payloads))
        return clean_names

    def process_records(self, cleaned_data):
        for i in cleaned_data:
            try:
                parsed_requests = int(i['requests'])
                parsed_errors = float(i['errors'])
                parsed_latency = float(i['latency_ms'])
                error_rate = (parsed_errors / parsed_requests) * 100
            
            except KeyError:
                self.audit_logs.append(f"[ERROR] {i['service']}: Missing metric key.")
            except ValueError:
                self.audit_logs.append(f"[ERROR] {i['service']}: Malformed numeric attribute.")
            except ZeroDivisionError:
                self.audit_logs.append(f"[ERROR] {i['service']}: Zero request recorded; error rate undefined.")

            else: 
                self.valid_records.append((i['service'], parsed_latency, error_rate))      

    def calculate_avg_error_rate(self):
        valid_errors = [e[2] for e in self.valid_records]
        if not valid_errors:
            return 0.0
        return reduce(lambda x, y: x + y, valid_errors) / len(valid_errors) 
    def generate_dashboard(self):
        print("="*50)
        print(f"{'DASHBOARD':^50}")
        print("="*50)
        print(f"{self.pipeline_name:^50}")     
        print(f"{'Service':<30}{'Error Rate':>20}")
        for t in self.valid_records:
            print(f"{t[0]:<30}{f'{t[2]:.2f}%':>20}")
        print("-"*50)
        print("AUDIT LOGS:")
        for log in self.audit_logs:
            print(f"  {log}")
        avg = self.calculate_avg_error_rate()
        print(f"{'Average Error Rate'}{avg:.2f}")
        print("="*50)
        print(f"{'DASHBOARD':^50}")
        print("="*50)       

sentinel1 = PipelineSentinel("PROD-TELEMETRY-ETL")
cleaned = sentinel1.clean_stream(raw_stream)
sentinel1.process_records(cleaned)
sentinel1.generate_dashboard()

        

        
