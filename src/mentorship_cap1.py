transaction_data = [
    {"sender": "Adaeze Okafor", "receiver": "Chinedu Eze", "amount": 15000.50, "currency": "NGN", "status": "success"},
    {"sender": "Tunde Bakare", "receiver": "Ngozi Umeh", "amount": -230000.00, "currency": "NGN", "status": "success"},
    {"sender": "Fatima Bello", "receiver": "Aisha Sule", "amount": 5000.75, "currency": "NGN", "status": "pending"},
    {"sender": "", "receiver": "Blessing Uche", "amount": 89000.00, "currency": "NGN", "status": "failed"},
    {"sender": "Kelechi Obi", "receiver": "Chioma Ike", "amount": 1200000.00, "currency": "NGN", "status": "success"},
    {"sender": "Halima Yusuf", "receiver": "Ibrahim Musa", "amount": 3000.00, "currency": "NGN", "status": "cancelled"},
    {"sender": "Grace Adeyemi", "receiver": "Peter Nnamdi", "amount": 67000.20, "currency": "NGN", "status": "failed"},
    {"sender": "Segun Alao", "receiver": "", "amount": 450000.00, "currency": "NGN", "status": "pending"},
]

class Transaction:

    def __init__(self, sender, receiver, amount, currency, status):
        if amount <= 0:
            raise ValueError('The amount must be greater than zero') 
        elif Transaction.is_valid_status(status) == False:
            raise ValueError('Invalid Status')
        elif len(sender) < 1 or len(receiver) < 1:
            raise ValueError('Sender or Receiver can not be an empty string')
        else:
            self.sender = sender
            self.receiver = receiver
            self._amount = amount
            self.currency = currency
            self.status = status          

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value <= 0:
            raise ValueError('The amount must be greater than zero')
        else:
            self._amount = value
            return self._amount

    def summary(self):
        return f"{self.sender} sent {self._amount}{self.currency} to {self.receiver} - {self.status}"

    @classmethod
    def from_dict(cls, data):
        sender = data['sender']
        receiver = data['receiver']
        amount = data['amount']
        currency = data['currency']
        status = data['status']
        return cls(sender, receiver, amount, currency, status)

    @staticmethod
    def is_valid_status(status):
        valid_status = {"success", "failed", "pending"}
        if status not in valid_status:
            return False
        else:
            return True

successful_transactions = []
for record in transaction_data:
    try: 
        txn = Transaction.from_dict(record)
    except ValueError as e:
        print(f"{record['sender']}'s transaction failed due to error: {e}")
    else:
        successful_transactions.append(txn)
        print(txn.summary())    


