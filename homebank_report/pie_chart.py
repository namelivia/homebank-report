import time
from .operation_set import OperationSet
from matplotlib import pyplot as plt

def draw_pie_chart(data, graphs_path, labels, title):
    plt.figure(figsize=(8, 8))  # Set the figure size
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)  # Create the pie chart
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular
    plt.title(title)
    current_timestamp = int(time.time())
    slug = title.lower().replace(' ', '_').replace(':', '')
    path = f'{graphs_path}/{slug}_{current_timestamp}.png'
    plt.savefig(path)
    return path

def generate_expenses_pie_chart(account_name: str, options, categories, operations: OperationSet):
    data = []
    labels = []
    for category_key, category in categories.items():
        balance = abs(operations.get_for_category(category_key).get_balance())
        if balance > 0:
            labels.append(category.name)
            data.append(balance)

    if (len(data) == 0):
        return ''
    return draw_pie_chart(data, options.get("graphs_path"), labels, f'{account_name}: Gastos')

def generate_revenue_pie_chart(account_name: str, options, categories, operations: OperationSet):
    data = []
    labels = []
    for category_key, category in categories.items():
        balance = operations.get_for_category(category_key).get_balance()
        if balance > 0:
            labels.append(category.name)
            data.append(balance)

    if (len(data) == 0):
        return ''
    return draw_pie_chart(data, options.get("graphs_path"), labels, f'{account_name}: Ingresos')

