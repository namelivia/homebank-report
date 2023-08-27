class AccountReport:
    def __init__(self, *, period, name, balance, expenses_graph_path, revenue_graph_path,
                 evolution_graph_path, top_10):
        self.name = name
        self.period = period
        self.balance = balance
        self.expenses_graph_path = expenses_graph_path
        self.revenue_graph_path = revenue_graph_path
        self.evolution_graph_path = evolution_graph_path
        self.top_10 = top_10

    def __str__(self):
        return f"AccountReport: name={self.name}, balance={self.balance}, expenses_graph_path={self.expenses_graph_path}, revenue_graph_path={self.revenue_graph_path}, evolution_graph_path={self.evolution_graph_path}"
