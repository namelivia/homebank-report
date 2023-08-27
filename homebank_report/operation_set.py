class OperationSet:
    def __init__(self, operations):
        self.operations = operations

    def get_balance(self):
        return sum([operation.amount for operation in self.operations])

    def get_operations_for_category(self, category):
        operations = [operation for operation in self.operations if operation.category == category]
        return OperationSet(operations)

    def get_expenses(self):
        return OperationSet([operation for operation in self.operations if operation.amount < 0])
    def get_revenues(self):
        return OperationSet([operation for operation in self.operations if operation.amount > 0])

    def get_for_category(self, category):
        return OperationSet([operation for operation in self.operations if operation.category == category])

    def get_top_10(self):
        return sorted(self.operations, key=lambda operation: operation.amount)[:10]

    def __len__(self):
        return len(self.operations)
