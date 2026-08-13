from functools import reduce

raw_data_stream = [
    {"item_id": " ITEM-101 ", "price": "45.50", "qty": "100", "status": "active"},
    {"item_id": "item-102", "price": "120.00", "qty": "INVALID", "status": "active"},    # Malformed quantity!
    {"item_id": "item-103", "price": "0.00", "qty": "50", "status": "active"},          # Zero price!
    {"item_id": "item-104", "price": "85.25", "status": "active"},                       # Missing 'qty' key!
    {"item_id": "  ITEM-105  ", "price": "300.00", "qty": "15", "status": "active"},
    {"item_id": "item-106", "price": "10.00", "qty": "500", "status": "discontinued"}    # Non-active status!
]

class WarehouseEngine:
    total_warehouses_active = 0

    def __init__(self, warehouse_code, min_margin=0.05):
        self.warehouse_code = warehouse_code
        self._min_margin = min_margin
        self.inventory = []
        self.error_logs = []
        WarehouseEngine.total_warehouses_active += 1

    @property
    def min_margin(self):
        return self._min_margin    

    @min_margin.setter
    def min_margin(self, min_margin):
        if min_margin < 0.0 or min_margin > 0.50:
            raise ValueError("Margin rate must be between 0.0 and 0.50")
        else:
            self._min_margin = min_margin    

    @staticmethod
    def is_valid_item_code(code):
        return code.startswith('item-')

    @classmethod
    def from_config_string(cls, config_str):
        split_input = config_str.split(",")
        parsed_string = split_input[0]
        parsed_min = float(split_input[1])     
        return cls(parsed_string, parsed_min)

    def clean_stream(self, raw_stream):
        active_items = list(filter(lambda x : x['status'] == 'active', raw_stream))
        cleaned_stream = list(map(lambda y : {**y, 'item_id': y['item_id'].strip().lower()}, active_items))
        return cleaned_stream

    def process_inventory(self, cleaned_stream):  
        for i in cleaned_stream:
            valid_code = self.is_valid_item_code(i['item_id']) 
            if not valid_code:
                self.error_logs.append(f"[REJECTED] {i['item_id']}: Invalid code format.")
                continue
            try:
                parsed_price = float(i['price'])
                parsed_qty = int(i['qty'])
                if parsed_price <= 0:
                    raise ValueError("Price must be positive")
                total_valuation = parsed_price * parsed_qty
                
            except KeyError:
                self.error_logs.append(f"[ERROR] {i['item_id']}: Missing field.")
            except ValueError:
                self.error_logs.append(f"[ERROR] {i['item_id']}: Invalid value.")        
            else:
                self.inventory.append((i['item_id'], parsed_price, parsed_qty, total_valuation))

    def calculate_total_warehouse_value(self):
        total_valuation = [t[3] for t in self.inventory]
        if not total_valuation:
            return 0.0
        return reduce(lambda x , y : x + y, total_valuation)

    def generate_report(self):
        print("="*50)
        print(f"{'TERMINAL DASHBOARD':^50}")
        print("="*50)
        print(f"{self.warehouse_code:^50}")
        print(f"{'Total active warehouses':<30}{WarehouseEngine.total_warehouses_active:>20}")
        print("-"*50)
        print(f"{'ITEM ID':<30}{'TOTAL VALUATION'}")
        print("-"*50)
        for i in self.inventory:
            print(f"{i[0]:<30}{f'{i[3]:.2f}':>20}")
        print("-"*50)    
        print(f"Error Logs")
        for e in self.error_logs:
            print(f" {e}")
        print("-"*50)
        valuation = self.calculate_total_warehouse_value()
        print(f"{'Grand Total Warehouse Valuation:':<35}{f'{valuation:.2f}':>15}")  
        print("="*50)          



engine = WarehouseEngine.from_config_string("WH-LAGOS-01,0.15")
cleaned_data_stream = engine.clean_stream(raw_data_stream)
processed_stream = engine.process_inventory(cleaned_data_stream)
engine.generate_report()

        
