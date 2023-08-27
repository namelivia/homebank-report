from homebank_report.operation_set import OperationSet

class Account:
    def __init__(self, key, pos, type, curr, name, initial, minimum, maximum):
        self.key = key
        self.pos = pos
        self.type = type
        self.curr = curr
        self.name = name
        self.initial = float(initial)
        self.minimum = minimum
        self.maximum = maximum
        self.operations = []

    def get_operation_set_between(self, start_date, end_date):
        operations = [operation for operation in self.operations if start_date <= operation.date <= end_date]
        return OperationSet(operations)

    def __str__(self):
        return f"Account: key={self.key}, pos={self.pos}, type={self.type}, curr={self.curr}, name={self.name}, initial={self.initial}, minimum={self.minimum}, maximum={self.maximum}"
