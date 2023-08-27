import time
from matplotlib import pyplot as plt
from .operation_set import OperationSet
import numpy as np

def generate_evolution_graph(account_name: str, options, operations: OperationSet):
    data = []
    for operation in operations.operations:
        data.append(operation.amount)
    if len(data) == 0:
        return ''
    plt.figure(figsize=(8, 8))  # Set the figure size
    plt.plot(np.cumsum(data))
    plt.title(f'{account_name}: Evolución')
    current_timestamp = int(time.time())
    slug = f'{account_name}_evolucion'
    graphs_path = options.get("graphs_path")
    path = f'{graphs_path}/{slug}_{current_timestamp}.png'
    plt.savefig(path)
    return path
