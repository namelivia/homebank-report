class AccountReport:
    def __init__(self, *, name, balance, expenses_graph_path, revenue_graph_path,
                 evolution_graph_path):
        self.name = name
        self.balance = balance
        self.expenses_graph_path = expenses_graph_path
        self.revenue_graph_path = revenue_graph_path
        self.evolution_graph_path = evolution_graph_path

    def __str__(self):
        return f"AccountReport: name={self.name}, balance={self.balance}, expenses_graph_path={self.expenses_graph_path}, revenue_graph_path={self.revenue_graph_path}, evolution_graph_path={self.evolution_graph_path}"
