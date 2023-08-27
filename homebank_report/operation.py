class Operation:
    def __init__(self, date, amount, account, category=None, flags=None, wording=None, info=None):
        self.date = int(date)
        self.amount = float(amount)
        self.account = account
        self.category = category
        self.flags = flags
        self.wording = wording
        self.info = info
    
    def __str__(self):
        return f"Operation: date={self.date}, amount={self.amount}, account={self.account}, category={self.category}, flags={self.flags}, wording={self.wording}, info={self.info}"
